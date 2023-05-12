# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import build_cancer_profiling_infer_cancer_profile_request
from .._vendor import CancerProfilingClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CancerProfilingClientOperationsMixin(CancerProfilingClientMixinABC):
    async def _infer_cancer_profile_initial(
        self,
        body: Union[_models.OncoPhenotypeData, JSON, IO],
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> Optional[_models.OncoPhenotypeResult]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.OncoPhenotypeResult]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_cancer_profiling_infer_cancer_profile_request(
            repeatability_request_id=repeatability_request_id,
            repeatability_first_sent=repeatability_first_sent,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = _deserialize(_models.OncoPhenotypeResult, response.json())

        if response.status_code == 202:
            response_headers["Operation-Location"] = self._deserialize(
                "str", response.headers.get("Operation-Location")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Repeatability-Result"] = self._deserialize(
                "str", response.headers.get("Repeatability-Result")
            )

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    @overload
    async def begin_infer_cancer_profile(
        self,
        body: _models.OncoPhenotypeData,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.OncoPhenotypeResult]:
        """Create Onco Phenotype job.

        Creates an Onco Phenotype job with the given request body.

        :param body: Required.
        :type body: ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeData
        :keyword repeatability_request_id: An opaque, globally-unique, client-generated string
         identifier for the request. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: Specifies the date and time at which the request was first
         created. Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns OncoPhenotypeResult. The
         OncoPhenotypeResult is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.healthinsights.cancerprofiling.models.OncoPhenotypeResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_infer_cancer_profile(
        self,
        body: JSON,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.OncoPhenotypeResult]:
        """Create Onco Phenotype job.

        Creates an Onco Phenotype job with the given request body.

        :param body: Required.
        :type body: JSON
        :keyword repeatability_request_id: An opaque, globally-unique, client-generated string
         identifier for the request. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: Specifies the date and time at which the request was first
         created. Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns OncoPhenotypeResult. The
         OncoPhenotypeResult is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.healthinsights.cancerprofiling.models.OncoPhenotypeResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_infer_cancer_profile(
        self,
        body: IO,
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.OncoPhenotypeResult]:
        """Create Onco Phenotype job.

        Creates an Onco Phenotype job with the given request body.

        :param body: Required.
        :type body: IO
        :keyword repeatability_request_id: An opaque, globally-unique, client-generated string
         identifier for the request. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: Specifies the date and time at which the request was first
         created. Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns OncoPhenotypeResult. The
         OncoPhenotypeResult is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.healthinsights.cancerprofiling.models.OncoPhenotypeResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_infer_cancer_profile(
        self,
        body: Union[_models.OncoPhenotypeData, JSON, IO],
        *,
        repeatability_request_id: Optional[str] = None,
        repeatability_first_sent: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.OncoPhenotypeResult]:
        """Create Onco Phenotype job.

        Creates an Onco Phenotype job with the given request body.

        :param body: Is one of the following types: OncoPhenotypeData, JSON, IO Required.
        :type body: ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeData or JSON or IO
        :keyword repeatability_request_id: An opaque, globally-unique, client-generated string
         identifier for the request. Default value is None.
        :paramtype repeatability_request_id: str
        :keyword repeatability_first_sent: Specifies the date and time at which the request was first
         created. Default value is None.
        :paramtype repeatability_first_sent: ~datetime.datetime
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns OncoPhenotypeResult. The
         OncoPhenotypeResult is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.healthinsights.cancerprofiling.models.OncoPhenotypeResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.OncoPhenotypeResult] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._infer_cancer_profile_initial(
                body=body,
                repeatability_request_id=repeatability_request_id,
                repeatability_first_sent=repeatability_first_sent,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.OncoPhenotypeResult, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
