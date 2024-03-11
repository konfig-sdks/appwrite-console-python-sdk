# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_repositories_repository_id.patch import AuthorizeExternalDeploymentRaw
from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_provider_repositories.post import CreateProviderRepositoryRaw
from appwrite_console_python_sdk.paths.vcs_installations_installation_id.delete import DeleteInstallationRaw
from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_provider_repositories_provider_repository_id_detection.post import DetectRuntimeSettingsRaw
from appwrite_console_python_sdk.paths.vcs_installations_installation_id.get import GetInstallationByIdRaw
from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_provider_repositories_provider_repository_id.get import GetRepositoryRaw
from appwrite_console_python_sdk.paths.vcs_installations.get import ListInstallationsRaw
from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_provider_repositories.get import ListProviderRepositoriesRaw
from appwrite_console_python_sdk.paths.vcs_github_installations_installation_id_provider_repositories_provider_repository_id_branches.get import ListRepositoryBranchesRaw


class VcsApiRaw(
    AuthorizeExternalDeploymentRaw,
    CreateProviderRepositoryRaw,
    DeleteInstallationRaw,
    DetectRuntimeSettingsRaw,
    GetInstallationByIdRaw,
    GetRepositoryRaw,
    ListInstallationsRaw,
    ListProviderRepositoriesRaw,
    ListRepositoryBranchesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
