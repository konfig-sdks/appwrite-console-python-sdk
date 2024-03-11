# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from appwrite_console_python_sdk import schemas  # noqa: F401


class ProjectsCreateNewProjectRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "teamId",
            "name",
            "projectId",
        }
        
        class properties:
            projectId = schemas.StrSchema
            name = schemas.StrSchema
            teamId = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class region(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
                
                @schemas.classproperty
                def FRA(cls):
                    return cls("fra")
            logo = schemas.StrSchema
            url = schemas.StrSchema
            legalName = schemas.StrSchema
            legalCountry = schemas.StrSchema
            legalState = schemas.StrSchema
            legalCity = schemas.StrSchema
            legalAddress = schemas.StrSchema
            legalTaxId = schemas.StrSchema
            __annotations__ = {
                "projectId": projectId,
                "name": name,
                "teamId": teamId,
                "description": description,
                "region": region,
                "logo": logo,
                "url": url,
                "legalName": legalName,
                "legalCountry": legalCountry,
                "legalState": legalState,
                "legalCity": legalCity,
                "legalAddress": legalAddress,
                "legalTaxId": legalTaxId,
            }
    
    teamId: MetaOapg.properties.teamId
    name: MetaOapg.properties.name
    projectId: MetaOapg.properties.projectId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalCountry"]) -> MetaOapg.properties.legalCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalState"]) -> MetaOapg.properties.legalState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalCity"]) -> MetaOapg.properties.legalCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalAddress"]) -> MetaOapg.properties.legalAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalTaxId"]) -> MetaOapg.properties.legalTaxId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["projectId", "name", "teamId", "description", "region", "logo", "url", "legalName", "legalCountry", "legalState", "legalCity", "legalAddress", "legalTaxId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> typing.Union[MetaOapg.properties.legalName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalCountry"]) -> typing.Union[MetaOapg.properties.legalCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalState"]) -> typing.Union[MetaOapg.properties.legalState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalCity"]) -> typing.Union[MetaOapg.properties.legalCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalAddress"]) -> typing.Union[MetaOapg.properties.legalAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalTaxId"]) -> typing.Union[MetaOapg.properties.legalTaxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["projectId", "name", "teamId", "description", "region", "logo", "url", "legalName", "legalCountry", "legalState", "legalCity", "legalAddress", "legalTaxId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        teamId: typing.Union[MetaOapg.properties.teamId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        projectId: typing.Union[MetaOapg.properties.projectId, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        legalName: typing.Union[MetaOapg.properties.legalName, str, schemas.Unset] = schemas.unset,
        legalCountry: typing.Union[MetaOapg.properties.legalCountry, str, schemas.Unset] = schemas.unset,
        legalState: typing.Union[MetaOapg.properties.legalState, str, schemas.Unset] = schemas.unset,
        legalCity: typing.Union[MetaOapg.properties.legalCity, str, schemas.Unset] = schemas.unset,
        legalAddress: typing.Union[MetaOapg.properties.legalAddress, str, schemas.Unset] = schemas.unset,
        legalTaxId: typing.Union[MetaOapg.properties.legalTaxId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsCreateNewProjectRequest':
        return super().__new__(
            cls,
            *args,
            teamId=teamId,
            name=name,
            projectId=projectId,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legalName=legalName,
            legalCountry=legalCountry,
            legalState=legalState,
            legalCity=legalCity,
            legalAddress=legalAddress,
            legalTaxId=legalTaxId,
            _configuration=_configuration,
            **kwargs,
        )