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


class ProjectsUpdateOAuthRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "provider",
        }
        
        class properties:
            
            
            class provider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AMAZON(cls):
                    return cls("amazon")
                
                @schemas.classproperty
                def APPLE(cls):
                    return cls("apple")
                
                @schemas.classproperty
                def AUTH0(cls):
                    return cls("auth0")
                
                @schemas.classproperty
                def AUTHENTIK(cls):
                    return cls("authentik")
                
                @schemas.classproperty
                def AUTODESK(cls):
                    return cls("autodesk")
                
                @schemas.classproperty
                def BITBUCKET(cls):
                    return cls("bitbucket")
                
                @schemas.classproperty
                def BITLY(cls):
                    return cls("bitly")
                
                @schemas.classproperty
                def BOX(cls):
                    return cls("box")
                
                @schemas.classproperty
                def DAILYMOTION(cls):
                    return cls("dailymotion")
                
                @schemas.classproperty
                def DISCORD(cls):
                    return cls("discord")
                
                @schemas.classproperty
                def DISQUS(cls):
                    return cls("disqus")
                
                @schemas.classproperty
                def DROPBOX(cls):
                    return cls("dropbox")
                
                @schemas.classproperty
                def ETSY(cls):
                    return cls("etsy")
                
                @schemas.classproperty
                def FACEBOOK(cls):
                    return cls("facebook")
                
                @schemas.classproperty
                def GITHUB(cls):
                    return cls("github")
                
                @schemas.classproperty
                def GITLAB(cls):
                    return cls("gitlab")
                
                @schemas.classproperty
                def GOOGLE(cls):
                    return cls("google")
                
                @schemas.classproperty
                def LINKEDIN(cls):
                    return cls("linkedin")
                
                @schemas.classproperty
                def MICROSOFT(cls):
                    return cls("microsoft")
                
                @schemas.classproperty
                def NOTION(cls):
                    return cls("notion")
                
                @schemas.classproperty
                def OIDC(cls):
                    return cls("oidc")
                
                @schemas.classproperty
                def OKTA(cls):
                    return cls("okta")
                
                @schemas.classproperty
                def PAYPAL(cls):
                    return cls("paypal")
                
                @schemas.classproperty
                def PAYPAL_SANDBOX(cls):
                    return cls("paypalSandbox")
                
                @schemas.classproperty
                def PODIO(cls):
                    return cls("podio")
                
                @schemas.classproperty
                def SALESFORCE(cls):
                    return cls("salesforce")
                
                @schemas.classproperty
                def SLACK(cls):
                    return cls("slack")
                
                @schemas.classproperty
                def SPOTIFY(cls):
                    return cls("spotify")
                
                @schemas.classproperty
                def STRIPE(cls):
                    return cls("stripe")
                
                @schemas.classproperty
                def TRADESHIFT(cls):
                    return cls("tradeshift")
                
                @schemas.classproperty
                def TRADESHIFT_BOX(cls):
                    return cls("tradeshiftBox")
                
                @schemas.classproperty
                def TWITCH(cls):
                    return cls("twitch")
                
                @schemas.classproperty
                def WORDPRESS(cls):
                    return cls("wordpress")
                
                @schemas.classproperty
                def YAHOO(cls):
                    return cls("yahoo")
                
                @schemas.classproperty
                def YAMMER(cls):
                    return cls("yammer")
                
                @schemas.classproperty
                def YANDEX(cls):
                    return cls("yandex")
                
                @schemas.classproperty
                def ZOHO(cls):
                    return cls("zoho")
                
                @schemas.classproperty
                def ZOOM(cls):
                    return cls("zoom")
                
                @schemas.classproperty
                def MOCK(cls):
                    return cls("mock")
            appId = schemas.StrSchema
            secret = schemas.StrSchema
            enabled = schemas.BoolSchema
            __annotations__ = {
                "provider": provider,
                "appId": appId,
                "secret": secret,
                "enabled": enabled,
            }
    
    provider: MetaOapg.properties.provider
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provider", "appId", "secret", "enabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> typing.Union[MetaOapg.properties.secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provider", "appId", "secret", "enabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        appId: typing.Union[MetaOapg.properties.appId, str, schemas.Unset] = schemas.unset,
        secret: typing.Union[MetaOapg.properties.secret, str, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsUpdateOAuthRequest':
        return super().__new__(
            cls,
            *args,
            provider=provider,
            appId=appId,
            secret=secret,
            enabled=enabled,
            _configuration=_configuration,
            **kwargs,
        )
