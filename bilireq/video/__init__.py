from typing import Union

from bilireq.utils import get, post
from bilireq.utils.av_bv import bv2av


async def get_video_base_info(video_id: Union[int, str]):
    """获取哔哩哔哩视频基本信息"""
    base_url = "https://api.bilibili.com/x/web-interface/view"
    if isinstance(video_id, int):
        url = f"{base_url}?aid={video_id}"
    elif video_id[:2].lower() == "av" and video_id[2:].isdigit():
        url = f"{base_url}?aid={video_id[2:]}"
    elif video_id[:2].lower() == "bv":
        url = f"{base_url}?bvid={video_id}"
    else:
        raise ValueError(f"{video_id} 不是一个有效的 AV 或 BV 号")
    return await get(url)


async def get_video_share(video_id: Union[int, str]):
    """模拟移动端哔哩哔哩视频分享点击"""
    if isinstance(video_id, int):
        av_id = video_id
    elif video_id[:2].lower() == "av" and video_id[2:].isdigit():
        av_id = int(video_id[2:])
    elif video_id[:2].lower() == "bv":
        av_id = bv2av(video_id)
    else:
        raise ValueError(f"{video_id} 不是一个有效的 AV 或 BV 号")

    body = {
        "build": "6060600",
        "buvid": "0",
        "oid": av_id,
        "platform": "android",
        "share_channel": "QQ",
        "share_id": "main.ugc-video-detail.0.0.pv",
        "share_mode": "7",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = "https://api.biliapi.net/x/share/click"
    return await post(url, data=body, headers=headers)
