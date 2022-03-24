import collections
import time

from .._typing import T_Auth


TOKEN_NAMES = ["access_token", "refresh_token"]


class Auth(collections.UserDict):
    def __init__(self, auth: T_Auth = None, uid: int = 0, expired: int = 0, **kwargs):
        super().__init__()
        self.uid = uid
        self.expired = expired
        self.update(auth)
        self.update(kwargs)

    def get_cookies(self):
        return {
            name: value
            for name, value in self.items()
            if value and name not in TOKEN_NAMES
        }

    def get_tokens(self):
        return {name: self.data[name] for name in TOKEN_NAMES if self.get(name)}

    async def refresh(self):
        from ..login import refresh_token

        resp = await refresh_token(auth=self)
        self.uid = resp["token_info"]["mid"]
        self.expired = resp["token_info"]["expires_in"] + int(time.time())
        self.update(
            {
                name: value
                for name, value in resp["token_info"].items()
                if name in TOKEN_NAMES
            }
        )
        self.update(
            {
                cookie["name"]: cookie["value"]
                for cookie in resp["cookie_info"]["cookies"]
            }
        )
        return self

    async def get_info(self):
        from ..login import get_token_info

        return await get_token_info(self)

    def update(self, auth: T_Auth = None):
        if auth:
            super().update(auth)

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return None
