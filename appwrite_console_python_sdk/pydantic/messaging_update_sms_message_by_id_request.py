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

from appwrite_console_python_sdk.pydantic.messaging_update_sms_message_by_id_request_targets import MessagingUpdateSmsMessageByIdRequestTargets
from appwrite_console_python_sdk.pydantic.messaging_update_sms_message_by_id_request_topics import MessagingUpdateSmsMessageByIdRequestTopics
from appwrite_console_python_sdk.pydantic.messaging_update_sms_message_by_id_request_users import MessagingUpdateSmsMessageByIdRequestUsers

class MessagingUpdateSmsMessageByIdRequest(BaseModel):
    topics: typing.Optional[MessagingUpdateSmsMessageByIdRequestTopics] = Field(None, alias='topics')

    users: typing.Optional[MessagingUpdateSmsMessageByIdRequestUsers] = Field(None, alias='users')

    targets: typing.Optional[MessagingUpdateSmsMessageByIdRequestTargets] = Field(None, alias='targets')

    # Email Content.
    content: typing.Optional[str] = Field(None, alias='content')

    # Is message a draft
    draft: typing.Optional[bool] = Field(None, alias='draft')

    # Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
    scheduled_at: typing.Optional[str] = Field(None, alias='scheduledAt')
    class Config:
        arbitrary_types_allowed = True
