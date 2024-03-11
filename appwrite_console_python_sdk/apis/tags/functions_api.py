# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.functions_function_id_deployments.post import CreateDeployment
from appwrite_console_python_sdk.paths.functions.post import CreateFunction
from appwrite_console_python_sdk.paths.functions_function_id_variables.post import CreateVariable
from appwrite_console_python_sdk.paths.functions_function_id_deployments_deployment_id.delete import DeleteDeployment
from appwrite_console_python_sdk.paths.functions_function_id.delete import DeleteFunctionById
from appwrite_console_python_sdk.paths.functions_function_id_variables_variable_id.delete import DeleteVariableById
from appwrite_console_python_sdk.paths.functions_function_id_deployments_deployment_id_download.get import DownloadDeploymentContents
from appwrite_console_python_sdk.paths.functions_function_id.get import GetById
from appwrite_console_python_sdk.paths.functions_function_id_deployments_deployment_id.get import GetDeploymentById
from appwrite_console_python_sdk.paths.functions_function_id_executions_execution_id.get import GetExecutionLog
from appwrite_console_python_sdk.paths.functions_function_id_usage.get import GetFunctionUsage
from appwrite_console_python_sdk.paths.functions_usage.get import GetUsageStats
from appwrite_console_python_sdk.paths.functions_function_id_variables_variable_id.get import GetVariableById
from appwrite_console_python_sdk.paths.functions.get import ListAll
from appwrite_console_python_sdk.paths.functions_function_id_deployments.get import ListDeployments
from appwrite_console_python_sdk.paths.functions_function_id_executions.get import ListExecutions
from appwrite_console_python_sdk.paths.functions_runtimes.get import ListRuntimes
from appwrite_console_python_sdk.paths.functions_function_id_variables.get import ListVariables
from appwrite_console_python_sdk.paths.functions_function_id_deployments_deployment_id_builds_build_id.post import RetryBuild
from appwrite_console_python_sdk.paths.functions_function_id_executions.post import TriggerExecution
from appwrite_console_python_sdk.paths.functions_function_id.put import UpdateById
from appwrite_console_python_sdk.paths.functions_function_id_deployments_deployment_id.patch import UpdateDeploymentByFunctionAndId
from appwrite_console_python_sdk.paths.functions_function_id_variables_variable_id.put import UpdateVariableById
from appwrite_console_python_sdk.apis.tags.functions_api_raw import FunctionsApiRaw


class FunctionsApi(
    CreateDeployment,
    CreateFunction,
    CreateVariable,
    DeleteDeployment,
    DeleteFunctionById,
    DeleteVariableById,
    DownloadDeploymentContents,
    GetById,
    GetDeploymentById,
    GetExecutionLog,
    GetFunctionUsage,
    GetUsageStats,
    GetVariableById,
    ListAll,
    ListDeployments,
    ListExecutions,
    ListRuntimes,
    ListVariables,
    RetryBuild,
    TriggerExecution,
    UpdateById,
    UpdateDeploymentByFunctionAndId,
    UpdateVariableById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FunctionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FunctionsApiRaw(api_client)
