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


class FunctionsUpdateByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class runtime(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "node-14.5": "NODE14_5",
                        "node-16.0": "NODE16_0",
                        "node-18.0": "NODE18_0",
                        "node-19.0": "NODE19_0",
                        "node-20.0": "NODE20_0",
                        "node-21.0": "NODE21_0",
                        "php-8.0": "PHP8_0",
                        "php-8.1": "PHP8_1",
                        "php-8.2": "PHP8_2",
                        "php-8.3": "PHP8_3",
                        "ruby-3.0": "RUBY3_0",
                        "ruby-3.1": "RUBY3_1",
                        "ruby-3.2": "RUBY3_2",
                        "ruby-3.3": "RUBY3_3",
                        "python-3.8": "PYTHON3_8",
                        "python-3.9": "PYTHON3_9",
                        "python-3.10": "PYTHON3_10",
                        "python-3.11": "PYTHON3_11",
                        "python-3.12": "PYTHON3_12",
                        "deno-1.40": "DENO1_40",
                        "dart-2.15": "DART2_15",
                        "dart-2.16": "DART2_16",
                        "dart-2.17": "DART2_17",
                        "dart-2.18": "DART2_18",
                        "dart-3.0": "DART3_0",
                        "dart-3.1": "DART3_1",
                        "dart-3.3": "DART3_3",
                        "dotnet-3.1": "DOTNET3_1",
                        "dotnet-6.0": "DOTNET6_0",
                        "dotnet-7.0": "DOTNET7_0",
                        "java-8.0": "JAVA8_0",
                        "java-11.0": "JAVA11_0",
                        "java-17.0": "JAVA17_0",
                        "java-18.0": "JAVA18_0",
                        "java-21.0": "JAVA21_0",
                        "swift-5.5": "SWIFT5_5",
                        "swift-5.8": "SWIFT5_8",
                        "swift-5.9": "SWIFT5_9",
                        "kotlin-1.6": "KOTLIN1_6",
                        "kotlin-1.8": "KOTLIN1_8",
                        "kotlin-1.9": "KOTLIN1_9",
                        "cpp-17": "CPP17",
                        "cpp-20": "CPP20",
                        "bun-1.0": "BUN1_0",
                    }
                
                @schemas.classproperty
                def NODE14_5(cls):
                    return cls("node-14.5")
                
                @schemas.classproperty
                def NODE16_0(cls):
                    return cls("node-16.0")
                
                @schemas.classproperty
                def NODE18_0(cls):
                    return cls("node-18.0")
                
                @schemas.classproperty
                def NODE19_0(cls):
                    return cls("node-19.0")
                
                @schemas.classproperty
                def NODE20_0(cls):
                    return cls("node-20.0")
                
                @schemas.classproperty
                def NODE21_0(cls):
                    return cls("node-21.0")
                
                @schemas.classproperty
                def PHP8_0(cls):
                    return cls("php-8.0")
                
                @schemas.classproperty
                def PHP8_1(cls):
                    return cls("php-8.1")
                
                @schemas.classproperty
                def PHP8_2(cls):
                    return cls("php-8.2")
                
                @schemas.classproperty
                def PHP8_3(cls):
                    return cls("php-8.3")
                
                @schemas.classproperty
                def RUBY3_0(cls):
                    return cls("ruby-3.0")
                
                @schemas.classproperty
                def RUBY3_1(cls):
                    return cls("ruby-3.1")
                
                @schemas.classproperty
                def RUBY3_2(cls):
                    return cls("ruby-3.2")
                
                @schemas.classproperty
                def RUBY3_3(cls):
                    return cls("ruby-3.3")
                
                @schemas.classproperty
                def PYTHON3_8(cls):
                    return cls("python-3.8")
                
                @schemas.classproperty
                def PYTHON3_9(cls):
                    return cls("python-3.9")
                
                @schemas.classproperty
                def PYTHON3_10(cls):
                    return cls("python-3.10")
                
                @schemas.classproperty
                def PYTHON3_11(cls):
                    return cls("python-3.11")
                
                @schemas.classproperty
                def PYTHON3_12(cls):
                    return cls("python-3.12")
                
                @schemas.classproperty
                def DENO1_40(cls):
                    return cls("deno-1.40")
                
                @schemas.classproperty
                def DART2_15(cls):
                    return cls("dart-2.15")
                
                @schemas.classproperty
                def DART2_16(cls):
                    return cls("dart-2.16")
                
                @schemas.classproperty
                def DART2_17(cls):
                    return cls("dart-2.17")
                
                @schemas.classproperty
                def DART2_18(cls):
                    return cls("dart-2.18")
                
                @schemas.classproperty
                def DART3_0(cls):
                    return cls("dart-3.0")
                
                @schemas.classproperty
                def DART3_1(cls):
                    return cls("dart-3.1")
                
                @schemas.classproperty
                def DART3_3(cls):
                    return cls("dart-3.3")
                
                @schemas.classproperty
                def DOTNET3_1(cls):
                    return cls("dotnet-3.1")
                
                @schemas.classproperty
                def DOTNET6_0(cls):
                    return cls("dotnet-6.0")
                
                @schemas.classproperty
                def DOTNET7_0(cls):
                    return cls("dotnet-7.0")
                
                @schemas.classproperty
                def JAVA8_0(cls):
                    return cls("java-8.0")
                
                @schemas.classproperty
                def JAVA11_0(cls):
                    return cls("java-11.0")
                
                @schemas.classproperty
                def JAVA17_0(cls):
                    return cls("java-17.0")
                
                @schemas.classproperty
                def JAVA18_0(cls):
                    return cls("java-18.0")
                
                @schemas.classproperty
                def JAVA21_0(cls):
                    return cls("java-21.0")
                
                @schemas.classproperty
                def SWIFT5_5(cls):
                    return cls("swift-5.5")
                
                @schemas.classproperty
                def SWIFT5_8(cls):
                    return cls("swift-5.8")
                
                @schemas.classproperty
                def SWIFT5_9(cls):
                    return cls("swift-5.9")
                
                @schemas.classproperty
                def KOTLIN1_6(cls):
                    return cls("kotlin-1.6")
                
                @schemas.classproperty
                def KOTLIN1_8(cls):
                    return cls("kotlin-1.8")
                
                @schemas.classproperty
                def KOTLIN1_9(cls):
                    return cls("kotlin-1.9")
                
                @schemas.classproperty
                def CPP17(cls):
                    return cls("cpp-17")
                
                @schemas.classproperty
                def CPP20(cls):
                    return cls("cpp-20")
                
                @schemas.classproperty
                def BUN1_0(cls):
                    return cls("bun-1.0")
        
            @staticmethod
            def execute() -> typing.Type['FunctionsUpdateByIdRequestExecute']:
                return FunctionsUpdateByIdRequestExecute
        
            @staticmethod
            def events() -> typing.Type['FunctionsUpdateByIdRequestEvents']:
                return FunctionsUpdateByIdRequestEvents
            schedule = schemas.StrSchema
            timeout = schemas.IntSchema
            enabled = schemas.BoolSchema
            logging = schemas.BoolSchema
            entrypoint = schemas.StrSchema
            commands = schemas.StrSchema
            installationId = schemas.StrSchema
            providerRepositoryId = schemas.StrSchema
            providerBranch = schemas.StrSchema
            providerSilentMode = schemas.BoolSchema
            providerRootDirectory = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "runtime": runtime,
                "execute": execute,
                "events": events,
                "schedule": schedule,
                "timeout": timeout,
                "enabled": enabled,
                "logging": logging,
                "entrypoint": entrypoint,
                "commands": commands,
                "installationId": installationId,
                "providerRepositoryId": providerRepositoryId,
                "providerBranch": providerBranch,
                "providerSilentMode": providerSilentMode,
                "providerRootDirectory": providerRootDirectory,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runtime"]) -> MetaOapg.properties.runtime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["execute"]) -> 'FunctionsUpdateByIdRequestExecute': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'FunctionsUpdateByIdRequestEvents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> MetaOapg.properties.schedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeout"]) -> MetaOapg.properties.timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logging"]) -> MetaOapg.properties.logging: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entrypoint"]) -> MetaOapg.properties.entrypoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commands"]) -> MetaOapg.properties.commands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["installationId"]) -> MetaOapg.properties.installationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRepositoryId"]) -> MetaOapg.properties.providerRepositoryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerBranch"]) -> MetaOapg.properties.providerBranch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerSilentMode"]) -> MetaOapg.properties.providerSilentMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerRootDirectory"]) -> MetaOapg.properties.providerRootDirectory: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "runtime", "execute", "events", "schedule", "timeout", "enabled", "logging", "entrypoint", "commands", "installationId", "providerRepositoryId", "providerBranch", "providerSilentMode", "providerRootDirectory", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runtime"]) -> typing.Union[MetaOapg.properties.runtime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["execute"]) -> typing.Union['FunctionsUpdateByIdRequestExecute', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union['FunctionsUpdateByIdRequestEvents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union[MetaOapg.properties.schedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeout"]) -> typing.Union[MetaOapg.properties.timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logging"]) -> typing.Union[MetaOapg.properties.logging, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entrypoint"]) -> typing.Union[MetaOapg.properties.entrypoint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commands"]) -> typing.Union[MetaOapg.properties.commands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["installationId"]) -> typing.Union[MetaOapg.properties.installationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRepositoryId"]) -> typing.Union[MetaOapg.properties.providerRepositoryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerBranch"]) -> typing.Union[MetaOapg.properties.providerBranch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerSilentMode"]) -> typing.Union[MetaOapg.properties.providerSilentMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerRootDirectory"]) -> typing.Union[MetaOapg.properties.providerRootDirectory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "runtime", "execute", "events", "schedule", "timeout", "enabled", "logging", "entrypoint", "commands", "installationId", "providerRepositoryId", "providerBranch", "providerSilentMode", "providerRootDirectory", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        runtime: typing.Union[MetaOapg.properties.runtime, str, schemas.Unset] = schemas.unset,
        execute: typing.Union['FunctionsUpdateByIdRequestExecute', schemas.Unset] = schemas.unset,
        events: typing.Union['FunctionsUpdateByIdRequestEvents', schemas.Unset] = schemas.unset,
        schedule: typing.Union[MetaOapg.properties.schedule, str, schemas.Unset] = schemas.unset,
        timeout: typing.Union[MetaOapg.properties.timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        logging: typing.Union[MetaOapg.properties.logging, bool, schemas.Unset] = schemas.unset,
        entrypoint: typing.Union[MetaOapg.properties.entrypoint, str, schemas.Unset] = schemas.unset,
        commands: typing.Union[MetaOapg.properties.commands, str, schemas.Unset] = schemas.unset,
        installationId: typing.Union[MetaOapg.properties.installationId, str, schemas.Unset] = schemas.unset,
        providerRepositoryId: typing.Union[MetaOapg.properties.providerRepositoryId, str, schemas.Unset] = schemas.unset,
        providerBranch: typing.Union[MetaOapg.properties.providerBranch, str, schemas.Unset] = schemas.unset,
        providerSilentMode: typing.Union[MetaOapg.properties.providerSilentMode, bool, schemas.Unset] = schemas.unset,
        providerRootDirectory: typing.Union[MetaOapg.properties.providerRootDirectory, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionsUpdateByIdRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            runtime=runtime,
            execute=execute,
            events=events,
            schedule=schedule,
            timeout=timeout,
            enabled=enabled,
            logging=logging,
            entrypoint=entrypoint,
            commands=commands,
            installationId=installationId,
            providerRepositoryId=providerRepositoryId,
            providerBranch=providerBranch,
            providerSilentMode=providerSilentMode,
            providerRootDirectory=providerRootDirectory,
            _configuration=_configuration,
            **kwargs,
        )

from appwrite_console_python_sdk.model.functions_update_by_id_request_events import FunctionsUpdateByIdRequestEvents
from appwrite_console_python_sdk.model.functions_update_by_id_request_execute import FunctionsUpdateByIdRequestExecute