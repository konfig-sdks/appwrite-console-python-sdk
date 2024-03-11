# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.users_argon2.post import CreateArgonUserRaw
from appwrite_console_python_sdk.paths.users_bcrypt.post import CreateBcryptPasswordRaw
from appwrite_console_python_sdk.paths.users_md5.post import CreateMd5UserRaw
from appwrite_console_python_sdk.paths.users_user_id_targets.post import CreateMessagingTargetRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.patch import CreateMfaRecoveryCodesRaw
from appwrite_console_python_sdk.paths.users.post import CreateNewUserRaw
from appwrite_console_python_sdk.paths.users_scrypt_modified.post import CreateScryptModifiedUserRaw
from appwrite_console_python_sdk.paths.users_scrypt.post import CreateScryptUserRaw
from appwrite_console_python_sdk.paths.users_user_id_sessions.post import CreateSessionRaw
from appwrite_console_python_sdk.paths.users_phpass.post import CreateWithPhPassRaw
from appwrite_console_python_sdk.paths.users_sha.post import CreateWithShaPasswordRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa_authenticators_type.delete import DeleteAuthenticatorRaw
from appwrite_console_python_sdk.paths.users_user_id.delete import DeleteByIdRaw
from appwrite_console_python_sdk.paths.users_identities_identity_id.delete import DeleteIdentityByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_sessions_session_id.delete import DeleteSessionByUserIdAndSessionIdRaw
from appwrite_console_python_sdk.paths.users_user_id_sessions.delete import DeleteSessionsByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.delete import DeleteTargetMessagingRaw
from appwrite_console_python_sdk.paths.users_user_id_tokens.post import GenerateTokenRaw
from appwrite_console_python_sdk.paths.users_user_id_logs.get import GetLogsByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_memberships.get import GetMembershipsByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.get import GetMfaRecoveryCodesRaw
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.get import GetTargetRaw
from appwrite_console_python_sdk.paths.users_usage.get import GetUsageStatsRaw
from appwrite_console_python_sdk.paths.users_user_id.get import GetUserByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_prefs.get import GetUserPrefsByIdRaw
from appwrite_console_python_sdk.paths.users.get import ListFilteredUsersRaw
from appwrite_console_python_sdk.paths.users_identities.get import ListIdentitiesRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa_factors.get import ListMfaFactorsRaw
from appwrite_console_python_sdk.paths.users_user_id_sessions.get import ListSessionsByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_targets.get import ListTargetsRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa_recovery_codes.put import RegenerateMfaRecoveryCodesByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_email.patch import UpdateEmailByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_verification.patch import UpdateEmailVerificationStatusRaw
from appwrite_console_python_sdk.paths.users_user_id_labels.put import UpdateLabelsByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_targets_target_id.patch import UpdateMessagingTargetRaw
from appwrite_console_python_sdk.paths.users_user_id_mfa.patch import UpdateMfaStatusRaw
from appwrite_console_python_sdk.paths.users_user_id_name.patch import UpdateNameByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_password.patch import UpdatePasswordByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_phone.patch import UpdatePhoneByUserIdRaw
from appwrite_console_python_sdk.paths.users_user_id_verification_phone.patch import UpdatePhoneVerificationRaw
from appwrite_console_python_sdk.paths.users_user_id_prefs.patch import UpdatePrefsByIdRaw
from appwrite_console_python_sdk.paths.users_user_id_status.patch import UpdateStatusByUserIdRaw


class UsersApiRaw(
    CreateArgonUserRaw,
    CreateBcryptPasswordRaw,
    CreateMd5UserRaw,
    CreateMessagingTargetRaw,
    CreateMfaRecoveryCodesRaw,
    CreateNewUserRaw,
    CreateScryptModifiedUserRaw,
    CreateScryptUserRaw,
    CreateSessionRaw,
    CreateWithPhPassRaw,
    CreateWithShaPasswordRaw,
    DeleteAuthenticatorRaw,
    DeleteByIdRaw,
    DeleteIdentityByIdRaw,
    DeleteSessionByUserIdAndSessionIdRaw,
    DeleteSessionsByIdRaw,
    DeleteTargetMessagingRaw,
    GenerateTokenRaw,
    GetLogsByUserIdRaw,
    GetMembershipsByIdRaw,
    GetMfaRecoveryCodesRaw,
    GetTargetRaw,
    GetUsageStatsRaw,
    GetUserByIdRaw,
    GetUserPrefsByIdRaw,
    ListFilteredUsersRaw,
    ListIdentitiesRaw,
    ListMfaFactorsRaw,
    ListSessionsByUserIdRaw,
    ListTargetsRaw,
    RegenerateMfaRecoveryCodesByUserIdRaw,
    UpdateEmailByIdRaw,
    UpdateEmailVerificationStatusRaw,
    UpdateLabelsByUserIdRaw,
    UpdateMessagingTargetRaw,
    UpdateMfaStatusRaw,
    UpdateNameByIdRaw,
    UpdatePasswordByUserIdRaw,
    UpdatePhoneByUserIdRaw,
    UpdatePhoneVerificationRaw,
    UpdatePrefsByIdRaw,
    UpdateStatusByUserIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
