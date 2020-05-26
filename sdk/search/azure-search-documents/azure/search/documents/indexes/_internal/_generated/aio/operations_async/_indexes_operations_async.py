# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IndexesOperations:
    """IndexesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.search.documents.indexes.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create(
        self,
        index: "models.SearchIndex",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SearchIndex":
        """Creates a new search index.

        :param index: The definition of the index to create.
        :type index: ~azure.search.documents.indexes.models.SearchIndex
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndex
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SearchIndex"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(index, 'SearchIndex')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchIndex', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/indexes'}  # type: ignore

    def list(
        self,
        select: Optional[str] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> AsyncIterable["models.ListIndexesResult"]:
        """Lists all indexes available for a search service.

        :param select: Selects which top-level properties of the index definitions to retrieve.
     Specified as a comma-separated list of JSON property names, or '*' for all properties. The
     default is all properties.
        :type select: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ListIndexesResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.search.documents.indexes.models.ListIndexesResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ListIndexesResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if _x_ms_client_request_id is not None:
                header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListIndexesResult', pipeline_response)
            list_of_elem = deserialized.indexes
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.SearchError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/indexes'}  # type: ignore

    async def create_or_update(
        self,
        index_name: str,
        index: "models.SearchIndex",
        allow_index_downtime: Optional[bool] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SearchIndex":
        """Creates a new search index or updates an index if it already exists.

        :param index_name: The definition of the index to create or update.
        :type index_name: str
        :param index: The definition of the index to create or update.
        :type index: ~azure.search.documents.indexes.models.SearchIndex
        :param allow_index_downtime: Allows new analyzers, tokenizers, token filters, or char filters
         to be added to an index by taking the index offline for at least a few seconds. This
         temporarily causes indexing and query requests to fail. Performance and write availability of
         the index can be impaired for several minutes after the index is updated, or longer for very
         large indexes.
        :type allow_index_downtime: bool
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndex
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SearchIndex"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        prefer = "return=representation"
        api_version = "2019-05-06-Preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("index_name", index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if allow_index_downtime is not None:
            query_parameters['allowIndexDowntime'] = self._serialize.query("allow_index_downtime", allow_index_downtime, 'bool')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Prefer'] = self._serialize.header("prefer", prefer, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(index, 'SearchIndex')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SearchIndex', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SearchIndex', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/indexes(\'{indexName}\')'}  # type: ignore

    async def delete(
        self,
        index_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> None:
        """Deletes a search index and all the documents it contains. This operation is permanent, with no recovery option. Make sure you have a master copy of your index definition, data ingestion code, and a backup of the primary data source in case you need to re-build the index.

        :param index_name: The name of the index to delete.
        :type index_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value.
        :type if_none_match: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("index_name", index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/indexes(\'{indexName}\')'}  # type: ignore

    async def get(
        self,
        index_name: str,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.SearchIndex":
        """Retrieves an index definition.

        :param index_name: The name of the index to retrieve.
        :type index_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchIndex or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndex
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SearchIndex"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("index_name", index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchIndex', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/indexes(\'{indexName}\')'}  # type: ignore

    async def get_statistics(
        self,
        index_name: str,
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.GetIndexStatisticsResult":
        """Returns statistics for the given index, including a document count and storage usage.

        :param index_name: The name of the index for which to retrieve statistics.
        :type index_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetIndexStatisticsResult or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.GetIndexStatisticsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.GetIndexStatisticsResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"

        # Construct URL
        url = self.get_statistics.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("index_name", index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('GetIndexStatisticsResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_statistics.metadata = {'url': '/indexes(\'{indexName}\')/search.stats'}  # type: ignore

    async def analyze(
        self,
        index_name: str,
        request: "models.AnalyzeRequest",
        request_options: Optional["models.RequestOptions"] = None,
        **kwargs
    ) -> "models.AnalyzeResult":
        """Shows how an analyzer breaks text into tokens.

        :param index_name: The name of the index for which to test an analyzer.
        :type index_name: str
        :param request: The text and analyzer or analysis components to test.
        :type request: ~azure.search.documents.indexes.models.AnalyzeRequest
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeResult or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.AnalyzeResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AnalyzeResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        api_version = "2019-05-06-Preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.analyze.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'indexName': self._serialize.url("index_name", index_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _x_ms_client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", _x_ms_client_request_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(request, 'AnalyzeRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.SearchError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AnalyzeResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    analyze.metadata = {'url': '/indexes(\'{indexName}\')/search.analyze'}  # type: ignore
