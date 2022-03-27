from typing import Union
from ..utils import get

BASE_URL = "https://api.bilibili.com"


async def get_user_info(uid: Union[int, str], *, auth=None, reqtype="both", **kwargs):
    """根据 UID 获取指定用户信息"""
    url = f"{BASE_URL}/x/space/acc/info"
    params = {"mid": uid}
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)
