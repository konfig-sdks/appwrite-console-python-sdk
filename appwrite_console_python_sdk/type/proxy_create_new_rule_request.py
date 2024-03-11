# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredProxyCreateNewRuleRequest(TypedDict):
    # Domain name.
    domain: str

    # Action definition for the rule. Possible values are \"api\", \"function\"
    resourceType: str

class OptionalProxyCreateNewRuleRequest(TypedDict, total=False):
    # ID of resource for the action type. If resourceType is \"api\", leave empty. If resourceType is \"function\", provide ID of the function.
    resourceId: str

class ProxyCreateNewRuleRequest(RequiredProxyCreateNewRuleRequest, OptionalProxyCreateNewRuleRequest):
    pass
