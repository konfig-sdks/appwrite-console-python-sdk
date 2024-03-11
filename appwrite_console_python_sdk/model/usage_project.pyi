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


class UsageProject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    UsageProject
    """


    class MetaOapg:
        required = {
            "usersTotal",
            "executionsTotal",
            "executions",
            "databasesTotal",
            "executionsBreakdown",
            "bucketsTotal",
            "documentsTotal",
            "requests",
            "filesStorageTotal",
            "bucketsBreakdown",
            "users",
            "network",
        }
        
        class properties:
            executionsTotal = schemas.Int32Schema
            documentsTotal = schemas.Int32Schema
            databasesTotal = schemas.Int32Schema
            usersTotal = schemas.Int32Schema
            filesStorageTotal = schemas.Int32Schema
            bucketsTotal = schemas.Int32Schema
            
            
            class requests(
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
                ) -> 'requests':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class network(
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
                ) -> 'network':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class users(
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
                ) -> 'users':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class executions(
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
                ) -> 'executions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Metric':
                    return super().__getitem__(i)
            
            
            class executionsBreakdown(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MetricBreakdown']:
                        return MetricBreakdown
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MetricBreakdown'], typing.List['MetricBreakdown']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'executionsBreakdown':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MetricBreakdown':
                    return super().__getitem__(i)
            
            
            class bucketsBreakdown(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MetricBreakdown']:
                        return MetricBreakdown
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MetricBreakdown'], typing.List['MetricBreakdown']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bucketsBreakdown':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MetricBreakdown':
                    return super().__getitem__(i)
            __annotations__ = {
                "executionsTotal": executionsTotal,
                "documentsTotal": documentsTotal,
                "databasesTotal": databasesTotal,
                "usersTotal": usersTotal,
                "filesStorageTotal": filesStorageTotal,
                "bucketsTotal": bucketsTotal,
                "requests": requests,
                "network": network,
                "users": users,
                "executions": executions,
                "executionsBreakdown": executionsBreakdown,
                "bucketsBreakdown": bucketsBreakdown,
            }
    
    usersTotal: MetaOapg.properties.usersTotal
    executionsTotal: MetaOapg.properties.executionsTotal
    executions: MetaOapg.properties.executions
    databasesTotal: MetaOapg.properties.databasesTotal
    executionsBreakdown: MetaOapg.properties.executionsBreakdown
    bucketsTotal: MetaOapg.properties.bucketsTotal
    documentsTotal: MetaOapg.properties.documentsTotal
    requests: MetaOapg.properties.requests
    filesStorageTotal: MetaOapg.properties.filesStorageTotal
    bucketsBreakdown: MetaOapg.properties.bucketsBreakdown
    users: MetaOapg.properties.users
    network: MetaOapg.properties.network
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["executionsTotal"]) -> MetaOapg.properties.executionsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentsTotal"]) -> MetaOapg.properties.documentsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databasesTotal"]) -> MetaOapg.properties.databasesTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usersTotal"]) -> MetaOapg.properties.usersTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filesStorageTotal"]) -> MetaOapg.properties.filesStorageTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketsTotal"]) -> MetaOapg.properties.bucketsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requests"]) -> MetaOapg.properties.requests: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["executions"]) -> MetaOapg.properties.executions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["executionsBreakdown"]) -> MetaOapg.properties.executionsBreakdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketsBreakdown"]) -> MetaOapg.properties.bucketsBreakdown: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["executionsTotal", "documentsTotal", "databasesTotal", "usersTotal", "filesStorageTotal", "bucketsTotal", "requests", "network", "users", "executions", "executionsBreakdown", "bucketsBreakdown", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["executionsTotal"]) -> MetaOapg.properties.executionsTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentsTotal"]) -> MetaOapg.properties.documentsTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databasesTotal"]) -> MetaOapg.properties.databasesTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usersTotal"]) -> MetaOapg.properties.usersTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filesStorageTotal"]) -> MetaOapg.properties.filesStorageTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketsTotal"]) -> MetaOapg.properties.bucketsTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requests"]) -> MetaOapg.properties.requests: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> MetaOapg.properties.users: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["executions"]) -> MetaOapg.properties.executions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["executionsBreakdown"]) -> MetaOapg.properties.executionsBreakdown: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketsBreakdown"]) -> MetaOapg.properties.bucketsBreakdown: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["executionsTotal", "documentsTotal", "databasesTotal", "usersTotal", "filesStorageTotal", "bucketsTotal", "requests", "network", "users", "executions", "executionsBreakdown", "bucketsBreakdown", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        usersTotal: typing.Union[MetaOapg.properties.usersTotal, decimal.Decimal, int, ],
        executionsTotal: typing.Union[MetaOapg.properties.executionsTotal, decimal.Decimal, int, ],
        executions: typing.Union[MetaOapg.properties.executions, list, tuple, ],
        databasesTotal: typing.Union[MetaOapg.properties.databasesTotal, decimal.Decimal, int, ],
        executionsBreakdown: typing.Union[MetaOapg.properties.executionsBreakdown, list, tuple, ],
        bucketsTotal: typing.Union[MetaOapg.properties.bucketsTotal, decimal.Decimal, int, ],
        documentsTotal: typing.Union[MetaOapg.properties.documentsTotal, decimal.Decimal, int, ],
        requests: typing.Union[MetaOapg.properties.requests, list, tuple, ],
        filesStorageTotal: typing.Union[MetaOapg.properties.filesStorageTotal, decimal.Decimal, int, ],
        bucketsBreakdown: typing.Union[MetaOapg.properties.bucketsBreakdown, list, tuple, ],
        users: typing.Union[MetaOapg.properties.users, list, tuple, ],
        network: typing.Union[MetaOapg.properties.network, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsageProject':
        return super().__new__(
            cls,
            *args,
            usersTotal=usersTotal,
            executionsTotal=executionsTotal,
            executions=executions,
            databasesTotal=databasesTotal,
            executionsBreakdown=executionsBreakdown,
            bucketsTotal=bucketsTotal,
            documentsTotal=documentsTotal,
            requests=requests,
            filesStorageTotal=filesStorageTotal,
            bucketsBreakdown=bucketsBreakdown,
            users=users,
            network=network,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.metric import Metric
from appwrite_console_python_sdk.model.metric_breakdown import MetricBreakdown