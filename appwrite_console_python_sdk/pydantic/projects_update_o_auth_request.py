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


class ProjectsUpdateOAuthRequest(BaseModel):
    # Provider Name
    provider: Literal["amazon", "apple", "auth0", "authentik", "autodesk", "bitbucket", "bitly", "box", "dailymotion", "discord", "disqus", "dropbox", "etsy", "facebook", "github", "gitlab", "google", "linkedin", "microsoft", "notion", "oidc", "okta", "paypal", "paypalSandbox", "podio", "salesforce", "slack", "spotify", "stripe", "tradeshift", "tradeshiftBox", "twitch", "wordpress", "yahoo", "yammer", "yandex", "zoho", "zoom", "mock"] = Field(alias='provider')

    # Provider app ID. Max length: 256 chars.
    app_id: typing.Optional[str] = Field(None, alias='appId')

    # Provider secret key. Max length: 512 chars.
    secret: typing.Optional[str] = Field(None, alias='secret')

    # Provider status. Set to 'false' to disable new session creation.
    enabled: typing.Optional[bool] = Field(None, alias='enabled')
    class Config:
        arbitrary_types_allowed = True
