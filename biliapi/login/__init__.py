import asyncio
import io
from base64 import b64encode
from typing import Union

from ..exceptions import ResponseCodeError
from .qrcode_login import get_qrcode_login_info, get_qrcode_login_result
from .sms_login import send_sms, sms_login


class Login:
    auth_code: str
    qrcode_url: str
    tel: int
    cid: int
    captcha_key: str

    async def get_qrcode_url(self) -> str:
        r = await get_qrcode_login_info()
        self.auth_code = r['auth_code']
        self.qrcode_url = r['url']
        return self.qrcode_url
    
    async def get_qrcode(self, url: str=None, print_=False, base64=False):
        try:
            import qrcode
        except ImportError:
            raise ImportError("biliapi[qrcode] did not installed.")
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
        img.save(buf, format='PNG')
        return b64encode(buf.getvalue()).decode()
    
    async def qrcode_login(self, auth_code=None, retry=10):
        auth_code = auth_code or self.auth_code
        while retry:
            try:
                return await get_qrcode_login_result(auth_code)
            except ResponseCodeError as e:
                if e.code != 86039:
                    raise
            await asyncio.sleep(1)
            retry -= 1
    
    async def send_sms(self, tel, cid=86) -> str:
        self.tel = tel
        self.cid = cid
        self.captcha_key: str = (await send_sms(tel, cid=cid))["captcha_key"]
        return self.captcha_key
    
    async def sms_login(
        self,
        code: Union[int, str],
        tel: Union[int, str] = None,
        cid: Union[int, str] = None,
        captcha_key: str = None
    ):
        return await sms_login(
            code = code,
            tel = tel or self.tel,
            cid = cid or self.cid,
            captcha_key = captcha_key or self.captcha_key
        )
        
