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


class Platform(BaseModel):
    # Platform ID.
    $id_: str = Field(alias='$id')

    # Platform creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Platform update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Platform name.
    name: str = Field(alias='name')

    # Platform type. Possible values are: web, flutter-web, flutter-ios, flutter-android, ios, android, and unity.
    type: str = Field(alias='type')

    # Platform Key. iOS bundle ID or Android package name.  Empty string for other platforms.
    key: str = Field(alias='key')

    # App store or Google Play store ID.
    store: str = Field(alias='store')

    # Web app hostname. Empty string for other platforms.
    hostname: str = Field(alias='hostname')

    # HTTP basic authentication username.
    http_user: str = Field(alias='httpUser')

    # HTTP basic authentication password.
    http_pass: str = Field(alias='httpPass')
    class Config:
        arbitrary_types_allowed = True
