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
