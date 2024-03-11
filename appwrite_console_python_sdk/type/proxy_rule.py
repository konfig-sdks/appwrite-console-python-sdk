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


RequiredProxyRule = TypedDict("RequiredProxyRule", {
    # Rule ID.
    "$id": str,

    # Rule creation date in ISO 8601 format.
    "$createdAt": str,

    # Rule update date in ISO 8601 format.
    "$updatedAt": str,

    # Domain name.
    "domain": str,

    # Action definition for the rule. Possible values are \"api\", \"function\", or \"redirect\"
    "resourceType": str,

    # ID of resource for the action type. If resourceType is \"api\" or \"url\", it is empty. If resourceType is \"function\", it is ID of the function.
    "resourceId": str,

    # Domain verification status. Possible values are \"created\", \"verifying\", \"verified\" and \"unverified\"
    "status": str,

    # Certificate generation logs. This will return an empty string if generation did not run, or succeeded.
    "logs": str,

    # Certificate auto-renewal date in ISO 8601 format.
    "renewAt": str,
    })

OptionalProxyRule = TypedDict("OptionalProxyRule", {
    }, total=False)

class ProxyRule(RequiredProxyRule, OptionalProxyRule):
    pass
