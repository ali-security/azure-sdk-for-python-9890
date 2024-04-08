# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import ApiManagementClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_service_request(
    resource_group_name: str,
    service_name: str,
    gateway_id: str,
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/hostnameConfigurations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "gatewayId": _SERIALIZER.url("gateway_id", gateway_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=1)
    if skip is not None:
        _params["$skip"] = _SERIALIZER.query("skip", skip, "int", minimum=0)
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_entity_tag_request(
    resource_group_name: str, service_name: str, gateway_id: str, hc_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/hostnameConfigurations/{hcId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "gatewayId": _SERIALIZER.url("gateway_id", gateway_id, "str", max_length=80, min_length=1),
        "hcId": _SERIALIZER.url("hc_id", hc_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, service_name: str, gateway_id: str, hc_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/hostnameConfigurations/{hcId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "gatewayId": _SERIALIZER.url("gateway_id", gateway_id, "str", max_length=80, min_length=1),
        "hcId": _SERIALIZER.url("hc_id", hc_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    service_name: str,
    gateway_id: str,
    hc_id: str,
    subscription_id: str,
    *,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/hostnameConfigurations/{hcId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "gatewayId": _SERIALIZER.url("gateway_id", gateway_id, "str", max_length=80, min_length=1),
        "hcId": _SERIALIZER.url("hc_id", hc_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    service_name: str,
    gateway_id: str,
    hc_id: str,
    subscription_id: str,
    *,
    if_match: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/gateways/{gatewayId}/hostnameConfigurations/{hcId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "serviceName": _SERIALIZER.url(
            "service_name",
            service_name,
            "str",
            max_length=50,
            min_length=1,
            pattern=r"^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$",
        ),
        "gatewayId": _SERIALIZER.url("gateway_id", gateway_id, "str", max_length=80, min_length=1),
        "hcId": _SERIALIZER.url("hc_id", hc_id, "str", max_length=80, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class GatewayHostnameConfigurationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.apimanagement.ApiManagementClient`'s
        :attr:`gateway_hostname_configuration` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_service(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_id: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.GatewayHostnameConfigurationContract"]:
        """Lists the collection of hostname configurations for the specified gateway.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param filter: |     Field     |     Usage     |     Supported operators     |     Supported
         functions     |</br>|-------------|-------------|-------------|-------------|</br>| name |
         filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>| hostname
         | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |</br>. Default
         value is None.
        :type filter: str
        :param top: Number of records to return. Default value is None.
        :type top: int
        :param skip: Number of records to skip. Default value is None.
        :type skip: int
        :return: An iterator like instance of either GatewayHostnameConfigurationContract or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.GatewayHostnameConfigurationCollection] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_service_request(
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    gateway_id=gateway_id,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    skip=skip,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

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
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("GatewayHostnameConfigurationCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def get_entity_tag(
        self, resource_group_name: str, service_name: str, gateway_id: str, hc_id: str, **kwargs: Any
    ) -> bool:
        """Checks that hostname configuration entity specified by identifier exists for specified Gateway
        entity.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :return: bool or the result of cls(response)
        :rtype: bool
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_get_entity_tag_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_id=gateway_id,
            hc_id=hc_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
        return 200 <= response.status_code <= 299

    @distributed_trace
    def get(
        self, resource_group_name: str, service_name: str, gateway_id: str, hc_id: str, **kwargs: Any
    ) -> _models.GatewayHostnameConfigurationContract:
        """Get details of a hostname configuration.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :return: GatewayHostnameConfigurationContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.GatewayHostnameConfigurationContract] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_id=gateway_id,
            hc_id=hc_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("GatewayHostnameConfigurationContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_id: str,
        hc_id: str,
        parameters: _models.GatewayHostnameConfigurationContract,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GatewayHostnameConfigurationContract:
        """Creates of updates hostname configuration for a Gateway.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :param parameters: Required.
        :type parameters: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: GatewayHostnameConfigurationContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_id: str,
        hc_id: str,
        parameters: IO[bytes],
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GatewayHostnameConfigurationContract:
        """Creates of updates hostname configuration for a Gateway.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :param parameters: Required.
        :type parameters: IO[bytes]
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: GatewayHostnameConfigurationContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_id: str,
        hc_id: str,
        parameters: Union[_models.GatewayHostnameConfigurationContract, IO[bytes]],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.GatewayHostnameConfigurationContract:
        """Creates of updates hostname configuration for a Gateway.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :param parameters: Is either a GatewayHostnameConfigurationContract type or a IO[bytes] type.
         Required.
        :type parameters: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract or
         IO[bytes]
        :param if_match: ETag of the Entity. Not required when creating an entity, but required when
         updating an entity. Default value is None.
        :type if_match: str
        :return: GatewayHostnameConfigurationContract or the result of cls(response)
        :rtype: ~azure.mgmt.apimanagement.models.GatewayHostnameConfigurationContract
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.GatewayHostnameConfigurationContract] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "GatewayHostnameConfigurationContract")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_id=gateway_id,
            hc_id=hc_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("GatewayHostnameConfigurationContract", pipeline_response)

        if response.status_code == 201:
            response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

            deserialized = self._deserialize("GatewayHostnameConfigurationContract", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, service_name: str, gateway_id: str, hc_id: str, if_match: str, **kwargs: Any
    ) -> None:
        """Deletes the specified hostname configuration from the specified Gateway.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param service_name: The name of the API Management service. Required.
        :type service_name: str
        :param gateway_id: Gateway entity identifier. Must be unique in the current API Management
         service instance. Must not have value 'managed'. Required.
        :type gateway_id: str
        :param hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent
         Gateway entity. Required.
        :type hc_id: str
        :param if_match: ETag of the Entity. ETag should match the current entity state from the header
         response of the GET request or it should be * for unconditional update. Required.
        :type if_match: str
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_id=gateway_id,
            hc_id=hc_id,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
