from ..protos.bilibili.live.app.room.v1.room_pb2 import GetStudioListReq
from ..protos.bilibili.live.app.room.v1.room_pb2_grpc import StudioListStub
from ..utils import grpc_request


@grpc_request
async def grpc_get_room_info(room_id: int, **kwargs):
    stub = StudioListStub(kwargs.pop("_channel"))
    req = GetStudioListReq(room_id=int(room_id))
    return await stub.GetStudioList(req, **kwargs)
