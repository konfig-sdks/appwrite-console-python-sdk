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

from appwrite_console_python_sdk.pydantic.index_attributes import IndexAttributes
from appwrite_console_python_sdk.pydantic.index_orders import IndexOrders

class Index(BaseModel):
    # Index Key.
    key: str = Field(alias='key')

    # Index type.
    type: str = Field(alias='type')

    # Index status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    status: str = Field(alias='status')

    # Error message. Displays error generated on failure of creating or deleting an index.
    error: str = Field(alias='error')

    attributes: IndexAttributes = Field(alias='attributes')

    orders: typing.Optional[IndexOrders] = Field(None, alias='orders')
    class Config:
        arbitrary_types_allowed = True