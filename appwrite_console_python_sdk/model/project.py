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


class Project(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Project
    """


    class MetaOapg:
        required = {
            "serviceStatusForLocale",
            "authInvites",
            "serviceStatusForTeams",
            "authEmailPassword",
            "legalTaxId",
            "smtpPort",
            "authPersonalDataCheck",
            "authJWT",
            "legalAddress",
            "$updatedAt",
            "platforms",
            "legalName",
            "authEmailOtp",
            "serviceStatusForDatabases",
            "logo",
            "serviceStatusForAvatars",
            "authPhone",
            "authPasswordDictionary",
            "smtpUsername",
            "legalCity",
            "smtpSecure",
            "serviceStatusForMessaging",
            "smtpReplyTo",
            "name",
            "serviceStatusForAccount",
            "legalState",
            "$id",
            "serviceStatusForFunctions",
            "smtpSenderEmail",
            "smtpEnabled",
            "keys",
            "description",
            "authUsersAuthMagicURL",
            "serviceStatusForUsers",
            "authSessionsLimit",
            "oAuthProviders",
            "authDuration",
            "serviceStatusForGraphql",
            "serviceStatusForStorage",
            "smtpPassword",
            "serviceStatusForHealth",
            "legalCountry",
            "$createdAt",
            "smtpSenderName",
            "url",
            "authLimit",
            "smtpHost",
            "webhooks",
            "authAnonymous",
            "teamId",
            "authPasswordHistory",
        }
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            name = schemas.StrSchema
            teamId = schemas.StrSchema
            logo = schemas.StrSchema
            url = schemas.StrSchema
            legalName = schemas.StrSchema
            legalCountry = schemas.StrSchema
            legalState = schemas.StrSchema
            legalCity = schemas.StrSchema
            legalAddress = schemas.StrSchema
            legalTaxId = schemas.StrSchema
            authDuration = schemas.Int32Schema
            authLimit = schemas.Int32Schema
            authSessionsLimit = schemas.Int32Schema
            authPasswordHistory = schemas.Int32Schema
            authPasswordDictionary = schemas.BoolSchema
            authPersonalDataCheck = schemas.BoolSchema
            
            
            class oAuthProviders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AuthProvider']:
                        return AuthProvider
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AuthProvider'], typing.List['AuthProvider']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'oAuthProviders':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AuthProvider':
                    return super().__getitem__(i)
            
            
            class platforms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Platform']:
                        return Platform
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Platform'], typing.List['Platform']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'platforms':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Platform':
                    return super().__getitem__(i)
            
            
            class webhooks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Webhook']:
                        return Webhook
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Webhook'], typing.List['Webhook']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'webhooks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Webhook':
                    return super().__getitem__(i)
            
            
            class keys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Key']:
                        return Key
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Key'], typing.List['Key']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'keys':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Key':
                    return super().__getitem__(i)
            smtpEnabled = schemas.BoolSchema
            smtpSenderName = schemas.StrSchema
            smtpSenderEmail = schemas.StrSchema
            smtpReplyTo = schemas.StrSchema
            smtpHost = schemas.StrSchema
            smtpPort = schemas.Int32Schema
            smtpUsername = schemas.StrSchema
            smtpPassword = schemas.StrSchema
            smtpSecure = schemas.StrSchema
            authEmailPassword = schemas.BoolSchema
            authUsersAuthMagicURL = schemas.BoolSchema
            authEmailOtp = schemas.BoolSchema
            authAnonymous = schemas.BoolSchema
            authInvites = schemas.BoolSchema
            authJWT = schemas.BoolSchema
            authPhone = schemas.BoolSchema
            serviceStatusForAccount = schemas.BoolSchema
            serviceStatusForAvatars = schemas.BoolSchema
            serviceStatusForDatabases = schemas.BoolSchema
            serviceStatusForLocale = schemas.BoolSchema
            serviceStatusForHealth = schemas.BoolSchema
            serviceStatusForStorage = schemas.BoolSchema
            serviceStatusForTeams = schemas.BoolSchema
            serviceStatusForUsers = schemas.BoolSchema
            serviceStatusForFunctions = schemas.BoolSchema
            serviceStatusForGraphql = schemas.BoolSchema
            serviceStatusForMessaging = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "$id": id,
                "$createdAt": created_at,
                "$updatedAt": updated_at,
                "name": name,
                "teamId": teamId,
                "logo": logo,
                "url": url,
                "legalName": legalName,
                "legalCountry": legalCountry,
                "legalState": legalState,
                "legalCity": legalCity,
                "legalAddress": legalAddress,
                "legalTaxId": legalTaxId,
                "authDuration": authDuration,
                "authLimit": authLimit,
                "authSessionsLimit": authSessionsLimit,
                "authPasswordHistory": authPasswordHistory,
                "authPasswordDictionary": authPasswordDictionary,
                "authPersonalDataCheck": authPersonalDataCheck,
                "oAuthProviders": oAuthProviders,
                "platforms": platforms,
                "webhooks": webhooks,
                "keys": keys,
                "smtpEnabled": smtpEnabled,
                "smtpSenderName": smtpSenderName,
                "smtpSenderEmail": smtpSenderEmail,
                "smtpReplyTo": smtpReplyTo,
                "smtpHost": smtpHost,
                "smtpPort": smtpPort,
                "smtpUsername": smtpUsername,
                "smtpPassword": smtpPassword,
                "smtpSecure": smtpSecure,
                "authEmailPassword": authEmailPassword,
                "authUsersAuthMagicURL": authUsersAuthMagicURL,
                "authEmailOtp": authEmailOtp,
                "authAnonymous": authAnonymous,
                "authInvites": authInvites,
                "authJWT": authJWT,
                "authPhone": authPhone,
                "serviceStatusForAccount": serviceStatusForAccount,
                "serviceStatusForAvatars": serviceStatusForAvatars,
                "serviceStatusForDatabases": serviceStatusForDatabases,
                "serviceStatusForLocale": serviceStatusForLocale,
                "serviceStatusForHealth": serviceStatusForHealth,
                "serviceStatusForStorage": serviceStatusForStorage,
                "serviceStatusForTeams": serviceStatusForTeams,
                "serviceStatusForUsers": serviceStatusForUsers,
                "serviceStatusForFunctions": serviceStatusForFunctions,
                "serviceStatusForGraphql": serviceStatusForGraphql,
                "serviceStatusForMessaging": serviceStatusForMessaging,
            }
    
    serviceStatusForLocale: MetaOapg.properties.serviceStatusForLocale
    authInvites: MetaOapg.properties.authInvites
    serviceStatusForTeams: MetaOapg.properties.serviceStatusForTeams
    authEmailPassword: MetaOapg.properties.authEmailPassword
    legalTaxId: MetaOapg.properties.legalTaxId
    smtpPort: MetaOapg.properties.smtpPort
    authPersonalDataCheck: MetaOapg.properties.authPersonalDataCheck
    authJWT: MetaOapg.properties.authJWT
    legalAddress: MetaOapg.properties.legalAddress
    platforms: MetaOapg.properties.platforms
    legalName: MetaOapg.properties.legalName
    authEmailOtp: MetaOapg.properties.authEmailOtp
    serviceStatusForDatabases: MetaOapg.properties.serviceStatusForDatabases
    logo: MetaOapg.properties.logo
    serviceStatusForAvatars: MetaOapg.properties.serviceStatusForAvatars
    authPhone: MetaOapg.properties.authPhone
    authPasswordDictionary: MetaOapg.properties.authPasswordDictionary
    smtpUsername: MetaOapg.properties.smtpUsername
    legalCity: MetaOapg.properties.legalCity
    smtpSecure: MetaOapg.properties.smtpSecure
    serviceStatusForMessaging: MetaOapg.properties.serviceStatusForMessaging
    smtpReplyTo: MetaOapg.properties.smtpReplyTo
    name: MetaOapg.properties.name
    serviceStatusForAccount: MetaOapg.properties.serviceStatusForAccount
    legalState: MetaOapg.properties.legalState
    serviceStatusForFunctions: MetaOapg.properties.serviceStatusForFunctions
    smtpSenderEmail: MetaOapg.properties.smtpSenderEmail
    smtpEnabled: MetaOapg.properties.smtpEnabled
    keys: MetaOapg.properties.keys
    description: MetaOapg.properties.description
    authUsersAuthMagicURL: MetaOapg.properties.authUsersAuthMagicURL
    serviceStatusForUsers: MetaOapg.properties.serviceStatusForUsers
    authSessionsLimit: MetaOapg.properties.authSessionsLimit
    oAuthProviders: MetaOapg.properties.oAuthProviders
    authDuration: MetaOapg.properties.authDuration
    serviceStatusForGraphql: MetaOapg.properties.serviceStatusForGraphql
    serviceStatusForStorage: MetaOapg.properties.serviceStatusForStorage
    smtpPassword: MetaOapg.properties.smtpPassword
    serviceStatusForHealth: MetaOapg.properties.serviceStatusForHealth
    legalCountry: MetaOapg.properties.legalCountry
    smtpSenderName: MetaOapg.properties.smtpSenderName
    url: MetaOapg.properties.url
    authLimit: MetaOapg.properties.authLimit
    smtpHost: MetaOapg.properties.smtpHost
    webhooks: MetaOapg.properties.webhooks
    authAnonymous: MetaOapg.properties.authAnonymous
    teamId: MetaOapg.properties.teamId
    authPasswordHistory: MetaOapg.properties.authPasswordHistory
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["authDuration"]) -> MetaOapg.properties.authDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authLimit"]) -> MetaOapg.properties.authLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authSessionsLimit"]) -> MetaOapg.properties.authSessionsLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authPasswordHistory"]) -> MetaOapg.properties.authPasswordHistory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authPasswordDictionary"]) -> MetaOapg.properties.authPasswordDictionary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authPersonalDataCheck"]) -> MetaOapg.properties.authPersonalDataCheck: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oAuthProviders"]) -> MetaOapg.properties.oAuthProviders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platforms"]) -> MetaOapg.properties.platforms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhooks"]) -> MetaOapg.properties.webhooks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keys"]) -> MetaOapg.properties.keys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpEnabled"]) -> MetaOapg.properties.smtpEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpSenderName"]) -> MetaOapg.properties.smtpSenderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpSenderEmail"]) -> MetaOapg.properties.smtpSenderEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpReplyTo"]) -> MetaOapg.properties.smtpReplyTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpHost"]) -> MetaOapg.properties.smtpHost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpPort"]) -> MetaOapg.properties.smtpPort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpUsername"]) -> MetaOapg.properties.smtpUsername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpPassword"]) -> MetaOapg.properties.smtpPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smtpSecure"]) -> MetaOapg.properties.smtpSecure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authEmailPassword"]) -> MetaOapg.properties.authEmailPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authUsersAuthMagicURL"]) -> MetaOapg.properties.authUsersAuthMagicURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authEmailOtp"]) -> MetaOapg.properties.authEmailOtp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authAnonymous"]) -> MetaOapg.properties.authAnonymous: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authInvites"]) -> MetaOapg.properties.authInvites: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authJWT"]) -> MetaOapg.properties.authJWT: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authPhone"]) -> MetaOapg.properties.authPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForAccount"]) -> MetaOapg.properties.serviceStatusForAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForAvatars"]) -> MetaOapg.properties.serviceStatusForAvatars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForDatabases"]) -> MetaOapg.properties.serviceStatusForDatabases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForLocale"]) -> MetaOapg.properties.serviceStatusForLocale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForHealth"]) -> MetaOapg.properties.serviceStatusForHealth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForStorage"]) -> MetaOapg.properties.serviceStatusForStorage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForTeams"]) -> MetaOapg.properties.serviceStatusForTeams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForUsers"]) -> MetaOapg.properties.serviceStatusForUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForFunctions"]) -> MetaOapg.properties.serviceStatusForFunctions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForGraphql"]) -> MetaOapg.properties.serviceStatusForGraphql: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusForMessaging"]) -> MetaOapg.properties.serviceStatusForMessaging: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "$id", "$createdAt", "$updatedAt", "name", "teamId", "logo", "url", "legalName", "legalCountry", "legalState", "legalCity", "legalAddress", "legalTaxId", "authDuration", "authLimit", "authSessionsLimit", "authPasswordHistory", "authPasswordDictionary", "authPersonalDataCheck", "oAuthProviders", "platforms", "webhooks", "keys", "smtpEnabled", "smtpSenderName", "smtpSenderEmail", "smtpReplyTo", "smtpHost", "smtpPort", "smtpUsername", "smtpPassword", "smtpSecure", "authEmailPassword", "authUsersAuthMagicURL", "authEmailOtp", "authAnonymous", "authInvites", "authJWT", "authPhone", "serviceStatusForAccount", "serviceStatusForAvatars", "serviceStatusForDatabases", "serviceStatusForLocale", "serviceStatusForHealth", "serviceStatusForStorage", "serviceStatusForTeams", "serviceStatusForUsers", "serviceStatusForFunctions", "serviceStatusForGraphql", "serviceStatusForMessaging", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$createdAt"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$updatedAt"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teamId"]) -> MetaOapg.properties.teamId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalCountry"]) -> MetaOapg.properties.legalCountry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalState"]) -> MetaOapg.properties.legalState: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalCity"]) -> MetaOapg.properties.legalCity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalAddress"]) -> MetaOapg.properties.legalAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalTaxId"]) -> MetaOapg.properties.legalTaxId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authDuration"]) -> MetaOapg.properties.authDuration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authLimit"]) -> MetaOapg.properties.authLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authSessionsLimit"]) -> MetaOapg.properties.authSessionsLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authPasswordHistory"]) -> MetaOapg.properties.authPasswordHistory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authPasswordDictionary"]) -> MetaOapg.properties.authPasswordDictionary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authPersonalDataCheck"]) -> MetaOapg.properties.authPersonalDataCheck: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oAuthProviders"]) -> MetaOapg.properties.oAuthProviders: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platforms"]) -> MetaOapg.properties.platforms: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhooks"]) -> MetaOapg.properties.webhooks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keys"]) -> MetaOapg.properties.keys: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpEnabled"]) -> MetaOapg.properties.smtpEnabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpSenderName"]) -> MetaOapg.properties.smtpSenderName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpSenderEmail"]) -> MetaOapg.properties.smtpSenderEmail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpReplyTo"]) -> MetaOapg.properties.smtpReplyTo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpHost"]) -> MetaOapg.properties.smtpHost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpPort"]) -> MetaOapg.properties.smtpPort: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpUsername"]) -> MetaOapg.properties.smtpUsername: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpPassword"]) -> MetaOapg.properties.smtpPassword: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smtpSecure"]) -> MetaOapg.properties.smtpSecure: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authEmailPassword"]) -> MetaOapg.properties.authEmailPassword: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authUsersAuthMagicURL"]) -> MetaOapg.properties.authUsersAuthMagicURL: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authEmailOtp"]) -> MetaOapg.properties.authEmailOtp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authAnonymous"]) -> MetaOapg.properties.authAnonymous: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authInvites"]) -> MetaOapg.properties.authInvites: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authJWT"]) -> MetaOapg.properties.authJWT: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authPhone"]) -> MetaOapg.properties.authPhone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForAccount"]) -> MetaOapg.properties.serviceStatusForAccount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForAvatars"]) -> MetaOapg.properties.serviceStatusForAvatars: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForDatabases"]) -> MetaOapg.properties.serviceStatusForDatabases: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForLocale"]) -> MetaOapg.properties.serviceStatusForLocale: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForHealth"]) -> MetaOapg.properties.serviceStatusForHealth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForStorage"]) -> MetaOapg.properties.serviceStatusForStorage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForTeams"]) -> MetaOapg.properties.serviceStatusForTeams: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForUsers"]) -> MetaOapg.properties.serviceStatusForUsers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForFunctions"]) -> MetaOapg.properties.serviceStatusForFunctions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForGraphql"]) -> MetaOapg.properties.serviceStatusForGraphql: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusForMessaging"]) -> MetaOapg.properties.serviceStatusForMessaging: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "$id", "$createdAt", "$updatedAt", "name", "teamId", "logo", "url", "legalName", "legalCountry", "legalState", "legalCity", "legalAddress", "legalTaxId", "authDuration", "authLimit", "authSessionsLimit", "authPasswordHistory", "authPasswordDictionary", "authPersonalDataCheck", "oAuthProviders", "platforms", "webhooks", "keys", "smtpEnabled", "smtpSenderName", "smtpSenderEmail", "smtpReplyTo", "smtpHost", "smtpPort", "smtpUsername", "smtpPassword", "smtpSecure", "authEmailPassword", "authUsersAuthMagicURL", "authEmailOtp", "authAnonymous", "authInvites", "authJWT", "authPhone", "serviceStatusForAccount", "serviceStatusForAvatars", "serviceStatusForDatabases", "serviceStatusForLocale", "serviceStatusForHealth", "serviceStatusForStorage", "serviceStatusForTeams", "serviceStatusForUsers", "serviceStatusForFunctions", "serviceStatusForGraphql", "serviceStatusForMessaging", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        serviceStatusForLocale: typing.Union[MetaOapg.properties.serviceStatusForLocale, bool, ],
        authInvites: typing.Union[MetaOapg.properties.authInvites, bool, ],
        serviceStatusForTeams: typing.Union[MetaOapg.properties.serviceStatusForTeams, bool, ],
        authEmailPassword: typing.Union[MetaOapg.properties.authEmailPassword, bool, ],
        legalTaxId: typing.Union[MetaOapg.properties.legalTaxId, str, ],
        smtpPort: typing.Union[MetaOapg.properties.smtpPort, decimal.Decimal, int, ],
        authPersonalDataCheck: typing.Union[MetaOapg.properties.authPersonalDataCheck, bool, ],
        authJWT: typing.Union[MetaOapg.properties.authJWT, bool, ],
        legalAddress: typing.Union[MetaOapg.properties.legalAddress, str, ],
        platforms: typing.Union[MetaOapg.properties.platforms, list, tuple, ],
        legalName: typing.Union[MetaOapg.properties.legalName, str, ],
        authEmailOtp: typing.Union[MetaOapg.properties.authEmailOtp, bool, ],
        serviceStatusForDatabases: typing.Union[MetaOapg.properties.serviceStatusForDatabases, bool, ],
        logo: typing.Union[MetaOapg.properties.logo, str, ],
        serviceStatusForAvatars: typing.Union[MetaOapg.properties.serviceStatusForAvatars, bool, ],
        authPhone: typing.Union[MetaOapg.properties.authPhone, bool, ],
        authPasswordDictionary: typing.Union[MetaOapg.properties.authPasswordDictionary, bool, ],
        smtpUsername: typing.Union[MetaOapg.properties.smtpUsername, str, ],
        legalCity: typing.Union[MetaOapg.properties.legalCity, str, ],
        smtpSecure: typing.Union[MetaOapg.properties.smtpSecure, str, ],
        serviceStatusForMessaging: typing.Union[MetaOapg.properties.serviceStatusForMessaging, bool, ],
        smtpReplyTo: typing.Union[MetaOapg.properties.smtpReplyTo, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        serviceStatusForAccount: typing.Union[MetaOapg.properties.serviceStatusForAccount, bool, ],
        legalState: typing.Union[MetaOapg.properties.legalState, str, ],
        serviceStatusForFunctions: typing.Union[MetaOapg.properties.serviceStatusForFunctions, bool, ],
        smtpSenderEmail: typing.Union[MetaOapg.properties.smtpSenderEmail, str, ],
        smtpEnabled: typing.Union[MetaOapg.properties.smtpEnabled, bool, ],
        keys: typing.Union[MetaOapg.properties.keys, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        authUsersAuthMagicURL: typing.Union[MetaOapg.properties.authUsersAuthMagicURL, bool, ],
        serviceStatusForUsers: typing.Union[MetaOapg.properties.serviceStatusForUsers, bool, ],
        authSessionsLimit: typing.Union[MetaOapg.properties.authSessionsLimit, decimal.Decimal, int, ],
        oAuthProviders: typing.Union[MetaOapg.properties.oAuthProviders, list, tuple, ],
        authDuration: typing.Union[MetaOapg.properties.authDuration, decimal.Decimal, int, ],
        serviceStatusForGraphql: typing.Union[MetaOapg.properties.serviceStatusForGraphql, bool, ],
        serviceStatusForStorage: typing.Union[MetaOapg.properties.serviceStatusForStorage, bool, ],
        smtpPassword: typing.Union[MetaOapg.properties.smtpPassword, str, ],
        serviceStatusForHealth: typing.Union[MetaOapg.properties.serviceStatusForHealth, bool, ],
        legalCountry: typing.Union[MetaOapg.properties.legalCountry, str, ],
        smtpSenderName: typing.Union[MetaOapg.properties.smtpSenderName, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        authLimit: typing.Union[MetaOapg.properties.authLimit, decimal.Decimal, int, ],
        smtpHost: typing.Union[MetaOapg.properties.smtpHost, str, ],
        webhooks: typing.Union[MetaOapg.properties.webhooks, list, tuple, ],
        authAnonymous: typing.Union[MetaOapg.properties.authAnonymous, bool, ],
        teamId: typing.Union[MetaOapg.properties.teamId, str, ],
        authPasswordHistory: typing.Union[MetaOapg.properties.authPasswordHistory, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Project':
        return super().__new__(
            cls,
            *args,
            serviceStatusForLocale=serviceStatusForLocale,
            authInvites=authInvites,
            serviceStatusForTeams=serviceStatusForTeams,
            authEmailPassword=authEmailPassword,
            legalTaxId=legalTaxId,
            smtpPort=smtpPort,
            authPersonalDataCheck=authPersonalDataCheck,
            authJWT=authJWT,
            legalAddress=legalAddress,
            platforms=platforms,
            legalName=legalName,
            authEmailOtp=authEmailOtp,
            serviceStatusForDatabases=serviceStatusForDatabases,
            logo=logo,
            serviceStatusForAvatars=serviceStatusForAvatars,
            authPhone=authPhone,
            authPasswordDictionary=authPasswordDictionary,
            smtpUsername=smtpUsername,
            legalCity=legalCity,
            smtpSecure=smtpSecure,
            serviceStatusForMessaging=serviceStatusForMessaging,
            smtpReplyTo=smtpReplyTo,
            name=name,
            serviceStatusForAccount=serviceStatusForAccount,
            legalState=legalState,
            serviceStatusForFunctions=serviceStatusForFunctions,
            smtpSenderEmail=smtpSenderEmail,
            smtpEnabled=smtpEnabled,
            keys=keys,
            description=description,
            authUsersAuthMagicURL=authUsersAuthMagicURL,
            serviceStatusForUsers=serviceStatusForUsers,
            authSessionsLimit=authSessionsLimit,
            oAuthProviders=oAuthProviders,
            authDuration=authDuration,
            serviceStatusForGraphql=serviceStatusForGraphql,
            serviceStatusForStorage=serviceStatusForStorage,
            smtpPassword=smtpPassword,
            serviceStatusForHealth=serviceStatusForHealth,
            legalCountry=legalCountry,
            smtpSenderName=smtpSenderName,
            url=url,
            authLimit=authLimit,
            smtpHost=smtpHost,
            webhooks=webhooks,
            authAnonymous=authAnonymous,
            teamId=teamId,
            authPasswordHistory=authPasswordHistory,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.auth_provider import AuthProvider
from appwrite_console_python_sdk.model.key import Key
from appwrite_console_python_sdk.model.platform import Platform
from appwrite_console_python_sdk.model.webhook import Webhook