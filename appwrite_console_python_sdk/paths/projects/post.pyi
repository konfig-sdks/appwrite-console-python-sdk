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

from appwrite_console_python_sdk.model.projects_create_new_project_request import ProjectsCreateNewProjectRequest as ProjectsCreateNewProjectRequestSchema
from appwrite_console_python_sdk.model.project import Project as ProjectSchema

from appwrite_console_python_sdk.type.project import Project
from appwrite_console_python_sdk.type.projects_create_new_project_request import ProjectsCreateNewProjectRequest

from ...api_client import Dictionary
from appwrite_console_python_sdk.pydantic.project import Project as ProjectPydantic
from appwrite_console_python_sdk.pydantic.projects_create_new_project_request import ProjectsCreateNewProjectRequest as ProjectsCreateNewProjectRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = ProjectsCreateNewProjectRequestSchema


request_body_projects_create_new_project_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = ProjectSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Project


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Project


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

    def _create_new_project_mapped_args(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if project_id is not None:
            _body["projectId"] = project_id
        if name is not None:
            _body["name"] = name
        if team_id is not None:
            _body["teamId"] = team_id
        if region is not None:
            _body["region"] = region
        if logo is not None:
            _body["logo"] = logo
        if url is not None:
            _body["url"] = url
        if legal_name is not None:
            _body["legalName"] = legal_name
        if legal_country is not None:
            _body["legalCountry"] = legal_country
        if legal_state is not None:
            _body["legalState"] = legal_state
        if legal_city is not None:
            _body["legalCity"] = legal_city
        if legal_address is not None:
            _body["legalAddress"] = legal_address
        if legal_tax_id is not None:
            _body["legalTaxId"] = legal_tax_id
        args.body = _body
        return args

    async def _acreate_new_project_oapg(
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
        Create project
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
            path_template='/projects',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_projects_create_new_project_request.serialize(body, content_type)
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


    def _create_new_project_oapg(
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
        Create project
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
            path_template='/projects',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_projects_create_new_project_request.serialize(body, content_type)
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


class CreateNewProjectRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_project(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_project_mapped_args(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
        )
        return await self._acreate_new_project_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_project(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_project_mapped_args(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
        )
        return self._create_new_project_oapg(
            body=args.body,
        )

class CreateNewProject(BaseApi):

    async def acreate_new_project(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectPydantic:
        raw_response = await self.raw.acreate_new_project(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
            **kwargs,
        )
        if validate:
            return ProjectPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectPydantic, raw_response.body)
    
    
    def create_new_project(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ProjectPydantic:
        raw_response = self.raw.create_new_project(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
        )
        if validate:
            return ProjectPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_project_mapped_args(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
        )
        return await self._acreate_new_project_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        project_id: str,
        name: str,
        team_id: str,
        description: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        logo: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        legal_name: typing.Optional[str] = None,
        legal_country: typing.Optional[str] = None,
        legal_state: typing.Optional[str] = None,
        legal_city: typing.Optional[str] = None,
        legal_address: typing.Optional[str] = None,
        legal_tax_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_project_mapped_args(
            project_id=project_id,
            name=name,
            team_id=team_id,
            description=description,
            region=region,
            logo=logo,
            url=url,
            legal_name=legal_name,
            legal_country=legal_country,
            legal_state=legal_state,
            legal_city=legal_city,
            legal_address=legal_address,
            legal_tax_id=legal_tax_id,
        )
        return self._create_new_project_oapg(
            body=args.body,
        )

