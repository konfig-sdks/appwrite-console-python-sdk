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

from appwrite_console_python_sdk.pydantic.messaging_create_sms_message_request_targets import MessagingCreateSmsMessageRequestTargets
from appwrite_console_python_sdk.pydantic.messaging_create_sms_message_request_topics import MessagingCreateSmsMessageRequestTopics
from appwrite_console_python_sdk.pydantic.messaging_create_sms_message_request_users import MessagingCreateSmsMessageRequestUsers

class MessagingCreateSmsMessageRequest(BaseModel):
    # Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    message_id: str = Field(alias='messageId')

    # SMS Content.
    content: str = Field(alias='content')

    topics: typing.Optional[MessagingCreateSmsMessageRequestTopics] = Field(None, alias='topics')

    users: typing.Optional[MessagingCreateSmsMessageRequestUsers] = Field(None, alias='users')

    targets: typing.Optional[MessagingCreateSmsMessageRequestTargets] = Field(None, alias='targets')

    # Is message a draft
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduled_at: typing.Optional[str] = Field(None, alias='scheduledAt')
    class Config:
        arbitrary_types_allowed = True
