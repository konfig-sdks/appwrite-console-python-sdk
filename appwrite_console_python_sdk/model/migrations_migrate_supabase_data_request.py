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


class MigrationsMigrateSupabaseDataRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "endpoint",
            "password",
            "databaseHost",
            "apiKey",
            "resources",
            "username",
        }
        
        class properties:
        
            @staticmethod
            def resources() -> typing.Type['MigrationsMigrateSupabaseDataRequestResources']:
                return MigrationsMigrateSupabaseDataRequestResources
            endpoint = schemas.StrSchema
            apiKey = schemas.StrSchema
            databaseHost = schemas.StrSchema
            username = schemas.StrSchema
            password = schemas.StrSchema
            port = schemas.IntSchema
            __annotations__ = {
                "resources": resources,
                "endpoint": endpoint,
                "apiKey": apiKey,
                "databaseHost": databaseHost,
                "username": username,
                "password": password,
                "port": port,
            }
    
    endpoint: MetaOapg.properties.endpoint
    password: MetaOapg.properties.password
    databaseHost: MetaOapg.properties.databaseHost
    apiKey: MetaOapg.properties.apiKey
    resources: 'MigrationsMigrateSupabaseDataRequestResources'
    username: MetaOapg.properties.username
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'MigrationsMigrateSupabaseDataRequestResources': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databaseHost"]) -> MetaOapg.properties.databaseHost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resources", "endpoint", "apiKey", "databaseHost", "username", "password", "port", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> 'MigrationsMigrateSupabaseDataRequestResources': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databaseHost"]) -> MetaOapg.properties.databaseHost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resources", "endpoint", "apiKey", "databaseHost", "username", "password", "port", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endpoint: typing.Union[MetaOapg.properties.endpoint, str, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        databaseHost: typing.Union[MetaOapg.properties.databaseHost, str, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, ],
        resources: 'MigrationsMigrateSupabaseDataRequestResources',
        username: typing.Union[MetaOapg.properties.username, str, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MigrationsMigrateSupabaseDataRequest':
        return super().__new__(
            cls,
            *args,
            endpoint=endpoint,
            password=password,
            databaseHost=databaseHost,
            apiKey=apiKey,
            resources=resources,
            username=username,
            port=port,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.migrations_migrate_supabase_data_request_resources import MigrationsMigrateSupabaseDataRequestResources
