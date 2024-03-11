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

from appwrite_console_python_sdk.pydantic.migration_errors import MigrationErrors
from appwrite_console_python_sdk.pydantic.migration_resources import MigrationResources

class Migration(BaseModel):
    # Migration ID.
    $id_: str = Field(alias='$id')

    # Variable creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Variable creation date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Migration status ( pending, processing, failed, completed ) 
    status: str = Field(alias='status')

    # Migration stage ( init, processing, source-check, destination-check, migrating, finished )
    stage: str = Field(alias='stage')

    # A string containing the type of source of the migration.
    source: str = Field(alias='source')

    resources: MigrationResources = Field(alias='resources')

    # A group of counters that represent the total progress of the migration.
    status_counters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='statusCounters')

    # An array of objects containing the report data of the resources that were migrated.
    resource_data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='resourceData')

    errors: MigrationErrors = Field(alias='errors')
    class Config:
        arbitrary_types_allowed = True
