from typing import Union
from ..utils import get, post

BASE_URL = "https://api.bilibili.com"


async def get_user_info(uid: Union[int, str]):
    """根据 UID 获取指定用户信息"""

    url = "/x/space/acc/info"
    params = {"mid": uid}
    return await get(BASE_URL+url, params=params)