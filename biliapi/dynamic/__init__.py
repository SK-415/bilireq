from ..utils import get, post

BASE_URL = "https://api.vc.bilibili.com"


async def get_user_dynamics(uid: int, offset: int=0, need_top: bool=False):
    """获取指定用户历史动态"""

    url = "/dynamic_svr/v1/dynamic_svr/space_history"
    params = {
        "host_uid": uid,
        "offset_dynamic_id": offset,
        "need_top": int(bool(need_top))
    }
    return await get(BASE_URL+url, params=params)
