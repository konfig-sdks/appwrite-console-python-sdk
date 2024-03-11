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


class AlgoScrypt(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    AlgoScrypt
    """


    class MetaOapg:
        required = {
            "costCpu",
            "length",
            "costMemory",
            "type",
            "costParallel",
        }
        
        class properties:
            type = schemas.StrSchema
            costCpu = schemas.Int32Schema
            costMemory = schemas.Int32Schema
            costParallel = schemas.Int32Schema
            length = schemas.Int32Schema
            __annotations__ = {
                "type": type,
                "costCpu": costCpu,
                "costMemory": costMemory,
                "costParallel": costParallel,
                "length": length,
            }
    
    costCpu: MetaOapg.properties.costCpu
    length: MetaOapg.properties.length
    costMemory: MetaOapg.properties.costMemory
    type: MetaOapg.properties.type
    costParallel: MetaOapg.properties.costParallel
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costCpu"]) -> MetaOapg.properties.costCpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costMemory"]) -> MetaOapg.properties.costMemory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["costParallel"]) -> MetaOapg.properties.costParallel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "costCpu", "costMemory", "costParallel", "length", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costCpu"]) -> MetaOapg.properties.costCpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costMemory"]) -> MetaOapg.properties.costMemory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["costParallel"]) -> MetaOapg.properties.costParallel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "costCpu", "costMemory", "costParallel", "length", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        costCpu: typing.Union[MetaOapg.properties.costCpu, decimal.Decimal, int, ],
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, ],
        costMemory: typing.Union[MetaOapg.properties.costMemory, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        costParallel: typing.Union[MetaOapg.properties.costParallel, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AlgoScrypt':
        return super().__new__(
            cls,
            *args,
            costCpu=costCpu,
            length=length,
            costMemory=costMemory,
            type=type,
            costParallel=costParallel,
            _configuration=_configuration,
            **kwargs,
        )
