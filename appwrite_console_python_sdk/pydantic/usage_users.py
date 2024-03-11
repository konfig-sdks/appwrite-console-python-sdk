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

class UsageUsers(BaseModel):
    # Time range of the usage stats.
    range: str = Field(alias='range')

    # Total aggregated number of statistics of users.
    users_total: int = Field(alias='usersTotal')

    # Total aggregated number of active sessions.
    sessions_total: int = Field(alias='sessionsTotal')

    # Aggregated number of users per period.
    users: typing.List[Metric] = Field(alias='users')

    # Aggregated number of active sessions  per period.
    sessions: typing.List[Metric] = Field(alias='sessions')
    class Config:
        arbitrary_types_allowed = True
