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


class Runtime(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Runtime
    """


    class MetaOapg:
        required = {
            "image",
            "name",
            "logo",
            "supports",
            "version",
            "$id",
            "base",
        }
        
        class properties:
            version = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            base = schemas.StrSchema
            image = schemas.StrSchema
            logo = schemas.StrSchema
        
            @staticmethod
            def supports() -> typing.Type['RuntimeSupports']:
                return RuntimeSupports
            __annotations__ = {
                "version": version,
                "$id": id,
                "name": name,
                "base": base,
                "image": image,
                "logo": logo,
                "supports": supports,
            }
    
    image: MetaOapg.properties.image
    name: MetaOapg.properties.name
    logo: MetaOapg.properties.logo
    supports: 'RuntimeSupports'
    version: MetaOapg.properties.version
    base: MetaOapg.properties.base
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base"]) -> MetaOapg.properties.base: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supports"]) -> 'RuntimeSupports': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "$id", "name", "base", "image", "logo", "supports", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base"]) -> MetaOapg.properties.base: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supports"]) -> 'RuntimeSupports': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "$id", "name", "base", "image", "logo", "supports", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        logo: typing.Union[MetaOapg.properties.logo, str, ],
        supports: 'RuntimeSupports',
        version: typing.Union[MetaOapg.properties.version, str, ],
        base: typing.Union[MetaOapg.properties.base, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Runtime':
        return super().__new__(
            cls,
            *args,
            image=image,
            name=name,
            logo=logo,
            supports=supports,
            version=version,
            base=base,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.runtime_supports import RuntimeSupports
