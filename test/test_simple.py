# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

import unittest

import os
from pprint import pprint
from appwrite_console_python_sdk import AppwriteConsole

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        appwriteconsole = AppwriteConsole(
        
                        jwt = 'YOUR_API_KEY',
        
                        key = 'YOUR_API_KEY',
        
                        locale = 'YOUR_API_KEY',
        
                        mode = 'YOUR_API_KEY',
        
                        project = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(appwriteconsole)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
