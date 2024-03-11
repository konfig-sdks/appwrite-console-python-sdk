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

from appwrite_console_python_sdk.pydantic.auth_provider import AuthProvider
from appwrite_console_python_sdk.pydantic.key import Key
from appwrite_console_python_sdk.pydantic.platform import Platform
from appwrite_console_python_sdk.pydantic.webhook import Webhook

class Project(BaseModel):
    # Project description.
    description: str = Field(alias='description')

    # Project ID.
    $id_: str = Field(alias='$id')

    # Project creation date in ISO 8601 format.
    $created_at_: str = Field(alias='$createdAt')

    # Project update date in ISO 8601 format.
    $updated_at_: str = Field(alias='$updatedAt')

    # Project name.
    name: str = Field(alias='name')

    # Project team ID.
    team_id: str = Field(alias='teamId')

    # Project logo file ID.
    logo: str = Field(alias='logo')

    # Project website URL.
    url: str = Field(alias='url')

    # Company legal name.
    legal_name: str = Field(alias='legalName')

    # Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format.
    legal_country: str = Field(alias='legalCountry')

    # State name.
    legal_state: str = Field(alias='legalState')

    # City name.
    legal_city: str = Field(alias='legalCity')

    # Company Address.
    legal_address: str = Field(alias='legalAddress')

    # Company Tax ID.
    legal_tax_id: str = Field(alias='legalTaxId')

    # Session duration in seconds.
    auth_duration: int = Field(alias='authDuration')

    # Max users allowed. 0 is unlimited.
    auth_limit: int = Field(alias='authLimit')

    # Max sessions allowed per user. 100 maximum.
    auth_sessions_limit: int = Field(alias='authSessionsLimit')

    # Max allowed passwords in the history list per user. Max passwords limit allowed in history is 20. Use 0 for disabling password history.
    auth_password_history: int = Field(alias='authPasswordHistory')

    # Whether or not to check user's password against most commonly used passwords.
    auth_password_dictionary: bool = Field(alias='authPasswordDictionary')

    # Whether or not to check the user password for similarity with their personal data.
    auth_personal_data_check: bool = Field(alias='authPersonalDataCheck')

    # List of Auth Providers.
    o_auth_providers: typing.List[AuthProvider] = Field(alias='oAuthProviders')

    # List of Platforms.
    platforms: typing.List[Platform] = Field(alias='platforms')

    # List of Webhooks.
    webhooks: typing.List[Webhook] = Field(alias='webhooks')

    # List of API Keys.
    keys: typing.List[Key] = Field(alias='keys')

    # Status for custom SMTP
    smtp_enabled: bool = Field(alias='smtpEnabled')

    # SMTP sender name
    smtp_sender_name: str = Field(alias='smtpSenderName')

    # SMTP sender email
    smtp_sender_email: str = Field(alias='smtpSenderEmail')

    # SMTP reply to email
    smtp_reply_to: str = Field(alias='smtpReplyTo')

    # SMTP server host name
    smtp_host: str = Field(alias='smtpHost')

    # SMTP server port
    smtp_port: int = Field(alias='smtpPort')

    # SMTP server username
    smtp_username: str = Field(alias='smtpUsername')

    # SMTP server password
    smtp_password: str = Field(alias='smtpPassword')

    # SMTP server secure protocol
    smtp_secure: str = Field(alias='smtpSecure')

    # Email/Password auth method status
    auth_email_password: bool = Field(alias='authEmailPassword')

    # Magic URL auth method status
    auth_users_auth_magic_u_r_l: bool = Field(alias='authUsersAuthMagicURL')

    # Email (OTP) auth method status
    auth_email_otp: bool = Field(alias='authEmailOtp')

    # Anonymous auth method status
    auth_anonymous: bool = Field(alias='authAnonymous')

    # Invites auth method status
    auth_invites: bool = Field(alias='authInvites')

    # JWT auth method status
    auth_j_w_t: bool = Field(alias='authJWT')

    # Phone auth method status
    auth_phone: bool = Field(alias='authPhone')

    # Account service status
    service_status_for_account: bool = Field(alias='serviceStatusForAccount')

    # Avatars service status
    service_status_for_avatars: bool = Field(alias='serviceStatusForAvatars')

    # Databases service status
    service_status_for_databases: bool = Field(alias='serviceStatusForDatabases')

    # Locale service status
    service_status_for_locale: bool = Field(alias='serviceStatusForLocale')

    # Health service status
    service_status_for_health: bool = Field(alias='serviceStatusForHealth')

    # Storage service status
    service_status_for_storage: bool = Field(alias='serviceStatusForStorage')

    # Teams service status
    service_status_for_teams: bool = Field(alias='serviceStatusForTeams')

    # Users service status
    service_status_for_users: bool = Field(alias='serviceStatusForUsers')

    # Functions service status
    service_status_for_functions: bool = Field(alias='serviceStatusForFunctions')

    # GraphQL service status
    service_status_for_graphql: bool = Field(alias='serviceStatusForGraphql')

    # Messaging service status
    service_status_for_messaging: bool = Field(alias='serviceStatusForMessaging')
    class Config:
        arbitrary_types_allowed = True
