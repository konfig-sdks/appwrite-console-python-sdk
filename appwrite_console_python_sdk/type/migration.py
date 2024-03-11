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

from appwrite_console_python_sdk.type.migration_errors import MigrationErrors
from appwrite_console_python_sdk.type.migration_resources import MigrationResources

RequiredMigration = TypedDict("RequiredMigration", {
    # Migration ID.
    "$id": str,

    # Variable creation date in ISO 8601 format.
    "$createdAt": str,

    # Variable creation date in ISO 8601 format.
    "$updatedAt": str,

    # Migration status ( pending, processing, failed, completed ) 
    "status": str,

    # Migration stage ( init, processing, source-check, destination-check, migrating, finished )
    "stage": str,

    # A string containing the type of source of the migration.
    "source": str,

    "resources": MigrationResources,

    # A group of counters that represent the total progress of the migration.
    "statusCounters": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    # An array of objects containing the report data of the resources that were migrated.
    "resourceData": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "errors": MigrationErrors,
    })

OptionalMigration = TypedDict("OptionalMigration", {
    }, total=False)

class Migration(RequiredMigration, OptionalMigration):
    pass
