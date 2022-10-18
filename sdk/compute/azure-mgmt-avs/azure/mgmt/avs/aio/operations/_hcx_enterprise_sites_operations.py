# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._hcx_enterprise_sites_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HcxEnterpriseSitesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.avs.aio.AVSClient`'s
        :attr:`hcx_enterprise_sites` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, private_cloud_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.HcxEnterpriseSite"]:
        """List HCX Enterprise Sites in a private cloud.

        List HCX Enterprise Sites in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either HcxEnterpriseSite or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.avs.models.HcxEnterpriseSite]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.HcxEnterpriseSiteList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    private_cloud_name=private_cloud_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

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
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("HcxEnterpriseSiteList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/hcxEnterpriseSites"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, private_cloud_name: str, hcx_enterprise_site_name: str, **kwargs: Any
    ) -> _models.HcxEnterpriseSite:
        """Get an HCX Enterprise Site by name in a private cloud.

        Get an HCX Enterprise Site by name in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud.
         Required.
        :type hcx_enterprise_site_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HcxEnterpriseSite or the result of cls(response)
        :rtype: ~azure.mgmt.avs.models.HcxEnterpriseSite
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.HcxEnterpriseSite]

        request = build_get_request(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            hcx_enterprise_site_name=hcx_enterprise_site_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("HcxEnterpriseSite", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        hcx_enterprise_site_name: str,
        hcx_enterprise_site: _models.HcxEnterpriseSite,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.HcxEnterpriseSite:
        """Create or update an HCX Enterprise Site in a private cloud.

        Create or update an HCX Enterprise Site in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: The name of the private cloud. Required.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud.
         Required.
        :type hcx_enterprise_site_name: str
        :param hcx_enterprise_site: The HCX Enterprise Site. Required.
        :type hcx_enterprise_site: ~azure.mgmt.avs.models.HcxEnterpriseSite
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HcxEnterpriseSite or the result of cls(response)
        :rtype: ~azure.mgmt.avs.models.HcxEnterpriseSite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        hcx_enterprise_site_name: str,
        hcx_enterprise_site: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.HcxEnterpriseSite:
        """Create or update an HCX Enterprise Site in a private cloud.

        Create or update an HCX Enterprise Site in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: The name of the private cloud. Required.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud.
         Required.
        :type hcx_enterprise_site_name: str
        :param hcx_enterprise_site: The HCX Enterprise Site. Required.
        :type hcx_enterprise_site: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HcxEnterpriseSite or the result of cls(response)
        :rtype: ~azure.mgmt.avs.models.HcxEnterpriseSite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        hcx_enterprise_site_name: str,
        hcx_enterprise_site: Union[_models.HcxEnterpriseSite, IO],
        **kwargs: Any
    ) -> _models.HcxEnterpriseSite:
        """Create or update an HCX Enterprise Site in a private cloud.

        Create or update an HCX Enterprise Site in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: The name of the private cloud. Required.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud.
         Required.
        :type hcx_enterprise_site_name: str
        :param hcx_enterprise_site: The HCX Enterprise Site. Is either a model type or a IO type.
         Required.
        :type hcx_enterprise_site: ~azure.mgmt.avs.models.HcxEnterpriseSite or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HcxEnterpriseSite or the result of cls(response)
        :rtype: ~azure.mgmt.avs.models.HcxEnterpriseSite
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.HcxEnterpriseSite]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(hcx_enterprise_site, (IO, bytes)):
            _content = hcx_enterprise_site
        else:
            _json = self._serialize.body(hcx_enterprise_site, "HcxEnterpriseSite")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            hcx_enterprise_site_name=hcx_enterprise_site_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("HcxEnterpriseSite", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("HcxEnterpriseSite", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, private_cloud_name: str, hcx_enterprise_site_name: str, **kwargs: Any
    ) -> None:
        """Delete an HCX Enterprise Site in a private cloud.

        Delete an HCX Enterprise Site in a private cloud.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud.
         Required.
        :type hcx_enterprise_site_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            hcx_enterprise_site_name=hcx_enterprise_site_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}"}  # type: ignore
