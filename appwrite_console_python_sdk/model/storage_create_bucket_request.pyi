# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from appwrite_console_python_sdk import schemas  # noqa: F401


class StorageCreateBucketRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "bucketId",
        }
        
        class properties:
            bucketId = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def permissions() -> typing.Type['StorageCreateBucketRequestPermissions']:
                return StorageCreateBucketRequestPermissions
            fileSecurity = schemas.BoolSchema
            enabled = schemas.BoolSchema
            maximumFileSize = schemas.IntSchema
        
            @staticmethod
            def allowedFileExtensions() -> typing.Type['StorageCreateBucketRequestAllowedFileExtensions']:
                return StorageCreateBucketRequestAllowedFileExtensions
            
            
            class compression(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
                
                @schemas.classproperty
                def GZIP(cls):
                    return cls("gzip")
                
                @schemas.classproperty
                def ZSTD(cls):
                    return cls("zstd")
            encryption = schemas.BoolSchema
            antivirus = schemas.BoolSchema
            __annotations__ = {
                "bucketId": bucketId,
                "name": name,
                "permissions": permissions,
                "fileSecurity": fileSecurity,
                "enabled": enabled,
                "maximumFileSize": maximumFileSize,
                "allowedFileExtensions": allowedFileExtensions,
                "compression": compression,
                "encryption": encryption,
                "antivirus": antivirus,
            }
    
    name: MetaOapg.properties.name
    bucketId: MetaOapg.properties.bucketId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'StorageCreateBucketRequestPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSecurity"]) -> MetaOapg.properties.fileSecurity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumFileSize"]) -> MetaOapg.properties.maximumFileSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedFileExtensions"]) -> 'StorageCreateBucketRequestAllowedFileExtensions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compression"]) -> MetaOapg.properties.compression: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encryption"]) -> MetaOapg.properties.encryption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["antivirus"]) -> MetaOapg.properties.antivirus: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bucketId", "name", "permissions", "fileSecurity", "enabled", "maximumFileSize", "allowedFileExtensions", "compression", "encryption", "antivirus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['StorageCreateBucketRequestPermissions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSecurity"]) -> typing.Union[MetaOapg.properties.fileSecurity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumFileSize"]) -> typing.Union[MetaOapg.properties.maximumFileSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedFileExtensions"]) -> typing.Union['StorageCreateBucketRequestAllowedFileExtensions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compression"]) -> typing.Union[MetaOapg.properties.compression, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encryption"]) -> typing.Union[MetaOapg.properties.encryption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["antivirus"]) -> typing.Union[MetaOapg.properties.antivirus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bucketId", "name", "permissions", "fileSecurity", "enabled", "maximumFileSize", "allowedFileExtensions", "compression", "encryption", "antivirus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        bucketId: typing.Union[MetaOapg.properties.bucketId, str, ],
        permissions: typing.Union['StorageCreateBucketRequestPermissions', schemas.Unset] = schemas.unset,
        fileSecurity: typing.Union[MetaOapg.properties.fileSecurity, bool, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        maximumFileSize: typing.Union[MetaOapg.properties.maximumFileSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        allowedFileExtensions: typing.Union['StorageCreateBucketRequestAllowedFileExtensions', schemas.Unset] = schemas.unset,
        compression: typing.Union[MetaOapg.properties.compression, str, schemas.Unset] = schemas.unset,
        encryption: typing.Union[MetaOapg.properties.encryption, bool, schemas.Unset] = schemas.unset,
        antivirus: typing.Union[MetaOapg.properties.antivirus, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StorageCreateBucketRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            bucketId=bucketId,
            permissions=permissions,
            fileSecurity=fileSecurity,
            enabled=enabled,
            maximumFileSize=maximumFileSize,
            allowedFileExtensions=allowedFileExtensions,
            compression=compression,
            encryption=encryption,
            antivirus=antivirus,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.storage_create_bucket_request_allowed_file_extensions import StorageCreateBucketRequestAllowedFileExtensions
from appwrite_console_python_sdk.model.storage_create_bucket_request_permissions import StorageCreateBucketRequestPermissions
