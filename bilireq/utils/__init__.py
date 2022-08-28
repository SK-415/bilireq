import time
from hashlib import md5
from typing import Any, Dict, Optional
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
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        "Safari/537.36 Edg/87.0.664.60"
    ),
    "Referer": "https://www.bilibili.com/",
}
APPKEY = "4409e2ce8ffd12b8"
APPSEC = "59b43e04ad6965f34319062b478f83dd"


def _encrypt_params(params: Dict[str, Any], local_id: int = 0) -> Dict[str, Any]:
    params["local_id"] = local_id
    params["appkey"] = APPKEY
    params["ts"] = int(time.time())
    params["sign"] = md5(
        f"{urlencode(sorted(params.items()))}{APPSEC}".encode("utf-8")
    ).hexdigest()
    return params


async def _request(
    method: str,
    url: URLTypes,
    *,
    params: Optional[Dict[str, Any]] = None,
    cookies: Optional[Dict[str, Any]] = None,
    auth: T_Auth = None,
    reqtype: str = "app",
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
    async with AsyncClient(proxies=proxies) as client:
        resp = await client.request(
            method, url, headers=headers, params=params, cookies=cookies, **kwargs
        )
    resp.encoding = "utf-8"
    return resp


async def request(
    method: str, url: URLTypes, *, raw: bool = False, **kwargs
) -> Dict[str, Any]:
    raw_json: Dict[str, Any] = (await _request(method, url, **kwargs)).json()
    if raw:
        return raw_json
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
