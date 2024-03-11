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


class Deployment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Deployment
    """


    class MetaOapg:
        required = {
            "providerRepositoryName",
            "providerCommitUrl",
            "resourceId",
            "buildTime",
            "buildLogs",
            "providerBranchUrl",
            "$createdAt",
            "buildId",
            "type",
            "providerBranch",
            "$updatedAt",
            "providerRepositoryOwner",
            "providerCommitMessage",
            "providerRepositoryUrl",
            "size",
            "entrypoint",
            "activate",
            "providerCommitAuthor",
            "providerCommitHash",
            "providerCommitAuthorUrl",
            "$id",
            "resourceType",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            type = schemas.StrSchema
            resourceId = schemas.StrSchema
            resourceType = schemas.StrSchema
            entrypoint = schemas.StrSchema
            size = schemas.Int32Schema
            buildId = schemas.StrSchema
            activate = schemas.BoolSchema
            status = schemas.StrSchema
            buildLogs = schemas.StrSchema
            buildTime = schemas.Int32Schema
            providerRepositoryName = schemas.StrSchema
            providerRepositoryOwner = schemas.StrSchema
            providerRepositoryUrl = schemas.StrSchema
            providerBranch = schemas.StrSchema
            providerCommitHash = schemas.StrSchema
            providerCommitAuthorUrl = schemas.StrSchema
            providerCommitAuthor = schemas.StrSchema
            providerCommitMessage = schemas.StrSchema
            providerCommitUrl = schemas.StrSchema
            providerBranchUrl = schemas.StrSchema
            __annotations__ = {
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "type": type,
                "resourceId": resourceId,
                "resourceType": resourceType,
                "entrypoint": entrypoint,
                "size": size,
                "buildId": buildId,
                "activate": activate,
                "status": status,
                "buildLogs": buildLogs,
                "buildTime": buildTime,
                "providerRepositoryName": providerRepositoryName,
                "providerRepositoryOwner": providerRepositoryOwner,
                "providerRepositoryUrl": providerRepositoryUrl,
                "providerBranch": providerBranch,
                "providerCommitHash": providerCommitHash,
                "providerCommitAuthorUrl": providerCommitAuthorUrl,
                "providerCommitAuthor": providerCommitAuthor,
                "providerCommitMessage": providerCommitMessage,
                "providerCommitUrl": providerCommitUrl,
                "providerBranchUrl": providerBranchUrl,
            }
    
    providerRepositoryName: MetaOapg.properties.providerRepositoryName
    providerCommitUrl: MetaOapg.properties.providerCommitUrl
    resourceId: MetaOapg.properties.resourceId
    buildTime: MetaOapg.properties.buildTime
    buildLogs: MetaOapg.properties.buildLogs
    providerBranchUrl: MetaOapg.properties.providerBranchUrl
    buildId: MetaOapg.properties.buildId
    type: MetaOapg.properties.type
    providerBranch: MetaOapg.properties.providerBranch
    providerRepositoryOwner: MetaOapg.properties.providerRepositoryOwner
    providerCommitMessage: MetaOapg.properties.providerCommitMessage
    providerRepositoryUrl: MetaOapg.properties.providerRepositoryUrl
    size: MetaOapg.properties.size
    entrypoint: MetaOapg.properties.entrypoint
    activate: MetaOapg.properties.activate
    providerCommitAuthor: MetaOapg.properties.providerCommitAuthor
    providerCommitHash: MetaOapg.properties.providerCommitHash
    providerCommitAuthorUrl: MetaOapg.properties.providerCommitAuthorUrl
    resourceType: MetaOapg.properties.resourceType
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entrypoint"]) -> MetaOapg.properties.entrypoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildId"]) -> MetaOapg.properties.buildId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activate"]) -> MetaOapg.properties.activate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildLogs"]) -> MetaOapg.properties.buildLogs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildTime"]) -> MetaOapg.properties.buildTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRepositoryName"]) -> MetaOapg.properties.providerRepositoryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRepositoryOwner"]) -> MetaOapg.properties.providerRepositoryOwner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRepositoryUrl"]) -> MetaOapg.properties.providerRepositoryUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerBranch"]) -> MetaOapg.properties.providerBranch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerCommitHash"]) -> MetaOapg.properties.providerCommitHash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerCommitAuthorUrl"]) -> MetaOapg.properties.providerCommitAuthorUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerCommitAuthor"]) -> MetaOapg.properties.providerCommitAuthor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerCommitMessage"]) -> MetaOapg.properties.providerCommitMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerCommitUrl"]) -> MetaOapg.properties.providerCommitUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerBranchUrl"]) -> MetaOapg.properties.providerBranchUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "type", "resourceId", "resourceType", "entrypoint", "size", "buildId", "activate", "status", "buildLogs", "buildTime", "providerRepositoryName", "providerRepositoryOwner", "providerRepositoryUrl", "providerBranch", "providerCommitHash", "providerCommitAuthorUrl", "providerCommitAuthor", "providerCommitMessage", "providerCommitUrl", "providerBranchUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceId"]) -> MetaOapg.properties.resourceId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceType"]) -> MetaOapg.properties.resourceType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entrypoint"]) -> MetaOapg.properties.entrypoint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildId"]) -> MetaOapg.properties.buildId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activate"]) -> MetaOapg.properties.activate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildLogs"]) -> MetaOapg.properties.buildLogs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildTime"]) -> MetaOapg.properties.buildTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRepositoryName"]) -> MetaOapg.properties.providerRepositoryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRepositoryOwner"]) -> MetaOapg.properties.providerRepositoryOwner: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRepositoryUrl"]) -> MetaOapg.properties.providerRepositoryUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerBranch"]) -> MetaOapg.properties.providerBranch: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerCommitHash"]) -> MetaOapg.properties.providerCommitHash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerCommitAuthorUrl"]) -> MetaOapg.properties.providerCommitAuthorUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerCommitAuthor"]) -> MetaOapg.properties.providerCommitAuthor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerCommitMessage"]) -> MetaOapg.properties.providerCommitMessage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerCommitUrl"]) -> MetaOapg.properties.providerCommitUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerBranchUrl"]) -> MetaOapg.properties.providerBranchUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$id", "$createdAt", "$updatedAt", "type", "resourceId", "resourceType", "entrypoint", "size", "buildId", "activate", "status", "buildLogs", "buildTime", "providerRepositoryName", "providerRepositoryOwner", "providerRepositoryUrl", "providerBranch", "providerCommitHash", "providerCommitAuthorUrl", "providerCommitAuthor", "providerCommitMessage", "providerCommitUrl", "providerBranchUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        providerRepositoryName: typing.Union[MetaOapg.properties.providerRepositoryName, str, ],
        providerCommitUrl: typing.Union[MetaOapg.properties.providerCommitUrl, str, ],
        resourceId: typing.Union[MetaOapg.properties.resourceId, str, ],
        buildTime: typing.Union[MetaOapg.properties.buildTime, decimal.Decimal, int, ],
        buildLogs: typing.Union[MetaOapg.properties.buildLogs, str, ],
        providerBranchUrl: typing.Union[MetaOapg.properties.providerBranchUrl, str, ],
        buildId: typing.Union[MetaOapg.properties.buildId, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        providerBranch: typing.Union[MetaOapg.properties.providerBranch, str, ],
        providerRepositoryOwner: typing.Union[MetaOapg.properties.providerRepositoryOwner, str, ],
        providerCommitMessage: typing.Union[MetaOapg.properties.providerCommitMessage, str, ],
        providerRepositoryUrl: typing.Union[MetaOapg.properties.providerRepositoryUrl, str, ],
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, ],
        entrypoint: typing.Union[MetaOapg.properties.entrypoint, str, ],
        activate: typing.Union[MetaOapg.properties.activate, bool, ],
        providerCommitAuthor: typing.Union[MetaOapg.properties.providerCommitAuthor, str, ],
        providerCommitHash: typing.Union[MetaOapg.properties.providerCommitHash, str, ],
        providerCommitAuthorUrl: typing.Union[MetaOapg.properties.providerCommitAuthorUrl, str, ],
        resourceType: typing.Union[MetaOapg.properties.resourceType, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Deployment':
        return super().__new__(
            cls,
            *args,
            providerRepositoryName=providerRepositoryName,
            providerCommitUrl=providerCommitUrl,
            resourceId=resourceId,
            buildTime=buildTime,
            buildLogs=buildLogs,
            providerBranchUrl=providerBranchUrl,
            buildId=buildId,
            type=type,
            providerBranch=providerBranch,
            providerRepositoryOwner=providerRepositoryOwner,
            providerCommitMessage=providerCommitMessage,
            providerRepositoryUrl=providerRepositoryUrl,
            size=size,
            entrypoint=entrypoint,
            activate=activate,
            providerCommitAuthor=providerCommitAuthor,
            providerCommitHash=providerCommitHash,
            providerCommitAuthorUrl=providerCommitAuthorUrl,
            resourceType=resourceType,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
