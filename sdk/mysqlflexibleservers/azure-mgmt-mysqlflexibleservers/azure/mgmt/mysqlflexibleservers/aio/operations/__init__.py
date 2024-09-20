# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._azure_ad_administrators_operations import AzureADAdministratorsOperations
from ._backups_operations import BackupsOperations
from ._backup_and_export_operations import BackupAndExportOperations
from ._long_running_backup_operations import LongRunningBackupOperations
from ._long_running_backups_operations import LongRunningBackupsOperations
from ._configurations_operations import ConfigurationsOperations
from ._databases_operations import DatabasesOperations
from ._firewall_rules_operations import FirewallRulesOperations
from ._log_files_operations import LogFilesOperations
from ._location_based_capabilities_operations import LocationBasedCapabilitiesOperations
from ._location_based_capability_set_operations import LocationBasedCapabilitySetOperations
from ._check_virtual_network_subnet_usage_operations import CheckVirtualNetworkSubnetUsageOperations
from ._check_name_availability_operations import CheckNameAvailabilityOperations
from ._check_name_availability_without_location_operations import CheckNameAvailabilityWithoutLocationOperations
from ._operation_results_operations import OperationResultsOperations
from ._operation_progress_operations import OperationProgressOperations
from ._get_private_dns_zone_suffix_operations import GetPrivateDnsZoneSuffixOperations
from ._operations import Operations
from ._maintenances_operations import MaintenancesOperations
from ._servers_operations import ServersOperations
from ._replicas_operations import ReplicasOperations
from ._servers_migration_operations import ServersMigrationOperations
from ._advanced_threat_protection_settings_operations import AdvancedThreatProtectionSettingsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureADAdministratorsOperations",
    "BackupsOperations",
    "BackupAndExportOperations",
    "LongRunningBackupOperations",
    "LongRunningBackupsOperations",
    "ConfigurationsOperations",
    "DatabasesOperations",
    "FirewallRulesOperations",
    "LogFilesOperations",
    "LocationBasedCapabilitiesOperations",
    "LocationBasedCapabilitySetOperations",
    "CheckVirtualNetworkSubnetUsageOperations",
    "CheckNameAvailabilityOperations",
    "CheckNameAvailabilityWithoutLocationOperations",
    "OperationResultsOperations",
    "OperationProgressOperations",
    "GetPrivateDnsZoneSuffixOperations",
    "Operations",
    "MaintenancesOperations",
    "ServersOperations",
    "ReplicasOperations",
    "ServersMigrationOperations",
    "AdvancedThreatProtectionSettingsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
