from typing import Any, Dict
from httpx import AsyncClient
from httpx._types import URLTypes, ProxiesTypes, HeaderTypes

from .exceptions import ResponseCodeException

DEFAULT_HEADERS = {
    "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
        "Safari/537.36 Edg/87.0.664.60"),
    "Referer": "https://www.bilibili.com/"
}


async def request(
    method: str,
    url: URLTypes,
    *,
    headers: HeaderTypes = DEFAULT_HEADERS,
    proxies: ProxiesTypes = {"all://": None},
    **kwargs
) -> Dict[str, Any]:
    """请求基类"""

    async with AsyncClient(proxies=proxies) as client:
        resp = await client.request(method, url, headers=headers, **kwargs)
    resp.encoding = "utf-8"
    raw: Dict = resp.json()
    if raw['code'] != 0:
        print(resp.request.url)
        raise ResponseCodeException(
            code=raw['code'],
            msg=raw['message'],
            data=raw['data']
        )
    return raw['data']


async def get(url: URLTypes, **kwargs):
    return await request("GET", url, **kwargs)


async def post(url: URLTypes, **kwargs):
    return await request("POST", url, **kwargs)
