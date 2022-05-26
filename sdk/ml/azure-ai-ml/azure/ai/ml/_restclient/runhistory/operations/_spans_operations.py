# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_post_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    continuation_token_parameter = kwargs.pop('continuation_token_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if continuation_token_parameter is not None:
        query_parameters['continuationToken'] = _SERIALIZER.query("continuation_token_parameter", continuation_token_parameter, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_active_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    continuation_token_parameter = kwargs.pop('continuation_token_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans/active')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if continuation_token_parameter is not None:
        query_parameters['continuationToken'] = _SERIALIZER.query("continuation_token_parameter", continuation_token_parameter, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class SpansOperations(object):
    """SpansOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def post(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        run_id,  # type: str
        body=None,  # type: Optional["_models.RunStatusSpans"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """post.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.RunStatusSpans
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'RunStatusSpans')
        else:
            _json = None

        request = build_post_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            run_id=run_id,
            content_type=content_type,
            json=_json,
            template_url=self.post.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post.metadata = {'url': '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans'}  # type: ignore


    @distributed_trace
    def list(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        run_id,  # type: str
        continuation_token_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.PaginatedSpanDefinition1List"]
        """list.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedSpanDefinition1List or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedSpanDefinition1List]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedSpanDefinition1List"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedSpanDefinition1List", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans'}  # type: ignore

    @distributed_trace
    def get_active(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        run_id,  # type: str
        continuation_token_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.PaginatedSpanDefinition1List"]
        """get_active.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedSpanDefinition1List or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedSpanDefinition1List]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedSpanDefinition1List"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_active_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=self.get_active.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_get_active_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    continuation_token_parameter=continuation_token_parameter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedSpanDefinition1List", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    get_active.metadata = {'url': '/history/v1.0/private/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/spans/active'}  # type: ignore
