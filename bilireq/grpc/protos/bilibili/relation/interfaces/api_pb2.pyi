"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AtSearchReq(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """可以为 1 , 但是不能为 0 或空 不知道有啥用"""
    keyword: builtins.str
    """用户名搜索关键词"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        keyword: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keyword", b"keyword", "mid", b"mid"]) -> None: ...

global___AtSearchReq = AtSearchReq

@typing_extensions.final
class AtSearchReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AtGroup]:
        """搜索结果分组"""
    def __init__(
        self,
        *,
        items: collections.abc.Iterable[global___AtGroup] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items", b"items"]) -> None: ...

global___AtSearchReply = AtSearchReply

@typing_extensions.final
class AtGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_TYPE_FIELD_NUMBER: builtins.int
    GROUP_NAME_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    group_type: builtins.int
    """分组类型  2: 我的关注 4:其他 ,其他自测"""
    group_name: builtins.str
    """分组名称"""
    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AtItem]:
        """用户列表"""
    def __init__(
        self,
        *,
        group_type: builtins.int = ...,
        group_name: builtins.str = ...,
        items: collections.abc.Iterable[global___AtItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_name", b"group_name", "group_type", b"group_type", "items", b"items"]) -> None: ...

global___AtGroup = AtGroup

@typing_extensions.final
class AtItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    FACE_FIELD_NUMBER: builtins.int
    FANS_FIELD_NUMBER: builtins.int
    OFFICIAL_VERIFY_TYPE_FIELD_NUMBER: builtins.int
    mid: builtins.int
    name: builtins.str
    face: builtins.str
    fans: builtins.int
    official_verify_type: builtins.int
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        name: builtins.str = ...,
        face: builtins.str = ...,
        fans: builtins.int = ...,
        official_verify_type: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["face", b"face", "fans", b"fans", "mid", b"mid", "name", b"name", "official_verify_type", b"official_verify_type"]) -> None: ...

global___AtItem = AtItem
