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

from appwrite_console_python_sdk.type.projects_create_webhook_request_events import ProjectsCreateWebhookRequestEvents

class RequiredProjectsCreateWebhookRequest(TypedDict):
    # Certificate verification, false for disabled or true for enabled.
    security: bool

    # Webhook name. Max length: 128 chars.
    name: str

    events: ProjectsCreateWebhookRequestEvents

    # Webhook URL.
    url: str

class OptionalProjectsCreateWebhookRequest(TypedDict, total=False):
    # Enable or disable a webhook.
    enabled: bool

    # Webhook HTTP user. Max length: 256 chars.
    httpUser: str

    # Webhook HTTP password. Max length: 256 chars.
    httpPass: str

class ProjectsCreateWebhookRequest(RequiredProjectsCreateWebhookRequest, OptionalProjectsCreateWebhookRequest):
    pass
