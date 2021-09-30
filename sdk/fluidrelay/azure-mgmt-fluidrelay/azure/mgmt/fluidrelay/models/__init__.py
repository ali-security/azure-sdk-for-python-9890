# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import FluidRelayEndpoints
    from ._models_py3 import FluidRelayServer
    from ._models_py3 import FluidRelayServerKeys
    from ._models_py3 import FluidRelayServerList
    from ._models_py3 import FluidRelayServerUpdate
    from ._models_py3 import Identity
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResult
    from ._models_py3 import RegenerateKeyRequest
    from ._models_py3 import Resource
    from ._models_py3 import SystemData
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import FluidRelayEndpoints  # type: ignore
    from ._models import FluidRelayServer  # type: ignore
    from ._models import FluidRelayServerKeys  # type: ignore
    from ._models import FluidRelayServerList  # type: ignore
    from ._models import FluidRelayServerUpdate  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import RegenerateKeyRequest  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TrackedResource  # type: ignore

from ._fluid_relay_management_client_enums import (
    CreatedByType,
    KeyName,
    ProvisioningState,
    ResourceIdentityType,
)

__all__ = [
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'FluidRelayEndpoints',
    'FluidRelayServer',
    'FluidRelayServerKeys',
    'FluidRelayServerList',
    'FluidRelayServerUpdate',
    'Identity',
    'OperationDisplay',
    'OperationListResult',
    'OperationResult',
    'RegenerateKeyRequest',
    'Resource',
    'SystemData',
    'TrackedResource',
    'CreatedByType',
    'KeyName',
    'ProvisioningState',
    'ResourceIdentityType',
]
