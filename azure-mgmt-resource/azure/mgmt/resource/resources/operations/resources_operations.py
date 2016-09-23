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
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class ResourcesOperations(object):
    """ResourcesOperations operations.

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

    def move_resources(
            self, source_resource_group_name, resources=None, target_resource_group=None, custom_headers=None, raw=False, **operation_config):
        """Move resources from one resource group to another. The resources being
        moved should all be in the same resource group.

        :param source_resource_group_name: Source resource group name.
        :type source_resource_group_name: str
        :param resources: The ids of the resources.
        :type resources: list of str
        :param target_resource_group: The target resource group.
        :type target_resource_group: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.ResourcesMoveInfo(resources=resources, target_resource_group=target_resource_group)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/moveResources'
        path_format_arguments = {
            'sourceResourceGroupName': self._serialize.url("source_resource_group_name", source_resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
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

        # Construct body
        body_content = self._serialize.body(parameters, 'ResourcesMoveInfo')

        # Construct and send request
        def long_running_send():

            request = self._client.post(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [202, 204]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def list(
            self, filter=None, expand=None, top=None, custom_headers=None, raw=False, **operation_config):
        """Get all of the resources under a subscription.

        :param filter: The filter to apply on the operation.
        :type filter: str
        :param expand: The $expand query parameter.
        :type expand: str
        :param top: Query parameters. If null is passed returns all resource
         groups.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GenericResourcePaged
         <azure.mgmt.resource.resources.models.GenericResourcePaged>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resources'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
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
        deserialized = models.GenericResourcePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.GenericResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def check_existence(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, custom_headers=None, raw=False, **operation_config):
        """Checks whether resource exists.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: Resource identity.
        :type resource_provider_namespace: str
        :param parent_resource_path: Resource identity.
        :type parent_resource_path: str
        :param resource_type: Resource identity.
        :type resource_type: str
        :param resource_name: Resource identity.
        :type resource_name: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: bool
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204, 404]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = (response.status_code == 204)
        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response
        return deserialized

    def delete(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, custom_headers=None, raw=False, **operation_config):
        """Deletes a resource.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: Resource identity.
        :type resource_provider_namespace: str
        :param parent_resource_path: Resource identity.
        :type parent_resource_path: str
        :param resource_type: Resource identity.
        :type resource_type: str
        :param resource_name: Resource identity.
        :type resource_name: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.delete(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 204, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def create_or_update(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, parameters, custom_headers=None, raw=False, **operation_config):
        """Create a resource.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: Resource identity.
        :type resource_provider_namespace: str
        :param parent_resource_path: Resource identity.
        :type parent_resource_path: str
        :param resource_type: Resource identity.
        :type resource_type: str
        :param resource_name: Resource identity.
        :type resource_name: str
        :param api_version: Api version to use.
        :type api_version: str
        :param parameters: Create or update resource parameters.
        :type parameters: :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'GenericResource')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [201, 200, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 201:
                deserialized = self._deserialize('GenericResource', response)
            if response.status_code == 200:
                deserialized = self._deserialize('GenericResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def get(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, custom_headers=None, raw=False, **operation_config):
        """Returns a resource belonging to a resource group.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: Resource identity.
        :type resource_provider_namespace: str
        :param parent_resource_path: Resource identity.
        :type parent_resource_path: str
        :param resource_type: Resource identity.
        :type resource_type: str
        :param resource_name: Resource identity.
        :type resource_name: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GenericResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def check_existence_by_id(
            self, resource_id, api_version, custom_headers=None, raw=False, **operation_config):
        """Checks whether resource exists.

        :param resource_id: The fully qualified Id of the resource, including
         the resource name and resource type. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite
        :type resource_id: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: bool
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{resourceId}'
        path_format_arguments = {
            'resourceId': self._serialize.url("resource_id", resource_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204, 404]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = (response.status_code == 204)
        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response
        return deserialized

    def delete_by_id(
            self, resource_id, api_version, custom_headers=None, raw=False, **operation_config):
        """Deletes a resource.

        :param resource_id: The fully qualified Id of the resource, including
         the resource name and resource type. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite
        :type resource_id: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{resourceId}'
        path_format_arguments = {
            'resourceId': self._serialize.url("resource_id", resource_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.delete(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 204, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def create_or_update_by_id(
            self, resource_id, api_version, parameters, custom_headers=None, raw=False, **operation_config):
        """Create a resource.

        :param resource_id: The fully qualified Id of the resource, including
         the resource name and resource type. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite
        :type resource_id: str
        :param api_version: Api version to use.
        :type api_version: str
        :param parameters: Create or update resource parameters.
        :type parameters: :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{resourceId}'
        path_format_arguments = {
            'resourceId': self._serialize.url("resource_id", resource_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'GenericResource')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [201, 200, 202]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 201:
                deserialized = self._deserialize('GenericResource', response)
            if response.status_code == 200:
                deserialized = self._deserialize('GenericResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def get_by_id(
            self, resource_id, api_version, custom_headers=None, raw=False, **operation_config):
        """Gets a resource.

        :param resource_id: The fully qualified Id of the resource, including
         the resource name and resource type. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite
        :type resource_id: str
        :param api_version: Api version to use.
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GenericResource
         <azure.mgmt.resource.resources.models.GenericResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{resourceId}'
        path_format_arguments = {
            'resourceId': self._serialize.url("resource_id", resource_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GenericResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
