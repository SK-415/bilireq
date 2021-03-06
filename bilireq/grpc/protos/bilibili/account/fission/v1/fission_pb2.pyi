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

class EntranceReq(google.protobuf.message.Message):
    """活动入口-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___EntranceReq = EntranceReq

class EntranceReply(google.protobuf.message.Message):
    """活动入口-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ICON_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    ANIMATE_ICON_FIELD_NUMBER: builtins.int
    icon: typing.Text
    """展示图标"""

    name: typing.Text
    """活动名称"""

    url: typing.Text
    """活动跳转链接"""

    @property
    def animate_icon(self) -> global___AnimateIcon:
        """动画效果"""
        pass
    def __init__(self,
        *,
        icon: typing.Text = ...,
        name: typing.Text = ...,
        url: typing.Text = ...,
        animate_icon: typing.Optional[global___AnimateIcon] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["animate_icon",b"animate_icon"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["animate_icon",b"animate_icon","icon",b"icon","name",b"name","url",b"url"]) -> None: ...
global___EntranceReply = EntranceReply

class WindowReq(google.protobuf.message.Message):
    """首页弹窗-请求"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___WindowReq = WindowReq

class WindowReply(google.protobuf.message.Message):
    """首页弹窗-响应"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    REPORT_DATA_FIELD_NUMBER: builtins.int
    type: builtins.int
    """弹窗类型
    0:弹窗 1:普通页面
    """

    url: typing.Text
    """跳转链接"""

    report_data: typing.Text
    """上报数据字段"""

    def __init__(self,
        *,
        type: builtins.int = ...,
        url: typing.Text = ...,
        report_data: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["report_data",b"report_data","type",b"type","url",b"url"]) -> None: ...
global___WindowReply = WindowReply

class AnimateIcon(google.protobuf.message.Message):
    """动画效果"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ICON_FIELD_NUMBER: builtins.int
    JSON_FIELD_NUMBER: builtins.int
    icon: typing.Text
    """icon文件"""

    json: typing.Text
    """动效json文件"""

    def __init__(self,
        *,
        icon: typing.Text = ...,
        json: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["icon",b"icon","json",b"json"]) -> None: ...
global___AnimateIcon = AnimateIcon
