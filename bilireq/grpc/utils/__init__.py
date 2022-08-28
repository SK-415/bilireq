from functools import wraps
from typing import Any, List, Optional, Tuple

import grpc
from google.protobuf.json_format import MessageToDict
from grpc import RpcError

from ..._typing import T_Auth
from ...exceptions import GrpcError
from ..protos.bilibili.rpc.status_pb2 import Status
from .metadata import make_metadata

# _channel = None


# async def get_channel():
#     global _channel
#     if _channel is None or _channel.get_state() == grpc.ChannelConnectivity.SHUTDOWN:
#         _channel = grpc.aio.secure_channel(
#             "grpc.biliapi.net",
#             grpc.ssl_channel_credentials(),
#             options=[("grpc.keepalive_time_ms", 10000)],
#         )
#     return _channel


def grpc_request(func):
    @wraps(func)
    async def wrapper(
        *args,
        proxy=None,
        auth: T_Auth = None,
        access_key: Optional[str] = None,
        timeout: int = 10,
        to_dict: bool = False,
        **kwargs
    ):
        options: List[Tuple[str, Any]] = [
            # ("grpc.keepalive_timeout_ms", 10000),
            ("grpc.http_proxy", proxy or ""),
        ]
        async with grpc.aio.secure_channel(
            "grpc.biliapi.net",
            grpc.ssl_channel_credentials(),
            options=options,
        ) as channel:
            try:
                result = await func(
                    *args,
                    _channel=channel,
                    metadata=make_metadata(auth, access_key),
                    timeout=timeout,
                    **kwargs
                )
                if to_dict:
                    result = MessageToDict(result)
                return result
            except RpcError as e:
                status = e.trailing_metadata().get(  # type: ignore
                    "grpc-status-details-bin"
                )
                if not status:
                    raise
                status_dict = MessageToDict(Status.FromString(status))
                if status_dict["code"] == 2:
                    raise GrpcError(
                        status_dict["details"][0]["code"],
                        status_dict["details"][0]["message"],
                    )
                else:
                    raise GrpcError(status_dict["code"], status_dict["message"])

    return wrapper
