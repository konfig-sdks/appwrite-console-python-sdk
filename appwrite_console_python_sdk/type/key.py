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

from appwrite_console_python_sdk.type.key_scopes import KeyScopes
from appwrite_console_python_sdk.type.key_sdks import KeySdks

RequiredKey = TypedDict("RequiredKey", {
    # Key ID.
    "$id": str,

    # Key creation date in ISO 8601 format.
    "$createdAt": str,

    # Key update date in ISO 8601 format.
    "$updatedAt": str,

    # Key name.
    "name": str,

    # Key expiration date in ISO 8601 format.
    "expire": str,

    "scopes": KeyScopes,

    # Secret key.
    "secret": str,

    # Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    "accessedAt": str,

    "sdks": KeySdks,
    })

OptionalKey = TypedDict("OptionalKey", {
    }, total=False)

class Key(RequiredKey, OptionalKey):
    pass
