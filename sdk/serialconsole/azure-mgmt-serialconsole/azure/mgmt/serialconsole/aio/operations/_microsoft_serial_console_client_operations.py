# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MicrosoftSerialConsoleClientOperationsMixin:

    async def list_operations(
        self,
        **kwargs
    ) -> "_models.SerialConsoleOperations":
        """Gets a list of Serial Console API operations.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SerialConsoleOperations, or the result of cls(response)
        :rtype: ~azure.mgmt.serialconsole.models.SerialConsoleOperations
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SerialConsoleOperations"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"

        # Construct URL
        url = self.list_operations.metadata['url']  # type: ignore

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

        deserialized = self._deserialize('SerialConsoleOperations', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_operations.metadata = {'url': '/providers/Microsoft.SerialConsole/operations'}  # type: ignore

    async def get_console_status(
        self,
        default: str,
        **kwargs
    ) -> Union["_models.SerialConsoleStatus", "_models.GetSerialConsoleSubscriptionNotFound"]:
        """Get the disabled status for a subscription.

        Gets whether or not Serial Console is disabled for a given subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SerialConsoleStatus or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~azure.mgmt.serialconsole.models.SerialConsoleStatus or ~azure.mgmt.serialconsole.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.SerialConsoleStatus", "_models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"

        # Construct URL
        url = self.get_console_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
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

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('SerialConsoleStatus', pipeline_response)

        if response.status_code == 404:
            deserialized = self._deserialize('GetSerialConsoleSubscriptionNotFound', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_console_status.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}'}  # type: ignore

    async def disable_console(
        self,
        default: str,
        **kwargs
    ) -> Union["_models.DisableSerialConsoleResult", "_models.GetSerialConsoleSubscriptionNotFound"]:
        """Disable Serial Console for a subscription.

        Disables the Serial Console service for all VMs and VM scale sets in the provided subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DisableSerialConsoleResult or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~azure.mgmt.serialconsole.models.DisableSerialConsoleResult or ~azure.mgmt.serialconsole.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.DisableSerialConsoleResult", "_models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"

        # Construct URL
        url = self.disable_console.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('DisableSerialConsoleResult', pipeline_response)

        if response.status_code == 404:
            deserialized = self._deserialize('GetSerialConsoleSubscriptionNotFound', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    disable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/disableConsole'}  # type: ignore

    async def enable_console(
        self,
        default: str,
        **kwargs
    ) -> Union["_models.EnableSerialConsoleResult", "_models.GetSerialConsoleSubscriptionNotFound"]:
        """Enable Serial Console for a subscription.

        Enables the Serial Console service for all VMs and VM scale sets in the provided subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EnableSerialConsoleResult or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~azure.mgmt.serialconsole.models.EnableSerialConsoleResult or ~azure.mgmt.serialconsole.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.EnableSerialConsoleResult", "_models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"

        # Construct URL
        url = self.enable_console.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('EnableSerialConsoleResult', pipeline_response)

        if response.status_code == 404:
            deserialized = self._deserialize('GetSerialConsoleSubscriptionNotFound', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    enable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/enableConsole'}  # type: ignore
