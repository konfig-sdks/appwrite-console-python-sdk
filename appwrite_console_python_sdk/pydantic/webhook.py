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

from appwrite_console_python_sdk.pydantic.webhook_events import WebhookEvents

class Webhook(BaseModel):
    # Indicated if SSL / TLS Certificate verification is enabled.
    security: bool = Field(alias='security')

    # Webhook ID.
    $id_: str = Field(alias='$id')

    # Webhook creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Webhook update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Webhook name.
    name: str = Field(alias='name')

    # Webhook URL endpoint.
    url: str = Field(alias='url')

    events: WebhookEvents = Field(alias='events')

    # HTTP basic authentication username.
    http_user: str = Field(alias='httpUser')

    # HTTP basic authentication password.
    http_pass: str = Field(alias='httpPass')

    # Signature key which can be used to validated incoming
    signature_key: str = Field(alias='signatureKey')

    # Indicates if this webhook is enabled.
    enabled: bool = Field(alias='enabled')

    # Webhook error logs from the most recent failure.
    logs: str = Field(alias='logs')

    # Number of consecutive failed webhook attempts.
    attempts: int = Field(alias='attempts')
    class Config:
        arbitrary_types_allowed = True
