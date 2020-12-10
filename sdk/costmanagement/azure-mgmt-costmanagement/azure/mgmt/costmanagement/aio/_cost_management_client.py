# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import CostManagementClientConfiguration
from .operations import ViewsOperations
from .operations import AlertsOperations
from .operations import ForecastOperations
from .operations import DimensionsOperations
from .operations import QueryOperations
from .operations import Operations
from .operations import ExportsOperations
from .. import models


class CostManagementClient(object):
    """CostManagementClient.

    :ivar views: ViewsOperations operations
    :vartype views: azure.mgmt.costmanagement.aio.operations.ViewsOperations
    :ivar alerts: AlertsOperations operations
    :vartype alerts: azure.mgmt.costmanagement.aio.operations.AlertsOperations
    :ivar forecast: ForecastOperations operations
    :vartype forecast: azure.mgmt.costmanagement.aio.operations.ForecastOperations
    :ivar dimensions: DimensionsOperations operations
    :vartype dimensions: azure.mgmt.costmanagement.aio.operations.DimensionsOperations
    :ivar query: QueryOperations operations
    :vartype query: azure.mgmt.costmanagement.aio.operations.QueryOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.costmanagement.aio.operations.Operations
    :ivar exports: ExportsOperations operations
    :vartype exports: azure.mgmt.costmanagement.aio.operations.ExportsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = CostManagementClientConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.views = ViewsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.forecast = ForecastOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dimensions = DimensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exports = ExportsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "CostManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
