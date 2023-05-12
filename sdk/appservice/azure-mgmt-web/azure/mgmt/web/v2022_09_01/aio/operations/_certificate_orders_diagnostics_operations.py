# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import sys
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._certificate_orders_diagnostics_operations import (
    build_get_app_service_certificate_order_detector_response_request,
    build_list_app_service_certificate_order_detector_response_request,
)
from .._vendor import WebSiteManagementClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CertificateOrdersDiagnosticsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.web.v2022_09_01.aio.WebSiteManagementClient`'s
        :attr:`certificate_orders_diagnostics` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_app_service_certificate_order_detector_response(
        self, resource_group_name: str, certificate_order_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.DetectorResponse"]:
        """Microsoft.CertificateRegistration to get the list of detectors for this RP.

        Description for Microsoft.CertificateRegistration to get the list of detectors for this RP.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param certificate_order_name: The certificate order name for which the response is needed.
         Required.
        :type certificate_order_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DetectorResponse or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.web.v2022_09_01.models.DetectorResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
        cls: ClsType[_models.DetectorResponseCollection] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_app_service_certificate_order_detector_response_request(
                    resource_group_name=resource_group_name,
                    certificate_order_name=certificate_order_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_app_service_certificate_order_detector_response.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DetectorResponseCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_app_service_certificate_order_detector_response.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/detectors"
    }

    @distributed_trace_async
    async def get_app_service_certificate_order_detector_response(
        self,
        resource_group_name: str,
        certificate_order_name: str,
        detector_name: str,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        time_grain: Optional[str] = None,
        **kwargs: Any
    ) -> _models.DetectorResponse:
        """Microsoft.CertificateRegistration call to get a detector response from App Lens.

        Description for Microsoft.CertificateRegistration call to get a detector response from App
        Lens.

        :param resource_group_name: Name of the resource group to which the resource belongs. Required.
        :type resource_group_name: str
        :param certificate_order_name: The certificate order name for which the response is needed.
         Required.
        :type certificate_order_name: str
        :param detector_name: The detector name which needs to be run. Required.
        :type detector_name: str
        :param start_time: The start time for detector response. Default value is None.
        :type start_time: ~datetime.datetime
        :param end_time: The end time for the detector response. Default value is None.
        :type end_time: ~datetime.datetime
        :param time_grain: The time grain for the detector response. Default value is None.
        :type time_grain: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DetectorResponse or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2022_09_01.models.DetectorResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))
        cls: ClsType[_models.DetectorResponse] = kwargs.pop("cls", None)

        request = build_get_app_service_certificate_order_detector_response_request(
            resource_group_name=resource_group_name,
            certificate_order_name=certificate_order_name,
            detector_name=detector_name,
            subscription_id=self._config.subscription_id,
            start_time=start_time,
            end_time=end_time,
            time_grain=time_grain,
            api_version=api_version,
            template_url=self.get_app_service_certificate_order_detector_response.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DetectorResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_app_service_certificate_order_detector_response.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/detectors/{detectorName}"
    }
