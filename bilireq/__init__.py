import sys
from pathlib import Path

# from .login import Login
from .utils import get, post  # noqa

sys.path.append(str(Path(__file__).absolute().parent / "grpc" / "protos"))

# class BaseAPI:
#     def __init__(
#         self,
#         access_token=None,
#         refresh_token=None,
#         sessdata=None,
#         bili_jct=None,
#         token=None,
#     ):
#         pass


# class Self:
#     def __init__(self, access_token, refresh_token, sessdata, bili_jct):
#         self.access_token = access_token
#         self.refresh_token = refresh_token
#         self.bilisessdata = sessdata
#         self.bilijct = bili_jct
#         self.login = Login()
