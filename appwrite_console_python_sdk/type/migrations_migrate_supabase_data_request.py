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

from appwrite_console_python_sdk.type.migrations_migrate_supabase_data_request_resources import MigrationsMigrateSupabaseDataRequestResources

class RequiredMigrationsMigrateSupabaseDataRequest(TypedDict):
    resources: MigrationsMigrateSupabaseDataRequestResources

    # Source's Supabase Endpoint
    endpoint: str

    # Source's API Key
    apiKey: str

    # Source's Database Host
    databaseHost: str

    # Source's Database Username
    username: str

    # Source's Database Password
    password: str

class OptionalMigrationsMigrateSupabaseDataRequest(TypedDict, total=False):
    # Source's Database Port
    port: int

class MigrationsMigrateSupabaseDataRequest(RequiredMigrationsMigrateSupabaseDataRequest, OptionalMigrationsMigrateSupabaseDataRequest):
    pass
