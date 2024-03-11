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


class Platform(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Platform
    """


    class MetaOapg:
        required = {
            "hostname",
            "httpUser",
            "httpPass",
            "name",
            "$createdAt",
            "store",
            "type",
            "key",
            "$id",
            "$updatedAt",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            key = schemas.StrSchema
            store = schemas.StrSchema
            hostname = schemas.StrSchema
            httpUser = schemas.StrSchema
            httpPass = schemas.StrSchema
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "name": name,
                "type": type,
                "key": key,
                "store": store,
                "hostname": hostname,
                "httpUser": httpUser,
                "httpPass": httpPass,
            }
    
    hostname: MetaOapg.properties.hostname
    httpUser: MetaOapg.properties.httpUser
    httpPass: MetaOapg.properties.httpPass
    name: MetaOapg.properties.name
    store: MetaOapg.properties.store
    type: MetaOapg.properties.type
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["store"]) -> MetaOapg.properties.store: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpUser"]) -> MetaOapg.properties.httpUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpPass"]) -> MetaOapg.properties.httpPass: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "name", "type", "key", "store", "hostname", "httpUser", "httpPass", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["store"]) -> MetaOapg.properties.store: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpUser"]) -> MetaOapg.properties.httpUser: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpPass"]) -> MetaOapg.properties.httpPass: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "name", "type", "key", "store", "hostname", "httpUser", "httpPass", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hostname: typing.Union[MetaOapg.properties.hostname, str, ],
        httpUser: typing.Union[MetaOapg.properties.httpUser, str, ],
        httpPass: typing.Union[MetaOapg.properties.httpPass, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        store: typing.Union[MetaOapg.properties.store, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Platform':
        return super().__new__(
            cls,
            *args,
            hostname=hostname,
            httpUser=httpUser,
            httpPass=httpPass,
            name=name,
            store=store,
            type=type,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )
