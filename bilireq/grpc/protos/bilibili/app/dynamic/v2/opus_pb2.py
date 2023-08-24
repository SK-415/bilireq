# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/dynamic/v2/opus.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.app.archive.middleware.v1 import preload_pb2 as bilibili_dot_app_dot_archive_dot_middleware_dot_v1_dot_preload__pb2
from bilireq.grpc.protos.bilibili.app.dynamic.v2 import dynamic_pb2 as bilibili_dot_app_dot_dynamic_dot_v2_dot_dynamic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"bilibili/app/dynamic/v2/opus.proto\x12\x17\x62ilibili.app.dynamic.v2\x1a\x30\x62ilibili/app/archive/middleware/v1/preload.proto\x1a%bilibili/app/dynamic/v2/dynamic.proto\"\x94\x02\n\rOpusDetailReq\x12\x34\n\topus_type\x18\x01 \x01(\x0e\x32!.bilibili.app.dynamic.v2.OpusType\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x10\n\x08\x64yn_type\x18\x03 \x01(\x03\x12\x10\n\x08share_id\x18\x04 \x01(\t\x12\x12\n\nshare_mode\x18\t \x01(\x05\x12\x12\n\nlocal_time\x18\n \x01(\x05\x12\x43\n\x0bplayer_args\x18\x0b \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\x12/\n\x06\x63onfig\x18\x0c \x01(\x0b\x32\x1f.bilibili.app.dynamic.v2.Config\"F\n\x0eOpusDetailResp\x12\x34\n\topus_item\x18\x01 \x01(\x0b\x32!.bilibili.app.dynamic.v2.OpusItem\"\xc1\x01\n\x08OpusItem\x12\x0f\n\x07opus_id\x18\x01 \x01(\x03\x12\x34\n\topus_type\x18\x02 \x01(\x0e\x32!.bilibili.app.dynamic.v2.OpusType\x12\x0b\n\x03oid\x18\x03 \x01(\x03\x12\x30\n\x07modules\x18\x04 \x03(\x0b\x32\x1f.bilibili.app.dynamic.v2.Module\x12/\n\x06\x65xtend\x18\x05 \x01(\x0b\x32\x1f.bilibili.app.dynamic.v2.Extend*\\\n\x08OpusType\x12\x11\n\rOPUS_TYPE_DYN\x10\x00\x12\x15\n\x11OPUS_TYPE_ARTICLE\x10\x01\x12\x12\n\x0eOPUS_TYPE_NOTE\x10\x02\x12\x12\n\x0eOPUS_TYPE_WORD\x10\x03\x32\x65\n\x04Opus\x12]\n\nOpusDetail\x12&.bilibili.app.dynamic.v2.OpusDetailReq\x1a\'.bilibili.app.dynamic.v2.OpusDetailRespb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.dynamic.v2.opus_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_OPUSTYPE']._serialized_start=699
  _globals['_OPUSTYPE']._serialized_end=791
  _globals['_OPUSDETAILREQ']._serialized_start=153
  _globals['_OPUSDETAILREQ']._serialized_end=429
  _globals['_OPUSDETAILRESP']._serialized_start=431
  _globals['_OPUSDETAILRESP']._serialized_end=501
  _globals['_OPUSITEM']._serialized_start=504
  _globals['_OPUSITEM']._serialized_end=697
  _globals['_OPUS']._serialized_start=793
  _globals['_OPUS']._serialized_end=894
# @@protoc_insertion_point(module_scope)