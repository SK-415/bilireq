from typing import Dict


class Token:
    def __init__(
        self,
        *,
        # token: Dict[str, str]= None,
        access_token = None,
        refresh_token = None,
        sessdata = None,
        bili_jct = None
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.sessdata = sessdata
        self.bili_jct = bili_jct
    
    def keys(self):
        return ("access_token", "refresh_token", "sessdata", "bili_jct")
    
    def __getitem__(self, key):
        return getattr(self, key)


if __name__ == "__main__":
    token = Token()
    print(dict(token))
    