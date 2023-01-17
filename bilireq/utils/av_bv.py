# TODO 对这部分重构
from re import compile
from typing import Union


class VideoID:
    # 哔哩哔哩视频ID类
    # TODO 对avid>=29460791296进行处理（虽然这种情况还很遥远）
    def __init__(self, id: Union[int, str]):
        if isinstance(id, int):
            self.aid = id
            self.bvid = av2bv(id)
        else:
            # 构造正则表达式对象
            av_pattern = compile(r"av[0-9]*")
            bv_pattern = compile(r"BV1[A-Za-z0-9]{9}")
            if av_pattern.match(id):
                self.aid = int(id[2:])
                self.bvid = av2bv(self.aid)
            elif bv_pattern.match(id):
                # 进一步判断是否为合法的视频id
                if id[5] != "4":
                    raise ValueError("Invalid video id.")
                elif id[7] != "1":
                    raise ValueError("Invalid video id.")
                elif id[9] != "7":
                    raise ValueError("Invalid video id.")
                self.bvid = id
                self.aid = bv2av(id)
            else:
                raise ValueError("Invalid video id.")


table = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def av2bv(aid: int) -> str:
    aid = (aid ^ xor) + add
    r = list("BV1  4 1 7  ")
    for i in range(6):
        r[s[i]] = table[aid // 58**i % 58]
    return "".join(r)


def bv2av(bid: str) -> int:
    r = 0
    for i in range(6):
        r += tr[bid[s[i]]] * 58**i
    return (r - add) ^ xor
