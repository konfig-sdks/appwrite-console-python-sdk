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


class ProjectsUpdateCustomEmailTemplatesRequest(BaseModel):
    # Email Subject
    subject: str = Field(alias='subject')

    # Template message
    message: str = Field(alias='message')

    # Name of the email sender
    sender_name: typing.Optional[str] = Field(None, alias='senderName')

    # Email of the sender
    sender_email: typing.Optional[str] = Field(None, alias='senderEmail')

    # Reply to email
    reply_to: typing.Optional[str] = Field(None, alias='replyTo')
    class Config:
        arbitrary_types_allowed = True
