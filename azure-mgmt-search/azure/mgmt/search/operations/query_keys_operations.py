# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
import uuid

from .. import models


class QueryKeysOperations(object):
    """QueryKeysOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create(
            self, resource_group_name, search_service_name, name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Generates a new query key for the specified Search service. You can
        create up to 50 query keys per service.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param name: The name of the new query API key.
        :type name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`QueryKey <azure.mgmt.search.models.QueryKey>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/createQueryKey/{name}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('QueryKey', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list_by_search_service(
            self, resource_group_name, search_service_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Returns the list of query API keys for the given Azure Search service.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`QueryKeyPaged
         <azure.mgmt.search.models.QueryKeyPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/listQueryKeys'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.QueryKeyPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.QueryKeyPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_group_name, search_service_name, key, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes the specified query key. Unlike admin keys, query keys are not
        regenerated. The process for regenerating a query key is to delete and
        then recreate it.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param key: The query key to be deleted. Query keys are identified by
         value, not by name.
        :type key: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/deleteQueryKey/{key}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204, 404]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
