import hashlib
import random
from typing import Optional

from ..._typing import T_Auth
from ..protos.bilibili.metadata.device.device_pb2 import Device
from ..protos.bilibili.metadata.locale.locale_pb2 import Locale
from ..protos.bilibili.metadata.metadata_pb2 import Metadata
from ..protos.bilibili.metadata.network.network_pb2 import Network, NetworkType


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
    fake_mac = ("XY" + md5_mac[2] + md5_mac[12] + md5_mac[22] + md5_mac_str).upper()
    return fake_mac


BUVID = fake_buvid()


def make_metadata(auth: T_Auth = None, access_key: Optional[str] = None):
    if not access_key and auth:
        access_key = auth["access_token"]
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
    }
    if access_key:
        metadata["authorization"] = f"identify_v1 {access_key}".encode()
    return tuple(metadata.items())
