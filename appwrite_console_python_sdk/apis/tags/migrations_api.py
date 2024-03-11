# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.migrations_appwrite.post import CreateAppwriteMigration
from appwrite_console_python_sdk.paths.migrations_nhost.post import CreateNHostMigration
from appwrite_console_python_sdk.paths.migrations_migration_id.delete import DeleteMigration
from appwrite_console_python_sdk.paths.migrations_firebase.post import FirebaseDataMigration
from appwrite_console_python_sdk.paths.migrations_firebase_oauth.post import FirebaseOAuthMigrate
from appwrite_console_python_sdk.paths.migrations_firebase_report.get import GenerateFirebaseReport
from appwrite_console_python_sdk.paths.migrations_firebase_report_oauth.get import GenerateFirebaseReportOAuth
from appwrite_console_python_sdk.paths.migrations_nhost_report.get import GenerateNhostReport
from appwrite_console_python_sdk.paths.migrations_appwrite_report.get import GenerateReportOnAppwriteData
from appwrite_console_python_sdk.paths.migrations_supabase_report.get import GenerateSupabaseReport
from appwrite_console_python_sdk.paths.migrations_migration_id.get import GetById
from appwrite_console_python_sdk.paths.migrations_firebase_projects.get import ListFirebaseProjects
from appwrite_console_python_sdk.paths.migrations.get import ListMigrations
from appwrite_console_python_sdk.paths.migrations_supabase.post import MigrateSupabaseData
from appwrite_console_python_sdk.paths.migrations_migration_id.patch import RetryMigration
from appwrite_console_python_sdk.paths.migrations_firebase_deauthorize.get import RevokeFirebaseAuthorization
from appwrite_console_python_sdk.apis.tags.migrations_api_raw import MigrationsApiRaw


class MigrationsApi(
    CreateAppwriteMigration,
    CreateNHostMigration,
    DeleteMigration,
    FirebaseDataMigration,
    FirebaseOAuthMigrate,
    GenerateFirebaseReport,
    GenerateFirebaseReportOAuth,
    GenerateNhostReport,
    GenerateReportOnAppwriteData,
    GenerateSupabaseReport,
    GetById,
    ListFirebaseProjects,
    ListMigrations,
    MigrateSupabaseData,
    RetryMigration,
    RevokeFirebaseAuthorization,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MigrationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MigrationsApiRaw(api_client)