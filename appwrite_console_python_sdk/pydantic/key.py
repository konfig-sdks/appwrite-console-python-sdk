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

from appwrite_console_python_sdk.pydantic.key_scopes import KeyScopes
from appwrite_console_python_sdk.pydantic.key_sdks import KeySdks

class Key(BaseModel):
    # Key ID.
    $id_: str = Field(alias='$id')

    # Key creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Key update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Key name.
    name: str = Field(alias='name')

    # Key expiration date in ISO 8601 format.
    expire: str = Field(alias='expire')

    scopes: KeyScopes = Field(alias='scopes')

    # Secret key.
    secret: str = Field(alias='secret')

    # Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    accessed_at: str = Field(alias='accessedAt')

    sdks: KeySdks = Field(alias='sdks')
    class Config:
        arbitrary_types_allowed = True
