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
class MidPrivacySettingsConfig(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECOMMEND_TO_KNOWN_FIELD_NUMBER: builtins.int
    @property
    def recommend_to_known(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """"""
    def __init__(
        self,
        *,
        recommend_to_known: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["recommend_to_known", b"recommend_to_known"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["recommend_to_known", b"recommend_to_known"]) -> None: ...

global___MidPrivacySettingsConfig = MidPrivacySettingsConfig

@typing_extensions.final
class PrivacySettingsConfig(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AD_RECOMMAND_STORE_FIELD_NUMBER: builtins.int
    SENSOR_ACCESS_FIELD_NUMBER: builtins.int
    @property
    def ad_recommand_store(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """"""
    @property
    def sensor_access(self) -> bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue:
        """传感器权限"""
    def __init__(
        self,
        *,
        ad_recommand_store: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
        sensor_access: bilireq.grpc.protos.bilibili.app.distribution.v1.distribution_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ad_recommand_store", b"ad_recommand_store", "sensor_access", b"sensor_access"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_recommand_store", b"ad_recommand_store", "sensor_access", b"sensor_access"]) -> None: ...

global___PrivacySettingsConfig = PrivacySettingsConfig
