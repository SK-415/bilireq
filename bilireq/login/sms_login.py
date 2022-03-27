from typing import Union

from ..utils import post

BASE_URL = "https://passport.bilibili.com/x/passport-tv-login/"


async def send_sms(tel: Union[int, str], cid: Union[int, str] = 86, **kwargs):
    """
    发送短信验证码

    Args:
        tel (int): 手机号
        cid (int, optional): 区号，默认 86

    Raises:
        ResponseCodeError: 返回码不为 0
            -400: 请求错误
            66031: 手机号码格式不正确
            86046: 请使用中国大陆手机号
            86200: 短信请求过快，请60秒后重试

    Returns:
        captcha_key (str): 验证码秘钥
    """
    url = f"{BASE_URL}sms/send"
    params = {"tel": tel, "cid": cid}
    return await post(url, params=params, reqtype="app", **kwargs)


async def sms_login(
    code: Union[int, str],
    tel: Union[int, str],
    captcha_key: str,
    cid: Union[int, str] = 86,
    **kwargs,
):
    """
    短信验证码登录

    Args:
        code (Union[int, str]): 验证码
        tel (Union[int, str]): 手机号
        captcha_key (str): 验证码秘钥
        cid (Union[int, str]): 区号，默认 86

    Raises:
        ResponseCodeError: 返回码不为 0
            -400: 请求错误
            -500: 服务器错误
            86202: 验证码错误
            86205: 验证码失效，请重新获取（错误次数过多或秘钥超时）
            86206: 区号不一致，请重新确认
            86207: 手机号不一致，请重新确认

    Returns:
        Dict: 登录 Tokens
    """
    url = f"{BASE_URL}login/sms"
    params = {"code": code, "tel": tel, "cid": cid, "captcha_key": captcha_key}
    return await post(url, params=params, reqtype="app", **kwargs)
