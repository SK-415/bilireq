import collections
import time

from .._typing import T_Auth


class Auth(collections.UserDict):
    def __init__(self, auth: T_Auth = None):
        super().__init__()
        self.update({"token": {"tokens": {}}, "cookie": {"cookies": {}}})
        if auth:
            self.update(auth)
        # self.update(kwargs)

    def __bool__(self):
        return bool(self.tokens) and bool(self.cookies)

    @property
    def uid(self):
        return self["uid"]

    @property
    def tokens_expired(self):
        return self["token"]["expired"]

    @property
    def access_token(self):
        return self["token"]["tokens"].get("access_key")

    @access_token.setter
    def access_token(self, value):
        self["token"]["tokens"]["access_token"] = value

    @property
    def refresh_token(self):
        return self["token"]["tokens"].get("refresh_token")

    @refresh_token.setter
    def refresh_token(self, value):
        self["token"]["tokens"]["refresh_token"] = value

    @property
    def tokens(self):
        return self["token"]["tokens"]

    @property
    def cookies_expired(self):
        return self["cookie"]["expired"]

    @property
    def cookies(self):
        return self["cookie"]["cookies"]

    def refresh_handler(self, data):
        result = {}
        result["origin"] = data
        result["uid"] = data["token_info"]["mid"]
        result["token"] = {}
        result["token"]["expired"] = data["token_info"]["expires_in"] + int(time.time())
        result["token"]["tokens"] = {
            k: v
            for k, v in data["token_info"].items()
            if k in ["access_token", "refresh_token"]
        }
        result["token"]["tokens"]["access_key"] = result["token"]["tokens"][
            "access_token"
        ]
        result["cookie"] = {}
        result["cookie"]["expired"] = data["cookie_info"]["cookies"][0]["expires"]
        result["cookie"]["cookies"] = {
            cookie["name"]: cookie["value"] for cookie in data["cookie_info"]["cookies"]
        }
        return result

    async def refresh(self) -> "Auth":
        from ..login import refresh_token

        resp = await refresh_token(auth=self)
        self.data = self.refresh_handler(resp)
        return self

    async def get_info(self):
        from ..login import get_token_info

        return await get_token_info(self)


class WebAuth(collections.UserDict):
    def __init__(self, auth: T_Auth = None):
        super().__init__()
        self.update({"refresh_token": None, "cookies": {}})
        if auth:
            self.update(auth)
        # self.update(kwargs)

    def __bool__(self):
        return bool(self.refresh_token) and bool(self.cookies)

    @property
    def uid(self):
        return self["cookies"].get("DedeUserID")

    @property
    def DedeUserID(self):
        return self["cookies"].get("DedeUserID")

    @property
    def bili_jct(self):
        return self["cookies"].get("bili_jct")

    @property
    def csrf(self):
        return self["cookies"].get("bili_jct")

    @property
    def refresh_token(self):
        return self["refresh_token"]

    @refresh_token.setter
    def refresh_token(self, value):
        self["refresh_token"] = value

    @property
    def cookies(self):
        return self["cookies"]

    @cookies.setter
    def cookies(self, value):
        self["cookies"] = value

    def refresh_handler(self, refresh_token, cookies):
        result = {}
        result["refresh_token"] = refresh_token
        result["cookies"] = cookies
        return result

    async def refresh(self) -> "Auth":
        from ..login.web_qrcode_login import (
            refresh_cookie,
            confirm_refresh_cookie,
        )

        refresh_csrf = await self.get_refresh_csrf()
        resp = await refresh_cookie(
            auth=self, cookies=self.cookies, refresh_csrf=refresh_csrf
        )
        new_refresh_token = resp["refresh_token"]
        await confirm_refresh_cookie(auth=self)
        self.refresh_token = new_refresh_token
        return self

    async def check_cookie_status(self):
        from ..login.web_qrcode_login import check_cookie_status

        return await check_cookie_status(auth=self)

    async def get_refresh_csrf(self, timestamp=None, **kwargs):
        """
        获取refresh_csrf

        """

        import time
        import binascii
        from httpx import AsyncClient
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP
        from Crypto.Hash import SHA256
        from bilireq.utils import DEFAULT_HEADERS
        from bilireq.exceptions import AuthParamError

        try:
            from lxml import html  # type: ignore
        except ImportError:
            raise ImportError("bilireq[web_qrcode] not installed.")

        if not self.cookies:
            raise AuthParamError("没有cookies")
        timestamp = timestamp if timestamp else round(time.time() * 1000)
        key = RSA.importKey(
            """\
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLgd2OAkcGVtoE3ThUREbio0Eg
Uc/prcajMKXvkCKFCWhJYJcLkcM2DKKcSeFpD/j6Boy538YXnR6VhcuUJOhH2x71
nzPjfdTcqMz7djHum0qSZA0AyCBDABUqCrfNgCiJ00Ra7GmRj+YCK1NJEuewlb40
JNrRuoEUXpabUzGB8QIDAQAB
-----END PUBLIC KEY-----"""
        )
        cipher = PKCS1_OAEP.new(key, SHA256)
        encrypted = cipher.encrypt(f"refresh_{timestamp}".encode())
        correspond_path = binascii.b2a_hex(encrypted).decode()

        async with AsyncClient(verify=False) as client:
            headers = {
                "User-Agent": DEFAULT_HEADERS["User-Agent"],
            }
            resp = await client.request(
                "GET",
                f"https://www.bilibili.com/correspond/1/{correspond_path}",
                headers=headers,
                cookies=self.cookies,
                follow_redirects=True,
            )
            resp.encoding = "utf-8"
        tree = html.fromstring(resp.text)
        content: list = tree.xpath('//div[@id="1-name"]/text()')
        return content[0]
