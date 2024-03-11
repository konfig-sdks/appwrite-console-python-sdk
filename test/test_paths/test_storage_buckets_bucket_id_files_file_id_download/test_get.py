# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

import unittest
from unittest.mock import patch

import urllib3

import appwrite_console_python_sdk
from appwrite_console_python_sdk.paths.storage_buckets_bucket_id_files_file_id_download import get
from appwrite_console_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestStorageBucketsBucketIdFilesFileIdDownload(ApiTestMixin, unittest.TestCase):
    """
    StorageBucketsBucketIdFilesFileIdDownload unit test stubs
        Get file for download
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()