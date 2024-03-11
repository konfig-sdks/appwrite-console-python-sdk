# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from appwrite_console_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT = "account"
    DATABASES = "databases"
    MESSAGING = "messaging"
    PROJECTS = "projects"
    USERS = "users"
    HEALTH = "health"
    FUNCTIONS = "functions"
    MIGRATIONS = "migrations"
    STORAGE = "storage"
    TEAMS = "teams"
    VCS = "vcs"
    LOCALE = "locale"
    AVATARS = "avatars"
    PROJECT = "project"
    PROXY = "proxy"
    GRAPHQL = "graphql"
    CONSOLE = "console"
    ASSISTANT = "assistant"
