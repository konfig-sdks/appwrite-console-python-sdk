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


RequiredPlatform = TypedDict("RequiredPlatform", {
    # Platform ID.
    "$id": str,

    # Platform creation date in ISO 8601 format.
    "$createdAt": str,

    # Platform update date in ISO 8601 format.
    "$updatedAt": str,

    # Platform name.
    "name": str,

    # Platform type. Possible values are: web, flutter-web, flutter-ios, flutter-android, ios, android, and unity.
    "type": str,

    # Platform Key. iOS bundle ID or Android package name.  Empty string for other platforms.
    "key": str,

    # App store or Google Play store ID.
    "store": str,

    # Web app hostname. Empty string for other platforms.
    "hostname": str,

    # HTTP basic authentication username.
    "httpUser": str,

    # HTTP basic authentication password.
    "httpPass": str,
    })

OptionalPlatform = TypedDict("OptionalPlatform", {
    }, total=False)

class Platform(RequiredPlatform, OptionalPlatform):
    pass
