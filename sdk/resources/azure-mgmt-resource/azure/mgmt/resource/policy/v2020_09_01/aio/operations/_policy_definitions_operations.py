# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicyDefinitionsOperations:
    """PolicyDefinitionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2020_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def create_or_update(
        self,
        policy_definition_name: str,
        parameters: "_models.PolicyDefinition",
        **kwargs: Any
    ) -> "_models.PolicyDefinition":
        """Creates or updates a policy definition in a subscription.

        This operation creates or updates a policy definition in the given subscription with the given
        name.

        :param policy_definition_name: The name of the policy definition to create.
        :type policy_definition_name: str
        :param parameters: The policy definition properties.
        :type parameters: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'PolicyDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def delete(
        self,
        policy_definition_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a policy definition in a subscription.

        This operation deletes the policy definition in the given subscription with the given name.

        :param policy_definition_name: The name of the policy definition to delete.
        :type policy_definition_name: str
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
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def get(
        self,
        policy_definition_name: str,
        **kwargs: Any
    ) -> "_models.PolicyDefinition":
        """Retrieves a policy definition in a subscription.

        This operation retrieves the policy definition in the given subscription with the given name.

        :param policy_definition_name: The name of the policy definition to get.
        :type policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def get_built_in(
        self,
        policy_definition_name: str,
        **kwargs: Any
    ) -> "_models.PolicyDefinition":
        """Retrieves a built-in policy definition.

        This operation retrieves the built-in policy definition with the given name.

        :param policy_definition_name: The name of the built-in policy definition to get.
        :type policy_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.get_built_in.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_built_in.metadata = {'url': '/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def create_or_update_at_management_group(
        self,
        policy_definition_name: str,
        management_group_id: str,
        parameters: "_models.PolicyDefinition",
        **kwargs: Any
    ) -> "_models.PolicyDefinition":
        """Creates or updates a policy definition in a management group.

        This operation creates or updates a policy definition in the given management group with the
        given name.

        :param policy_definition_name: The name of the policy definition to create.
        :type policy_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :param parameters: The policy definition properties.
        :type parameters: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update_at_management_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'PolicyDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def delete_at_management_group(
        self,
        policy_definition_name: str,
        management_group_id: str,
        **kwargs: Any
    ) -> None:
        """Deletes a policy definition in a management group.

        This operation deletes the policy definition in the given management group with the given name.

        :param policy_definition_name: The name of the policy definition to delete.
        :type policy_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
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
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.delete_at_management_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    async def get_at_management_group(
        self,
        policy_definition_name: str,
        management_group_id: str,
        **kwargs: Any
    ) -> "_models.PolicyDefinition":
        """Retrieve a policy definition in a management group.

        This operation retrieves the policy definition in the given management group with the given
        name.

        :param policy_definition_name: The name of the policy definition to get.
        :type policy_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        # Construct URL
        url = self.get_at_management_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyDefinitionName': self._serialize.url("policy_definition_name", policy_definition_name, 'str'),
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}'}  # type: ignore

    def list(
        self,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyDefinitionListResult"]:
        """Retrieves policy definitions in a subscription.

        This operation retrieves a list of all the policy definitions in a given subscription that
        match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType
        -eq {value}' or 'category eq '{value}''. If $filter is not provided, the unfiltered list
        includes all policy definitions associated with the subscription, including those that apply
        directly or from management groups that contain the given subscription. If
        $filter=atExactScope() is provided, the returned list only includes all policy definitions that
        at the given subscription. If $filter='policyType -eq {value}' is provided, the returned list
        only includes all policy definitions whose type match the {value}. Possible policyType values
        are NotSpecified, BuiltIn, Custom, and Static. If $filter='category -eq {value}' is provided,
        the returned list only includes all policy definitions whose category match the {value}.

        :param filter: The filter to apply on the operation. Valid values for $filter are:
         'atExactScope()', 'policyType -eq {value}' or 'category eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter=atExactScope() is provided, the returned list
         only includes all policy definitions that at the given scope. If $filter='policyType -eq
         {value}' is provided, the returned list only includes all policy definitions whose type match
         the {value}. Possible policyType values are NotSpecified, BuiltIn, Custom, and Static. If
         $filter='category -eq {value}' is provided, the returned list only includes all policy
         definitions whose category match the {value}.
        :type filter: str
        :param top: Maximum number of records to return. When the $top filter is not provided, it will
         return 500 records.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyDefinitionListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PolicyDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions'}  # type: ignore

    def list_built_in(
        self,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyDefinitionListResult"]:
        """Retrieve built-in policy definitions.

        This operation retrieves a list of all the built-in policy definitions that match the optional
        given $filter. If $filter='policyType -eq {value}' is provided, the returned list only includes
        all built-in policy definitions whose type match the {value}. Possible policyType values are
        NotSpecified, BuiltIn, Custom, and Static. If $filter='category -eq {value}' is provided, the
        returned list only includes all built-in policy definitions whose category match the {value}.

        :param filter: The filter to apply on the operation. Valid values for $filter are:
         'atExactScope()', 'policyType -eq {value}' or 'category eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter=atExactScope() is provided, the returned list
         only includes all policy definitions that at the given scope. If $filter='policyType -eq
         {value}' is provided, the returned list only includes all policy definitions whose type match
         the {value}. Possible policyType values are NotSpecified, BuiltIn, Custom, and Static. If
         $filter='category -eq {value}' is provided, the returned list only includes all policy
         definitions whose category match the {value}.
        :type filter: str
        :param top: Maximum number of records to return. When the $top filter is not provided, it will
         return 500 records.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyDefinitionListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_built_in.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PolicyDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_built_in.metadata = {'url': '/providers/Microsoft.Authorization/policyDefinitions'}  # type: ignore

    def list_by_management_group(
        self,
        management_group_id: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyDefinitionListResult"]:
        """Retrieve policy definitions in a management group.

        This operation retrieves a list of all the policy definitions in a given management group that
        match the optional given $filter. Valid values for $filter are: 'atExactScope()', 'policyType
        -eq {value}' or 'category eq '{value}''. If $filter is not provided, the unfiltered list
        includes all policy definitions associated with the management group, including those that
        apply directly or from management groups that contain the given management group. If
        $filter=atExactScope() is provided, the returned list only includes all policy definitions that
        at the given management group. If $filter='policyType -eq {value}' is provided, the returned
        list only includes all policy definitions whose type match the {value}. Possible policyType
        values are NotSpecified, BuiltIn, Custom, and Static. If $filter='category -eq {value}' is
        provided, the returned list only includes all policy definitions whose category match the
        {value}.

        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :param filter: The filter to apply on the operation. Valid values for $filter are:
         'atExactScope()', 'policyType -eq {value}' or 'category eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter=atExactScope() is provided, the returned list
         only includes all policy definitions that at the given scope. If $filter='policyType -eq
         {value}' is provided, the returned list only includes all policy definitions whose type match
         the {value}. Possible policyType values are NotSpecified, BuiltIn, Custom, and Static. If
         $filter='category -eq {value}' is provided, the returned list only includes all policy
         definitions whose category match the {value}.
        :type filter: str
        :param top: Maximum number of records to return. When the $top filter is not provided, it will
         return 500 records.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyDefinitionListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-09-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_management_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PolicyDefinitionListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_management_group.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/policyDefinitions'}  # type: ignore
