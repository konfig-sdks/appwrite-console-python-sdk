# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.project_variables.post import CreateVariable
from appwrite_console_python_sdk.paths.project_variables_variable_id.delete import DeleteVariableById
from appwrite_console_python_sdk.paths.project_usage.get import GetUsageStats
from appwrite_console_python_sdk.paths.project_variables.get import ListVariables
from appwrite_console_python_sdk.paths.project_variables_variable_id.put import UpdateVariableById
from appwrite_console_python_sdk.paths.project_variables_variable_id.get import VariableDetails
from appwrite_console_python_sdk.apis.tags.project_api_raw import ProjectApiRaw


class ProjectApi(
    CreateVariable,
    DeleteVariableById,
    GetUsageStats,
    ListVariables,
    UpdateVariableById,
    VariableDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectApiRaw(api_client)
