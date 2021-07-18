from typing import List, Union

from ..utils import get, post

BASE_URL = "https://api.live.bilibili.com"


async def get_rooms_info(uids: List[Union[int, str]]):
    """根据 UID 批量获取直播间信息"""

    url = "/room/v1/Room/get_status_info_by_uids"
    data = {"uids": uids}
    return await post(BASE_URL+url, json=data)


async def get_room_info(uid: Union[int, str]):
    """根据 UID 获取指定直播间信息"""

    url = "/room/v1/Room/getRoomInfoOld"
    params = {"mid": uid}
    return await get(BASE_URL+url, params=params)
