# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MonitorManagementClientConfiguration
from .operations import DiagnosticSettingsCategoryOperations
from .operations import DiagnosticSettingsOperations
from .operations import MetricDefinitionsOperations
from .operations import MetricsOperations
from .operations import SubscriptionDiagnosticSettingsOperations
from .. import models


class MonitorManagementClient(object):
    """Monitor Management Client.

    :ivar diagnostic_settings_category: DiagnosticSettingsCategoryOperations operations
    :vartype diagnostic_settings_category: $(python-base-namespace).v2017_05_01_preview.aio.operations.DiagnosticSettingsCategoryOperations
    :ivar diagnostic_settings: DiagnosticSettingsOperations operations
    :vartype diagnostic_settings: $(python-base-namespace).v2017_05_01_preview.aio.operations.DiagnosticSettingsOperations
    :ivar metric_definitions: MetricDefinitionsOperations operations
    :vartype metric_definitions: $(python-base-namespace).v2017_05_01_preview.aio.operations.MetricDefinitionsOperations
    :ivar metrics: MetricsOperations operations
    :vartype metrics: $(python-base-namespace).v2017_05_01_preview.aio.operations.MetricsOperations
    :ivar subscription_diagnostic_settings: SubscriptionDiagnosticSettingsOperations operations
    :vartype subscription_diagnostic_settings: $(python-base-namespace).v2017_05_01_preview.aio.operations.SubscriptionDiagnosticSettingsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MonitorManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.diagnostic_settings_category = DiagnosticSettingsCategoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.diagnostic_settings = DiagnosticSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.metric_definitions = MetricDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.metrics = MetricsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_diagnostic_settings = SubscriptionDiagnosticSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MonitorManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
