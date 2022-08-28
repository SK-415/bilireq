from ..utils import get

BASE_URL = "https://api.vc.bilibili.com"


async def get_user_dynamics(
    uid: int,
    offset: int = 0,
    need_top: bool = False,
    *,
    auth=None,
    reqtype="app",
    **kwargs,
):
    """获取指定用户历史动态"""
    url = f"{BASE_URL}/dynamic_svr/v1/dynamic_svr/space_history"
    params = {
        "host_uid": uid,
        "offset_dynamic_id": offset,
        "need_top": int(bool(need_top)),
    }
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)


async def get_followed_new_dynamics(*, auth, reqtype="web", **kwargs):
    """获取最新关注动态"""
    url = f"{BASE_URL}/dynamic_svr/v1/dynamic_svr/dynamic_new"
    params = {
        "type_list": 268435455,
    }
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)


async def get_followed_history_dynamics(offset: int, *, auth, reqtype="web", **kwargs):
    """获取历史关注动态"""
    url = f"{BASE_URL}/dynamic_svr/v1/dynamic_svr/dynamic_history"
    params = {
        "type_list": 268435455,
        "offset_dynamic_id": offset,
    }
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)


async def get_followed_dynamics_update_info(offset=0, *, auth, reqtype="web", **kwargs):
    """获取关注动态更新信息"""
    url = f"{BASE_URL}/dynamic_svr/v1/dynamic_svr/web_cyclic_num"
    params = {
        "type_list": 268435455,
        "offset": offset,
    }
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)
