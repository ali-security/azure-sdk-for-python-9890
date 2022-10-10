# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union

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
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_query_results_for_management_group_request(
    management_group_name: str,
    policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    management_groups_namespace = kwargs.pop("management_groups_namespace", "Microsoft.Management")  # type: str
    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupsNamespace": _SERIALIZER.url("management_groups_namespace", management_groups_namespace, "str"),
        "managementGroupName": _SERIALIZER.url("management_group_name", management_group_name, "str"),
        "policyTrackedResourcesResource": _SERIALIZER.url(
            "policy_tracked_resources_resource", policy_tracked_resources_resource, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=0)
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_query_results_for_subscription_request(
    policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
    subscription_id: str,
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "policyTrackedResourcesResource": _SERIALIZER.url(
            "policy_tracked_resources_resource", policy_tracked_resources_resource, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=0)
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_query_results_for_resource_group_request(
    resource_group_name: str,
    policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
    subscription_id: str,
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "policyTrackedResourcesResource": _SERIALIZER.url(
            "policy_tracked_resources_resource", policy_tracked_resources_resource, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=0)
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_query_results_for_resource_request(
    resource_id: str,
    policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{resourceId}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceId": _SERIALIZER.url("resource_id", resource_id, "str", skip_quote=True),
        "policyTrackedResourcesResource": _SERIALIZER.url(
            "policy_tracked_resources_resource", policy_tracked_resources_resource, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", minimum=0)
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class PolicyTrackedResourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.policyinsights.PolicyInsightsClient`'s
        :attr:`policy_tracked_resources` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_query_results_for_management_group(
        self,
        management_group_name: str,
        policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
        query_options: Optional[_models.QueryOptions] = None,
        **kwargs: Any
    ) -> Iterable["_models.PolicyTrackedResource"]:
        """Queries policy tracked resources under the management group.

        :param management_group_name: Management group name. Required.
        :type management_group_name: str
        :param policy_tracked_resources_resource: The name of the virtual resource under
         PolicyTrackedResources resource type; only "default" is allowed. "default" Required.
        :type policy_tracked_resources_resource: str or
         ~azure.mgmt.policyinsights.models.PolicyTrackedResourcesResourceType
        :param query_options: Parameter group. Default value is None.
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :keyword management_groups_namespace: The namespace for Microsoft Management RP; only
         "Microsoft.Management" is allowed. Default value is "Microsoft.Management". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype management_groups_namespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyTrackedResource or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.policyinsights.models.PolicyTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        management_groups_namespace = kwargs.pop("management_groups_namespace", "Microsoft.Management")  # type: str
        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyTrackedResourcesQueryResults]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _top = None
                _filter = None
                if query_options is not None:
                    _filter = query_options.filter
                    _top = query_options.top

                request = build_list_query_results_for_management_group_request(
                    management_group_name=management_group_name,
                    policy_tracked_resources_resource=policy_tracked_resources_resource,
                    top=_top,
                    filter=_filter,
                    management_groups_namespace=management_groups_namespace,
                    api_version=api_version,
                    template_url=self.list_query_results_for_management_group.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyTrackedResourcesQueryResults", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.QueryFailure, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_query_results_for_management_group.metadata = {"url": "/providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults"}  # type: ignore

    @distributed_trace
    def list_query_results_for_subscription(
        self,
        policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
        query_options: Optional[_models.QueryOptions] = None,
        **kwargs: Any
    ) -> Iterable["_models.PolicyTrackedResource"]:
        """Queries policy tracked resources under the subscription.

        :param policy_tracked_resources_resource: The name of the virtual resource under
         PolicyTrackedResources resource type; only "default" is allowed. "default" Required.
        :type policy_tracked_resources_resource: str or
         ~azure.mgmt.policyinsights.models.PolicyTrackedResourcesResourceType
        :param query_options: Parameter group. Default value is None.
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyTrackedResource or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.policyinsights.models.PolicyTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyTrackedResourcesQueryResults]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _top = None
                _filter = None
                if query_options is not None:
                    _filter = query_options.filter
                    _top = query_options.top

                request = build_list_query_results_for_subscription_request(
                    policy_tracked_resources_resource=policy_tracked_resources_resource,
                    subscription_id=self._config.subscription_id,
                    top=_top,
                    filter=_filter,
                    api_version=api_version,
                    template_url=self.list_query_results_for_subscription.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyTrackedResourcesQueryResults", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.QueryFailure, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_query_results_for_subscription.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults"}  # type: ignore

    @distributed_trace
    def list_query_results_for_resource_group(
        self,
        resource_group_name: str,
        policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
        query_options: Optional[_models.QueryOptions] = None,
        **kwargs: Any
    ) -> Iterable["_models.PolicyTrackedResource"]:
        """Queries policy tracked resources under the resource group.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param policy_tracked_resources_resource: The name of the virtual resource under
         PolicyTrackedResources resource type; only "default" is allowed. "default" Required.
        :type policy_tracked_resources_resource: str or
         ~azure.mgmt.policyinsights.models.PolicyTrackedResourcesResourceType
        :param query_options: Parameter group. Default value is None.
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyTrackedResource or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.policyinsights.models.PolicyTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyTrackedResourcesQueryResults]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _top = None
                _filter = None
                if query_options is not None:
                    _filter = query_options.filter
                    _top = query_options.top

                request = build_list_query_results_for_resource_group_request(
                    resource_group_name=resource_group_name,
                    policy_tracked_resources_resource=policy_tracked_resources_resource,
                    subscription_id=self._config.subscription_id,
                    top=_top,
                    filter=_filter,
                    api_version=api_version,
                    template_url=self.list_query_results_for_resource_group.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyTrackedResourcesQueryResults", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.QueryFailure, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_query_results_for_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults"}  # type: ignore

    @distributed_trace
    def list_query_results_for_resource(
        self,
        resource_id: str,
        policy_tracked_resources_resource: Union[str, _models.PolicyTrackedResourcesResourceType],
        query_options: Optional[_models.QueryOptions] = None,
        **kwargs: Any
    ) -> Iterable["_models.PolicyTrackedResource"]:
        """Queries policy tracked resources under the resource.

        :param resource_id: Resource ID. Required.
        :type resource_id: str
        :param policy_tracked_resources_resource: The name of the virtual resource under
         PolicyTrackedResources resource type; only "default" is allowed. "default" Required.
        :type policy_tracked_resources_resource: str or
         ~azure.mgmt.policyinsights.models.PolicyTrackedResourcesResourceType
        :param query_options: Parameter group. Default value is None.
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyTrackedResource or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.policyinsights.models.PolicyTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-07-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PolicyTrackedResourcesQueryResults]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _top = None
                _filter = None
                if query_options is not None:
                    _filter = query_options.filter
                    _top = query_options.top

                request = build_list_query_results_for_resource_request(
                    resource_id=resource_id,
                    policy_tracked_resources_resource=policy_tracked_resources_resource,
                    top=_top,
                    filter=_filter,
                    api_version=api_version,
                    template_url=self.list_query_results_for_resource.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyTrackedResourcesQueryResults", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.QueryFailure, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_query_results_for_resource.metadata = {"url": "/{resourceId}/providers/Microsoft.PolicyInsights/policyTrackedResources/{policyTrackedResourcesResource}/queryResults"}  # type: ignore
