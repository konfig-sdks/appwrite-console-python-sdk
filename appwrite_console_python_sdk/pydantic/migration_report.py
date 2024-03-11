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


class MigrationReport(BaseModel):
    # Version of the Appwrite instance to be migrated.
    version: str = Field(alias='version')

    # Number of users to be migrated.
    user: int = Field(alias='user')

    # Number of teams to be migrated.
    team: int = Field(alias='team')

    # Number of databases to be migrated.
    database: int = Field(alias='database')

    # Number of documents to be migrated.
    document: int = Field(alias='document')

    # Number of files to be migrated.
    file: int = Field(alias='file')

    # Number of buckets to be migrated.
    bucket: int = Field(alias='bucket')

    # Number of functions to be migrated.
    function: int = Field(alias='function')

    # Size of files to be migrated in mb.
    size: int = Field(alias='size')
    class Config:
        arbitrary_types_allowed = True
