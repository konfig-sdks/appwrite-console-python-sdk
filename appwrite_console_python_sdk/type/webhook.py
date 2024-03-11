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

from appwrite_console_python_sdk.type.webhook_events import WebhookEvents

RequiredWebhook = TypedDict("RequiredWebhook", {
    # Indicated if SSL / TLS Certificate verification is enabled.
    "security": bool,

    # Webhook ID.
    "$id": str,

    # Webhook creation date in ISO 8601 format.
    "$createdAt": str,

    # Webhook update date in ISO 8601 format.
    "$updatedAt": str,

    # Webhook name.
    "name": str,

    # Webhook URL endpoint.
    "url": str,

    "events": WebhookEvents,

    # HTTP basic authentication username.
    "httpUser": str,

    # HTTP basic authentication password.
    "httpPass": str,

    # Signature key which can be used to validated incoming
    "signatureKey": str,

    # Indicates if this webhook is enabled.
    "enabled": bool,

    # Webhook error logs from the most recent failure.
    "logs": str,

    # Number of consecutive failed webhook attempts.
    "attempts": int,
    })

OptionalWebhook = TypedDict("OptionalWebhook", {
    }, total=False)

class Webhook(RequiredWebhook, OptionalWebhook):
    pass
