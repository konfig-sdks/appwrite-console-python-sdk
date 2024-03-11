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

from appwrite_console_python_sdk.type.auth_provider import AuthProvider
from appwrite_console_python_sdk.type.key import Key
from appwrite_console_python_sdk.type.platform import Platform
from appwrite_console_python_sdk.type.webhook import Webhook

RequiredProject = TypedDict("RequiredProject", {
    # Project description.
    "description": str,

    # Project ID.
    "$id": str,

    # Project creation date in ISO 8601 format.
    "$createdAt": str,

    # Project update date in ISO 8601 format.
    "$updatedAt": str,

    # Project name.
    "name": str,

    # Project team ID.
    "teamId": str,

    # Project logo file ID.
    "logo": str,

    # Project website URL.
    "url": str,

    # Company legal name.
    "legalName": str,

    # Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format.
    "legalCountry": str,

    # State name.
    "legalState": str,

    # City name.
    "legalCity": str,

    # Company Address.
    "legalAddress": str,

    # Company Tax ID.
    "legalTaxId": str,

    # Session duration in seconds.
    "authDuration": int,

    # Max users allowed. 0 is unlimited.
    "authLimit": int,

    # Max sessions allowed per user. 100 maximum.
    "authSessionsLimit": int,

    # Max allowed passwords in the history list per user. Max passwords limit allowed in history is 20. Use 0 for disabling password history.
    "authPasswordHistory": int,

    # Whether or not to check user's password against most commonly used passwords.
    "authPasswordDictionary": bool,

    # Whether or not to check the user password for similarity with their personal data.
    "authPersonalDataCheck": bool,

    # List of Auth Providers.
    "oAuthProviders": typing.List[AuthProvider],

    # List of Platforms.
    "platforms": typing.List[Platform],

    # List of Webhooks.
    "webhooks": typing.List[Webhook],

    # List of API Keys.
    "keys": typing.List[Key],

    # Status for custom SMTP
    "smtpEnabled": bool,

    # SMTP sender name
    "smtpSenderName": str,

    # SMTP sender email
    "smtpSenderEmail": str,

    # SMTP reply to email
    "smtpReplyTo": str,

    # SMTP server host name
    "smtpHost": str,

    # SMTP server port
    "smtpPort": int,

    # SMTP server username
    "smtpUsername": str,

    # SMTP server password
    "smtpPassword": str,

    # SMTP server secure protocol
    "smtpSecure": str,

    # Email/Password auth method status
    "authEmailPassword": bool,

    # Magic URL auth method status
    "authUsersAuthMagicURL": bool,

    # Email (OTP) auth method status
    "authEmailOtp": bool,

    # Anonymous auth method status
    "authAnonymous": bool,

    # Invites auth method status
    "authInvites": bool,

    # JWT auth method status
    "authJWT": bool,

    # Phone auth method status
    "authPhone": bool,

    # Account service status
    "serviceStatusForAccount": bool,

    # Avatars service status
    "serviceStatusForAvatars": bool,

    # Databases service status
    "serviceStatusForDatabases": bool,

    # Locale service status
    "serviceStatusForLocale": bool,

    # Health service status
    "serviceStatusForHealth": bool,

    # Storage service status
    "serviceStatusForStorage": bool,

    # Teams service status
    "serviceStatusForTeams": bool,

    # Users service status
    "serviceStatusForUsers": bool,

    # Functions service status
    "serviceStatusForFunctions": bool,

    # GraphQL service status
    "serviceStatusForGraphql": bool,

    # Messaging service status
    "serviceStatusForMessaging": bool,
    })

OptionalProject = TypedDict("OptionalProject", {
    }, total=False)

class Project(RequiredProject, OptionalProject):
    pass
