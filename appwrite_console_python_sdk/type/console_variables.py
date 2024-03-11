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


class RequiredConsoleVariables(TypedDict):
    # CNAME target for your Appwrite custom domains.
    _APP_DOMAIN_TARGET: str

    # Maximum file size allowed for file upload in bytes.
    _APP_STORAGE_LIMIT: int

    # Maximum file size allowed for deployment in bytes.
    _APP_FUNCTIONS_SIZE_LIMIT: int

    # Defines if usage stats are enabled. This value is set to 'enabled' by default, to disable the usage stats set the value to 'disabled'.
    _APP_USAGE_STATS: str

    # Defines if VCS (Version Control System) is enabled.
    _APP_VCS_ENABLED: bool

    # Defines if main domain is configured. If so, custom domains can be created.
    _APP_DOMAIN_ENABLED: bool

    # Defines if AI assistant is enabled.
    _APP_ASSISTANT_ENABLED: bool

class OptionalConsoleVariables(TypedDict, total=False):
    pass

class ConsoleVariables(RequiredConsoleVariables, OptionalConsoleVariables):
    pass
