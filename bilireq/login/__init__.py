import asyncio
import io
from base64 import b64encode
from typing import Optional, Union

from .._typing import T_Auth
from ..auth import Auth
from ..exceptions import ResponseCodeError
from ..utils import get, post
from .pwd_login import pwd_login as _pwd_login
from .qrcode_login import get_qrcode_login_info, get_qrcode_login_result
from .sms_login import send_sms
from .sms_login import sms_login as _sms_login

BASE_URL = "https://passport.bilibili.com/api/v2/oauth2/"


async def refresh_token(auth: T_Auth = None, *, reqtype="app", **kwargs):
    """
    刷新 Token

    Args:
        access_token (str): Access Token
        refresh_token (str): Refresh Token

    Raises:
        ResponseCodeError: 返回码不为 0

    Returns:
        Dict: 刷新后的 Token 信息，原 Token 失效
    """
    url = f"{BASE_URL}refresh_token"
    return await post(url, auth=auth, reqtype=reqtype, **kwargs)


async def get_token_info(auth: T_Auth = None, *, reqtype="app", **kwargs):
    """
    获取 Token 登录信息

    Args:
        access_token (str): Access Token

    Raises:
        ResponseCodeError: 返回码不为 0
            -101: user not login

    Returns:
        Dict: Token 信息
    """
    url = f"{BASE_URL}info"
    return await get(url, auth=auth, reqtype=reqtype, **kwargs)


class Login:
    auth_code: str
    qrcode_url: str
    tel: int
    cid: int
    captcha_key: str

    async def get_qrcode_url(self) -> str:
        r = await get_qrcode_login_info()
        self.auth_code = r["auth_code"]
        self.qrcode_url = r["url"]
        return self.qrcode_url

    async def get_qrcode(self, url: Optional[str] = None, print_=False, base64=False):
        try:
            import qrcode  # type: ignore
        except ImportError:
            raise ImportError("bilireq[qrcode] not installed.")
        url = url or await self.get_qrcode_url()
        qr = qrcode.QRCode()
        qr.add_data(url)
        if print_:
            qr.print_tty()
            return None
        img = qr.make_image()
        if not base64:
            return img
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return b64encode(buf.getvalue()).decode()

    async def qrcode_login(self, auth_code=None, retry=-1, interval=1):
        auth_code = auth_code or self.auth_code
        while retry:
            try:
                resp = await get_qrcode_login_result(auth_code)
                auth = Auth()
                auth.access_token = resp["token_info"]["access_token"]
                auth.refresh_token = resp["token_info"]["refresh_token"]
                return await auth.refresh()
            except ResponseCodeError as e:
                if e.code != 86039:
                    raise
            await asyncio.sleep(interval)
            retry -= 1

    async def send_sms(self, tel, cid=86) -> str:
        self.tel = tel
        self.cid = cid
        self.captcha_key: str = (await send_sms(tel, cid=cid))["captcha_key"]
        return self.captcha_key

    async def sms_login(
        self,
        code: Union[int, str],
        tel: Union[int, str, None] = None,
        cid: Union[int, str, None] = None,
        captcha_key: Optional[str] = None,
    ):
        resp = await _sms_login(
            code=code,
            tel=tel or self.tel,
            cid=cid or self.cid,
            captcha_key=captcha_key or self.captcha_key,
        )
        auth = Auth()
        auth.access_token = resp["access_token"]
        auth.refresh_token = resp["refresh_token"]
        return await auth.refresh()

    async def pwd_login(self, username: str, password: str):
        resp = await _pwd_login(username, password)
        auth = Auth()
        auth.access_token = resp["access_token"]
        auth.refresh_token = resp["refresh_token"]
        return await auth.refresh()
