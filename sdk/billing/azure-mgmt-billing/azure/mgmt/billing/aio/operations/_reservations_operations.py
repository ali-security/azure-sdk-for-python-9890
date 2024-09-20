# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, AsyncIterator, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ...operations._reservations_operations import (
    build_get_by_reservation_order_request,
    build_list_by_billing_account_request,
    build_list_by_billing_profile_request,
    build_list_by_reservation_order_request,
    build_update_by_billing_account_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ReservationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.billing.aio.BillingManagementClient`'s
        :attr:`reservations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_billing_account(
        self,
        billing_account_name: str,
        filter: Optional[str] = None,
        order_by: Optional[str] = None,
        skiptoken: Optional[float] = None,
        refresh_summary: Optional[str] = None,
        selected_state: Optional[str] = None,
        take: Optional[float] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.Reservation"]:
        """Lists the reservations in the billing account and the roll up counts of reservations group by
        provisioning states.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param filter: The filter query option allows clients to filter a collection of resources that
         are addressed by a request URL. Default value is None.
        :type filter: str
        :param order_by: The orderby query option allows clients to request resources in a particular
         order. Default value is None.
        :type order_by: str
        :param skiptoken: The number of reservations to skip from the list before returning results.
         Default value is None.
        :type skiptoken: float
        :param refresh_summary: To indicate whether to refresh the roll up counts of the reservations
         group by provisioning states. Default value is None.
        :type refresh_summary: str
        :param selected_state: The selected provisioning state. Default value is None.
        :type selected_state: str
        :param take: The number of reservations to return in API response. Default value is None.
        :type take: float
        :return: An iterator like instance of either Reservation or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ReservationsListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_billing_account_request(
                    billing_account_name=billing_account_name,
                    filter=filter,
                    order_by=order_by,
                    skiptoken=skiptoken,
                    refresh_summary=refresh_summary,
                    selected_state=selected_state,
                    take=take,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
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
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationsListResult", pipeline_response)
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

    @distributed_trace
    def list_by_billing_profile(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        filter: Optional[str] = None,
        order_by: Optional[str] = None,
        skiptoken: Optional[float] = None,
        refresh_summary: Optional[str] = None,
        selected_state: Optional[str] = None,
        take: Optional[float] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.Reservation"]:
        """Lists the reservations for a billing profile and the roll up counts of reservations group by
        provisioning state.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing profile. Required.
        :type billing_profile_name: str
        :param filter: The filter query option allows clients to filter a collection of resources that
         are addressed by a request URL. Default value is None.
        :type filter: str
        :param order_by: The orderby query option allows clients to request resources in a particular
         order. Default value is None.
        :type order_by: str
        :param skiptoken: The number of reservations to skip from the list before returning results.
         Default value is None.
        :type skiptoken: float
        :param refresh_summary: To indicate whether to refresh the roll up counts of the reservations
         group by provisioning states. Default value is None.
        :type refresh_summary: str
        :param selected_state: The selected provisioning state. Default value is None.
        :type selected_state: str
        :param take: The number of reservations to return in API response. Default value is None.
        :type take: float
        :return: An iterator like instance of either Reservation or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ReservationsListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_billing_profile_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    filter=filter,
                    order_by=order_by,
                    skiptoken=skiptoken,
                    refresh_summary=refresh_summary,
                    selected_state=selected_state,
                    take=take,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
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
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationsListResult", pipeline_response)
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
    async def get_by_reservation_order(
        self,
        billing_account_name: str,
        reservation_order_id: str,
        reservation_id: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Reservation:
        """Get Reservation details in the billing account.

        Get specific Reservation details in the billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param reservation_order_id: Order Id of the reservation. Required.
        :type reservation_order_id: str
        :param reservation_id: Id of the reservation item. Required.
        :type reservation_id: str
        :param expand: May be used to expand the detail information of some properties. Default value
         is None.
        :type expand: str
        :return: Reservation or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.Reservation
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Reservation] = kwargs.pop("cls", None)

        _request = build_get_by_reservation_order_request(
            billing_account_name=billing_account_name,
            reservation_order_id=reservation_order_id,
            reservation_id=reservation_id,
            expand=expand,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
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

        deserialized = self._deserialize("Reservation", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _update_by_billing_account_initial(
        self,
        billing_account_name: str,
        reservation_order_id: str,
        reservation_id: str,
        body: Union[_models.Patch, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "Patch")

        _request = build_update_by_billing_account_request(
            billing_account_name=billing_account_name,
            reservation_order_id=reservation_order_id,
            reservation_id=reservation_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _decompress = kwargs.pop("decompress", True)
        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.stream_download(self._client._pipeline, decompress=_decompress)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        reservation_order_id: str,
        reservation_id: str,
        body: _models.Patch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Reservation]:
        """Update reservation by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param reservation_order_id: Order Id of the reservation. Required.
        :type reservation_order_id: str
        :param reservation_id: Id of the reservation item. Required.
        :type reservation_id: str
        :param body: Request body for patching a reservation. Required.
        :type body: ~azure.mgmt.billing.models.Patch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Reservation or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        reservation_order_id: str,
        reservation_id: str,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Reservation]:
        """Update reservation by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param reservation_order_id: Order Id of the reservation. Required.
        :type reservation_order_id: str
        :param reservation_id: Id of the reservation item. Required.
        :type reservation_id: str
        :param body: Request body for patching a reservation. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Reservation or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        reservation_order_id: str,
        reservation_id: str,
        body: Union[_models.Patch, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Reservation]:
        """Update reservation by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param reservation_order_id: Order Id of the reservation. Required.
        :type reservation_order_id: str
        :param reservation_id: Id of the reservation item. Required.
        :type reservation_id: str
        :param body: Request body for patching a reservation. Is either a Patch type or a IO[bytes]
         type. Required.
        :type body: ~azure.mgmt.billing.models.Patch or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Reservation or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Reservation] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_by_billing_account_initial(
                billing_account_name=billing_account_name,
                reservation_order_id=reservation_order_id,
                reservation_id=reservation_id,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Reservation", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Reservation].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Reservation](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace
    def list_by_reservation_order(
        self, billing_account_name: str, reservation_order_id: str, **kwargs: Any
    ) -> AsyncIterable["_models.Reservation"]:
        """Get Reservations in a given reservation Order in the billing account.

        List Reservations within a single ReservationOrder in the billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param reservation_order_id: Order Id of the reservation. Required.
        :type reservation_order_id: str
        :return: An iterator like instance of either Reservation or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.billing.models.Reservation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ReservationList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_reservation_order_request(
                    billing_account_name=billing_account_name,
                    reservation_order_id=reservation_order_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
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
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationList", pipeline_response)
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
