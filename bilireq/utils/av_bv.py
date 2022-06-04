# TODO 对这部分重构
from typing import Union

table = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def av2bv(aid: Union[int, str]) -> str:
    # TODO 没考虑 av 开头的字符串
    aid = int(aid)
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
