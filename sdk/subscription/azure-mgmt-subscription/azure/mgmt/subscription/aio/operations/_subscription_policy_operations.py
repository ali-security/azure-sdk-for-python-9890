# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from ...operations._subscription_policy_operations import (
    build_add_update_policy_for_tenant_request,
    build_get_policy_for_tenant_request,
    build_list_policy_for_tenant_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SubscriptionPolicyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.subscription.aio.SubscriptionClient`'s
        :attr:`subscription_policy` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def add_update_policy_for_tenant(
        self, body: _models.PutTenantPolicyRequestProperties, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.GetTenantPolicyResponse:
        """Create or Update Subscription tenant policy for user's tenant.

        :param body: Required.
        :type body: ~azure.mgmt.subscription.models.PutTenantPolicyRequestProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetTenantPolicyResponse or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.GetTenantPolicyResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def add_update_policy_for_tenant(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.GetTenantPolicyResponse:
        """Create or Update Subscription tenant policy for user's tenant.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetTenantPolicyResponse or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.GetTenantPolicyResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def add_update_policy_for_tenant(
        self, body: Union[_models.PutTenantPolicyRequestProperties, IO], **kwargs: Any
    ) -> _models.GetTenantPolicyResponse:
        """Create or Update Subscription tenant policy for user's tenant.

        :param body: Is either a model type or a IO type. Required.
        :type body: ~azure.mgmt.subscription.models.PutTenantPolicyRequestProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetTenantPolicyResponse or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.GetTenantPolicyResponse
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

        api_version: Literal["2021-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.GetTenantPolicyResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "PutTenantPolicyRequestProperties")

        request = build_add_update_policy_for_tenant_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.add_update_policy_for_tenant.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GetTenantPolicyResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_update_policy_for_tenant.metadata = {"url": "/providers/Microsoft.Subscription/policies/default"}

    @distributed_trace_async
    async def get_policy_for_tenant(self, **kwargs: Any) -> _models.GetTenantPolicyResponse:
        """Get the subscription tenant policy for the user's tenant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetTenantPolicyResponse or the result of cls(response)
        :rtype: ~azure.mgmt.subscription.models.GetTenantPolicyResponse
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

        api_version: Literal["2021-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
        cls: ClsType[_models.GetTenantPolicyResponse] = kwargs.pop("cls", None)

        request = build_get_policy_for_tenant_request(
            api_version=api_version,
            template_url=self.get_policy_for_tenant.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GetTenantPolicyResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_policy_for_tenant.metadata = {"url": "/providers/Microsoft.Subscription/policies/default"}

    @distributed_trace
    def list_policy_for_tenant(self, **kwargs: Any) -> AsyncIterable["_models.GetTenantPolicyResponse"]:
        """Get the subscription tenant policy for the user's tenant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GetTenantPolicyResponse or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.subscription.models.GetTenantPolicyResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
        cls: ClsType[_models.GetTenantPolicyListResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_policy_for_tenant_request(
                    api_version=api_version,
                    template_url=self.list_policy_for_tenant.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("GetTenantPolicyListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_policy_for_tenant.metadata = {"url": "/providers/Microsoft.Subscription/policies"}
