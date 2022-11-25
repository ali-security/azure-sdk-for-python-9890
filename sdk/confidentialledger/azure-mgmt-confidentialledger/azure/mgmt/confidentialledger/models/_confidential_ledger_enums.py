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


class LedgerRoleName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LedgerRole associated with the Security Principal of Ledger."""

    READER = "Reader"
    CONTRIBUTOR = "Contributor"
    ADMINISTRATOR = "Administrator"


class LedgerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the ledger. Private means transaction data is encrypted."""

    UNKNOWN = "Unknown"
    PUBLIC = "Public"
    PRIVATE = "Private"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing ProvisioningState for Confidential Ledger."""

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
