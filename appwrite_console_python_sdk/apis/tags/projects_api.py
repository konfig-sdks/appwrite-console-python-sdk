# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.projects_project_id_keys.post import CreateKey
from appwrite_console_python_sdk.paths.projects.post import CreateNewProject
from appwrite_console_python_sdk.paths.projects_project_id_platforms.post import CreatePlatform
from appwrite_console_python_sdk.paths.projects_project_id_smtp_tests.post import CreateSmtpTest
from appwrite_console_python_sdk.paths.projects_project_id_webhooks.post import CreateWebhook
from appwrite_console_python_sdk.paths.projects_project_id_keys_key_id.delete import DeleteKey
from appwrite_console_python_sdk.paths.projects_project_id_platforms_platform_id.delete import DeletePlatform
from appwrite_console_python_sdk.paths.projects_project_id_webhooks_webhook_id.delete import DeleteWebhook
from appwrite_console_python_sdk.paths.projects_project_id_auth_personal_data.patch import EnablePersonalDataCheck
from appwrite_console_python_sdk.paths.projects_project_id.get import Get
from appwrite_console_python_sdk.paths.projects_project_id_templates_email_type_locale.get import GetEmailTemplate
from appwrite_console_python_sdk.paths.projects_project_id_keys_key_id.get import GetKey
from appwrite_console_python_sdk.paths.projects_project_id_platforms_platform_id.get import GetPlatformById
from appwrite_console_python_sdk.paths.projects_project_id_templates_sms_type_locale.get import GetSmsTemplate
from appwrite_console_python_sdk.paths.projects_project_id_webhooks_webhook_id.get import GetWebhook
from appwrite_console_python_sdk.paths.projects_project_id_keys.get import ListKeys
from appwrite_console_python_sdk.paths.projects_project_id_platforms.get import ListPlatforms
from appwrite_console_python_sdk.paths.projects.get import ListProjects
from appwrite_console_python_sdk.paths.projects_project_id_webhooks.get import ListWebhooks
from appwrite_console_python_sdk.paths.projects_project_id.delete import RemoveById
from appwrite_console_python_sdk.paths.projects_project_id_templates_email_type_locale.delete import ResetEmailTemplate
from appwrite_console_python_sdk.paths.projects_project_id_templates_sms_type_locale.delete import ResetSmsTemplate
from appwrite_console_python_sdk.paths.projects_project_id_api_all.patch import UpdateAllApiStatus
from appwrite_console_python_sdk.paths.projects_project_id_service_all.patch import UpdateAllServiceStatus
from appwrite_console_python_sdk.paths.projects_project_id_api.patch import UpdateApiStatus
from appwrite_console_python_sdk.paths.projects_project_id_auth_duration.patch import UpdateAuthDuration
from appwrite_console_python_sdk.paths.projects_project_id_auth_method.patch import UpdateAuthMethodStatus
from appwrite_console_python_sdk.paths.projects_project_id_auth_password_dictionary.patch import UpdateAuthPasswordDictionary
from appwrite_console_python_sdk.paths.projects_project_id_auth_password_history.patch import UpdateAuthPasswordHistory
from appwrite_console_python_sdk.paths.projects_project_id_templates_email_type_locale.patch import UpdateCustomEmailTemplates
from appwrite_console_python_sdk.paths.projects_project_id.patch import UpdateDetail
from appwrite_console_python_sdk.paths.projects_project_id_keys_key_id.put import UpdateKey
from appwrite_console_python_sdk.paths.projects_project_id_auth_max_sessions.patch import UpdateMaxSessionsLimit
from appwrite_console_python_sdk.paths.projects_project_id_oauth2.patch import UpdateOAuth
from appwrite_console_python_sdk.paths.projects_project_id_platforms_platform_id.put import UpdatePlatformById
from appwrite_console_python_sdk.paths.projects_project_id_service.patch import UpdateServiceStatus
from appwrite_console_python_sdk.paths.projects_project_id_templates_sms_type_locale.patch import UpdateSmsTemplate
from appwrite_console_python_sdk.paths.projects_project_id_smtp.patch import UpdateSmtp
from appwrite_console_python_sdk.paths.projects_project_id_team.patch import UpdateTeam
from appwrite_console_python_sdk.paths.projects_project_id_auth_limit.patch import UpdateUserLimit
from appwrite_console_python_sdk.paths.projects_project_id_webhooks_webhook_id.put import UpdateWebhook
from appwrite_console_python_sdk.paths.projects_project_id_webhooks_webhook_id_signature.patch import UpdateWebhookSignature
from appwrite_console_python_sdk.apis.tags.projects_api_raw import ProjectsApiRaw


class ProjectsApi(
    CreateKey,
    CreateNewProject,
    CreatePlatform,
    CreateSmtpTest,
    CreateWebhook,
    DeleteKey,
    DeletePlatform,
    DeleteWebhook,
    EnablePersonalDataCheck,
    Get,
    GetEmailTemplate,
    GetKey,
    GetPlatformById,
    GetSmsTemplate,
    GetWebhook,
    ListKeys,
    ListPlatforms,
    ListProjects,
    ListWebhooks,
    RemoveById,
    ResetEmailTemplate,
    ResetSmsTemplate,
    UpdateAllApiStatus,
    UpdateAllServiceStatus,
    UpdateApiStatus,
    UpdateAuthDuration,
    UpdateAuthMethodStatus,
    UpdateAuthPasswordDictionary,
    UpdateAuthPasswordHistory,
    UpdateCustomEmailTemplates,
    UpdateDetail,
    UpdateKey,
    UpdateMaxSessionsLimit,
    UpdateOAuth,
    UpdatePlatformById,
    UpdateServiceStatus,
    UpdateSmsTemplate,
    UpdateSmtp,
    UpdateTeam,
    UpdateUserLimit,
    UpdateWebhook,
    UpdateWebhookSignature,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectsApiRaw(api_client)
