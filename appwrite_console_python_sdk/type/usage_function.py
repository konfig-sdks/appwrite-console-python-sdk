# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from appwrite_console_python_sdk.type.metric import Metric

class RequiredUsageFunction(TypedDict):
    # The time range of the usage stats.
    range: str

    # Total aggregated number of function deployments.
    deploymentsTotal: int

    # Total aggregated sum of function deployments storage.
    deploymentsStorageTotal: int

    # Total aggregated number of function builds.
    buildsTotal: int

    # total aggregated sum of function builds storage.
    buildsStorageTotal: int

    # Total aggregated sum of function builds compute time.
    buildsTimeTotal: int

    # Total  aggregated number of function executions.
    executionsTotal: int

    # Total aggregated sum of function  executions compute time.
    executionsTimeTotal: int

    # Aggregated number of function deployments per period.
    deployments: typing.List[Metric]

    # Aggregated number of  function deployments storage per period.
    deploymentsStorage: typing.List[Metric]

    # Aggregated number of function builds per period.
    builds: typing.List[Metric]

    # Aggregated sum of function builds storage per period.
    buildsStorage: typing.List[Metric]

    # Aggregated sum of function builds compute time per period.
    buildsTime: typing.List[Metric]

    # Aggregated number of function executions per period.
    executions: typing.List[Metric]

    # Aggregated number of function executions compute time per period.
    executionsTime: typing.List[Metric]

class OptionalUsageFunction(TypedDict, total=False):
    pass

class UsageFunction(RequiredUsageFunction, OptionalUsageFunction):
    pass
