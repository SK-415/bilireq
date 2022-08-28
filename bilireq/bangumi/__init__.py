from ..utils import get

BASE_URL = "https://api.bilibili.com"


async def get_meta(media_id: int, auth=None, reqtype="app", **kwargs):
    """根据番剧 ID 获取番剧元数据信息"""
    url = f"{BASE_URL}/pgc/review/user"
    params = {"media_id": media_id}
    raw_json = await get(
        url, raw=True, params=params, auth=auth, reqtype=reqtype, **kwargs
    )
    return raw_json["result"]
