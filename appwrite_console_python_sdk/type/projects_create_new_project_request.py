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


class RequiredProjectsCreateNewProjectRequest(TypedDict):
    # Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, and hyphen. Can't start with a special char. Max length is 36 chars.
    projectId: str

    # Project name. Max length: 128 chars.
    name: str

    # Team unique ID.
    teamId: str

class OptionalProjectsCreateNewProjectRequest(TypedDict, total=False):
    # Project description. Max length: 256 chars.
    description: str

    # Project Region.
    region: str

    # Project logo.
    logo: str

    # Project URL.
    url: str

    # Project legal Name. Max length: 256 chars.
    legalName: str

    # Project legal Country. Max length: 256 chars.
    legalCountry: str

    # Project legal State. Max length: 256 chars.
    legalState: str

    # Project legal City. Max length: 256 chars.
    legalCity: str

    # Project legal Address. Max length: 256 chars.
    legalAddress: str

    # Project legal Tax ID. Max length: 256 chars.
    legalTaxId: str

class ProjectsCreateNewProjectRequest(RequiredProjectsCreateNewProjectRequest, OptionalProjectsCreateNewProjectRequest):
    pass
