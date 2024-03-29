# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.proxy_rules.post import CreateNewRuleRaw
from appwrite_console_python_sdk.paths.proxy_rules_rule_id.delete import DeleteRuleByIdRaw
from appwrite_console_python_sdk.paths.proxy_rules_rule_id.get import GetRuleByIdRaw
from appwrite_console_python_sdk.paths.proxy_rules.get import ListRulesRaw
from appwrite_console_python_sdk.paths.proxy_rules_rule_id_verification.patch import UpdateRuleVerificationStatusRaw


class ProxyApiRaw(
    CreateNewRuleRaw,
    DeleteRuleByIdRaw,
    GetRuleByIdRaw,
    ListRulesRaw,
    UpdateRuleVerificationStatusRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
