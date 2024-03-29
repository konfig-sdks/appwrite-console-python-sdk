# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from appwrite_console_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from appwrite_console_python_sdk.model.account_complete_email_verification_request import AccountCompleteEmailVerificationRequest
from appwrite_console_python_sdk.model.account_complete_mfa_challenge_request import AccountCompleteMfaChallengeRequest
from appwrite_console_python_sdk.model.account_complete_password_recovery_request import AccountCompletePasswordRecoveryRequest
from appwrite_console_python_sdk.model.account_confirm_phone_verification_request import AccountConfirmPhoneVerificationRequest
from appwrite_console_python_sdk.model.account_create_email_password_session_request import AccountCreateEmailPasswordSessionRequest
from appwrite_console_python_sdk.model.account_create_email_token_request import AccountCreateEmailTokenRequest
from appwrite_console_python_sdk.model.account_create_email_verification_request import AccountCreateEmailVerificationRequest
from appwrite_console_python_sdk.model.account_create_magic_url_token_request import AccountCreateMagicUrlTokenRequest
from appwrite_console_python_sdk.model.account_create_mfa_challenge_request import AccountCreateMfaChallengeRequest
from appwrite_console_python_sdk.model.account_create_new_user_request import AccountCreateNewUserRequest
from appwrite_console_python_sdk.model.account_create_password_recovery_request import AccountCreatePasswordRecoveryRequest
from appwrite_console_python_sdk.model.account_create_phone_token_request import AccountCreatePhoneTokenRequest
from appwrite_console_python_sdk.model.account_create_push_target_request import AccountCreatePushTargetRequest
from appwrite_console_python_sdk.model.account_create_session_from_token_request import AccountCreateSessionFromTokenRequest
from appwrite_console_python_sdk.model.account_delete_authenticator_by_id_request import AccountDeleteAuthenticatorByIdRequest
from appwrite_console_python_sdk.model.account_update_email_address_request import AccountUpdateEmailAddressRequest
from appwrite_console_python_sdk.model.account_update_magic_url_session_request import AccountUpdateMagicUrlSessionRequest
from appwrite_console_python_sdk.model.account_update_mfa_status_request import AccountUpdateMfaStatusRequest
from appwrite_console_python_sdk.model.account_update_name_request import AccountUpdateNameRequest
from appwrite_console_python_sdk.model.account_update_password_request import AccountUpdatePasswordRequest
from appwrite_console_python_sdk.model.account_update_phone_request import AccountUpdatePhoneRequest
from appwrite_console_python_sdk.model.account_update_phone_session_request import AccountUpdatePhoneSessionRequest
from appwrite_console_python_sdk.model.account_update_prefs_operation_request import AccountUpdatePrefsOperationRequest
from appwrite_console_python_sdk.model.account_update_push_target_request import AccountUpdatePushTargetRequest
from appwrite_console_python_sdk.model.account_verify_authenticator_request import AccountVerifyAuthenticatorRequest
from appwrite_console_python_sdk.model.algo_argon2 import AlgoArgon2
from appwrite_console_python_sdk.model.algo_bcrypt import AlgoBcrypt
from appwrite_console_python_sdk.model.algo_md5 import AlgoMd5
from appwrite_console_python_sdk.model.algo_phpass import AlgoPhpass
from appwrite_console_python_sdk.model.algo_scrypt import AlgoScrypt
from appwrite_console_python_sdk.model.algo_scrypt_modified import AlgoScryptModified
from appwrite_console_python_sdk.model.algo_sha import AlgoSha
from appwrite_console_python_sdk.model.any import Any
from appwrite_console_python_sdk.model.assistant_ask_query_request import AssistantAskQueryRequest
from appwrite_console_python_sdk.model.attribute_boolean import AttributeBoolean
from appwrite_console_python_sdk.model.attribute_datetime import AttributeDatetime
from appwrite_console_python_sdk.model.attribute_email import AttributeEmail
from appwrite_console_python_sdk.model.attribute_enum import AttributeEnum
from appwrite_console_python_sdk.model.attribute_enum_elements import AttributeEnumElements
from appwrite_console_python_sdk.model.attribute_float import AttributeFloat
from appwrite_console_python_sdk.model.attribute_integer import AttributeInteger
from appwrite_console_python_sdk.model.attribute_ip import AttributeIp
from appwrite_console_python_sdk.model.attribute_list import AttributeList
from appwrite_console_python_sdk.model.attribute_list_attributes import AttributeListAttributes
from appwrite_console_python_sdk.model.attribute_relationship import AttributeRelationship
from appwrite_console_python_sdk.model.attribute_string import AttributeString
from appwrite_console_python_sdk.model.attribute_url import AttributeUrl
from appwrite_console_python_sdk.model.auth_provider import AuthProvider
from appwrite_console_python_sdk.model.branch import Branch
from appwrite_console_python_sdk.model.branch_list import BranchList
from appwrite_console_python_sdk.model.bucket import Bucket
from appwrite_console_python_sdk.model.bucket_allowed_file_extensions import BucketAllowedFileExtensions
from appwrite_console_python_sdk.model.bucket_list import BucketList
from appwrite_console_python_sdk.model.bucketpermissions import Bucketpermissions
from appwrite_console_python_sdk.model.collection import Collection
from appwrite_console_python_sdk.model.collection_attributes import CollectionAttributes
from appwrite_console_python_sdk.model.collection_list import CollectionList
from appwrite_console_python_sdk.model.collectionpermissions import Collectionpermissions
from appwrite_console_python_sdk.model.console_variables import ConsoleVariables
from appwrite_console_python_sdk.model.continent import Continent
from appwrite_console_python_sdk.model.continent_list import ContinentList
from appwrite_console_python_sdk.model.country import Country
from appwrite_console_python_sdk.model.country_list import CountryList
from appwrite_console_python_sdk.model.currency import Currency
from appwrite_console_python_sdk.model.currency_list import CurrencyList
from appwrite_console_python_sdk.model.database import Database
from appwrite_console_python_sdk.model.database_list import DatabaseList
from appwrite_console_python_sdk.model.databases_create_boolean_attribute_request import DatabasesCreateBooleanAttributeRequest
from appwrite_console_python_sdk.model.databases_create_collection_request import DatabasesCreateCollectionRequest
from appwrite_console_python_sdk.model.databases_create_collection_request_permissions import DatabasesCreateCollectionRequestPermissions
from appwrite_console_python_sdk.model.databases_create_datetime_attribute_request import DatabasesCreateDatetimeAttributeRequest
from appwrite_console_python_sdk.model.databases_create_document_request import DatabasesCreateDocumentRequest
from appwrite_console_python_sdk.model.databases_create_document_request_permissions import DatabasesCreateDocumentRequestPermissions
from appwrite_console_python_sdk.model.databases_create_email_attribute_request import DatabasesCreateEmailAttributeRequest
from appwrite_console_python_sdk.model.databases_create_enum_attribute_request import DatabasesCreateEnumAttributeRequest
from appwrite_console_python_sdk.model.databases_create_enum_attribute_request_elements import DatabasesCreateEnumAttributeRequestElements
from appwrite_console_python_sdk.model.databases_create_float_attribute_request import DatabasesCreateFloatAttributeRequest
from appwrite_console_python_sdk.model.databases_create_index_on_attributes_request import DatabasesCreateIndexOnAttributesRequest
from appwrite_console_python_sdk.model.databases_create_index_on_attributes_request_attributes import DatabasesCreateIndexOnAttributesRequestAttributes
from appwrite_console_python_sdk.model.databases_create_index_on_attributes_request_orders import DatabasesCreateIndexOnAttributesRequestOrders
from appwrite_console_python_sdk.model.databases_create_integer_attribute_request import DatabasesCreateIntegerAttributeRequest
from appwrite_console_python_sdk.model.databases_create_ip_attribute_request import DatabasesCreateIpAttributeRequest
from appwrite_console_python_sdk.model.databases_create_new_database_request import DatabasesCreateNewDatabaseRequest
from appwrite_console_python_sdk.model.databases_create_relationship_attribute_request import DatabasesCreateRelationshipAttributeRequest
from appwrite_console_python_sdk.model.databases_create_string_attribute_request import DatabasesCreateStringAttributeRequest
from appwrite_console_python_sdk.model.databases_create_url_attribute_request import DatabasesCreateUrlAttributeRequest
from appwrite_console_python_sdk.model.databases_get_attribute_by_id_response import DatabasesGetAttributeByIdResponse
from appwrite_console_python_sdk.model.databases_patch_date_time_attribute_request import DatabasesPatchDateTimeAttributeRequest
from appwrite_console_python_sdk.model.databases_update_boolean_attribute_request import DatabasesUpdateBooleanAttributeRequest
from appwrite_console_python_sdk.model.databases_update_by_id_request import DatabasesUpdateByIdRequest
from appwrite_console_python_sdk.model.databases_update_collection_by_id_request import DatabasesUpdateCollectionByIdRequest
from appwrite_console_python_sdk.model.databases_update_collection_by_id_request_permissions import DatabasesUpdateCollectionByIdRequestPermissions
from appwrite_console_python_sdk.model.databases_update_document_by_id_request import DatabasesUpdateDocumentByIdRequest
from appwrite_console_python_sdk.model.databases_update_document_by_id_request_permissions import DatabasesUpdateDocumentByIdRequestPermissions
from appwrite_console_python_sdk.model.databases_update_email_attribute_request import DatabasesUpdateEmailAttributeRequest
from appwrite_console_python_sdk.model.databases_update_enum_attribute_request import DatabasesUpdateEnumAttributeRequest
from appwrite_console_python_sdk.model.databases_update_enum_attribute_request_elements import DatabasesUpdateEnumAttributeRequestElements
from appwrite_console_python_sdk.model.databases_update_float_attribute_request import DatabasesUpdateFloatAttributeRequest
from appwrite_console_python_sdk.model.databases_update_integer_attribute_request import DatabasesUpdateIntegerAttributeRequest
from appwrite_console_python_sdk.model.databases_update_ip_address_attribute_request import DatabasesUpdateIpAddressAttributeRequest
from appwrite_console_python_sdk.model.databases_update_relationship_attribute_request import DatabasesUpdateRelationshipAttributeRequest
from appwrite_console_python_sdk.model.databases_update_string_attribute_request import DatabasesUpdateStringAttributeRequest
from appwrite_console_python_sdk.model.databases_update_url_attribute_request import DatabasesUpdateUrlAttributeRequest
from appwrite_console_python_sdk.model.deployment import Deployment
from appwrite_console_python_sdk.model.deployment_list import DeploymentList
from appwrite_console_python_sdk.model.detection import Detection
from appwrite_console_python_sdk.model.document import Document
from appwrite_console_python_sdk.model.document_list import DocumentList
from appwrite_console_python_sdk.model.documentpermissions import Documentpermissions
from appwrite_console_python_sdk.model.email_template import EmailTemplate
from appwrite_console_python_sdk.model.error import Error
from appwrite_console_python_sdk.model.execution import Execution
from appwrite_console_python_sdk.model.execution_list import ExecutionList
from appwrite_console_python_sdk.model.executionpermissions import Executionpermissions
from appwrite_console_python_sdk.model.file import File
from appwrite_console_python_sdk.model.file_list import FileList
from appwrite_console_python_sdk.model.filepermissions import Filepermissions
from appwrite_console_python_sdk.model.firebase_project import FirebaseProject
from appwrite_console_python_sdk.model.firebase_project_list import FirebaseProjectList
from appwrite_console_python_sdk.model.function import Function
from appwrite_console_python_sdk.model.function_events import FunctionEvents
from appwrite_console_python_sdk.model.function_execute import FunctionExecute
from appwrite_console_python_sdk.model.function_list import FunctionList
from appwrite_console_python_sdk.model.functions_create_deployment_request import FunctionsCreateDeploymentRequest
from appwrite_console_python_sdk.model.functions_create_function_request import FunctionsCreateFunctionRequest
from appwrite_console_python_sdk.model.functions_create_function_request_events import FunctionsCreateFunctionRequestEvents
from appwrite_console_python_sdk.model.functions_create_function_request_execute import FunctionsCreateFunctionRequestExecute
from appwrite_console_python_sdk.model.functions_create_variable_request import FunctionsCreateVariableRequest
from appwrite_console_python_sdk.model.functions_trigger_execution_request import FunctionsTriggerExecutionRequest
from appwrite_console_python_sdk.model.functions_update_by_id_request import FunctionsUpdateByIdRequest
from appwrite_console_python_sdk.model.functions_update_by_id_request_events import FunctionsUpdateByIdRequestEvents
from appwrite_console_python_sdk.model.functions_update_by_id_request_execute import FunctionsUpdateByIdRequestExecute
from appwrite_console_python_sdk.model.functions_update_variable_by_id_request import FunctionsUpdateVariableByIdRequest
from appwrite_console_python_sdk.model.headers import Headers
from appwrite_console_python_sdk.model.health_antivirus import HealthAntivirus
from appwrite_console_python_sdk.model.health_certificate import HealthCertificate
from appwrite_console_python_sdk.model.health_queue import HealthQueue
from appwrite_console_python_sdk.model.health_status import HealthStatus
from appwrite_console_python_sdk.model.health_time import HealthTime
from appwrite_console_python_sdk.model.identity import Identity
from appwrite_console_python_sdk.model.identity_list import IdentityList
from appwrite_console_python_sdk.model.index import Index
from appwrite_console_python_sdk.model.index_attributes import IndexAttributes
from appwrite_console_python_sdk.model.index_list import IndexList
from appwrite_console_python_sdk.model.index_orders import IndexOrders
from appwrite_console_python_sdk.model.installation import Installation
from appwrite_console_python_sdk.model.installation_list import InstallationList
from appwrite_console_python_sdk.model.jwt import Jwt
from appwrite_console_python_sdk.model.key import Key
from appwrite_console_python_sdk.model.key_list import KeyList
from appwrite_console_python_sdk.model.key_scopes import KeyScopes
from appwrite_console_python_sdk.model.key_sdks import KeySdks
from appwrite_console_python_sdk.model.language import Language
from appwrite_console_python_sdk.model.language_list import LanguageList
from appwrite_console_python_sdk.model.locale import Locale
from appwrite_console_python_sdk.model.locale_code import LocaleCode
from appwrite_console_python_sdk.model.locale_code_list import LocaleCodeList
from appwrite_console_python_sdk.model.log import Log
from appwrite_console_python_sdk.model.log_list import LogList
from appwrite_console_python_sdk.model.membership import Membership
from appwrite_console_python_sdk.model.membership_list import MembershipList
from appwrite_console_python_sdk.model.membership_roles import MembershipRoles
from appwrite_console_python_sdk.model.message import Message
from appwrite_console_python_sdk.model.message_delivery_errors import MessageDeliveryErrors
from appwrite_console_python_sdk.model.message_list import MessageList
from appwrite_console_python_sdk.model.message_targets import MessageTargets
from appwrite_console_python_sdk.model.message_topics import MessageTopics
from appwrite_console_python_sdk.model.message_users import MessageUsers
from appwrite_console_python_sdk.model.messaging_create_apns_provider_request import MessagingCreateApnsProviderRequest
from appwrite_console_python_sdk.model.messaging_create_email_message_request import MessagingCreateEmailMessageRequest
from appwrite_console_python_sdk.model.messaging_create_email_message_request_attachments import MessagingCreateEmailMessageRequestAttachments
from appwrite_console_python_sdk.model.messaging_create_email_message_request_bcc import MessagingCreateEmailMessageRequestBcc
from appwrite_console_python_sdk.model.messaging_create_email_message_request_cc import MessagingCreateEmailMessageRequestCc
from appwrite_console_python_sdk.model.messaging_create_email_message_request_targets import MessagingCreateEmailMessageRequestTargets
from appwrite_console_python_sdk.model.messaging_create_email_message_request_topics import MessagingCreateEmailMessageRequestTopics
from appwrite_console_python_sdk.model.messaging_create_email_message_request_users import MessagingCreateEmailMessageRequestUsers
from appwrite_console_python_sdk.model.messaging_create_fcm_provider_request import MessagingCreateFcmProviderRequest
from appwrite_console_python_sdk.model.messaging_create_mailgun_provider_request import MessagingCreateMailgunProviderRequest
from appwrite_console_python_sdk.model.messaging_create_msg_provider_request import MessagingCreateMsgProviderRequest
from appwrite_console_python_sdk.model.messaging_create_new_topic_request import MessagingCreateNewTopicRequest
from appwrite_console_python_sdk.model.messaging_create_new_topic_request_subscribe import MessagingCreateNewTopicRequestSubscribe
from appwrite_console_python_sdk.model.messaging_create_push_notification_request import MessagingCreatePushNotificationRequest
from appwrite_console_python_sdk.model.messaging_create_push_notification_request_targets import MessagingCreatePushNotificationRequestTargets
from appwrite_console_python_sdk.model.messaging_create_push_notification_request_topics import MessagingCreatePushNotificationRequestTopics
from appwrite_console_python_sdk.model.messaging_create_push_notification_request_users import MessagingCreatePushNotificationRequestUsers
from appwrite_console_python_sdk.model.messaging_create_sendgrid_provider_request import MessagingCreateSendgridProviderRequest
from appwrite_console_python_sdk.model.messaging_create_sms_message_request import MessagingCreateSmsMessageRequest
from appwrite_console_python_sdk.model.messaging_create_sms_message_request_targets import MessagingCreateSmsMessageRequestTargets
from appwrite_console_python_sdk.model.messaging_create_sms_message_request_topics import MessagingCreateSmsMessageRequestTopics
from appwrite_console_python_sdk.model.messaging_create_sms_message_request_users import MessagingCreateSmsMessageRequestUsers
from appwrite_console_python_sdk.model.messaging_create_smtp_provider_request import MessagingCreateSmtpProviderRequest
from appwrite_console_python_sdk.model.messaging_create_subscriber_request import MessagingCreateSubscriberRequest
from appwrite_console_python_sdk.model.messaging_create_telesign_provider_request import MessagingCreateTelesignProviderRequest
from appwrite_console_python_sdk.model.messaging_create_textmagic_provider_request import MessagingCreateTextmagicProviderRequest
from appwrite_console_python_sdk.model.messaging_create_twilio_provider_request import MessagingCreateTwilioProviderRequest
from appwrite_console_python_sdk.model.messaging_create_vonage_provider_request import MessagingCreateVonageProviderRequest
from appwrite_console_python_sdk.model.messaging_update_apns_provider_request import MessagingUpdateApnsProviderRequest
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request import MessagingUpdateEmailByIdRequest
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request_bcc import MessagingUpdateEmailByIdRequestBcc
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request_cc import MessagingUpdateEmailByIdRequestCc
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request_targets import MessagingUpdateEmailByIdRequestTargets
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request_topics import MessagingUpdateEmailByIdRequestTopics
from appwrite_console_python_sdk.model.messaging_update_email_by_id_request_users import MessagingUpdateEmailByIdRequestUsers
from appwrite_console_python_sdk.model.messaging_update_fcm_provider_request import MessagingUpdateFcmProviderRequest
from appwrite_console_python_sdk.model.messaging_update_mailgun_provider_request import MessagingUpdateMailgunProviderRequest
from appwrite_console_python_sdk.model.messaging_update_provider_by_id_request import MessagingUpdateProviderByIdRequest
from appwrite_console_python_sdk.model.messaging_update_push_message_request import MessagingUpdatePushMessageRequest
from appwrite_console_python_sdk.model.messaging_update_push_message_request_targets import MessagingUpdatePushMessageRequestTargets
from appwrite_console_python_sdk.model.messaging_update_push_message_request_topics import MessagingUpdatePushMessageRequestTopics
from appwrite_console_python_sdk.model.messaging_update_push_message_request_users import MessagingUpdatePushMessageRequestUsers
from appwrite_console_python_sdk.model.messaging_update_sendgrid_provider_request import MessagingUpdateSendgridProviderRequest
from appwrite_console_python_sdk.model.messaging_update_sms_message_by_id_request import MessagingUpdateSmsMessageByIdRequest
from appwrite_console_python_sdk.model.messaging_update_sms_message_by_id_request_targets import MessagingUpdateSmsMessageByIdRequestTargets
from appwrite_console_python_sdk.model.messaging_update_sms_message_by_id_request_topics import MessagingUpdateSmsMessageByIdRequestTopics
from appwrite_console_python_sdk.model.messaging_update_sms_message_by_id_request_users import MessagingUpdateSmsMessageByIdRequestUsers
from appwrite_console_python_sdk.model.messaging_update_smtp_provider_request import MessagingUpdateSmtpProviderRequest
from appwrite_console_python_sdk.model.messaging_update_telesign_provider_request import MessagingUpdateTelesignProviderRequest
from appwrite_console_python_sdk.model.messaging_update_textmagic_provider_request import MessagingUpdateTextmagicProviderRequest
from appwrite_console_python_sdk.model.messaging_update_topic_by_id_request import MessagingUpdateTopicByIdRequest
from appwrite_console_python_sdk.model.messaging_update_topic_by_id_request_subscribe import MessagingUpdateTopicByIdRequestSubscribe
from appwrite_console_python_sdk.model.messaging_update_twilio_provider_request import MessagingUpdateTwilioProviderRequest
from appwrite_console_python_sdk.model.messaging_update_vonage_provider_by_id_request import MessagingUpdateVonageProviderByIdRequest
from appwrite_console_python_sdk.model.metric import Metric
from appwrite_console_python_sdk.model.metric_breakdown import MetricBreakdown
from appwrite_console_python_sdk.model.mfa_challenge import MfaChallenge
from appwrite_console_python_sdk.model.mfa_factors import MfaFactors
from appwrite_console_python_sdk.model.mfa_recovery_codes import MfaRecoveryCodes
from appwrite_console_python_sdk.model.mfa_recovery_codes_recovery_codes import MfaRecoveryCodesRecoveryCodes
from appwrite_console_python_sdk.model.mfa_type import MfaType
from appwrite_console_python_sdk.model.migration import Migration
from appwrite_console_python_sdk.model.migration_errors import MigrationErrors
from appwrite_console_python_sdk.model.migration_list import MigrationList
from appwrite_console_python_sdk.model.migration_report import MigrationReport
from appwrite_console_python_sdk.model.migration_resources import MigrationResources
from appwrite_console_python_sdk.model.migrations_create_appwrite_migration_request import MigrationsCreateAppwriteMigrationRequest
from appwrite_console_python_sdk.model.migrations_create_appwrite_migration_request_resources import MigrationsCreateAppwriteMigrationRequestResources
from appwrite_console_python_sdk.model.migrations_create_n_host_migration_request import MigrationsCreateNHostMigrationRequest
from appwrite_console_python_sdk.model.migrations_create_n_host_migration_request_resources import MigrationsCreateNHostMigrationRequestResources
from appwrite_console_python_sdk.model.migrations_firebase_data_migration_request import MigrationsFirebaseDataMigrationRequest
from appwrite_console_python_sdk.model.migrations_firebase_data_migration_request_resources import MigrationsFirebaseDataMigrationRequestResources
from appwrite_console_python_sdk.model.migrations_firebase_o_auth_migrate_request import MigrationsFirebaseOAuthMigrateRequest
from appwrite_console_python_sdk.model.migrations_firebase_o_auth_migrate_request_resources import MigrationsFirebaseOAuthMigrateRequestResources
from appwrite_console_python_sdk.model.migrations_migrate_supabase_data_request import MigrationsMigrateSupabaseDataRequest
from appwrite_console_python_sdk.model.migrations_migrate_supabase_data_request_resources import MigrationsMigrateSupabaseDataRequestResources
from appwrite_console_python_sdk.model.phone import Phone
from appwrite_console_python_sdk.model.phone_list import PhoneList
from appwrite_console_python_sdk.model.platform import Platform
from appwrite_console_python_sdk.model.platform_list import PlatformList
from appwrite_console_python_sdk.model.preferences import Preferences
from appwrite_console_python_sdk.model.project import Project
from appwrite_console_python_sdk.model.project_create_variable_request import ProjectCreateVariableRequest
from appwrite_console_python_sdk.model.project_list import ProjectList
from appwrite_console_python_sdk.model.project_update_variable_by_id_request import ProjectUpdateVariableByIdRequest
from appwrite_console_python_sdk.model.projects_create_key_request import ProjectsCreateKeyRequest
from appwrite_console_python_sdk.model.projects_create_key_request_scopes import ProjectsCreateKeyRequestScopes
from appwrite_console_python_sdk.model.projects_create_new_project_request import ProjectsCreateNewProjectRequest
from appwrite_console_python_sdk.model.projects_create_platform_request import ProjectsCreatePlatformRequest
from appwrite_console_python_sdk.model.projects_create_smtp_test_request import ProjectsCreateSmtpTestRequest
from appwrite_console_python_sdk.model.projects_create_smtp_test_request_emails import ProjectsCreateSmtpTestRequestEmails
from appwrite_console_python_sdk.model.projects_create_webhook_request import ProjectsCreateWebhookRequest
from appwrite_console_python_sdk.model.projects_create_webhook_request_events import ProjectsCreateWebhookRequestEvents
from appwrite_console_python_sdk.model.projects_enable_personal_data_check_request import ProjectsEnablePersonalDataCheckRequest
from appwrite_console_python_sdk.model.projects_update_all_api_status_request import ProjectsUpdateAllApiStatusRequest
from appwrite_console_python_sdk.model.projects_update_all_service_status_request import ProjectsUpdateAllServiceStatusRequest
from appwrite_console_python_sdk.model.projects_update_api_status_request import ProjectsUpdateApiStatusRequest
from appwrite_console_python_sdk.model.projects_update_auth_duration_request import ProjectsUpdateAuthDurationRequest
from appwrite_console_python_sdk.model.projects_update_auth_method_status_request import ProjectsUpdateAuthMethodStatusRequest
from appwrite_console_python_sdk.model.projects_update_auth_password_dictionary_request import ProjectsUpdateAuthPasswordDictionaryRequest
from appwrite_console_python_sdk.model.projects_update_auth_password_history_request import ProjectsUpdateAuthPasswordHistoryRequest
from appwrite_console_python_sdk.model.projects_update_custom_email_templates_request import ProjectsUpdateCustomEmailTemplatesRequest
from appwrite_console_python_sdk.model.projects_update_detail_request import ProjectsUpdateDetailRequest
from appwrite_console_python_sdk.model.projects_update_key_request import ProjectsUpdateKeyRequest
from appwrite_console_python_sdk.model.projects_update_key_request_scopes import ProjectsUpdateKeyRequestScopes
from appwrite_console_python_sdk.model.projects_update_max_sessions_limit_request import ProjectsUpdateMaxSessionsLimitRequest
from appwrite_console_python_sdk.model.projects_update_o_auth_request import ProjectsUpdateOAuthRequest
from appwrite_console_python_sdk.model.projects_update_platform_by_id_request import ProjectsUpdatePlatformByIdRequest
from appwrite_console_python_sdk.model.projects_update_service_status_request import ProjectsUpdateServiceStatusRequest
from appwrite_console_python_sdk.model.projects_update_sms_template_request import ProjectsUpdateSmsTemplateRequest
from appwrite_console_python_sdk.model.projects_update_smtp_request import ProjectsUpdateSmtpRequest
from appwrite_console_python_sdk.model.projects_update_team_request import ProjectsUpdateTeamRequest
from appwrite_console_python_sdk.model.projects_update_user_limit_request import ProjectsUpdateUserLimitRequest
from appwrite_console_python_sdk.model.projects_update_webhook_request import ProjectsUpdateWebhookRequest
from appwrite_console_python_sdk.model.projects_update_webhook_request_events import ProjectsUpdateWebhookRequestEvents
from appwrite_console_python_sdk.model.provider import Provider
from appwrite_console_python_sdk.model.provider_list import ProviderList
from appwrite_console_python_sdk.model.provider_repository import ProviderRepository
from appwrite_console_python_sdk.model.provider_repository_list import ProviderRepositoryList
from appwrite_console_python_sdk.model.proxy_create_new_rule_request import ProxyCreateNewRuleRequest
from appwrite_console_python_sdk.model.proxy_rule import ProxyRule
from appwrite_console_python_sdk.model.proxy_rule_list import ProxyRuleList
from appwrite_console_python_sdk.model.runtime import Runtime
from appwrite_console_python_sdk.model.runtime_list import RuntimeList
from appwrite_console_python_sdk.model.runtime_supports import RuntimeSupports
from appwrite_console_python_sdk.model.session import Session
from appwrite_console_python_sdk.model.session_factors import SessionFactors
from appwrite_console_python_sdk.model.session_list import SessionList
from appwrite_console_python_sdk.model.sms_template import SmsTemplate
from appwrite_console_python_sdk.model.storage_create_bucket_request import StorageCreateBucketRequest
from appwrite_console_python_sdk.model.storage_create_bucket_request_allowed_file_extensions import StorageCreateBucketRequestAllowedFileExtensions
from appwrite_console_python_sdk.model.storage_create_bucket_request_permissions import StorageCreateBucketRequestPermissions
from appwrite_console_python_sdk.model.storage_create_file_request import StorageCreateFileRequest
from appwrite_console_python_sdk.model.storage_create_file_request_permissions import StorageCreateFileRequestPermissions
from appwrite_console_python_sdk.model.storage_update_bucket_by_id_request import StorageUpdateBucketByIdRequest
from appwrite_console_python_sdk.model.storage_update_bucket_by_id_request_allowed_file_extensions import StorageUpdateBucketByIdRequestAllowedFileExtensions
from appwrite_console_python_sdk.model.storage_update_bucket_by_id_request_permissions import StorageUpdateBucketByIdRequestPermissions
from appwrite_console_python_sdk.model.storage_update_file_by_id_request import StorageUpdateFileByIdRequest
from appwrite_console_python_sdk.model.storage_update_file_by_id_request_permissions import StorageUpdateFileByIdRequestPermissions
from appwrite_console_python_sdk.model.subscriber import Subscriber
from appwrite_console_python_sdk.model.subscriber_list import SubscriberList
from appwrite_console_python_sdk.model.subscriber_target import SubscriberTarget
from appwrite_console_python_sdk.model.target import Target
from appwrite_console_python_sdk.model.target_list import TargetList
from appwrite_console_python_sdk.model.team import Team
from appwrite_console_python_sdk.model.team_list import TeamList
from appwrite_console_python_sdk.model.team_prefs import TeamPrefs
from appwrite_console_python_sdk.model.teams_create_membership_request import TeamsCreateMembershipRequest
from appwrite_console_python_sdk.model.teams_create_membership_request_roles import TeamsCreateMembershipRequestRoles
from appwrite_console_python_sdk.model.teams_create_team_request import TeamsCreateTeamRequest
from appwrite_console_python_sdk.model.teams_create_team_request_roles import TeamsCreateTeamRequestRoles
from appwrite_console_python_sdk.model.teams_update_membership_roles_request import TeamsUpdateMembershipRolesRequest
from appwrite_console_python_sdk.model.teams_update_membership_roles_request_roles import TeamsUpdateMembershipRolesRequestRoles
from appwrite_console_python_sdk.model.teams_update_membership_status_request import TeamsUpdateMembershipStatusRequest
from appwrite_console_python_sdk.model.teams_update_name_by_id_request import TeamsUpdateNameByIdRequest
from appwrite_console_python_sdk.model.teams_update_prefs_by_id_request import TeamsUpdatePrefsByIdRequest
from appwrite_console_python_sdk.model.token import Token
from appwrite_console_python_sdk.model.topic import Topic
from appwrite_console_python_sdk.model.topic_list import TopicList
from appwrite_console_python_sdk.model.topic_subscribe import TopicSubscribe
from appwrite_console_python_sdk.model.usage_buckets import UsageBuckets
from appwrite_console_python_sdk.model.usage_collection import UsageCollection
from appwrite_console_python_sdk.model.usage_database import UsageDatabase
from appwrite_console_python_sdk.model.usage_databases import UsageDatabases
from appwrite_console_python_sdk.model.usage_function import UsageFunction
from appwrite_console_python_sdk.model.usage_functions import UsageFunctions
from appwrite_console_python_sdk.model.usage_project import UsageProject
from appwrite_console_python_sdk.model.usage_storage import UsageStorage
from appwrite_console_python_sdk.model.usage_users import UsageUsers
from appwrite_console_python_sdk.model.user import User
from appwrite_console_python_sdk.model.user_hash_options import UserHashOptions
from appwrite_console_python_sdk.model.user_labels import UserLabels
from appwrite_console_python_sdk.model.user_list import UserList
from appwrite_console_python_sdk.model.user_prefs import UserPrefs
from appwrite_console_python_sdk.model.users_create_argon_user_request import UsersCreateArgonUserRequest
from appwrite_console_python_sdk.model.users_create_bcrypt_password_request import UsersCreateBcryptPasswordRequest
from appwrite_console_python_sdk.model.users_create_md5_user_request import UsersCreateMd5UserRequest
from appwrite_console_python_sdk.model.users_create_messaging_target_request import UsersCreateMessagingTargetRequest
from appwrite_console_python_sdk.model.users_create_new_user_request import UsersCreateNewUserRequest
from appwrite_console_python_sdk.model.users_create_scrypt_modified_user_request import UsersCreateScryptModifiedUserRequest
from appwrite_console_python_sdk.model.users_create_scrypt_user_request import UsersCreateScryptUserRequest
from appwrite_console_python_sdk.model.users_create_with_ph_pass_request import UsersCreateWithPhPassRequest
from appwrite_console_python_sdk.model.users_create_with_sha_password_request import UsersCreateWithShaPasswordRequest
from appwrite_console_python_sdk.model.users_generate_token_request import UsersGenerateTokenRequest
from appwrite_console_python_sdk.model.users_update_email_by_id_request import UsersUpdateEmailByIdRequest
from appwrite_console_python_sdk.model.users_update_email_verification_status_request import UsersUpdateEmailVerificationStatusRequest
from appwrite_console_python_sdk.model.users_update_labels_by_user_id_request import UsersUpdateLabelsByUserIdRequest
from appwrite_console_python_sdk.model.users_update_labels_by_user_id_request_labels import UsersUpdateLabelsByUserIdRequestLabels
from appwrite_console_python_sdk.model.users_update_messaging_target_request import UsersUpdateMessagingTargetRequest
from appwrite_console_python_sdk.model.users_update_mfa_status_request import UsersUpdateMfaStatusRequest
from appwrite_console_python_sdk.model.users_update_name_by_id_request import UsersUpdateNameByIdRequest
from appwrite_console_python_sdk.model.users_update_password_by_user_id_request import UsersUpdatePasswordByUserIdRequest
from appwrite_console_python_sdk.model.users_update_phone_by_user_id_request import UsersUpdatePhoneByUserIdRequest
from appwrite_console_python_sdk.model.users_update_phone_verification_request import UsersUpdatePhoneVerificationRequest
from appwrite_console_python_sdk.model.users_update_prefs_by_id_request import UsersUpdatePrefsByIdRequest
from appwrite_console_python_sdk.model.users_update_status_by_user_id_request import UsersUpdateStatusByUserIdRequest
from appwrite_console_python_sdk.model.variable import Variable
from appwrite_console_python_sdk.model.variable_list import VariableList
from appwrite_console_python_sdk.model.vcs_authorize_external_deployment_request import VcsAuthorizeExternalDeploymentRequest
from appwrite_console_python_sdk.model.vcs_create_provider_repository_request import VcsCreateProviderRepositoryRequest
from appwrite_console_python_sdk.model.vcs_detect_runtime_settings_request import VcsDetectRuntimeSettingsRequest
from appwrite_console_python_sdk.model.webhook import Webhook
from appwrite_console_python_sdk.model.webhook_events import WebhookEvents
from appwrite_console_python_sdk.model.webhook_list import WebhookList
