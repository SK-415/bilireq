"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GameNotifyReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    type: builtins.int
    """类型字段"""

    data: typing.Text
    """数据字段"""

    def __init__(self,
        *,
        type: builtins.int = ...,
        data: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","type",b"type"]) -> None: ...
global___GameNotifyReply = GameNotifyReply
