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


class MessagingUpdatePushMessageRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def topics() -> typing.Type['MessagingUpdatePushMessageRequestTopics']:
                return MessagingUpdatePushMessageRequestTopics
        
            @staticmethod
            def users() -> typing.Type['MessagingUpdatePushMessageRequestUsers']:
                return MessagingUpdatePushMessageRequestUsers
        
            @staticmethod
            def targets() -> typing.Type['MessagingUpdatePushMessageRequestTargets']:
                return MessagingUpdatePushMessageRequestTargets
            body = schemas.StrSchema
            data = schemas.DictSchema
            action = schemas.StrSchema
            image = schemas.StrSchema
            icon = schemas.StrSchema
            sound = schemas.StrSchema
            color = schemas.StrSchema
            tag = schemas.StrSchema
            badge = schemas.IntSchema
            draft = schemas.BoolSchema
            scheduledAt = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "topics": topics,
                "users": users,
                "targets": targets,
                "body": body,
                "data": data,
                "action": action,
                "image": image,
                "icon": icon,
                "sound": sound,
                "color": color,
                "tag": tag,
                "badge": badge,
                "draft": draft,
                "scheduledAt": scheduledAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topics"]) -> 'MessagingUpdatePushMessageRequestTopics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> 'MessagingUpdatePushMessageRequestUsers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targets"]) -> 'MessagingUpdatePushMessageRequestTargets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sound"]) -> MetaOapg.properties.sound: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badge"]) -> MetaOapg.properties.badge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduledAt"]) -> MetaOapg.properties.scheduledAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "topics", "users", "targets", "body", "data", "action", "image", "icon", "sound", "color", "tag", "badge", "draft", "scheduledAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topics"]) -> typing.Union['MessagingUpdatePushMessageRequestTopics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union['MessagingUpdatePushMessageRequestUsers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targets"]) -> typing.Union['MessagingUpdatePushMessageRequestTargets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sound"]) -> typing.Union[MetaOapg.properties.sound, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badge"]) -> typing.Union[MetaOapg.properties.badge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduledAt"]) -> typing.Union[MetaOapg.properties.scheduledAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "topics", "users", "targets", "body", "data", "action", "image", "icon", "sound", "color", "tag", "badge", "draft", "scheduledAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        topics: typing.Union['MessagingUpdatePushMessageRequestTopics', schemas.Unset] = schemas.unset,
        users: typing.Union['MessagingUpdatePushMessageRequestUsers', schemas.Unset] = schemas.unset,
        targets: typing.Union['MessagingUpdatePushMessageRequestTargets', schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        sound: typing.Union[MetaOapg.properties.sound, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        badge: typing.Union[MetaOapg.properties.badge, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, bool, schemas.Unset] = schemas.unset,
        scheduledAt: typing.Union[MetaOapg.properties.scheduledAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessagingUpdatePushMessageRequest':
        return super().__new__(
            cls,
            *args,
            title=title,
            topics=topics,
            users=users,
            targets=targets,
            body=body,
            data=data,
            action=action,
            image=image,
            icon=icon,
            sound=sound,
            color=color,
            tag=tag,
            badge=badge,
            draft=draft,
            scheduledAt=scheduledAt,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.messaging_update_push_message_request_targets import MessagingUpdatePushMessageRequestTargets
from appwrite_console_python_sdk.model.messaging_update_push_message_request_topics import MessagingUpdatePushMessageRequestTopics
from appwrite_console_python_sdk.model.messaging_update_push_message_request_users import MessagingUpdatePushMessageRequestUsers
