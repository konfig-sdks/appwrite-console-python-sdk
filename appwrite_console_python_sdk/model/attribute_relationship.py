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


class AttributeRelationship(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    AttributeRelationship
    """


    class MetaOapg:
        required = {
            "relationType",
            "onDelete",
            "twoWay",
            "side",
            "relatedCollection",
            "twoWayKey",
            "error",
            "type",
            "key",
            "required",
            "status",
        }
        
        class properties:
            key = schemas.StrSchema
            type = schemas.StrSchema
            status = schemas.StrSchema
            error = schemas.StrSchema
            required = schemas.BoolSchema
            relatedCollection = schemas.StrSchema
            relationType = schemas.StrSchema
            twoWay = schemas.BoolSchema
            twoWayKey = schemas.StrSchema
            onDelete = schemas.StrSchema
            side = schemas.StrSchema
            
            
            class array(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'array':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "key": key,
                "type": type,
                "status": status,
                "error": error,
                "required": required,
                "relatedCollection": relatedCollection,
                "relationType": relationType,
                "twoWay": twoWay,
                "twoWayKey": twoWayKey,
                "onDelete": onDelete,
                "side": side,
                "array": array,
            }
    
    relationType: MetaOapg.properties.relationType
    onDelete: MetaOapg.properties.onDelete
    twoWay: MetaOapg.properties.twoWay
    side: MetaOapg.properties.side
    relatedCollection: MetaOapg.properties.relatedCollection
    twoWayKey: MetaOapg.properties.twoWayKey
    error: MetaOapg.properties.error
    type: MetaOapg.properties.type
    key: MetaOapg.properties.key
    required: MetaOapg.properties.required
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatedCollection"]) -> MetaOapg.properties.relatedCollection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationType"]) -> MetaOapg.properties.relationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoWay"]) -> MetaOapg.properties.twoWay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoWayKey"]) -> MetaOapg.properties.twoWayKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onDelete"]) -> MetaOapg.properties.onDelete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["side"]) -> MetaOapg.properties.side: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array"]) -> MetaOapg.properties.array: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "type", "status", "error", "required", "relatedCollection", "relationType", "twoWay", "twoWayKey", "onDelete", "side", "array", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatedCollection"]) -> MetaOapg.properties.relatedCollection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationType"]) -> MetaOapg.properties.relationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoWay"]) -> MetaOapg.properties.twoWay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoWayKey"]) -> MetaOapg.properties.twoWayKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onDelete"]) -> MetaOapg.properties.onDelete: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["side"]) -> MetaOapg.properties.side: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["array"]) -> typing.Union[MetaOapg.properties.array, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "type", "status", "error", "required", "relatedCollection", "relationType", "twoWay", "twoWayKey", "onDelete", "side", "array", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        relationType: typing.Union[MetaOapg.properties.relationType, str, ],
        onDelete: typing.Union[MetaOapg.properties.onDelete, str, ],
        twoWay: typing.Union[MetaOapg.properties.twoWay, bool, ],
        side: typing.Union[MetaOapg.properties.side, str, ],
        relatedCollection: typing.Union[MetaOapg.properties.relatedCollection, str, ],
        twoWayKey: typing.Union[MetaOapg.properties.twoWayKey, str, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        array: typing.Union[MetaOapg.properties.array, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttributeRelationship':
        return super().__new__(
            cls,
            *args,
            relationType=relationType,
            onDelete=onDelete,
            twoWay=twoWay,
            side=side,
            relatedCollection=relatedCollection,
            twoWayKey=twoWayKey,
            error=error,
            type=type,
            key=key,
            required=required,
            status=status,
            array=array,
            _configuration=_configuration,
            **kwargs,
        )