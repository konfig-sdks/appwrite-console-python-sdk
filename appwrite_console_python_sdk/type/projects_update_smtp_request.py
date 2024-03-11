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


class RequiredProjectsUpdateSmtpRequest(TypedDict):
    # Enable custom SMTP service
    enabled: bool

class OptionalProjectsUpdateSmtpRequest(TypedDict, total=False):
    # Name of the email sender
    senderName: str

    # Email of the sender
    senderEmail: str

    # Reply to email
    replyTo: str

    # SMTP server host name
    host: str

    # SMTP server port
    port: int

    # SMTP server username
    username: str

    # SMTP server password
    password: str

    # Does SMTP server use secure connection
    secure: str

class ProjectsUpdateSmtpRequest(RequiredProjectsUpdateSmtpRequest, OptionalProjectsUpdateSmtpRequest):
    pass
