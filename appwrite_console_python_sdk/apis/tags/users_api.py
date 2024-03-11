# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.users_argon2.post import CreateArgonUser
from appwrite_console_python_sdk.paths.users_bcrypt.post import CreateBcryptPassword
from appwrite_console_python_sdk.paths.users_md5.post import CreateMd5User
from appwrite_console_python_sdk.paths.users_user_id_targets.post import CreateMessagingTarget
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.patch import CreateMfaRecoveryCodes
from appwrite_console_python_sdk.paths.users.post import CreateNewUser
from appwrite_console_python_sdk.paths.users_scrypt_modified.post import CreateScryptModifiedUser
from appwrite_console_python_sdk.paths.users_scrypt.post import CreateScryptUser
from appwrite_console_python_sdk.paths.users_user_id_sessions.post import CreateSession
from appwrite_console_python_sdk.paths.users_phpass.post import CreateWithPhPass
from appwrite_console_python_sdk.paths.users_sha.post import CreateWithShaPassword
from appwrite_console_python_sdk.paths.users_user_id_mfa_authenticators_type.delete import DeleteAuthenticator
from appwrite_console_python_sdk.paths.users_user_id.delete import DeleteById
from appwrite_console_python_sdk.paths.users_identities_identity_id.delete import DeleteIdentityById
from appwrite_console_python_sdk.paths.users_user_id_sessions_session_id.delete import DeleteSessionByUserIdAndSessionId
from appwrite_console_python_sdk.paths.users_user_id_sessions.delete import DeleteSessionsById
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.delete import DeleteTargetMessaging
from appwrite_console_python_sdk.paths.users_user_id_tokens.post import GenerateToken
from appwrite_console_python_sdk.paths.users_user_id_logs.get import GetLogsByUserId
from appwrite_console_python_sdk.paths.users_user_id_memberships.get import GetMembershipsById
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.get import GetMfaRecoveryCodes
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.get import GetTarget
from appwrite_console_python_sdk.paths.users_usage.get import GetUsageStats
from appwrite_console_python_sdk.paths.users_user_id.get import GetUserById
from appwrite_console_python_sdk.paths.users_user_id_prefs.get import GetUserPrefsById
from appwrite_console_python_sdk.paths.users.get import ListFilteredUsers
from appwrite_console_python_sdk.paths.users_identities.get import ListIdentities
from appwrite_console_python_sdk.paths.users_user_id_mfa_factors.get import ListMfaFactors
from appwrite_console_python_sdk.paths.users_user_id_sessions.get import ListSessionsByUserId
from appwrite_console_python_sdk.paths.users_user_id_targets.get import ListTargets
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.put import RegenerateMfaRecoveryCodesByUserId
from appwrite_console_python_sdk.paths.users_user_id_email.patch import UpdateEmailById
from appwrite_console_python_sdk.paths.users_user_id_verification.patch import UpdateEmailVerificationStatus
from appwrite_console_python_sdk.paths.users_user_id_labels.put import UpdateLabelsByUserId
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.patch import UpdateMessagingTarget
from appwrite_console_python_sdk.paths.users_user_id_mfa.patch import UpdateMfaStatus
from appwrite_console_python_sdk.paths.users_user_id_name.patch import UpdateNameById
from appwrite_console_python_sdk.paths.users_user_id_password.patch import UpdatePasswordByUserId
from appwrite_console_python_sdk.paths.users_user_id_phone.patch import UpdatePhoneByUserId
from appwrite_console_python_sdk.paths.users_user_id_verification_phone.patch import UpdatePhoneVerification
from appwrite_console_python_sdk.paths.users_user_id_prefs.patch import UpdatePrefsById
from appwrite_console_python_sdk.paths.users_user_id_status.patch import UpdateStatusByUserId
from appwrite_console_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    CreateArgonUser,
    CreateBcryptPassword,
    CreateMd5User,
    CreateMessagingTarget,
    CreateMfaRecoveryCodes,
    CreateNewUser,
    CreateScryptModifiedUser,
    CreateScryptUser,
    CreateSession,
    CreateWithPhPass,
    CreateWithShaPassword,
    DeleteAuthenticator,
    DeleteById,
    DeleteIdentityById,
    DeleteSessionByUserIdAndSessionId,
    DeleteSessionsById,
    DeleteTargetMessaging,
    GenerateToken,
    GetLogsByUserId,
    GetMembershipsById,
    GetMfaRecoveryCodes,
    GetTarget,
    GetUsageStats,
    GetUserById,
    GetUserPrefsById,
    ListFilteredUsers,
    ListIdentities,
    ListMfaFactors,
    ListSessionsByUserId,
    ListTargets,
    RegenerateMfaRecoveryCodesByUserId,
    UpdateEmailById,
    UpdateEmailVerificationStatus,
    UpdateLabelsByUserId,
    UpdateMessagingTarget,
    UpdateMfaStatus,
    UpdateNameById,
    UpdatePasswordByUserId,
    UpdatePhoneByUserId,
    UpdatePhoneVerification,
    UpdatePrefsById,
    UpdateStatusByUserId,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)
