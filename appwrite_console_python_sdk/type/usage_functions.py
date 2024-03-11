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

class RequiredUsageFunctions(TypedDict):
    # Time range of the usage stats.
    range: str

    # Total aggregated number of functions.
    functionsTotal: int

    # Total aggregated number of functions deployments.
    deploymentsTotal: int

    # Total aggregated sum of functions deployment storage.
    deploymentsStorageTotal: int

    # Total aggregated number of functions build.
    buildsTotal: int

    # total aggregated sum of functions build storage.
    buildsStorageTotal: int

    # Total aggregated sum of functions build compute time.
    buildsTimeTotal: int

    # Total  aggregated number of functions execution.
    executionsTotal: int

    # Total aggregated sum of functions  execution compute time.
    executionsTimeTotal: int

    # Aggregated number of functions per period.
    functions: typing.List[Metric]

    # Aggregated number of functions deployment per period.
    deployments: typing.List[Metric]

    # Aggregated number of  functions deployment storage per period.
    deploymentsStorage: typing.List[Metric]

    # Aggregated number of functions build per period.
    builds: typing.List[Metric]

    # Aggregated sum of functions build storage per period.
    buildsStorage: typing.List[Metric]

    # Aggregated sum of  functions build compute time per period.
    buildsTime: typing.List[Metric]

    # Aggregated number of  functions execution per period.
    executions: typing.List[Metric]

    # Aggregated number of functions execution compute time per period.
    executionsTime: typing.List[Metric]

class OptionalUsageFunctions(TypedDict, total=False):
    pass

class UsageFunctions(RequiredUsageFunctions, OptionalUsageFunctions):
    pass
