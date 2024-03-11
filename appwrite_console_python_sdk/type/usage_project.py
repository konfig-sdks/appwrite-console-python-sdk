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
from appwrite_console_python_sdk.type.metric_breakdown import MetricBreakdown

class RequiredUsageProject(TypedDict):
    # Total aggregated number of function executions.
    executionsTotal: int

    # Total aggregated  number of documents.
    documentsTotal: int

    # Total aggregated number of databases.
    databasesTotal: int

    # Total aggregated number of users.
    usersTotal: int

    # Total aggregated sum of files storage size (in bytes).
    filesStorageTotal: int

    # Total aggregated number of buckets.
    bucketsTotal: int

    # Aggregated  number of requests per period.
    requests: typing.List[Metric]

    # Aggregated number of consumed bandwidth per period.
    network: typing.List[Metric]

    # Aggregated number of users per period.
    users: typing.List[Metric]

    # Aggregated number of executions per period.
    executions: typing.List[Metric]

    # Aggregated breakdown in totals of executions by functions.
    executionsBreakdown: typing.List[MetricBreakdown]

    # Aggregated breakdown in totals of usage by buckets.
    bucketsBreakdown: typing.List[MetricBreakdown]

class OptionalUsageProject(TypedDict, total=False):
    pass

class UsageProject(RequiredUsageProject, OptionalUsageProject):
    pass
