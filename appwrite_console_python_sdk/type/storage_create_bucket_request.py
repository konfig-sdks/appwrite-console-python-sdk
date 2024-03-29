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

from appwrite_console_python_sdk.type.storage_create_bucket_request_allowed_file_extensions import StorageCreateBucketRequestAllowedFileExtensions
from appwrite_console_python_sdk.type.storage_create_bucket_request_permissions import StorageCreateBucketRequestPermissions

class RequiredStorageCreateBucketRequest(TypedDict):
    # Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
    bucketId: str

    # Bucket name
    name: str

class OptionalStorageCreateBucketRequest(TypedDict, total=False):
    permissions: StorageCreateBucketRequestPermissions

    # Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).
    fileSecurity: bool

    # Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.
    enabled: bool

    # Maximum file size allowed in bytes. Maximum allowed value is 30MB.
    maximumFileSize: int

    allowedFileExtensions: StorageCreateBucketRequestAllowedFileExtensions

    # Compression algorithm choosen for compression. Can be one of none,  [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled
    compression: str

    # Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled
    encryption: bool

    # Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled
    antivirus: bool

class StorageCreateBucketRequest(RequiredStorageCreateBucketRequest, OptionalStorageCreateBucketRequest):
    pass
