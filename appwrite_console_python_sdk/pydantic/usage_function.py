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

class UsageFunction(BaseModel):
    # The time range of the usage stats.
    range: str = Field(alias='range')

    # Total aggregated number of function deployments.
    deployments_total: int = Field(alias='deploymentsTotal')

    # Total aggregated sum of function deployments storage.
    deployments_storage_total: int = Field(alias='deploymentsStorageTotal')

    # Total aggregated number of function builds.
    builds_total: int = Field(alias='buildsTotal')

    # total aggregated sum of function builds storage.
    builds_storage_total: int = Field(alias='buildsStorageTotal')

    # Total aggregated sum of function builds compute time.
    builds_time_total: int = Field(alias='buildsTimeTotal')

    # Total  aggregated number of function executions.
    executions_total: int = Field(alias='executionsTotal')

    # Total aggregated sum of function  executions compute time.
    executions_time_total: int = Field(alias='executionsTimeTotal')

    # Aggregated number of function deployments per period.
    deployments: typing.List[Metric] = Field(alias='deployments')

    # Aggregated number of  function deployments storage per period.
    deployments_storage: typing.List[Metric] = Field(alias='deploymentsStorage')

    # Aggregated number of function builds per period.
    builds: typing.List[Metric] = Field(alias='builds')

    # Aggregated sum of function builds storage per period.
    builds_storage: typing.List[Metric] = Field(alias='buildsStorage')

    # Aggregated sum of function builds compute time per period.
    builds_time: typing.List[Metric] = Field(alias='buildsTime')

    # Aggregated number of function executions per period.
    executions: typing.List[Metric] = Field(alias='executions')

    # Aggregated number of function executions compute time per period.
    executions_time: typing.List[Metric] = Field(alias='executionsTime')
    class Config:
        arbitrary_types_allowed = True
