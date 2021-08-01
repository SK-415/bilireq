from typing import Dict, Union


class Token:
    def __init__(
        self,
        *,
        token: Union[Dict[str, str], "Token"] = None,
        access_token: str = None,
        refresh_token: str = None,
        sessdata: str = None,
        bili_jct: str = None
    ):
        self.update(
            token, access_token=access_token, refresh_token=refresh_token,
            sessdata=sessdata, bili_jct=bili_jct
        )

    def _has_access_token(self, raise_error: bool = True) -> bool:
        if not raise_error:
            return bool(self.access_token)
        if not self.access_token:
            raise ValueError("access_token 不存在")
        return True

    def _has_refresh_token(self, raise_error: bool = True) -> bool:
        if not raise_error:
            return bool(self.refresh_token)
        if not self.refresh_token:
            raise ValueError("refresh_token 不存在")
        return True

    def _has_sessdata(self, raise_error: bool = True) -> bool:
        if not raise_error:
            return bool(self.sessdata)
        if not self.sessdata:
            raise ValueError("sessdata 不存在")
        return True

    def _has_bili_jct(self, raise_error: bool = True) -> bool:
        if not raise_error:
            return bool(self.bili_jct)
        if not self.bili_jct:
            raise ValueError("bili_jct 不存在")
        return True

    @property
    def has_access_token(self) -> bool:
        return self._has_access_token(False)
    
    @property
    def has_refresh_token(self) -> bool:
        return self._has_refresh_token(False)
    
    @property
    def has_sessdata(self) -> bool:
        return self._has_sessdata(False)
    
    @property
    def has_bili_jct(self) -> bool:
        return self._has_bili_jct(False)

    def update(
        self,
        token: Union[Dict[str, str], "Token", None] = None,
        *,
        access_token: str = None,
        refresh_token: str = None,
        sessdata: str = None,
        bili_jct: str = None
    ):
        token = {} if token is None else dict(token)
        self.access_token = token.get("access_token") and access_token
        self.refresh_token = token.get("refresh_token") and refresh_token
        self.sessdata = token.get("sessdata") and sessdata
        self.bili_jct = token.get("bili_jct") and bili_jct
        return self
    
    async def refresh(self):
        if self._has_access_token() or not self._has_refresh_token():
            raise ValueError

    def keys(self):
        return ("access_token", "refresh_token", "sessdata", "bili_jct")
    
    def __getitem__(self, key):
        return getattr(self, key)


if __name__ == "__main__":
    token = Token()
    print(dict(token))
    