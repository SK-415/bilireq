# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/pgc/service/premiere/v1/premiere.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bilibili/pgc/service/premiere/v1/premiere.proto\x12 bilibili.pgc.service.premiere.v1\"\"\n\x11PremiereStatusReq\x12\r\n\x05\x65p_id\x18\x01 \x01(\x03\"\x92\x01\n\x13PremiereStatusReply\x12\x10\n\x08progress\x18\x01 \x01(\x03\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x12\n\ndelay_time\x18\x03 \x01(\x03\x12\x14\n\x0conline_count\x18\x04 \x01(\x03\x12\x0e\n\x06status\x18\x05 \x01(\x05\x12\x1b\n\x13\x61\x66ter_premiere_type\x18\x06 \x01(\x05\x32\x80\x01\n\x08Premiere\x12t\n\x06Status\x12\x33.bilibili.pgc.service.premiere.v1.PremiereStatusReq\x1a\x35.bilibili.pgc.service.premiere.v1.PremiereStatusReplyb\x06proto3')



_PREMIERESTATUSREQ = DESCRIPTOR.message_types_by_name['PremiereStatusReq']
_PREMIERESTATUSREPLY = DESCRIPTOR.message_types_by_name['PremiereStatusReply']
PremiereStatusReq = _reflection.GeneratedProtocolMessageType('PremiereStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _PREMIERESTATUSREQ,
  '__module__' : 'bilibili.pgc.service.premiere.v1.premiere_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.pgc.service.premiere.v1.PremiereStatusReq)
  })
_sym_db.RegisterMessage(PremiereStatusReq)

PremiereStatusReply = _reflection.GeneratedProtocolMessageType('PremiereStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _PREMIERESTATUSREPLY,
  '__module__' : 'bilibili.pgc.service.premiere.v1.premiere_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.pgc.service.premiere.v1.PremiereStatusReply)
  })
_sym_db.RegisterMessage(PremiereStatusReply)

_PREMIERE = DESCRIPTOR.services_by_name['Premiere']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREMIERESTATUSREQ._serialized_start=85
  _PREMIERESTATUSREQ._serialized_end=119
  _PREMIERESTATUSREPLY._serialized_start=122
  _PREMIERESTATUSREPLY._serialized_end=268
  _PREMIERE._serialized_start=271
  _PREMIERE._serialized_end=399
# @@protoc_insertion_point(module_scope)
