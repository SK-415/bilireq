from bilireq.utils import post
from typing import Union


async def get_video_share(video_id: Union[int, str]):
    """模拟移动端哔哩哔哩视频分享点击"""
    if isinstance(video_id, str):
        if video_id[:2] in ["av", "AV", "aV", "Av"]:
            if video_id[2:].isdigit():
                av_id = int(video_id[2:])
        elif video_id[:2] in ["bv", "BV", "bV", "Bv"]:
            bv_id = video_id
            table = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
            tr = {}
            for i in range(58):
                tr[table[i]] = i
            s = [11, 10, 3, 8, 4, 6]
            xor = 177451812
            add = 8728348608
            r = 0
            for i in range(6):
                r += tr[bv_id[s[i]]] * 58**i
            av_id = (r - add) ^ xor
    else:
        av_id = video_id
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
