# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/polymer/demo/demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bilibili/polymer/demo/demo.proto\x12\x15\x62ilibili.polymer.demo\" \n\rHelloWorldReq\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x1e\n\x0eHelloWorldResp\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\tb\x06proto3')



_HELLOWORLDREQ = DESCRIPTOR.message_types_by_name['HelloWorldReq']
_HELLOWORLDRESP = DESCRIPTOR.message_types_by_name['HelloWorldResp']
HelloWorldReq = _reflection.GeneratedProtocolMessageType('HelloWorldReq', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDREQ,
  '__module__' : 'bilibili.polymer.demo.demo_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.demo.HelloWorldReq)
  })
_sym_db.RegisterMessage(HelloWorldReq)

HelloWorldResp = _reflection.GeneratedProtocolMessageType('HelloWorldResp', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDRESP,
  '__module__' : 'bilibili.polymer.demo.demo_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.demo.HelloWorldResp)
  })
_sym_db.RegisterMessage(HelloWorldResp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOWORLDREQ._serialized_start=59
  _HELLOWORLDREQ._serialized_end=91
  _HELLOWORLDRESP._serialized_start=93
  _HELLOWORLDRESP._serialized_end=123
# @@protoc_insertion_point(module_scope)
