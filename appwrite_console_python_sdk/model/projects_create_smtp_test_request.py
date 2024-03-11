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


class ProjectsCreateSmtpTestRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "emails",
            "senderName",
            "senderEmail",
            "host",
        }
        
        class properties:
        
            @staticmethod
            def emails() -> typing.Type['ProjectsCreateSmtpTestRequestEmails']:
                return ProjectsCreateSmtpTestRequestEmails
            senderName = schemas.StrSchema
            senderEmail = schemas.StrSchema
            host = schemas.StrSchema
            replyTo = schemas.StrSchema
            port = schemas.IntSchema
            username = schemas.StrSchema
            password = schemas.StrSchema
            
            
            class secure(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "tls": "TLS",
                    }
                
                @schemas.classproperty
                def TLS(cls):
                    return cls("tls")
            __annotations__ = {
                "emails": emails,
                "senderName": senderName,
                "senderEmail": senderEmail,
                "host": host,
                "replyTo": replyTo,
                "port": port,
                "username": username,
                "password": password,
                "secure": secure,
            }
    
    emails: 'ProjectsCreateSmtpTestRequestEmails'
    senderName: MetaOapg.properties.senderName
    senderEmail: MetaOapg.properties.senderEmail
    host: MetaOapg.properties.host
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emails"]) -> 'ProjectsCreateSmtpTestRequestEmails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderName"]) -> MetaOapg.properties.senderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderEmail"]) -> MetaOapg.properties.senderEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replyTo"]) -> MetaOapg.properties.replyTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secure"]) -> MetaOapg.properties.secure: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["emails", "senderName", "senderEmail", "host", "replyTo", "port", "username", "password", "secure", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emails"]) -> 'ProjectsCreateSmtpTestRequestEmails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderName"]) -> MetaOapg.properties.senderName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderEmail"]) -> MetaOapg.properties.senderEmail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replyTo"]) -> typing.Union[MetaOapg.properties.replyTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secure"]) -> typing.Union[MetaOapg.properties.secure, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["emails", "senderName", "senderEmail", "host", "replyTo", "port", "username", "password", "secure", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        emails: 'ProjectsCreateSmtpTestRequestEmails',
        senderName: typing.Union[MetaOapg.properties.senderName, str, ],
        senderEmail: typing.Union[MetaOapg.properties.senderEmail, str, ],
        host: typing.Union[MetaOapg.properties.host, str, ],
        replyTo: typing.Union[MetaOapg.properties.replyTo, str, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        secure: typing.Union[MetaOapg.properties.secure, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsCreateSmtpTestRequest':
        return super().__new__(
            cls,
            *args,
            emails=emails,
            senderName=senderName,
            senderEmail=senderEmail,
            host=host,
            replyTo=replyTo,
            port=port,
            username=username,
            password=password,
            secure=secure,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.projects_create_smtp_test_request_emails import ProjectsCreateSmtpTestRequestEmails
