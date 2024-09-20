# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class EncryptionAtHost(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """EncryptionAtHost represents encryption at host state."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class FipsValidatedModules(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """FipsValidatedModules determines if FIPS is used."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class OutboundType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The outbound routing strategy used to provide your cluster egress to the internet."""

    LOADBALANCER = "Loadbalancer"
    USER_DEFINED_ROUTING = "UserDefinedRouting"


class PreconfiguredNSG(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PreconfiguredNSG represents whether customers want to use their own NSG attached to the
    subnets.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProvisioningState represents a provisioning state."""

    ADMIN_UPDATING = "AdminUpdating"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class Visibility(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Visibility represents visibility."""

    PRIVATE = "Private"
    PUBLIC = "Public"
