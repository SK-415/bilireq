from typing import Union

from ..utils import get

BASE_URL = "https://api.bilibili.com"


async def get_user_info(uid: Union[int, str], *, auth=None, reqtype="app", **kwargs):
    """根据 UID 获取指定用户信息"""
    url = f"{BASE_URL}/x/space/wbi/acc/info"
    params = {"mid": uid}
    return await get(
        url, params=params, auth=auth, reqtype=reqtype, is_wbi=True, **kwargs
    )


async def get_videos(
    uid: int,
    tid: int = 0,
    pn: int = 1,
    keyword: str = "",
    order: str = "pubdate",
    *,
    auth=None,
    reqtype="app",
    **kwargs,
):
    """
    获取用户投该视频信息

    :param uid: 用户 UID
    :param tid: 分区 ID
    :param pn: 页码
    :param keyword: 搜索关键词
    :param order: 排序方式，可以为 “pubdate(上传日期从新到旧), stow(收藏从多到少), click(播放量从多到少)”
    """
    url = f"{BASE_URL}/x/space/arc/search"
    params = {
        "mid": uid,
        "ps": 30,
        "tid": tid,
        "pn": pn,
        "keyword": keyword,
        "order": order,
    }
    return await get(url, params=params, auth=auth, reqtype=reqtype, **kwargs)
