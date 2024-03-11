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


class AlgoScryptModified(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    AlgoScryptModified
    """


    class MetaOapg:
        required = {
            "signerKey",
            "salt",
            "saltSeparator",
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
            salt = schemas.StrSchema
            saltSeparator = schemas.StrSchema
            signerKey = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "salt": salt,
                "saltSeparator": saltSeparator,
                "signerKey": signerKey,
            }
    
    signerKey: MetaOapg.properties.signerKey
    salt: MetaOapg.properties.salt
    saltSeparator: MetaOapg.properties.saltSeparator
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salt"]) -> MetaOapg.properties.salt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saltSeparator"]) -> MetaOapg.properties.saltSeparator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signerKey"]) -> MetaOapg.properties.signerKey: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "salt", "saltSeparator", "signerKey", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salt"]) -> MetaOapg.properties.salt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saltSeparator"]) -> MetaOapg.properties.saltSeparator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signerKey"]) -> MetaOapg.properties.signerKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "salt", "saltSeparator", "signerKey", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signerKey: typing.Union[MetaOapg.properties.signerKey, str, ],
        salt: typing.Union[MetaOapg.properties.salt, str, ],
        saltSeparator: typing.Union[MetaOapg.properties.saltSeparator, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AlgoScryptModified':
        return super().__new__(
            cls,
            *args,
            signerKey=signerKey,
            salt=salt,
            saltSeparator=saltSeparator,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
