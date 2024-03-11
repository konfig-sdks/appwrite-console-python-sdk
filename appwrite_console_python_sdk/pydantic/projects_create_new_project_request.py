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
from pydantic import BaseModel, Field, RootModel


class ProjectsCreateNewProjectRequest(BaseModel):
    # Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, and hyphen. Can't start with a special char. Max length is 36 chars.
    project_id: str = Field(alias='projectId')

    # Project name. Max length: 128 chars.
    name: str = Field(alias='name')

    # Team unique ID.
    team_id: str = Field(alias='teamId')

    # Project description. Max length: 256 chars.
    description: typing.Optional[str] = Field(None, alias='description')

    # Project Region.
    region: typing.Optional[Literal["default", "fra"]] = Field(None, alias='region')

    # Project logo.
    logo: typing.Optional[str] = Field(None, alias='logo')

    # Project URL.
    url: typing.Optional[str] = Field(None, alias='url')

    # Project legal Name. Max length: 256 chars.
    legal_name: typing.Optional[str] = Field(None, alias='legalName')

    # Project legal Country. Max length: 256 chars.
    legal_country: typing.Optional[str] = Field(None, alias='legalCountry')

    # Project legal State. Max length: 256 chars.
    legal_state: typing.Optional[str] = Field(None, alias='legalState')

    # Project legal City. Max length: 256 chars.
    legal_city: typing.Optional[str] = Field(None, alias='legalCity')

    # Project legal Address. Max length: 256 chars.
    legal_address: typing.Optional[str] = Field(None, alias='legalAddress')

    # Project legal Tax ID. Max length: 256 chars.
    legal_tax_id: typing.Optional[str] = Field(None, alias='legalTaxId')
    class Config:
        arbitrary_types_allowed = True
