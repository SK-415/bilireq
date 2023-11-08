from ..utils import post, get
from bilireq._typing import T_Auth
from bilireq.auth import WebAuth
from bilireq.exceptions import AuthParamError

BASE_URL = "https://passport.bilibili.com/x/passport-login/web/"


async def get_web_qrcode_login_url(**kwargs):
    """获取二维码登录信息"""
    url = f"{BASE_URL}qrcode/generate"
    return await get(url, reqtype="web", **kwargs)


async def get_web_qrcode_login_info(qrcode_key: str, **kwargs):
    """获取二维码登录结果"""
    url = f"{BASE_URL}qrcode/poll"
    params = {"qrcode_key": qrcode_key}
    return await get(url, params=params, reqtype="web", **kwargs)


async def get_rsa_key(**kwargs):
    """
    获取RSA PUBLIC KEY

    Returns:
        hash (str): key的哈希
        key (str): rsa public key
    """
    url = f"{BASE_URL}key"
    return await get(url, reqtype="web", **kwargs)


async def check_cookie_status(auth: T_Auth, **kwargs):
    """
    检查cookie状态

    Returns:
        refresh (bool): 是否需要刷新
        timestamp (num): 当前毫秒值 可直接放置到get_refresh_csrf中获取 refresh_csrf
    """
    auth = WebAuth(auth)
    if not auth.cookies:
        raise AuthParamError("没有cookies")
    url = f"{BASE_URL}cookie/info"
    return await get(url, auth=auth, reqtype="web", **kwargs)


async def refresh_cookie(refresh_csrf, auth: T_Auth, **kwargs):
    url = f"{BASE_URL}cookie/refresh"
    params = {
        "csrf": auth.bili_jct,
        "refresh_csrf": refresh_csrf,
        "source": "main_web",
        "refresh_token": auth.refresh_token,
    }
    return await post(url, auth=auth, params=params, reqtype="web", **kwargs)


async def confirm_refresh_cookie(auth: T_Auth, **kwargs):
    url = f"{BASE_URL}confirm/refresh"
    params = {
        "csrf": auth.bili_jct,
        "refresh_token": auth.refresh_token,
    }
    return await post(url, auth=auth, params=params, raw=True, reqtype="web", **kwargs)
