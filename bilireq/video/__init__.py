from typing import Union
from bilireq.utils import get, post
from bilireq.utils.av_bv import VideoID


async def get_video_base_info(video_id: Union[int, str]):
    """获取哔哩哔哩视频基本信息"""
    url = "https://api.bilibili.com/x/web-interface/view"
    vid = VideoID(video_id)
    params = {"aid": vid.aid}
    return await get(url, params=params)


async def get_video_share(video_id: Union[int, str]):
    """模拟移动端哔哩哔哩视频分享点击"""
    vid = VideoID(video_id)
    body = {
        "build": "6060600",
        "buvid": "0",
        "oid": vid.aid,
        "platform": "android",
        "share_channel": "QQ",
        "share_id": "main.ugc-video-detail.0.0.pv",
        "share_mode": "7",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = "https://api.biliapi.net/x/share/click"
    return await post(url, data=body, headers=headers)
