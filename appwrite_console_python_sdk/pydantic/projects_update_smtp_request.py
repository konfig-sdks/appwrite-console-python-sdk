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


class ProjectsUpdateSmtpRequest(BaseModel):
    # Enable custom SMTP service
    enabled: bool = Field(alias='enabled')

    # Name of the email sender
    sender_name: typing.Optional[str] = Field(None, alias='senderName')

    # Email of the sender
    sender_email: typing.Optional[str] = Field(None, alias='senderEmail')

    # Reply to email
    reply_to: typing.Optional[str] = Field(None, alias='replyTo')

    # SMTP server host name
    host: typing.Optional[str] = Field(None, alias='host')

    # SMTP server port
    port: typing.Optional[int] = Field(None, alias='port')

    # SMTP server username
    username: typing.Optional[str] = Field(None, alias='username')

    # SMTP server password
    password: typing.Optional[str] = Field(None, alias='password')

    # Does SMTP server use secure connection
    secure: typing.Optional[Literal["tls", "ssl"]] = Field(None, alias='secure')
    class Config:
        arbitrary_types_allowed = True
