# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from appwrite_console_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from appwrite_console_python_sdk.api_response import AsyncGeneratorResponse
from appwrite_console_python_sdk import api_client, exceptions
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

from appwrite_console_python_sdk.model.function import Function as FunctionSchema
from appwrite_console_python_sdk.model.functions_create_function_request import FunctionsCreateFunctionRequest as FunctionsCreateFunctionRequestSchema
from appwrite_console_python_sdk.model.functions_create_function_request_events import FunctionsCreateFunctionRequestEvents as FunctionsCreateFunctionRequestEventsSchema
from appwrite_console_python_sdk.model.functions_create_function_request_execute import FunctionsCreateFunctionRequestExecute as FunctionsCreateFunctionRequestExecuteSchema

from appwrite_console_python_sdk.type.functions_create_function_request import FunctionsCreateFunctionRequest
from appwrite_console_python_sdk.type.functions_create_function_request_execute import FunctionsCreateFunctionRequestExecute
from appwrite_console_python_sdk.type.function import Function
from appwrite_console_python_sdk.type.functions_create_function_request_events import FunctionsCreateFunctionRequestEvents

from ...api_client import Dictionary
from appwrite_console_python_sdk.pydantic.function import Function as FunctionPydantic
from appwrite_console_python_sdk.pydantic.functions_create_function_request_events import FunctionsCreateFunctionRequestEvents as FunctionsCreateFunctionRequestEventsPydantic
from appwrite_console_python_sdk.pydantic.functions_create_function_request_execute import FunctionsCreateFunctionRequestExecute as FunctionsCreateFunctionRequestExecutePydantic
from appwrite_console_python_sdk.pydantic.functions_create_function_request import FunctionsCreateFunctionRequest as FunctionsCreateFunctionRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = FunctionsCreateFunctionRequestSchema


request_body_functions_create_function_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = FunctionSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Function


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Function


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_function_mapped_args(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if function_id is not None:
            _body["functionId"] = function_id
        if name is not None:
            _body["name"] = name
        if runtime is not None:
            _body["runtime"] = runtime
        if execute is not None:
            _body["execute"] = execute
        if events is not None:
            _body["events"] = events
        if schedule is not None:
            _body["schedule"] = schedule
        if timeout is not None:
            _body["timeout"] = timeout
        if enabled is not None:
            _body["enabled"] = enabled
        if logging is not None:
            _body["logging"] = logging
        if entrypoint is not None:
            _body["entrypoint"] = entrypoint
        if commands is not None:
            _body["commands"] = commands
        if installation_id is not None:
            _body["installationId"] = installation_id
        if provider_repository_id is not None:
            _body["providerRepositoryId"] = provider_repository_id
        if provider_branch is not None:
            _body["providerBranch"] = provider_branch
        if provider_silent_mode is not None:
            _body["providerSilentMode"] = provider_silent_mode
        if provider_root_directory is not None:
            _body["providerRootDirectory"] = provider_root_directory
        if template_repository is not None:
            _body["templateRepository"] = template_repository
        if template_owner is not None:
            _body["templateOwner"] = template_owner
        if template_root_directory is not None:
            _body["templateRootDirectory"] = template_root_directory
        if template_branch is not None:
            _body["templateBranch"] = template_branch
        args.body = _body
        return args

    async def _acreate_function_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/functions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_functions_create_function_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_function_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/functions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_functions_create_function_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateFunctionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_function(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_function_mapped_args(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
        )
        return await self._acreate_function_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_function(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_function_mapped_args(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
        )
        return self._create_function_oapg(
            body=args.body,
        )

class CreateFunction(BaseApi):

    async def acreate_function(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FunctionPydantic:
        raw_response = await self.raw.acreate_function(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
            **kwargs,
        )
        if validate:
            return FunctionPydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionPydantic, raw_response.body)
    
    
    def create_function(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FunctionPydantic:
        raw_response = self.raw.create_function(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
        )
        if validate:
            return FunctionPydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_function_mapped_args(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
        )
        return await self._acreate_function_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        function_id: str,
        name: str,
        runtime: str,
        execute: typing.Optional[FunctionsCreateFunctionRequestExecute] = None,
        events: typing.Optional[FunctionsCreateFunctionRequestEvents] = None,
        schedule: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        enabled: typing.Optional[bool] = None,
        logging: typing.Optional[bool] = None,
        entrypoint: typing.Optional[str] = None,
        commands: typing.Optional[str] = None,
        installation_id: typing.Optional[str] = None,
        provider_repository_id: typing.Optional[str] = None,
        provider_branch: typing.Optional[str] = None,
        provider_silent_mode: typing.Optional[bool] = None,
        provider_root_directory: typing.Optional[str] = None,
        template_repository: typing.Optional[str] = None,
        template_owner: typing.Optional[str] = None,
        template_root_directory: typing.Optional[str] = None,
        template_branch: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_function_mapped_args(
            function_id=function_id,
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
            installation_id=installation_id,
            provider_repository_id=provider_repository_id,
            provider_branch=provider_branch,
            provider_silent_mode=provider_silent_mode,
            provider_root_directory=provider_root_directory,
            template_repository=template_repository,
            template_owner=template_owner,
            template_root_directory=template_root_directory,
            template_branch=template_branch,
        )
        return self._create_function_oapg(
            body=args.body,
        )
