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

from appwrite_console_python_sdk.pydantic.databases_update_enum_attribute_request_elements import DatabasesUpdateEnumAttributeRequestElements

class DatabasesUpdateEnumAttributeRequest(BaseModel):
    elements: DatabasesUpdateEnumAttributeRequestElements = Field(alias='elements')

    # Is attribute required?
    required: bool = Field(alias='required')

    # Default value for attribute when not provided. Cannot be set when attribute is required.
    default: typing.Optional[str] = Field(alias='default')
    class Config:
        arbitrary_types_allowed = True