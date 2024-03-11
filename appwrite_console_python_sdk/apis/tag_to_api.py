import typing_extensions

from appwrite_console_python_sdk.apis.tags import TagValues
from appwrite_console_python_sdk.apis.tags.account_api import AccountApi
from appwrite_console_python_sdk.apis.tags.databases_api import DatabasesApi
from appwrite_console_python_sdk.apis.tags.messaging_api import MessagingApi
from appwrite_console_python_sdk.apis.tags.projects_api import ProjectsApi
from appwrite_console_python_sdk.apis.tags.users_api import UsersApi
from appwrite_console_python_sdk.apis.tags.health_api import HealthApi
from appwrite_console_python_sdk.apis.tags.functions_api import FunctionsApi
from appwrite_console_python_sdk.apis.tags.migrations_api import MigrationsApi
from appwrite_console_python_sdk.apis.tags.storage_api import StorageApi
from appwrite_console_python_sdk.apis.tags.teams_api import TeamsApi
from appwrite_console_python_sdk.apis.tags.vcs_api import VcsApi
from appwrite_console_python_sdk.apis.tags.locale_api import LocaleApi
from appwrite_console_python_sdk.apis.tags.avatars_api import AvatarsApi
from appwrite_console_python_sdk.apis.tags.project_api import ProjectApi
from appwrite_console_python_sdk.apis.tags.proxy_api import ProxyApi
from appwrite_console_python_sdk.apis.tags.graphql_api import GraphqlApi
from appwrite_console_python_sdk.apis.tags.console_api import ConsoleApi
from appwrite_console_python_sdk.apis.tags.assistant_api import AssistantApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.DATABASES: DatabasesApi,
        TagValues.MESSAGING: MessagingApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.USERS: UsersApi,
        TagValues.HEALTH: HealthApi,
        TagValues.FUNCTIONS: FunctionsApi,
        TagValues.MIGRATIONS: MigrationsApi,
        TagValues.STORAGE: StorageApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.VCS: VcsApi,
        TagValues.LOCALE: LocaleApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROXY: ProxyApi,
        TagValues.GRAPHQL: GraphqlApi,
        TagValues.CONSOLE: ConsoleApi,
        TagValues.ASSISTANT: AssistantApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.DATABASES: DatabasesApi,
        TagValues.MESSAGING: MessagingApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.USERS: UsersApi,
        TagValues.HEALTH: HealthApi,
        TagValues.FUNCTIONS: FunctionsApi,
        TagValues.MIGRATIONS: MigrationsApi,
        TagValues.STORAGE: StorageApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.VCS: VcsApi,
        TagValues.LOCALE: LocaleApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROXY: ProxyApi,
        TagValues.GRAPHQL: GraphqlApi,
        TagValues.CONSOLE: ConsoleApi,
        TagValues.ASSISTANT: AssistantApi,
    }
)
