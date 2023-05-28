import time
import re
from hashlib import md5
from typing import Any, Dict, Optional, Union, Tuple
from urllib.parse import urlencode

from httpx import AsyncClient
from httpx._models import Response
from httpx._types import HeaderTypes, ProxiesTypes, URLTypes

from .._typing import T_Auth
from ..auth import Auth
from ..exceptions import ResponseCodeError

DEFAULT_HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        " Safari/537.36 Edg/87.0.664.60"
    ),
    "Referer": "https://www.bilibili.com/",
}
APPKEY = "4409e2ce8ffd12b8"
APPSEC = "59b43e04ad6965f34319062b478f83dd"
homepage_cookies: Dict[str, str] = {}
_salt = None


async def get_homepage_cookies(proxies=None):
    if not homepage_cookies:
        async with AsyncClient(proxies=proxies) as client:
            resp = await client.request(
                "GET",
                "https://www.bilibili.com/",
                headers=DEFAULT_HEADERS,
                follow_redirects=True,
            )
        resp.encoding = "utf-8"
        homepage_cookies.update(resp.cookies)
    return homepage_cookies


def _encrypt_params(params: Dict[str, Any], local_id: int = 0) -> Dict[str, Any]:
    params["local_id"] = local_id
    params["appkey"] = APPKEY
    params["ts"] = int(time.time())
    params["sign"] = md5(
        f"{urlencode(sorted(params.items()))}{APPSEC}".encode("utf-8")
    ).hexdigest()
    return params


async def _getsalt(*, proxies: ProxiesTypes = {"all://": None}):
    async with AsyncClient(proxies=proxies) as client:
        url = "https://api.bilibili.com/x/web-interface/nav"
        req = await client.request("GET", url, headers=DEFAULT_HEADERS)
    con = req.json()
    img_url = con["data"]["wbi_img"]["img_url"]
    sub_url = con["data"]["wbi_img"]["sub_url"]
    re_rule = r"wbi/(.*?).png"
    img_key = "".join(re.findall(re_rule, img_url))
    sub_key = "".join(re.findall(re_rule, sub_url))
    n = img_key + sub_key
    array = list(n)
    # 注释fmt是为了阻止Black把下面的order格式化为更多行
    # fmt:off
    order = [46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5,49, 33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7,16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54,21, 56, 59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52]
    # fmt:on
    salt = "".join([array[i] for i in order])[:32]
    return salt


async def _encrypt_w_rid(params: Union[str, dict]) -> Tuple[str, str]:
    """传入参数字符串返回签名和时间tuple[w_rid,wts]
    -----------
    params:str格式：qn=32&fnver=0&fnval=4048&fourk=1&voice_balance=1&gaia_source=pre-load&avid=593238479&bvid=BV16q4y1k7mq&cid=486645610\n
    params:dict格式：{'qn': '32', 'fnver': '0', 'fnval': '4048', 'fourk': '1', 'voice_balance': '1', 'gaia_source': 'pre-load', 'avid': '593238479', 'bvid': 'BV16q4y1k7mq', 'cid': '486645610'}：
    """
    global _salt
    wts = str(int(time.time()))
    if type(params) == str:
        params_list = (params + "&wts=" + wts).split("&")
    elif type(params) == dict:
        params["wts"] = wts
        params_list = [f"{key}={value}" for key, value in params.items()]
    else:
        raise Exception(f"invalid type of e:{type(params)}")
    params_list.sort()
    if _salt is None:
        _salt = await _getsalt()
    w_rid = md5(("&".join(params_list) + _salt).encode(encoding="utf-8")).hexdigest()
    return w_rid, wts


async def _sign_params(params: Dict[str, Any]):
    params.pop("w_rid", "")
    params.pop("wts", "")
    params["token"] = params.get("token", "")
    params["platform"] = params.get("platform", "web")
    params["web_location"] = params.get("web_location", 1550101)
    w_rid, wts = await _encrypt_w_rid(params)
    params["w_rid"] = w_rid
    params["wts"] = wts


async def _request(
    method: str,
    url: URLTypes,
    *,
    params: Optional[Dict[str, Any]] = None,
    cookies: Optional[Dict[str, Any]] = None,
    auth: T_Auth = None,
    reqtype: str = "app",
    is_wbi: bool = False,
    headers: HeaderTypes = DEFAULT_HEADERS,
    proxies: ProxiesTypes = {"all://": None},
    **kwargs,
) -> Response:
    auth = Auth(auth)
    if params is None:
        params = {}
    if cookies is None:
        cookies = {}
    if reqtype.lower() == "app":
        params.update(auth.tokens)
        _encrypt_params(params)
    else:
        cookies.update(auth.cookies)
    cookies.update(await get_homepage_cookies(proxies))
    if is_wbi:
        await _sign_params(params)
    async with AsyncClient(proxies=proxies) as client:
        resp = await client.request(
            method, url, headers=headers, params=params, cookies=cookies, **kwargs
        )
    resp.encoding = "utf-8"
    return resp


async def request(
    method: str, url: URLTypes, retry_time: int = 3, *, raw: bool = False, **kwargs
) -> Dict[str, Any]:
    raw_json: Dict[str, Any] = (await _request(method, url, **kwargs)).json()
    if raw:
        return raw_json
    if raw_json["code"] == -403:
        retry_time = retry_time - 1
        if retry_time < 0:
            raise ResponseCodeError(
                code=raw_json["code"],
                msg=raw_json["message"],
                data=raw_json.get("data", None),
            )
        global _salt
        _salt = await _getsalt()
        return await request(method, url, retry_time, **kwargs)
    if raw_json["code"] != 0:
        raise ResponseCodeError(
            code=raw_json["code"],
            msg=raw_json["message"],
            data=raw_json.get("data", None),
        )
    return raw_json["data"]


async def get(url: URLTypes, **kwargs):
    return await request("GET", url, **kwargs)


async def post(url: URLTypes, **kwargs):
    return await request("POST", url, **kwargs)
