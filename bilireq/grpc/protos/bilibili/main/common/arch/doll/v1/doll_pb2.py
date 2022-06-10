# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/main/common/arch/doll/v1/doll.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,bilibili/main/common/arch/doll/v1/doll.proto\x12!bilibili.main.common.arch.doll.v1\":\n\x0c\x45rrorRequest\x12\r\n\x05\x65rror\x18\x02 \x01(\x05\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\r\n\x05\x64\x65lay\x18\x03 \x01(\x03\"+\n\rErrorResponse\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\"\x1b\n\x0bPingRequest\x12\x0c\n\x04time\x18\x01 \x01(\x03\"*\n\x0cPingResponse\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\"\x1d\n\nSayRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\":\n\x0bSayResponse\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x32\xc1\x02\n\x04\x45\x63ho\x12g\n\x04Ping\x12..bilibili.main.common.arch.doll.v1.PingRequest\x1a/.bilibili.main.common.arch.doll.v1.PingResponse\x12\x64\n\x03Say\x12-.bilibili.main.common.arch.doll.v1.SayRequest\x1a..bilibili.main.common.arch.doll.v1.SayResponse\x12j\n\x05\x45rror\x12/.bilibili.main.common.arch.doll.v1.ErrorRequest\x1a\x30.bilibili.main.common.arch.doll.v1.ErrorResponseb\x06proto3')



_ERRORREQUEST = DESCRIPTOR.message_types_by_name['ErrorRequest']
_ERRORRESPONSE = DESCRIPTOR.message_types_by_name['ErrorResponse']
_PINGREQUEST = DESCRIPTOR.message_types_by_name['PingRequest']
_PINGRESPONSE = DESCRIPTOR.message_types_by_name['PingResponse']
_SAYREQUEST = DESCRIPTOR.message_types_by_name['SayRequest']
_SAYRESPONSE = DESCRIPTOR.message_types_by_name['SayResponse']
ErrorRequest = _reflection.GeneratedProtocolMessageType('ErrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ERRORREQUEST,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.ErrorRequest)
  })
_sym_db.RegisterMessage(ErrorRequest)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), {
  'DESCRIPTOR' : _ERRORRESPONSE,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.ErrorResponse)
  })
_sym_db.RegisterMessage(ErrorResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

SayRequest = _reflection.GeneratedProtocolMessageType('SayRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAYREQUEST,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.SayRequest)
  })
_sym_db.RegisterMessage(SayRequest)

SayResponse = _reflection.GeneratedProtocolMessageType('SayResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAYRESPONSE,
  '__module__' : 'bilibili.main.common.arch.doll.v1.doll_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.main.common.arch.doll.v1.SayResponse)
  })
_sym_db.RegisterMessage(SayResponse)

_ECHO = DESCRIPTOR.services_by_name['Echo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ERRORREQUEST._serialized_start=83
  _ERRORREQUEST._serialized_end=141
  _ERRORRESPONSE._serialized_start=143
  _ERRORRESPONSE._serialized_end=186
  _PINGREQUEST._serialized_start=188
  _PINGREQUEST._serialized_end=215
  _PINGRESPONSE._serialized_start=217
  _PINGRESPONSE._serialized_end=259
  _SAYREQUEST._serialized_start=261
  _SAYREQUEST._serialized_end=290
  _SAYRESPONSE._serialized_start=292
  _SAYRESPONSE._serialized_end=350
  _ECHO._serialized_start=353
  _ECHO._serialized_end=674
# @@protoc_insertion_point(module_scope)