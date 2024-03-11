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


class ProviderRepository(BaseModel):
    # VCS (Version Control System) repository ID.
    id: str = Field(alias='id')

    # VCS (Version Control System) repository name.
    name: str = Field(alias='name')

    # VCS (Version Control System) organization name
    organization: str = Field(alias='organization')

    # VCS (Version Control System) provider name.
    provider: str = Field(alias='provider')

    # Is VCS (Version Control System) repository private?
    private: bool = Field(alias='private')

    # Auto-detected runtime suggestion. Empty if getting response of getRuntime().
    runtime: str = Field(alias='runtime')

    # Last commit date in ISO 8601 format.
    pushed_at: str = Field(alias='pushedAt')
    class Config:
        arbitrary_types_allowed = True
