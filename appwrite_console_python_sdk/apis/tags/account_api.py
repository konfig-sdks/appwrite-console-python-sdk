# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.post import AddAuthenticatorApp
from appwrite_console_python_sdk.paths.account_verification.put import CompleteEmailVerification
from appwrite_console_python_sdk.paths.account_mfa_challenge.put import CompleteMfaChallenge
from appwrite_console_python_sdk.paths.account_recovery.put import CompletePasswordRecovery
from appwrite_console_python_sdk.paths.account_verification_phone.put import ConfirmPhoneVerification
from appwrite_console_python_sdk.paths.account_sessions_anonymous.post import CreateAnonymousSession
from appwrite_console_python_sdk.paths.account_sessions_email.post import CreateEmailPasswordSession
from appwrite_console_python_sdk.paths.account_tokens_email.post import CreateEmailToken
from appwrite_console_python_sdk.paths.account_verification.post import CreateEmailVerification
from appwrite_console_python_sdk.paths.account_jwt.post import CreateJwt
from appwrite_console_python_sdk.paths.account_tokens_magic_url.post import CreateMagicUrlToken
from appwrite_console_python_sdk.paths.account_mfa_challenge.post import CreateMfaChallenge
from appwrite_console_python_sdk.paths.account.post import CreateNewUser
from appwrite_console_python_sdk.paths.account_sessions_oauth2_provider.get import CreateOAuth2Session
from appwrite_console_python_sdk.paths.account_tokens_oauth2_provider.get import CreateOAuth2Token
from appwrite_console_python_sdk.paths.account_recovery.post import CreatePasswordRecovery
from appwrite_console_python_sdk.paths.account_tokens_phone.post import CreatePhoneToken
from appwrite_console_python_sdk.paths.account_targets_push.post import CreatePushTarget
from appwrite_console_python_sdk.paths.account_sessions_token.post import CreateSessionFromToken
from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.delete import DeleteAuthenticatorById
from appwrite_console_python_sdk.paths.account_identities_identity_id.delete import DeleteIdentityById
from appwrite_console_python_sdk.paths.account_targets_target_id_push.delete import DeletePushTarget
from appwrite_console_python_sdk.paths.account_sessions.delete import DeleteSessions
from appwrite_console_python_sdk.paths.account.delete import DeleteUser
from appwrite_console_python_sdk.paths.account_sessions_session_id.patch import ExtendSessionLength
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.post import GenerateRecoveryCodes
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.get import GetMfaRecoveryCodes
from appwrite_console_python_sdk.paths.account_prefs.get import GetPrefsOperation
from appwrite_console_python_sdk.paths.account_sessions_session_id.get import GetSession
from appwrite_console_python_sdk.paths.account.get import GetUser
from appwrite_console_python_sdk.paths.account_identities.get import ListIdentities
from appwrite_console_python_sdk.paths.account_mfa_factors.get import ListMfaFactors
from appwrite_console_python_sdk.paths.account_sessions.get import ListSessions
from appwrite_console_python_sdk.paths.account_logs.get import ListUserLogs
from appwrite_console_python_sdk.paths.account_sessions_session_id.delete import LogoutSession
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.patch import RegenerateMfaRecoveryCodes
from appwrite_console_python_sdk.paths.account_verification_phone.post import SendVerificationSms
from appwrite_console_python_sdk.paths.account_email.patch import UpdateEmailAddress
from appwrite_console_python_sdk.paths.account_sessions_magic_url.put import UpdateMagicUrlSession
from appwrite_console_python_sdk.paths.account_mfa.patch import UpdateMfaStatus
from appwrite_console_python_sdk.paths.account_name.patch import UpdateName
from appwrite_console_python_sdk.paths.account_password.patch import UpdatePassword
from appwrite_console_python_sdk.paths.account_phone.patch import UpdatePhone
from appwrite_console_python_sdk.paths.account_sessions_phone.put import UpdatePhoneSession
from appwrite_console_python_sdk.paths.account_prefs.patch import UpdatePrefsOperation
from appwrite_console_python_sdk.paths.account_targets_target_id_push.put import UpdatePushTarget
from appwrite_console_python_sdk.paths.account_status.patch import UpdateStatus
from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.put import VerifyAuthenticator
from appwrite_console_python_sdk.apis.tags.account_api_raw import AccountApiRaw


class AccountApi(
    AddAuthenticatorApp,
    CompleteEmailVerification,
    CompleteMfaChallenge,
    CompletePasswordRecovery,
    ConfirmPhoneVerification,
    CreateAnonymousSession,
    CreateEmailPasswordSession,
    CreateEmailToken,
    CreateEmailVerification,
    CreateJwt,
    CreateMagicUrlToken,
    CreateMfaChallenge,
    CreateNewUser,
    CreateOAuth2Session,
    CreateOAuth2Token,
    CreatePasswordRecovery,
    CreatePhoneToken,
    CreatePushTarget,
    CreateSessionFromToken,
    DeleteAuthenticatorById,
    DeleteIdentityById,
    DeletePushTarget,
    DeleteSessions,
    DeleteUser,
    ExtendSessionLength,
    GenerateRecoveryCodes,
    GetMfaRecoveryCodes,
    GetPrefsOperation,
    GetSession,
    GetUser,
    ListIdentities,
    ListMfaFactors,
    ListSessions,
    ListUserLogs,
    LogoutSession,
    RegenerateMfaRecoveryCodes,
    SendVerificationSms,
    UpdateEmailAddress,
    UpdateMagicUrlSession,
    UpdateMfaStatus,
    UpdateName,
    UpdatePassword,
    UpdatePhone,
    UpdatePhoneSession,
    UpdatePrefsOperation,
    UpdatePushTarget,
    UpdateStatus,
    VerifyAuthenticator,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccountApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccountApiRaw(api_client)
