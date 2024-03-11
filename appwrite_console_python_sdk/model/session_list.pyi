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


class SessionList(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Sessions List
    """


    class MetaOapg:
        required = {
            "sessions",
            "total",
        }
        
        class properties:
            total = schemas.Int32Schema
            
            
            class sessions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Session']:
                        return Session
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Session'], typing.List['Session']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sessions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Session':
                    return super().__getitem__(i)
            __annotations__ = {
                "total": total,
                "sessions": sessions,
            }
    
    sessions: MetaOapg.properties.sessions
    total: MetaOapg.properties.total
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessions"]) -> MetaOapg.properties.sessions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "sessions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessions"]) -> MetaOapg.properties.sessions: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "sessions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sessions: typing.Union[MetaOapg.properties.sessions, list, tuple, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SessionList':
        return super().__new__(
            cls,
            *args,
            sessions=sessions,
            total=total,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.session import Session
