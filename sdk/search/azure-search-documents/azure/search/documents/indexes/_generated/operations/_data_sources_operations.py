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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_create_or_update_request(
    data_source_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id', None)  # type: Optional[str]
    if_match = kwargs.pop('if_match', None)  # type: Optional[str]
    if_none_match = kwargs.pop('if_none_match', None)  # type: Optional[str]
    skip_indexer_reset_requirement_for_cache = kwargs.pop('skip_indexer_reset_requirement_for_cache', None)  # type: Optional[bool]

    prefer = "return=representation"
    api_version = "2021-04-30-Preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/datasources(\'{dataSourceName}\')')
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if skip_indexer_reset_requirement_for_cache is not None:
        query_parameters['ignoreResetRequirements'] = _SERIALIZER.query("skip_indexer_reset_requirement_for_cache", skip_indexer_reset_requirement_for_cache, 'bool')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if x_ms_client_request_id is not None:
        header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if if_none_match is not None:
        header_parameters['If-None-Match'] = _SERIALIZER.header("if_none_match", if_none_match, 'str')
    header_parameters['Prefer'] = _SERIALIZER.header("prefer", prefer, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    data_source_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id', None)  # type: Optional[str]
    if_match = kwargs.pop('if_match', None)  # type: Optional[str]
    if_none_match = kwargs.pop('if_none_match', None)  # type: Optional[str]

    api_version = "2021-04-30-Preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/datasources(\'{dataSourceName}\')')
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if x_ms_client_request_id is not None:
        header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    if if_match is not None:
        header_parameters['If-Match'] = _SERIALIZER.header("if_match", if_match, 'str')
    if if_none_match is not None:
        header_parameters['If-None-Match'] = _SERIALIZER.header("if_none_match", if_none_match, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    data_source_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id', None)  # type: Optional[str]

    api_version = "2021-04-30-Preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/datasources(\'{dataSourceName}\')')
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if x_ms_client_request_id is not None:
        header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    select = kwargs.pop('select', None)  # type: Optional[str]
    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id', None)  # type: Optional[str]

    api_version = "2021-04-30-Preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/datasources')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if select is not None:
        query_parameters['$select'] = _SERIALIZER.query("select", select, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if x_ms_client_request_id is not None:
        header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id', None)  # type: Optional[str]

    api_version = "2021-04-30-Preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/datasources')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if x_ms_client_request_id is not None:
        header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class DataSourcesOperations(object):
    """DataSourcesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.search.documents.indexes.models
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
    def create_or_update(
        self,
        data_source_name,  # type: str
        data_source,  # type: "_models.SearchIndexerDataSource"
        if_match=None,  # type: Optional[str]
        if_none_match=None,  # type: Optional[str]
        skip_indexer_reset_requirement_for_cache=None,  # type: Optional[bool]
        request_options=None,  # type: Optional["_models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SearchIndexerDataSource"
        """Creates a new datasource or updates a datasource if it already exists.

        :param data_source_name: The name of the datasource to create or update.
        :type data_source_name: str
        :param data_source: The definition of the datasource to create or update.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param skip_indexer_reset_requirement_for_cache: Ignores cache reset requirements.
        :type skip_indexer_reset_requirement_for_cache: bool
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndexerDataSource, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SearchIndexerDataSource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        json = self._serialize.body(data_source, 'SearchIndexerDataSource')

        request = build_create_or_update_request(
            data_source_name=data_source_name,
            content_type=content_type,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            skip_indexer_reset_requirement_for_cache=skip_indexer_reset_requirement_for_cache,
            json=json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('SearchIndexerDataSource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SearchIndexerDataSource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/datasources(\'{dataSourceName}\')'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        data_source_name,  # type: str
        if_match=None,  # type: Optional[str]
        if_none_match=None,  # type: Optional[str]
        request_options=None,  # type: Optional["_models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a datasource.

        :param data_source_name: The name of the datasource to delete.
        :type data_source_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
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

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_delete_request(
            data_source_name=data_source_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/datasources(\'{dataSourceName}\')'}  # type: ignore


    @distributed_trace
    def get(
        self,
        data_source_name,  # type: str
        request_options=None,  # type: Optional["_models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SearchIndexerDataSource"
        """Retrieves a datasource definition.

        :param data_source_name: The name of the datasource to retrieve.
        :type data_source_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndexerDataSource, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SearchIndexerDataSource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_request(
            data_source_name=data_source_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchIndexerDataSource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/datasources(\'{dataSourceName}\')'}  # type: ignore


    @distributed_trace
    def list(
        self,
        select=None,  # type: Optional[str]
        request_options=None,  # type: Optional["_models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ListDataSourcesResult"
        """Lists all datasources available for a search service.

        :param select: Selects which top-level properties of the data sources to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties.
        :type select: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListDataSourcesResult, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ListDataSourcesResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListDataSourcesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_list_request(
            select=select,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ListDataSourcesResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/datasources'}  # type: ignore


    @distributed_trace
    def create(
        self,
        data_source,  # type: "_models.SearchIndexerDataSource"
        request_options=None,  # type: Optional["_models.RequestOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SearchIndexerDataSource"
        """Creates a new datasource.

        :param data_source: The definition of the datasource to create.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndexerDataSource, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SearchIndexerDataSource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        json = self._serialize.body(data_source, 'SearchIndexerDataSource')

        request = build_create_request(
            content_type=content_type,
            x_ms_client_request_id=_x_ms_client_request_id,
            json=json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchIndexerDataSource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/datasources'}  # type: ignore

