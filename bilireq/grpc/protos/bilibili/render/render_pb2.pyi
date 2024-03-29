"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Render(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    code: builtins.int
    """"""
    message: builtins.str
    """"""
    ttl: builtins.str
    """"""
    @property
    def data(self) -> google.protobuf.any_pb2.Any:
        """"""
    def __init__(
        self,
        *,
        code: builtins.int = ...,
        message: builtins.str = ...,
        ttl: builtins.str = ...,
        data: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "data", b"data", "message", b"message", "ttl", b"ttl"]) -> None: ...

global___Render = Render
