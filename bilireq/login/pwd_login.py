import base64
from typing import Dict

import rsa

from ..utils import post

BASE_URL = "https://passport.bilibili.com/"


async def _encrypt_pwd(pwd: str) -> str:
    """加密密码"""
    url = f"{BASE_URL}api/oauth2/getKey"
    resp: Dict[str, str] = await post(url, reqtype="app")
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(resp["key"].encode())
    msg = (resp["hash"] + pwd).encode()
    return base64.b64encode(rsa.encrypt(msg, pub_key)).decode("ascii")


async def pwd_login(username: str, password: str, **kwargs):
    """
    账号密码登录

    Args:
        username (str): 用户名
        password (str): 密码

    Raises:
        ResponseCodeError: 返回码不为 0
            -629: 用户名或密码错误
            86048: 密码错误超过次数限制,请尝试扫码登录或短信登录（十分钟重置）



    Returns:
        Dict: 登录 Token
    """
    url = f"{BASE_URL}x/passport-tv-login/login"
    params = {"username": username, "password": await _encrypt_pwd(password)}
    return await post(url, params=params, reqtype="app", **kwargs)
