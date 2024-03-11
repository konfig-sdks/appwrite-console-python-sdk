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

from appwrite_console_python_sdk.model.sms_template import SmsTemplate as SmsTemplateSchema

from appwrite_console_python_sdk.type.sms_template import SmsTemplate

from ...api_client import Dictionary
from appwrite_console_python_sdk.pydantic.sms_template import SmsTemplate as SmsTemplatePydantic

from . import path

# Path params
ProjectIdSchema = schemas.StrSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "verification": "VERIFICATION",
            "login": "LOGIN",
            "invitation": "INVITATION",
            "mfachallenge": "MFACHALLENGE",
        }
    
    @schemas.classproperty
    def VERIFICATION(cls):
        return cls("verification")
    
    @schemas.classproperty
    def LOGIN(cls):
        return cls("login")
    
    @schemas.classproperty
    def INVITATION(cls):
        return cls("invitation")
    
    @schemas.classproperty
    def MFACHALLENGE(cls):
        return cls("mfachallenge")


class LocaleSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "af": "AF",
            "ar-ae": "ARAE",
            "ar-bh": "ARBH",
            "ar-dz": "ARDZ",
            "ar-eg": "AREG",
            "ar-iq": "ARIQ",
            "ar-jo": "ARJO",
            "ar-kw": "ARKW",
            "ar-lb": "ARLB",
            "ar-ly": "ARLY",
            "ar-ma": "ARMA",
            "ar-om": "AROM",
            "ar-qa": "ARQA",
            "ar-sa": "ARSA",
            "ar-sy": "ARSY",
            "ar-tn": "ARTN",
            "ar-ye": "ARYE",
            "as": "AS",
            "az": "AZ",
            "be": "BE",
            "bg": "BG",
            "bh": "BH",
            "bn": "BN",
            "bs": "BS",
            "ca": "CA",
            "cs": "CS",
            "cy": "CY",
            "da": "DA",
            "de": "DE",
            "de-at": "DEAT",
            "de-ch": "DECH",
            "de-li": "DELI",
            "de-lu": "DELU",
            "el": "EL",
            "en": "EN",
            "en-au": "ENAU",
            "en-bz": "ENBZ",
            "en-ca": "ENCA",
            "en-gb": "ENGB",
            "en-ie": "ENIE",
            "en-jm": "ENJM",
            "en-nz": "ENNZ",
            "en-tt": "ENTT",
            "en-us": "ENUS",
            "en-za": "ENZA",
            "eo": "EO",
            "es": "ES",
            "es-ar": "ESAR",
            "es-bo": "ESBO",
            "es-cl": "ESCL",
            "es-co": "ESCO",
            "es-cr": "ESCR",
            "es-do": "ESDO",
            "es-ec": "ESEC",
            "es-gt": "ESGT",
            "es-hn": "ESHN",
            "es-mx": "ESMX",
            "es-ni": "ESNI",
            "es-pa": "ESPA",
            "es-pe": "ESPE",
            "es-pr": "ESPR",
            "es-py": "ESPY",
            "es-sv": "ESSV",
            "es-uy": "ESUY",
            "es-ve": "ESVE",
            "et": "ET",
            "eu": "EU",
            "fa": "FA",
            "fi": "FI",
            "fo": "FO",
            "fr": "FR",
            "fr-be": "FRBE",
            "fr-ca": "FRCA",
            "fr-ch": "FRCH",
            "fr-lu": "FRLU",
            "ga": "GA",
            "gd": "GD",
            "he": "HE",
            "hi": "HI",
            "hr": "HR",
            "hu": "HU",
            "id": "ID",
            "is": "IS",
            "it": "IT",
            "it-ch": "ITCH",
            "ja": "JA",
            "ji": "JI",
            "ko": "KO",
            "ku": "KU",
            "lt": "LT",
            "lv": "LV",
            "mk": "MK",
            "ml": "ML",
            "ms": "MS",
            "mt": "MT",
            "nb": "NB",
            "ne": "NE",
            "nl": "NL",
            "nl-be": "NLBE",
            "nn": "NN",
            "false": "FALSE",
            "pa": "PA",
            "pl": "PL",
            "pt": "PT",
            "pt-br": "PTBR",
            "rm": "RM",
            "ro": "RO",
            "ro-md": "ROMD",
            "ru": "RU",
            "ru-md": "RUMD",
            "sb": "SB",
            "sk": "SK",
            "sl": "SL",
            "sq": "SQ",
            "sr": "SR",
            "sv": "SV",
            "sv-fi": "SVFI",
            "th": "TH",
            "tn": "TN",
            "tr": "TR",
            "ts": "TS",
            "ua": "UA",
            "ur": "UR",
            "ve": "VE",
            "vi": "VI",
            "xh": "XH",
            "zh-cn": "ZHCN",
            "zh-hk": "ZHHK",
            "zh-sg": "ZHSG",
            "zh-tw": "ZHTW",
            "zu": "ZU",
        }
    
    @schemas.classproperty
    def AF(cls):
        return cls("af")
    
    @schemas.classproperty
    def ARAE(cls):
        return cls("ar-ae")
    
    @schemas.classproperty
    def ARBH(cls):
        return cls("ar-bh")
    
    @schemas.classproperty
    def ARDZ(cls):
        return cls("ar-dz")
    
    @schemas.classproperty
    def AREG(cls):
        return cls("ar-eg")
    
    @schemas.classproperty
    def ARIQ(cls):
        return cls("ar-iq")
    
    @schemas.classproperty
    def ARJO(cls):
        return cls("ar-jo")
    
    @schemas.classproperty
    def ARKW(cls):
        return cls("ar-kw")
    
    @schemas.classproperty
    def ARLB(cls):
        return cls("ar-lb")
    
    @schemas.classproperty
    def ARLY(cls):
        return cls("ar-ly")
    
    @schemas.classproperty
    def ARMA(cls):
        return cls("ar-ma")
    
    @schemas.classproperty
    def AROM(cls):
        return cls("ar-om")
    
    @schemas.classproperty
    def ARQA(cls):
        return cls("ar-qa")
    
    @schemas.classproperty
    def ARSA(cls):
        return cls("ar-sa")
    
    @schemas.classproperty
    def ARSY(cls):
        return cls("ar-sy")
    
    @schemas.classproperty
    def ARTN(cls):
        return cls("ar-tn")
    
    @schemas.classproperty
    def ARYE(cls):
        return cls("ar-ye")
    
    @schemas.classproperty
    def AS(cls):
        return cls("as")
    
    @schemas.classproperty
    def AZ(cls):
        return cls("az")
    
    @schemas.classproperty
    def BE(cls):
        return cls("be")
    
    @schemas.classproperty
    def BG(cls):
        return cls("bg")
    
    @schemas.classproperty
    def BH(cls):
        return cls("bh")
    
    @schemas.classproperty
    def BN(cls):
        return cls("bn")
    
    @schemas.classproperty
    def BS(cls):
        return cls("bs")
    
    @schemas.classproperty
    def CA(cls):
        return cls("ca")
    
    @schemas.classproperty
    def CS(cls):
        return cls("cs")
    
    @schemas.classproperty
    def CY(cls):
        return cls("cy")
    
    @schemas.classproperty
    def DA(cls):
        return cls("da")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def DEAT(cls):
        return cls("de-at")
    
    @schemas.classproperty
    def DECH(cls):
        return cls("de-ch")
    
    @schemas.classproperty
    def DELI(cls):
        return cls("de-li")
    
    @schemas.classproperty
    def DELU(cls):
        return cls("de-lu")
    
    @schemas.classproperty
    def EL(cls):
        return cls("el")
    
    @schemas.classproperty
    def EN(cls):
        return cls("en")
    
    @schemas.classproperty
    def ENAU(cls):
        return cls("en-au")
    
    @schemas.classproperty
    def ENBZ(cls):
        return cls("en-bz")
    
    @schemas.classproperty
    def ENCA(cls):
        return cls("en-ca")
    
    @schemas.classproperty
    def ENGB(cls):
        return cls("en-gb")
    
    @schemas.classproperty
    def ENIE(cls):
        return cls("en-ie")
    
    @schemas.classproperty
    def ENJM(cls):
        return cls("en-jm")
    
    @schemas.classproperty
    def ENNZ(cls):
        return cls("en-nz")
    
    @schemas.classproperty
    def ENTT(cls):
        return cls("en-tt")
    
    @schemas.classproperty
    def ENUS(cls):
        return cls("en-us")
    
    @schemas.classproperty
    def ENZA(cls):
        return cls("en-za")
    
    @schemas.classproperty
    def EO(cls):
        return cls("eo")
    
    @schemas.classproperty
    def ES(cls):
        return cls("es")
    
    @schemas.classproperty
    def ESAR(cls):
        return cls("es-ar")
    
    @schemas.classproperty
    def ESBO(cls):
        return cls("es-bo")
    
    @schemas.classproperty
    def ESCL(cls):
        return cls("es-cl")
    
    @schemas.classproperty
    def ESCO(cls):
        return cls("es-co")
    
    @schemas.classproperty
    def ESCR(cls):
        return cls("es-cr")
    
    @schemas.classproperty
    def ESDO(cls):
        return cls("es-do")
    
    @schemas.classproperty
    def ESEC(cls):
        return cls("es-ec")
    
    @schemas.classproperty
    def ESGT(cls):
        return cls("es-gt")
    
    @schemas.classproperty
    def ESHN(cls):
        return cls("es-hn")
    
    @schemas.classproperty
    def ESMX(cls):
        return cls("es-mx")
    
    @schemas.classproperty
    def ESNI(cls):
        return cls("es-ni")
    
    @schemas.classproperty
    def ESPA(cls):
        return cls("es-pa")
    
    @schemas.classproperty
    def ESPE(cls):
        return cls("es-pe")
    
    @schemas.classproperty
    def ESPR(cls):
        return cls("es-pr")
    
    @schemas.classproperty
    def ESPY(cls):
        return cls("es-py")
    
    @schemas.classproperty
    def ESSV(cls):
        return cls("es-sv")
    
    @schemas.classproperty
    def ESUY(cls):
        return cls("es-uy")
    
    @schemas.classproperty
    def ESVE(cls):
        return cls("es-ve")
    
    @schemas.classproperty
    def ET(cls):
        return cls("et")
    
    @schemas.classproperty
    def EU(cls):
        return cls("eu")
    
    @schemas.classproperty
    def FA(cls):
        return cls("fa")
    
    @schemas.classproperty
    def FI(cls):
        return cls("fi")
    
    @schemas.classproperty
    def FO(cls):
        return cls("fo")
    
    @schemas.classproperty
    def FR(cls):
        return cls("fr")
    
    @schemas.classproperty
    def FRBE(cls):
        return cls("fr-be")
    
    @schemas.classproperty
    def FRCA(cls):
        return cls("fr-ca")
    
    @schemas.classproperty
    def FRCH(cls):
        return cls("fr-ch")
    
    @schemas.classproperty
    def FRLU(cls):
        return cls("fr-lu")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def GD(cls):
        return cls("gd")
    
    @schemas.classproperty
    def HE(cls):
        return cls("he")
    
    @schemas.classproperty
    def HI(cls):
        return cls("hi")
    
    @schemas.classproperty
    def HR(cls):
        return cls("hr")
    
    @schemas.classproperty
    def HU(cls):
        return cls("hu")
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
    
    @schemas.classproperty
    def IS(cls):
        return cls("is")
    
    @schemas.classproperty
    def IT(cls):
        return cls("it")
    
    @schemas.classproperty
    def ITCH(cls):
        return cls("it-ch")
    
    @schemas.classproperty
    def JA(cls):
        return cls("ja")
    
    @schemas.classproperty
    def JI(cls):
        return cls("ji")
    
    @schemas.classproperty
    def KO(cls):
        return cls("ko")
    
    @schemas.classproperty
    def KU(cls):
        return cls("ku")
    
    @schemas.classproperty
    def LT(cls):
        return cls("lt")
    
    @schemas.classproperty
    def LV(cls):
        return cls("lv")
    
    @schemas.classproperty
    def MK(cls):
        return cls("mk")
    
    @schemas.classproperty
    def ML(cls):
        return cls("ml")
    
    @schemas.classproperty
    def MS(cls):
        return cls("ms")
    
    @schemas.classproperty
    def MT(cls):
        return cls("mt")
    
    @schemas.classproperty
    def NB(cls):
        return cls("nb")
    
    @schemas.classproperty
    def NE(cls):
        return cls("ne")
    
    @schemas.classproperty
    def NL(cls):
        return cls("nl")
    
    @schemas.classproperty
    def NLBE(cls):
        return cls("nl-be")
    
    @schemas.classproperty
    def NN(cls):
        return cls("nn")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
    
    @schemas.classproperty
    def PA(cls):
        return cls("pa")
    
    @schemas.classproperty
    def PL(cls):
        return cls("pl")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")
    
    @schemas.classproperty
    def PTBR(cls):
        return cls("pt-br")
    
    @schemas.classproperty
    def RM(cls):
        return cls("rm")
    
    @schemas.classproperty
    def RO(cls):
        return cls("ro")
    
    @schemas.classproperty
    def ROMD(cls):
        return cls("ro-md")
    
    @schemas.classproperty
    def RU(cls):
        return cls("ru")
    
    @schemas.classproperty
    def RUMD(cls):
        return cls("ru-md")
    
    @schemas.classproperty
    def SB(cls):
        return cls("sb")
    
    @schemas.classproperty
    def SK(cls):
        return cls("sk")
    
    @schemas.classproperty
    def SL(cls):
        return cls("sl")
    
    @schemas.classproperty
    def SQ(cls):
        return cls("sq")
    
    @schemas.classproperty
    def SR(cls):
        return cls("sr")
    
    @schemas.classproperty
    def SV(cls):
        return cls("sv")
    
    @schemas.classproperty
    def SVFI(cls):
        return cls("sv-fi")
    
    @schemas.classproperty
    def TH(cls):
        return cls("th")
    
    @schemas.classproperty
    def TN(cls):
        return cls("tn")
    
    @schemas.classproperty
    def TR(cls):
        return cls("tr")
    
    @schemas.classproperty
    def TS(cls):
        return cls("ts")
    
    @schemas.classproperty
    def UA(cls):
        return cls("ua")
    
    @schemas.classproperty
    def UR(cls):
        return cls("ur")
    
    @schemas.classproperty
    def VE(cls):
        return cls("ve")
    
    @schemas.classproperty
    def VI(cls):
        return cls("vi")
    
    @schemas.classproperty
    def XH(cls):
        return cls("xh")
    
    @schemas.classproperty
    def ZHCN(cls):
        return cls("zh-cn")
    
    @schemas.classproperty
    def ZHHK(cls):
        return cls("zh-hk")
    
    @schemas.classproperty
    def ZHSG(cls):
        return cls("zh-sg")
    
    @schemas.classproperty
    def ZHTW(cls):
        return cls("zh-tw")
    
    @schemas.classproperty
    def ZU(cls):
        return cls("zu")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'projectId': typing.Union[ProjectIdSchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
        'locale': typing.Union[LocaleSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_project_id = api_client.PathParameter(
    name="projectId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectIdSchema,
    required=True,
)
request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
request_path_locale = api_client.PathParameter(
    name="locale",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LocaleSchema,
    required=True,
)
_auth = [
    'Project',
]
SchemaFor200ResponseBodyApplicationJson = SmsTemplateSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SmsTemplate


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SmsTemplate


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _reset_sms_template_mapped_args(
        self,
        project_id: str,
        type: str,
        locale: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if project_id is not None:
            _path_params["projectId"] = project_id
        if type is not None:
            _path_params["type"] = type
        if locale is not None:
            _path_params["locale"] = locale
        args.path = _path_params
        return args

    async def _areset_sms_template_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Reset custom SMS template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
            request_path_type,
            request_path_locale,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/projects/{projectId}/templates/sms/{type}/{locale}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _reset_sms_template_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Reset custom SMS template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
            request_path_type,
            request_path_locale,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/projects/{projectId}/templates/sms/{type}/{locale}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class ResetSmsTemplateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def areset_sms_template(
        self,
        project_id: str,
        type: str,
        locale: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._reset_sms_template_mapped_args(
            project_id=project_id,
            type=type,
            locale=locale,
        )
        return await self._areset_sms_template_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def reset_sms_template(
        self,
        project_id: str,
        type: str,
        locale: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._reset_sms_template_mapped_args(
            project_id=project_id,
            type=type,
            locale=locale,
        )
        return self._reset_sms_template_oapg(
            path_params=args.path,
        )

class ResetSmsTemplate(BaseApi):

    async def areset_sms_template(
        self,
        project_id: str,
        type: str,
        locale: str,
        validate: bool = False,
        **kwargs,
    ) -> SmsTemplatePydantic:
        raw_response = await self.raw.areset_sms_template(
            project_id=project_id,
            type=type,
            locale=locale,
            **kwargs,
        )
        if validate:
            return SmsTemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(SmsTemplatePydantic, raw_response.body)
    
    
    def reset_sms_template(
        self,
        project_id: str,
        type: str,
        locale: str,
        validate: bool = False,
    ) -> SmsTemplatePydantic:
        raw_response = self.raw.reset_sms_template(
            project_id=project_id,
            type=type,
            locale=locale,
        )
        if validate:
            return SmsTemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(SmsTemplatePydantic, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        project_id: str,
        type: str,
        locale: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._reset_sms_template_mapped_args(
            project_id=project_id,
            type=type,
            locale=locale,
        )
        return await self._areset_sms_template_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        project_id: str,
        type: str,
        locale: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._reset_sms_template_mapped_args(
            project_id=project_id,
            type=type,
            locale=locale,
        )
        return self._reset_sms_template_oapg(
            path_params=args.path,
        )

