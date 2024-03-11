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

from appwrite_console_python_sdk.pydantic.migrations_create_n_host_migration_request_resources import MigrationsCreateNHostMigrationRequestResources

class MigrationsCreateNHostMigrationRequest(BaseModel):
    resources: MigrationsCreateNHostMigrationRequestResources = Field(alias='resources')

    # Source's Subdomain
    subdomain: str = Field(alias='subdomain')

    # Source's Region
    region: str = Field(alias='region')

    # Source's Admin Secret
    admin_secret: str = Field(alias='adminSecret')

    # Source's Database Name
    database: str = Field(alias='database')

    # Source's Database Username
    username: str = Field(alias='username')

    # Source's Database Password
    password: str = Field(alias='password')

    # Source's Database Port
    port: typing.Optional[int] = Field(None, alias='port')
    class Config:
        arbitrary_types_allowed = True
