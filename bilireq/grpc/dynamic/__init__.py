import json

from ..protos.bilibili.app.dynamic.v2.dynamic_pb2 import (
    DynAllReply,
    DynAllReq,
    DynMixUpListViewMoreReply,
    DynMixUpListViewMoreReq,
    DynSpaceReq,
    DynSpaceRsp,
    DynDetailsReq,
    DynDetailsReply,
    DynDetailReq,
    DynDetailReply,
    AdParam,
)
from ..protos.bilibili.app.dynamic.v2.dynamic_pb2_grpc import DynamicStub
from ..utils import grpc_request


@grpc_request
async def grpc_get_user_dynamics(uid: int, offset: str = "", page: int = 1, **kwargs) -> DynSpaceRsp:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynSpaceReq(host_uid=uid, history_offset=offset, page=page)
    return await stub.DynSpace(req, **kwargs)


@grpc_request
async def grpc_get_followed_dynamics(**kwargs) -> DynAllReply:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynAllReq()
    return await stub.DynAll(req, **kwargs)


@grpc_request
async def grpc_get_followed_dynamic_users(**kwargs) -> DynMixUpListViewMoreReply:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynMixUpListViewMoreReq(sort_type=1)
    return await stub.DynMixUpListViewMore(req, **kwargs)


@grpc_request
async def grpc_get_dynamic_details(dynamic_ids: list[int], **kwargs) -> DynDetailsReply:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynDetailsReq(dynamic_ids=json.dumps({"dyn_ids": dynamic_ids}))
    return await stub.DynDetails(req, **kwargs)


@grpc_request
async def grpc_get_dynamic_detail(dynamic_id: str, **kwargs) -> DynDetailReply:
    stub = DynamicStub(kwargs.pop("_channel"))
    req = DynDetailReq(dynamic_id=dynamic_id)
    return await stub.DynDetail(req, **kwargs)
