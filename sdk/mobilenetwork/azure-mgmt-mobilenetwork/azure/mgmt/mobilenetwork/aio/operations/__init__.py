# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._attached_data_networks_operations import AttachedDataNetworksOperations
from ._data_networks_operations import DataNetworksOperations
from ._diagnostics_packages_operations import DiagnosticsPackagesOperations
from ._mobile_networks_operations import MobileNetworksOperations
from ._operations import Operations
from ._packet_captures_operations import PacketCapturesOperations
from ._packet_core_control_planes_operations import PacketCoreControlPlanesOperations
from ._packet_core_control_plane_versions_operations import PacketCoreControlPlaneVersionsOperations
from ._packet_core_data_planes_operations import PacketCoreDataPlanesOperations
from ._services_operations import ServicesOperations
from ._sims_operations import SimsOperations
from ._sim_groups_operations import SimGroupsOperations
from ._sim_policies_operations import SimPoliciesOperations
from ._sites_operations import SitesOperations
from ._slices_operations import SlicesOperations
from ._extended_ue_information_operations import ExtendedUeInformationOperations
from ._ue_information_operations import UeInformationOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AttachedDataNetworksOperations",
    "DataNetworksOperations",
    "DiagnosticsPackagesOperations",
    "MobileNetworksOperations",
    "Operations",
    "PacketCapturesOperations",
    "PacketCoreControlPlanesOperations",
    "PacketCoreControlPlaneVersionsOperations",
    "PacketCoreDataPlanesOperations",
    "ServicesOperations",
    "SimsOperations",
    "SimGroupsOperations",
    "SimPoliciesOperations",
    "SitesOperations",
    "SlicesOperations",
    "ExtendedUeInformationOperations",
    "UeInformationOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
