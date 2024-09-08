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
from typing import Any, Callable, Dict, IO, Iterable, Iterator, Optional, Type, TypeVar, Union, cast, overload
import urllib.parse

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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_savings_plan_order_request(
    billing_account_name: str, savings_plan_order_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_billing_account_request(
    billing_account_name: str,
    *,
    filter: Optional[str] = None,
    order_by: Optional[str] = None,
    skiptoken: Optional[float] = None,
    take: Optional[float] = None,
    selected_state: Optional[str] = None,
    refresh_summary: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlans")
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["filter"] = _SERIALIZER.query("filter", filter, "str")
    if order_by is not None:
        _params["orderBy"] = _SERIALIZER.query("order_by", order_by, "str")
    if skiptoken is not None:
        _params["skiptoken"] = _SERIALIZER.query("skiptoken", skiptoken, "float")
    if take is not None:
        _params["take"] = _SERIALIZER.query("take", take, "float")
    if selected_state is not None:
        _params["selectedState"] = _SERIALIZER.query("selected_state", selected_state, "str")
    if refresh_summary is not None:
        _params["refreshSummary"] = _SERIALIZER.query("refresh_summary", refresh_summary, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_by_billing_account_request(
    billing_account_name: str,
    savings_plan_order_id: str,
    savings_plan_id: str,
    *,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
        "savingsPlanId": _SERIALIZER.url("savings_plan_id", savings_plan_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if expand is not None:
        _params["expand"] = _SERIALIZER.query("expand", expand, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_by_billing_account_request(
    billing_account_name: str, savings_plan_order_id: str, savings_plan_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
        "savingsPlanId": _SERIALIZER.url("savings_plan_id", savings_plan_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_validate_update_by_billing_account_request(  # pylint: disable=name-too-long
    billing_account_name: str, savings_plan_order_id: str, savings_plan_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-04-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}/validate",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountName": _SERIALIZER.url(
            "billing_account_name",
            billing_account_name,
            "str",
            pattern=r"^([0-9]+|([Pp][Cc][Nn]\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
        ),
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
        "savingsPlanId": _SERIALIZER.url("savings_plan_id", savings_plan_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class SavingsPlansOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.billing.BillingManagementClient`'s
        :attr:`savings_plans` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_savings_plan_order(
        self, billing_account_name: str, savings_plan_order_id: str, **kwargs: Any
    ) -> Iterable["_models.SavingsPlanModel"]:
        """List savings plans in an order by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :return: An iterator like instance of either SavingsPlanModel or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SavingsPlanModelList] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_savings_plan_order_request(
                    billing_account_name=billing_account_name,
                    savings_plan_order_id=savings_plan_order_id,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SavingsPlanModelList", pipeline_response)
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
    def list_by_billing_account(
        self,
        billing_account_name: str,
        filter: Optional[str] = None,
        order_by: Optional[str] = None,
        skiptoken: Optional[float] = None,
        take: Optional[float] = None,
        selected_state: Optional[str] = None,
        refresh_summary: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.SavingsPlanModel"]:
        """List savings plans by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param filter: The filter query option allows clients to filter a collection of resources that
         are addressed by a request URL. Default value is None.
        :type filter: str
        :param order_by: The orderby query option allows clients to request resources in a particular
         order. Default value is None.
        :type order_by: str
        :param skiptoken: The number of savings plans to skip from the list before returning results.
         Default value is None.
        :type skiptoken: float
        :param take: The number of savings plans to return. Default value is None.
        :type take: float
        :param selected_state: The selected provisioning state. Default value is None.
        :type selected_state: str
        :param refresh_summary: To indicate whether to refresh the roll up counts of the savings plans
         group by provisioning states. Default value is None.
        :type refresh_summary: str
        :return: An iterator like instance of either SavingsPlanModel or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.billing.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SavingsPlanModelListResult] = kwargs.pop("cls", None)

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
                    take=take,
                    selected_state=selected_state,
                    refresh_summary=refresh_summary,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SavingsPlanModelListResult", pipeline_response)
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
    def get_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.SavingsPlanModel:
        """Get savings plan by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param expand: May be used to expand the planInformation. Default value is None.
        :type expand: str
        :return: SavingsPlanModel or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.SavingsPlanModel
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
        cls: ClsType[_models.SavingsPlanModel] = kwargs.pop("cls", None)

        _request = build_get_by_billing_account_request(
            billing_account_name=billing_account_name,
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
            expand=expand,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
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

        deserialized = self._deserialize("SavingsPlanModel", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def _update_by_billing_account_initial(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: Union[_models.SavingsPlanUpdateRequest, IO[bytes]],
        **kwargs: Any
    ) -> Iterator[bytes]:
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
        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "SavingsPlanUpdateRequest")

        _request = build_update_by_billing_account_request(
            billing_account_name=billing_account_name,
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                response.read()  # Load the body in memory and close the socket
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
    def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: _models.SavingsPlanUpdateRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.SavingsPlanModel]:
        """Update savings plan by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: ~azure.mgmt.billing.models.SavingsPlanUpdateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either SavingsPlanModel or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.billing.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.SavingsPlanModel]:
        """Update savings plan by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either SavingsPlanModel or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.billing.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: Union[_models.SavingsPlanUpdateRequest, IO[bytes]],
        **kwargs: Any
    ) -> LROPoller[_models.SavingsPlanModel]:
        """Update savings plan by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Is either a
         SavingsPlanUpdateRequest type or a IO[bytes] type. Required.
        :type body: ~azure.mgmt.billing.models.SavingsPlanUpdateRequest or IO[bytes]
        :return: An instance of LROPoller that returns either SavingsPlanModel or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.billing.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SavingsPlanModel] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._update_by_billing_account_initial(
                billing_account_name=billing_account_name,
                savings_plan_order_id=savings_plan_order_id,
                savings_plan_id=savings_plan_id,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("SavingsPlanModel", pipeline_response.http_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.SavingsPlanModel].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.SavingsPlanModel](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @overload
    def validate_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: _models.SavingsPlanUpdateValidateRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: ~azure.mgmt.billing.models.SavingsPlanUpdateValidateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def validate_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def validate_update_by_billing_account(
        self,
        billing_account_name: str,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: Union[_models.SavingsPlanUpdateValidateRequest, IO[bytes]],
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch by billing account.

        :param billing_account_name: The ID that uniquely identifies a billing account. Required.
        :type billing_account_name: str
        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Is either a
         SavingsPlanUpdateValidateRequest type or a IO[bytes] type. Required.
        :type body: ~azure.mgmt.billing.models.SavingsPlanUpdateValidateRequest or IO[bytes]
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billing.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
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
        cls: ClsType[_models.SavingsPlanValidateResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "SavingsPlanUpdateValidateRequest")

        _request = build_validate_update_by_billing_account_request(
            billing_account_name=billing_account_name,
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
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

        deserialized = self._deserialize("SavingsPlanValidateResponse", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
