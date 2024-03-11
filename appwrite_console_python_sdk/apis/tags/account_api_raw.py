# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.post import AddAuthenticatorAppRaw
from appwrite_console_python_sdk.paths.account_verification.put import CompleteEmailVerificationRaw
from appwrite_console_python_sdk.paths.account_mfa_challenge.put import CompleteMfaChallengeRaw
from appwrite_console_python_sdk.paths.account_recovery.put import CompletePasswordRecoveryRaw
from appwrite_console_python_sdk.paths.account_verification_phone.put import ConfirmPhoneVerificationRaw
from appwrite_console_python_sdk.paths.account_sessions_anonymous.post import CreateAnonymousSessionRaw
from appwrite_console_python_sdk.paths.account_sessions_email.post import CreateEmailPasswordSessionRaw
from appwrite_console_python_sdk.paths.account_tokens_email.post import CreateEmailTokenRaw
from appwrite_console_python_sdk.paths.account_verification.post import CreateEmailVerificationRaw
from appwrite_console_python_sdk.paths.account_jwt.post import CreateJwtRaw
from appwrite_console_python_sdk.paths.account_tokens_magic_url.post import CreateMagicUrlTokenRaw
from appwrite_console_python_sdk.paths.account_mfa_challenge.post import CreateMfaChallengeRaw
from appwrite_console_python_sdk.paths.account.post import CreateNewUserRaw
from appwrite_console_python_sdk.paths.account_sessions_oauth2_provider.get import CreateOAuth2SessionRaw
from appwrite_console_python_sdk.paths.account_tokens_oauth2_provider.get import CreateOAuth2TokenRaw
from appwrite_console_python_sdk.paths.account_recovery.post import CreatePasswordRecoveryRaw
from appwrite_console_python_sdk.paths.account_tokens_phone.post import CreatePhoneTokenRaw
from appwrite_console_python_sdk.paths.account_targets_push.post import CreatePushTargetRaw
from appwrite_console_python_sdk.paths.account_sessions_token.post import CreateSessionFromTokenRaw
from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.delete import DeleteAuthenticatorByIdRaw
from appwrite_console_python_sdk.paths.account_identities_identity_id.delete import DeleteIdentityByIdRaw
from appwrite_console_python_sdk.paths.account_targets_target_id_push.delete import DeletePushTargetRaw
from appwrite_console_python_sdk.paths.account_sessions.delete import DeleteSessionsRaw
from appwrite_console_python_sdk.paths.account.delete import DeleteUserRaw
from appwrite_console_python_sdk.paths.account_sessions_session_id.patch import ExtendSessionLengthRaw
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.post import GenerateRecoveryCodesRaw
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.get import GetMfaRecoveryCodesRaw
from appwrite_console_python_sdk.paths.account_prefs.get import GetPrefsOperationRaw
from appwrite_console_python_sdk.paths.account_sessions_session_id.get import GetSessionRaw
from appwrite_console_python_sdk.paths.account.get import GetUserRaw
from appwrite_console_python_sdk.paths.account_identities.get import ListIdentitiesRaw
from appwrite_console_python_sdk.paths.account_mfa_factors.get import ListMfaFactorsRaw
from appwrite_console_python_sdk.paths.account_sessions.get import ListSessionsRaw
from appwrite_console_python_sdk.paths.account_logs.get import ListUserLogsRaw
from appwrite_console_python_sdk.paths.account_sessions_session_id.delete import LogoutSessionRaw
from appwrite_console_python_sdk.paths.account_mfa_recovery_codes.patch import RegenerateMfaRecoveryCodesRaw
from appwrite_console_python_sdk.paths.account_verification_phone.post import SendVerificationSmsRaw
from appwrite_console_python_sdk.paths.account_email.patch import UpdateEmailAddressRaw
from appwrite_console_python_sdk.paths.account_sessions_magic_url.put import UpdateMagicUrlSessionRaw
from appwrite_console_python_sdk.paths.account_mfa.patch import UpdateMfaStatusRaw
from appwrite_console_python_sdk.paths.account_name.patch import UpdateNameRaw
from appwrite_console_python_sdk.paths.account_password.patch import UpdatePasswordRaw
from appwrite_console_python_sdk.paths.account_phone.patch import UpdatePhoneRaw
from appwrite_console_python_sdk.paths.account_sessions_phone.put import UpdatePhoneSessionRaw
from appwrite_console_python_sdk.paths.account_prefs.patch import UpdatePrefsOperationRaw
from appwrite_console_python_sdk.paths.account_targets_target_id_push.put import UpdatePushTargetRaw
from appwrite_console_python_sdk.paths.account_status.patch import UpdateStatusRaw
from appwrite_console_python_sdk.paths.account_mfa_authenticators_type.put import VerifyAuthenticatorRaw


class AccountApiRaw(
    AddAuthenticatorAppRaw,
    CompleteEmailVerificationRaw,
    CompleteMfaChallengeRaw,
    CompletePasswordRecoveryRaw,
    ConfirmPhoneVerificationRaw,
    CreateAnonymousSessionRaw,
    CreateEmailPasswordSessionRaw,
    CreateEmailTokenRaw,
    CreateEmailVerificationRaw,
    CreateJwtRaw,
    CreateMagicUrlTokenRaw,
    CreateMfaChallengeRaw,
    CreateNewUserRaw,
    CreateOAuth2SessionRaw,
    CreateOAuth2TokenRaw,
    CreatePasswordRecoveryRaw,
    CreatePhoneTokenRaw,
    CreatePushTargetRaw,
    CreateSessionFromTokenRaw,
    DeleteAuthenticatorByIdRaw,
    DeleteIdentityByIdRaw,
    DeletePushTargetRaw,
    DeleteSessionsRaw,
    DeleteUserRaw,
    ExtendSessionLengthRaw,
    GenerateRecoveryCodesRaw,
    GetMfaRecoveryCodesRaw,
    GetPrefsOperationRaw,
    GetSessionRaw,
    GetUserRaw,
    ListIdentitiesRaw,
    ListMfaFactorsRaw,
    ListSessionsRaw,
    ListUserLogsRaw,
    LogoutSessionRaw,
    RegenerateMfaRecoveryCodesRaw,
    SendVerificationSmsRaw,
    UpdateEmailAddressRaw,
    UpdateMagicUrlSessionRaw,
    UpdateMfaStatusRaw,
    UpdateNameRaw,
    UpdatePasswordRaw,
    UpdatePhoneRaw,
    UpdatePhoneSessionRaw,
    UpdatePrefsOperationRaw,
    UpdatePushTargetRaw,
    UpdateStatusRaw,
    VerifyAuthenticatorRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
