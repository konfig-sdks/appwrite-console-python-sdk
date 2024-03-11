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


class MessagingCreateMailgunProviderRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "providerId",
            "name",
        }
        
        class properties:
            providerId = schemas.StrSchema
            name = schemas.StrSchema
            apiKey = schemas.StrSchema
            domain = schemas.StrSchema
            isEuRegion = schemas.BoolSchema
            fromName = schemas.StrSchema
            fromEmail = schemas.StrSchema
            replyToName = schemas.StrSchema
            replyToEmail = schemas.StrSchema
            enabled = schemas.BoolSchema
            __annotations__ = {
                "providerId": providerId,
                "name": name,
                "apiKey": apiKey,
                "domain": domain,
                "isEuRegion": isEuRegion,
                "fromName": fromName,
                "fromEmail": fromEmail,
                "replyToName": replyToName,
                "replyToEmail": replyToEmail,
                "enabled": enabled,
            }
    
    providerId: MetaOapg.properties.providerId
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerId"]) -> MetaOapg.properties.providerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEuRegion"]) -> MetaOapg.properties.isEuRegion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromName"]) -> MetaOapg.properties.fromName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromEmail"]) -> MetaOapg.properties.fromEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replyToName"]) -> MetaOapg.properties.replyToName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replyToEmail"]) -> MetaOapg.properties.replyToEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["providerId", "name", "apiKey", "domain", "isEuRegion", "fromName", "fromEmail", "replyToName", "replyToEmail", "enabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerId"]) -> MetaOapg.properties.providerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> typing.Union[MetaOapg.properties.apiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEuRegion"]) -> typing.Union[MetaOapg.properties.isEuRegion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromName"]) -> typing.Union[MetaOapg.properties.fromName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromEmail"]) -> typing.Union[MetaOapg.properties.fromEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replyToName"]) -> typing.Union[MetaOapg.properties.replyToName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replyToEmail"]) -> typing.Union[MetaOapg.properties.replyToEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["providerId", "name", "apiKey", "domain", "isEuRegion", "fromName", "fromEmail", "replyToName", "replyToEmail", "enabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        providerId: typing.Union[MetaOapg.properties.providerId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, schemas.Unset] = schemas.unset,
        domain: typing.Union[MetaOapg.properties.domain, str, schemas.Unset] = schemas.unset,
        isEuRegion: typing.Union[MetaOapg.properties.isEuRegion, bool, schemas.Unset] = schemas.unset,
        fromName: typing.Union[MetaOapg.properties.fromName, str, schemas.Unset] = schemas.unset,
        fromEmail: typing.Union[MetaOapg.properties.fromEmail, str, schemas.Unset] = schemas.unset,
        replyToName: typing.Union[MetaOapg.properties.replyToName, str, schemas.Unset] = schemas.unset,
        replyToEmail: typing.Union[MetaOapg.properties.replyToEmail, str, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessagingCreateMailgunProviderRequest':
        return super().__new__(
            cls,
            *args,
            providerId=providerId,
            name=name,
            apiKey=apiKey,
            domain=domain,
            isEuRegion=isEuRegion,
            fromName=fromName,
            fromEmail=fromEmail,
            replyToName=replyToName,
            replyToEmail=replyToEmail,
            enabled=enabled,
            _configuration=_configuration,
            **kwargs,
        )
