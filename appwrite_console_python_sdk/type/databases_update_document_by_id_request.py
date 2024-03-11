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

from appwrite_console_python_sdk.type.databases_update_document_by_id_request_permissions import DatabasesUpdateDocumentByIdRequestPermissions

class RequiredDatabasesUpdateDocumentByIdRequest(TypedDict):
    pass

class OptionalDatabasesUpdateDocumentByIdRequest(TypedDict, total=False):
    # Document data as JSON object. Include only attribute and value pairs to be updated.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    permissions: DatabasesUpdateDocumentByIdRequestPermissions

class DatabasesUpdateDocumentByIdRequest(RequiredDatabasesUpdateDocumentByIdRequest, OptionalDatabasesUpdateDocumentByIdRequest):
    pass
