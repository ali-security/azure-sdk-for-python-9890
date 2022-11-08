# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_usage_request(scope: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.CostManagement/query")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_usage_by_external_cloud_provider_type_request(
    external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
    external_cloud_provider_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/query",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "externalCloudProviderType": _SERIALIZER.url(
            "external_cloud_provider_type", external_cloud_provider_type, "str"
        ),
        "externalCloudProviderId": _SERIALIZER.url("external_cloud_provider_id", external_cloud_provider_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class QueryOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.costmanagement.CostManagementClient`'s
        :attr:`query` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def usage(
        self, scope: str, parameters: _models.QueryDefinition, *, content_type: str = "application/json", **kwargs: Any
    ) -> Optional[_models.QueryResult]:
        """Query the usage data for scope defined.

        :param scope: The scope associated with query and export operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.QueryDefinition
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def usage(
        self, scope: str, parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> Optional[_models.QueryResult]:
        """Query the usage data for scope defined.

        :param scope: The scope associated with query and export operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def usage(
        self, scope: str, parameters: Union[_models.QueryDefinition, IO], **kwargs: Any
    ) -> Optional[_models.QueryResult]:
        """Query the usage data for scope defined.

        :param scope: The scope associated with query and export operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Is either
         a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.QueryDefinition or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult or None
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[_models.QueryResult]]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "QueryDefinition")

        request = build_usage_request(
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.usage.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("QueryResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    usage.metadata = {"url": "/{scope}/providers/Microsoft.CostManagement/query"}  # type: ignore

    @overload
    def usage_by_external_cloud_provider_type(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: _models.QueryDefinition,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.QueryResult:
        """Query the usage data for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.QueryDefinition
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def usage_by_external_cloud_provider_type(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.QueryResult:
        """Query the usage data for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def usage_by_external_cloud_provider_type(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        parameters: Union[_models.QueryDefinition, IO],
        **kwargs: Any
    ) -> _models.QueryResult:
        """Query the usage data for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation. Is either
         a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.costmanagement.models.QueryDefinition or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.QueryResult
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.QueryResult]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "QueryDefinition")

        request = build_usage_by_external_cloud_provider_type_request(
            external_cloud_provider_type=external_cloud_provider_type,
            external_cloud_provider_id=external_cloud_provider_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.usage_by_external_cloud_provider_type.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("QueryResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    usage_by_external_cloud_provider_type.metadata = {"url": "/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/query"}  # type: ignore
