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


class MessagingUpdateProviderByIdRequest(BaseModel):
    # Provider name.
    name: typing.Optional[str] = Field(None, alias='name')

    # Set as enabled.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')

    # Msg91 Sender ID.
    sender_id: typing.Optional[str] = Field(None, alias='senderId')

    # Msg91 Auth Key.
    auth_key: typing.Optional[str] = Field(None, alias='authKey')

    # Sender number.
    from_: typing.Optional[str] = Field(None, alias='from')
    class Config:
        arbitrary_types_allowed = True
