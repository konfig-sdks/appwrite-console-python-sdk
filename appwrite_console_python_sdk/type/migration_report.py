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


class RequiredMigrationReport(TypedDict):
    # Version of the Appwrite instance to be migrated.
    version: str

    # Number of users to be migrated.
    user: int

    # Number of teams to be migrated.
    team: int

    # Number of databases to be migrated.
    database: int

    # Number of documents to be migrated.
    document: int

    # Number of files to be migrated.
    file: int

    # Number of buckets to be migrated.
    bucket: int

    # Number of functions to be migrated.
    function: int

    # Size of files to be migrated in mb.
    size: int

class OptionalMigrationReport(TypedDict, total=False):
    pass

class MigrationReport(RequiredMigrationReport, OptionalMigrationReport):
    pass
