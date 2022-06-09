from ..protos.bilibili.app.dynamic.v2.dynamic_pb2 import (
    DynAllReq,
    DynMixUpListViewMoreReq,
    DynSpaceReq,
    DynSpaceRsp,
)
from ..protos.bilibili.app.dynamic.v2.dynamic_pb2_grpc import DynamicStub
from ..utils import grpc_request


@grpc_request
async def grpc_get_user_dynamics(
    uid: int, offset: str = "", page: int = 1, **kwargs
) -> DynSpaceRsp:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynSpaceReq(host_uid=uid, history_offset=offset, page=page)
    return await stub.DynSpace(req, **kwargs)


@grpc_request
async def grpc_get_followed_dynamics(**kwargs):
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynAllReq()
    return await stub.DynAll(req, **kwargs)

    # exclude_list = [DynamicType.ad, DynamicType.live, DynamicType.live_rcmd]
    # dynlist = filter(
    #     lambda x: x.card_type not in exclude_list,
    #     resp.dynamic_list.list,
    # )
    # return list(dynlist)


@grpc_request
async def grpc_get_followed_dynamic_users(**kwargs):
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynMixUpListViewMoreReq(sort_type=1)
    return await stub.DynMixUpListViewMore(req, **kwargs)
