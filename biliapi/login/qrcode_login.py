from ..utils import post

BASE_URL = "https://passport.bilibili.com/x/passport-tv-login/"


async def get_qrcode_login_info():
    """获取二维码登录信息"""
    url = f"{BASE_URL}qrcode/auth_code"
    return await post(url, encrypt=True)


async def get_qrcode_login_result(auth_code: str):
    """获取二维码登录结果"""
    url = f"{BASE_URL}qrcode/poll"
    params = {"auth_code": auth_code}
    return await post(url, params=params, encrypt=True)
