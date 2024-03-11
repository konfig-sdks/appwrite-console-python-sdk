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


class ProviderRepository(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    ProviderRepository
    """


    class MetaOapg:
        required = {
            "private",
            "provider",
            "organization",
            "name",
            "runtime",
            "id",
            "pushedAt",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            organization = schemas.StrSchema
            provider = schemas.StrSchema
            private = schemas.BoolSchema
            runtime = schemas.StrSchema
            pushedAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "organization": organization,
                "provider": provider,
                "private": private,
                "runtime": runtime,
                "pushedAt": pushedAt,
            }
    
    private: MetaOapg.properties.private
    provider: MetaOapg.properties.provider
    organization: MetaOapg.properties.organization
    name: MetaOapg.properties.name
    runtime: MetaOapg.properties.runtime
    id: MetaOapg.properties.id
    pushedAt: MetaOapg.properties.pushedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runtime"]) -> MetaOapg.properties.runtime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pushedAt"]) -> MetaOapg.properties.pushedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "organization", "provider", "private", "runtime", "pushedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runtime"]) -> MetaOapg.properties.runtime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pushedAt"]) -> MetaOapg.properties.pushedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "organization", "provider", "private", "runtime", "pushedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        private: typing.Union[MetaOapg.properties.private, bool, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        organization: typing.Union[MetaOapg.properties.organization, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        runtime: typing.Union[MetaOapg.properties.runtime, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        pushedAt: typing.Union[MetaOapg.properties.pushedAt, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProviderRepository':
        return super().__new__(
            cls,
            *args,
            private=private,
            provider=provider,
            organization=organization,
            name=name,
            runtime=runtime,
            id=id,
            pushedAt=pushedAt,
            _configuration=_configuration,
            **kwargs,
        )
