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


class UsersCreateWithShaPasswordRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "password",
            "userId",
            "email",
        }
        
        class properties:
            userId = schemas.StrSchema
            email = schemas.StrSchema
            password = schemas.StrSchema
            
            
            class passwordVersion(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SHA1(cls):
                    return cls("sha1")
                
                @schemas.classproperty
                def SHA224(cls):
                    return cls("sha224")
                
                @schemas.classproperty
                def SHA256(cls):
                    return cls("sha256")
                
                @schemas.classproperty
                def SHA384(cls):
                    return cls("sha384")
                
                @schemas.classproperty
                def SHA512_224(cls):
                    return cls("sha512/224")
                
                @schemas.classproperty
                def SHA512_256(cls):
                    return cls("sha512/256")
                
                @schemas.classproperty
                def SHA512(cls):
                    return cls("sha512")
                
                @schemas.classproperty
                def SHA3224(cls):
                    return cls("sha3-224")
                
                @schemas.classproperty
                def SHA3256(cls):
                    return cls("sha3-256")
                
                @schemas.classproperty
                def SHA3384(cls):
                    return cls("sha3-384")
                
                @schemas.classproperty
                def SHA3512(cls):
                    return cls("sha3-512")
            name = schemas.StrSchema
            __annotations__ = {
                "userId": userId,
                "email": email,
                "password": password,
                "passwordVersion": passwordVersion,
                "name": name,
            }
    
    password: MetaOapg.properties.password
    userId: MetaOapg.properties.userId
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordVersion"]) -> MetaOapg.properties.passwordVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userId", "email", "password", "passwordVersion", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordVersion"]) -> typing.Union[MetaOapg.properties.passwordVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userId", "email", "password", "passwordVersion", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        passwordVersion: typing.Union[MetaOapg.properties.passwordVersion, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersCreateWithShaPasswordRequest':
        return super().__new__(
            cls,
            *args,
            password=password,
            userId=userId,
            email=email,
            passwordVersion=passwordVersion,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )