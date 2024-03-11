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


class RequiredProjectsCreatePlatformRequest(TypedDict):
    # Platform type.
    type: str

    # Platform name. Max length: 128 chars.
    name: str

class OptionalProjectsCreatePlatformRequest(TypedDict, total=False):
    # Package name for Android or bundle ID for iOS or macOS. Max length: 256 chars.
    key: str

    # App store or Google Play store ID. Max length: 256 chars.
    store: str

    # Platform client hostname. Max length: 256 chars.
    hostname: str

class ProjectsCreatePlatformRequest(RequiredProjectsCreatePlatformRequest, OptionalProjectsCreatePlatformRequest):
    pass
