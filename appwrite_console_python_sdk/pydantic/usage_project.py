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
from pydantic import BaseModel, Field, RootModel

from appwrite_console_python_sdk.pydantic.metric import Metric
from appwrite_console_python_sdk.pydantic.metric_breakdown import MetricBreakdown

class UsageProject(BaseModel):
    # Total aggregated number of function executions.
    executions_total: int = Field(alias='executionsTotal')

    # Total aggregated  number of documents.
    documents_total: int = Field(alias='documentsTotal')

    # Total aggregated number of databases.
    databases_total: int = Field(alias='databasesTotal')

    # Total aggregated number of users.
    users_total: int = Field(alias='usersTotal')

    # Total aggregated sum of files storage size (in bytes).
    files_storage_total: int = Field(alias='filesStorageTotal')

    # Total aggregated number of buckets.
    buckets_total: int = Field(alias='bucketsTotal')

    # Aggregated  number of requests per period.
    requests: typing.List[Metric] = Field(alias='requests')

    # Aggregated number of consumed bandwidth per period.
    network: typing.List[Metric] = Field(alias='network')

    # Aggregated number of users per period.
    users: typing.List[Metric] = Field(alias='users')

    # Aggregated number of executions per period.
    executions: typing.List[Metric] = Field(alias='executions')

    # Aggregated breakdown in totals of executions by functions.
    executions_breakdown: typing.List[MetricBreakdown] = Field(alias='executionsBreakdown')

    # Aggregated breakdown in totals of usage by buckets.
    buckets_breakdown: typing.List[MetricBreakdown] = Field(alias='bucketsBreakdown')
    class Config:
        arbitrary_types_allowed = True
