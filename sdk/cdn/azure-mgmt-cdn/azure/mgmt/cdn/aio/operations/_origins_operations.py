# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._origins_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_endpoint_request,
    build_update_request,
)
from .._vendor import CdnManagementClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class OriginsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.cdn.aio.CdnManagementClient`'s
        :attr:`origins` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_endpoint(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.Origin"]:
        """Lists all of the existing origins within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :return: An iterator like instance of either Origin or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.OriginListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_endpoint_request(
                    resource_group_name=resource_group_name,
                    profile_name=profile_name,
                    endpoint_name=endpoint_name,
                    subscription_id=self._config.subscription_id,
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OriginListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, origin_name: str, **kwargs: Any
    ) -> _models.Origin:
        """Gets an existing origin within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin which is unique within the endpoint. Required.
        :type origin_name: str
        :return: Origin or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.Origin
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
        cls: ClsType[_models.Origin] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            origin_name=origin_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Origin", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_initial(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin: Union[_models.Origin, IO[bytes]],
        **kwargs: Any
    ) -> _models.Origin:
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
        cls: ClsType[_models.Origin] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(origin, (IOBase, bytes)):
            _content = origin
        else:
            _json = self._serialize.body(origin, "Origin")

        _request = build_create_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            origin_name=origin_name,
            subscription_id=self._config.subscription_id,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("Origin", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Origin", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

            deserialized = self._deserialize("Origin", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin: _models.Origin,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Creates a new origin within the specified endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin that is unique within the endpoint. Required.
        :type origin_name: str
        :param origin: Origin properties. Required.
        :type origin: ~azure.mgmt.cdn.models.Origin
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Creates a new origin within the specified endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin that is unique within the endpoint. Required.
        :type origin_name: str
        :param origin: Origin properties. Required.
        :type origin: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin: Union[_models.Origin, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Creates a new origin within the specified endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin that is unique within the endpoint. Required.
        :type origin_name: str
        :param origin: Origin properties. Is either a Origin type or a IO[bytes] type. Required.
        :type origin: ~azure.mgmt.cdn.models.Origin or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Origin] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                origin_name=origin_name,
                origin=origin,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Origin", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Origin].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Origin](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_initial(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin_update_properties: Union[_models.OriginUpdateParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.Origin:
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
        cls: ClsType[_models.Origin] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(origin_update_properties, (IOBase, bytes)):
            _content = origin_update_properties
        else:
            _json = self._serialize.body(origin_update_properties, "OriginUpdateParameters")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            origin_name=origin_name,
            subscription_id=self._config.subscription_id,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("Origin", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

            deserialized = self._deserialize("Origin", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin_update_properties: _models.OriginUpdateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Updates an existing origin within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin which is unique within the endpoint. Required.
        :type origin_name: str
        :param origin_update_properties: Origin properties. Required.
        :type origin_update_properties: ~azure.mgmt.cdn.models.OriginUpdateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin_update_properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Updates an existing origin within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin which is unique within the endpoint. Required.
        :type origin_name: str
        :param origin_update_properties: Origin properties. Required.
        :type origin_update_properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        origin_name: str,
        origin_update_properties: Union[_models.OriginUpdateParameters, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Origin]:
        """Updates an existing origin within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin which is unique within the endpoint. Required.
        :type origin_name: str
        :param origin_update_properties: Origin properties. Is either a OriginUpdateParameters type or
         a IO[bytes] type. Required.
        :type origin_update_properties: ~azure.mgmt.cdn.models.OriginUpdateParameters or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Origin or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Origin]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Origin] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                origin_name=origin_name,
                origin_update_properties=origin_update_properties,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Origin", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Origin].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Origin](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, profile_name: str, endpoint_name: str, origin_name: str, **kwargs: Any
    ) -> None:
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
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            origin_name=origin_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, origin_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes an existing origin within an endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the CDN profile which is unique within the resource group.
         Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param origin_name: Name of the origin which is unique within the endpoint. Required.
        :type origin_name: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                origin_name=origin_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
