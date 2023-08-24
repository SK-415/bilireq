"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DynamicAutoPlay(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value:
        """"""
    def __init__(
        self,
        *,
        value: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

global___DynamicAutoPlay = DynamicAutoPlay

@typing_extensions.final
class DynamicDeviceConfig(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTO_PLAY_FIELD_NUMBER: builtins.int
    @property
    def auto_play(self) -> global___DynamicAutoPlay:
        """"""
    def __init__(
        self,
        *,
        auto_play: global___DynamicAutoPlay | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["auto_play", b"auto_play"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_play", b"auto_play"]) -> None: ...

global___DynamicDeviceConfig = DynamicDeviceConfig