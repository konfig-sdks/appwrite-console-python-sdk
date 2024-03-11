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


class Webhook(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Webhook
    """


    class MetaOapg:
        required = {
            "httpUser",
            "$createdAt",
            "enabled",
            "url",
            "$updatedAt",
            "security",
            "httpPass",
            "signatureKey",
            "name",
            "logs",
            "events",
            "$id",
            "attempts",
        }
        
        class properties:
            security = schemas.BoolSchema
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            name = schemas.StrSchema
            url = schemas.StrSchema
        
            @staticmethod
            def events() -> typing.Type['WebhookEvents']:
                return WebhookEvents
            httpUser = schemas.StrSchema
            httpPass = schemas.StrSchema
            signatureKey = schemas.StrSchema
            enabled = schemas.BoolSchema
            logs = schemas.StrSchema
            attempts = schemas.Int32Schema
            __annotations__ = {
                "security": security,
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "name": name,
                "url": url,
                "events": events,
                "httpUser": httpUser,
                "httpPass": httpPass,
                "signatureKey": signatureKey,
                "enabled": enabled,
                "logs": logs,
                "attempts": attempts,
            }
    
    httpUser: MetaOapg.properties.httpUser
    enabled: MetaOapg.properties.enabled
    url: MetaOapg.properties.url
    security: MetaOapg.properties.security
    httpPass: MetaOapg.properties.httpPass
    signatureKey: MetaOapg.properties.signatureKey
    name: MetaOapg.properties.name
    logs: MetaOapg.properties.logs
    events: 'WebhookEvents'
    attempts: MetaOapg.properties.attempts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["security"]) -> MetaOapg.properties.security: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'WebhookEvents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpUser"]) -> MetaOapg.properties.httpUser: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["httpPass"]) -> MetaOapg.properties.httpPass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signatureKey"]) -> MetaOapg.properties.signatureKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attempts"]) -> MetaOapg.properties.attempts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["security", "$id", "$createdAt", "$updatedAt", "name", "url", "events", "httpUser", "httpPass", "signatureKey", "enabled", "logs", "attempts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["security"]) -> MetaOapg.properties.security: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> 'WebhookEvents': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpUser"]) -> MetaOapg.properties.httpUser: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["httpPass"]) -> MetaOapg.properties.httpPass: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signatureKey"]) -> MetaOapg.properties.signatureKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attempts"]) -> MetaOapg.properties.attempts: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["security", "$id", "$createdAt", "$updatedAt", "name", "url", "events", "httpUser", "httpPass", "signatureKey", "enabled", "logs", "attempts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        httpUser: typing.Union[MetaOapg.properties.httpUser, str, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        security: typing.Union[MetaOapg.properties.security, bool, ],
        httpPass: typing.Union[MetaOapg.properties.httpPass, str, ],
        signatureKey: typing.Union[MetaOapg.properties.signatureKey, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        logs: typing.Union[MetaOapg.properties.logs, str, ],
        events: 'WebhookEvents',
        attempts: typing.Union[MetaOapg.properties.attempts, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Webhook':
        return super().__new__(
            cls,
            *args,
            httpUser=httpUser,
            enabled=enabled,
            url=url,
            security=security,
            httpPass=httpPass,
            signatureKey=signatureKey,
            name=name,
            logs=logs,
            events=events,
            attempts=attempts,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.webhook_events import WebhookEvents
