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


class RequiredUsersCreateWithShaPasswordRequest(TypedDict):
    # User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    userId: str

    # User email.
    email: str

    # User password hashed using SHA.
    password: str

class OptionalUsersCreateWithShaPasswordRequest(TypedDict, total=False):
    # Optional SHA version used to hash password. Allowed values are: 'sha1', 'sha224', 'sha256', 'sha384', 'sha512/224', 'sha512/256', 'sha512', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512'
    passwordVersion: str

    # User name. Max length: 128 chars.
    name: str

class UsersCreateWithShaPasswordRequest(RequiredUsersCreateWithShaPasswordRequest, OptionalUsersCreateWithShaPasswordRequest):
    pass
