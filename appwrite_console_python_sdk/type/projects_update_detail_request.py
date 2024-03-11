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


class RequiredProjectsUpdateDetailRequest(TypedDict):
    # Project name. Max length: 128 chars.
    name: str

class OptionalProjectsUpdateDetailRequest(TypedDict, total=False):
    # Project description. Max length: 256 chars.
    description: str

    # Project logo.
    logo: str

    # Project URL.
    url: str

    # Project legal name. Max length: 256 chars.
    legalName: str

    # Project legal country. Max length: 256 chars.
    legalCountry: str

    # Project legal state. Max length: 256 chars.
    legalState: str

    # Project legal city. Max length: 256 chars.
    legalCity: str

    # Project legal address. Max length: 256 chars.
    legalAddress: str

    # Project legal tax ID. Max length: 256 chars.
    legalTaxId: str

class ProjectsUpdateDetailRequest(RequiredProjectsUpdateDetailRequest, OptionalProjectsUpdateDetailRequest):
    pass
