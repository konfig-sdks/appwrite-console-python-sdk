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

from appwrite_console_python_sdk.pydantic.migrations_migrate_supabase_data_request_resources import MigrationsMigrateSupabaseDataRequestResources

class MigrationsMigrateSupabaseDataRequest(BaseModel):
    resources: MigrationsMigrateSupabaseDataRequestResources = Field(alias='resources')

    # Source's Supabase Endpoint
    endpoint: str = Field(alias='endpoint')

    # Source's API Key
    api_key: str = Field(alias='apiKey')

    # Source's Database Host
    database_host: str = Field(alias='databaseHost')

    # Source's Database Username
    username: str = Field(alias='username')

    # Source's Database Password
    password: str = Field(alias='password')

    # Source's Database Port
    port: typing.Optional[int] = Field(None, alias='port')
    class Config:
        arbitrary_types_allowed = True
