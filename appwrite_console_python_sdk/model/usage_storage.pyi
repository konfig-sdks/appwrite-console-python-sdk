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


class UsageStorage(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    StorageUsage
    """


    class MetaOapg:
        required = {
            "buckets",
            "filesTotal",
            "bucketsTotal",
            "files",
            "range",
            "storage",
            "filesStorageTotal",
        }
        
        class properties:
            range = schemas.StrSchema
            bucketsTotal = schemas.Int32Schema
            filesTotal = schemas.Int32Schema
            filesStorageTotal = schemas.Int32Schema
            
            
            class buckets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Metric']:
                        return Metric
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Metric'], typing.List['Metric']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'buckets':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Metric']:
                        return Metric
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Metric'], typing.List['Metric']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class storage(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Metric']:
                        return Metric
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Metric'], typing.List['Metric']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'storage':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            __annotations__ = {
                "range": range,
                "bucketsTotal": bucketsTotal,
                "filesTotal": filesTotal,
                "filesStorageTotal": filesStorageTotal,
                "buckets": buckets,
                "files": files,
                "storage": storage,
            }
    
    buckets: MetaOapg.properties.buckets
    filesTotal: MetaOapg.properties.filesTotal
    bucketsTotal: MetaOapg.properties.bucketsTotal
    files: MetaOapg.properties.files
    range: MetaOapg.properties.range
    storage: MetaOapg.properties.storage
    filesStorageTotal: MetaOapg.properties.filesStorageTotal
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketsTotal"]) -> MetaOapg.properties.bucketsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filesTotal"]) -> MetaOapg.properties.filesTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filesStorageTotal"]) -> MetaOapg.properties.filesStorageTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buckets"]) -> MetaOapg.properties.buckets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> MetaOapg.properties.storage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["range", "bucketsTotal", "filesTotal", "filesStorageTotal", "buckets", "files", "storage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketsTotal"]) -> MetaOapg.properties.bucketsTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filesTotal"]) -> MetaOapg.properties.filesTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filesStorageTotal"]) -> MetaOapg.properties.filesStorageTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buckets"]) -> MetaOapg.properties.buckets: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> MetaOapg.properties.storage: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["range", "bucketsTotal", "filesTotal", "filesStorageTotal", "buckets", "files", "storage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        buckets: typing.Union[MetaOapg.properties.buckets, list, tuple, ],
        filesTotal: typing.Union[MetaOapg.properties.filesTotal, decimal.Decimal, int, ],
        bucketsTotal: typing.Union[MetaOapg.properties.bucketsTotal, decimal.Decimal, int, ],
        files: typing.Union[MetaOapg.properties.files, list, tuple, ],
        range: typing.Union[MetaOapg.properties.range, str, ],
        storage: typing.Union[MetaOapg.properties.storage, list, tuple, ],
        filesStorageTotal: typing.Union[MetaOapg.properties.filesStorageTotal, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsageStorage':
        return super().__new__(
            cls,
            *args,
            buckets=buckets,
            filesTotal=filesTotal,
            bucketsTotal=bucketsTotal,
            files=files,
            range=range,
            storage=storage,
            filesStorageTotal=filesStorageTotal,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.metric import Metric
