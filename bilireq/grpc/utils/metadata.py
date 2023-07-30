import hashlib
import random
import base64
import time
from typing import Optional

from ..._typing import T_Auth
from ..protos.bilibili.metadata.device.device_pb2 import Device
from ..protos.bilibili.metadata.locale.locale_pb2 import Locale
from ..protos.bilibili.metadata.metadata_pb2 import Metadata
from ..protos.bilibili.metadata.network.network_pb2 import Network, NetworkType
from ..protos.bilibili.metadata.fawkes.fawkes_pb2 import FawkesReq
from ..protos.bilibili.metadata.restriction.restriction_pb2 import Restriction, ModeType
from ..protos.bilibili.metadata.parabox.parabox_pb2 import Exps


def random_id():
    return "".join(random.sample("0123456789abcdefghijklmnopqrstuvwxyz", 8))


def fake_buvid():
    mac_list = []
    for _ in range(1, 7):
        rand_str = "".join(random.sample("0123456789abcdef", 2))
        mac_list.append(rand_str)
    rand_mac = ":".join(mac_list)
    md5 = hashlib.md5()
    md5.update(rand_mac.encode())
    md5_mac_str = md5.hexdigest()
    md5_mac = list(md5_mac_str)
    return f"XY{md5_mac[2]}{md5_mac[12]}{md5_mac[22]}{md5_mac_str}".upper()


def gen_aurora_eid(uid: int) -> str:
    if uid == 0:
        raise ValueError("uid must not be 0")
    result_byte = bytearray()
    mid_byte = bytearray(str(uid), "utf-8")
    key = bytearray(b"ad1va46a7lza")
    for i, v in enumerate(mid_byte):
        result_byte.append(v ^ key[i % len(key)])
    return base64.b64encode(result_byte).decode("utf-8").rstrip("=")


def gen_trace_id() -> str:
    random_id = "".join(random.choices("0123456789abcdefghijklmnopqrstuvwxyz", k=32))
    random_trace_id = random_id[:24]
    b_arr = [0] * 3
    ts = int(time.time())
    for i in reversed(range(3)):
        ts >>= 8
        b_arr[i] = ts % 256 if (ts // 128) % 2 == 0 else ts % 256 - 256
    for i in range(3):
        random_trace_id += "{:02x}".format(b_arr[i] & 0xFF)
    random_trace_id += random_id[-2:]
    return f"{random_trace_id}:{random_trace_id[16:]}:0:0"


BUVID = fake_buvid()


def make_metadata(auth: T_Auth = None, access_key: Optional[str] = None):
    if access_key:
        raise NotImplementedError("access_key is not supported yet")

    mid = 0
    if auth:
        from ...auth import Auth

        access_key = Auth(auth).access_token
        mid = Auth(auth).uid
    device_params = {
        "mobi_app": "android",
        "device": "phone",
        "build": 6550400,
        "channel": "bili",
        "buvid": BUVID,
        "platform": "android",
    }
    metadata_params = device_params.copy()
    if access_key:
        metadata_params["access_key"] = access_key
    metadata = {
        "x-bili-device-bin": Device(**device_params).SerializeToString(),
        "x-bili-local-bin": Locale().SerializeToString(),
        "x-bili-metadata-bin": Metadata(**metadata_params).SerializeToString(),
        "x-bili-network-bin": Network(type=NetworkType.WIFI).SerializeToString(),
        "x-bili-fawkes-request-bin": FawkesReq(
            appkey="android64", env="prod", session_id=random_id()
        ).SerializeToString(),
        "x-bili-restriction-bin": Restriction(
            teenagers_mode=False, lessons_mode=False, mode=ModeType.NORMAL, review=True, disable_rcmd=False
        ).SerializeToString(),
        "x-bili-exps-bin": Exps().SerializeToString(),
        "x-bili-aurora-zone": "",
        "x-bili-mid": str(mid).encode(),
        "x-bili-trace-id": gen_trace_id(),
        "buvid": BUVID,
    }
    if access_key:
        metadata["authorization"] = f"identify_v1 {access_key}"
        metadata["x-bili-aurora-eid"] = gen_aurora_eid(mid)
    return tuple(metadata.items())
