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


class EmailTemplate(BaseModel):
    # Template type
    type: str = Field(alias='type')

    # Template locale
    locale: str = Field(alias='locale')

    # Template message
    message: str = Field(alias='message')

    # Name of the sender
    sender_name: str = Field(alias='senderName')

    # Email of the sender
    sender_email: str = Field(alias='senderEmail')

    # Reply to email address
    reply_to: str = Field(alias='replyTo')

    # Email subject
    subject: str = Field(alias='subject')
    class Config:
        arbitrary_types_allowed = True
