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


class RequiredProjectsUpdateOAuthRequest(TypedDict):
    # Provider Name
    provider: str

class OptionalProjectsUpdateOAuthRequest(TypedDict, total=False):
    # Provider app ID. Max length: 256 chars.
    appId: str

    # Provider secret key. Max length: 512 chars.
    secret: str

    # Provider status. Set to 'false' to disable new session creation.
    enabled: bool

class ProjectsUpdateOAuthRequest(RequiredProjectsUpdateOAuthRequest, OptionalProjectsUpdateOAuthRequest):
    pass
