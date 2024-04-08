# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class FleetMemberProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the last accepted operation."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    JOINING = "Joining"
    """The provisioning state of a member joining a fleet."""
    LEAVING = "Leaving"
    """The provisioning state of a member leaving a fleet."""
    UPDATING = "Updating"
    """The provisioning state of a member being updated."""


class FleetProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the last accepted operation."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    CREATING = "Creating"
    """The provisioning state of a fleet being created."""
    UPDATING = "Updating"
    """The provisioning state of a fleet being updated."""
    DELETING = "Deleting"
    """The provisioning state of a fleet being deleted."""


class ManagedClusterUpgradeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of upgrade to perform when targeting ManagedClusters."""

    FULL = "Full"
    """Full upgrades the control plane and all agent pools of the target ManagedClusters. Requires the
    ManagedClusterUpgradeSpec.KubernetesVersion property to be set."""
    NODE_IMAGE_ONLY = "NodeImageOnly"
    """NodeImageOnly upgrades only the node images of the target ManagedClusters. Requires the
    ManagedClusterUpgradeSpec.KubernetesVersion property to NOT be set."""


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class NodeImageSelectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The node image upgrade type."""

    LATEST = "Latest"
    """Use the latest image version when upgrading nodes. Clusters may use different image versions
    (e.g., 'AKSUbuntu-1804gen2containerd-2021.10.12' and 'AKSUbuntu-1804gen2containerd-2021.10.19')
    because, for example, the latest available version is different in different regions."""
    CONSISTENT = "Consistent"
    """The image versions to upgrade nodes to are selected as described below: for each node pool in
    managed clusters affected by the update run, the system selects the latest image version such
    that it is available across all other node pools (in all other clusters) of the same image
    type. As a result, all node pools of the same image type will be upgraded to the same image
    version. For example, if the latest image version for image type 'AKSUbuntu-1804gen2containerd'
    is 'AKSUbuntu-1804gen2containerd-2021.10.12' for a node pool in cluster A in region X, and is
    'AKSUbuntu-1804gen2containerd-2021.10.17' for a node pool in cluster B in region Y, the system
    will upgrade both node pools to image version 'AKSUbuntu-1804gen2containerd-2021.10.12'."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class UpdateRunProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the UpdateRun resource."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class UpdateState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the UpdateRun, UpdateStage, UpdateGroup, or MemberUpdate."""

    NOT_STARTED = "NotStarted"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that has not been started."""
    RUNNING = "Running"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that is running."""
    STOPPING = "Stopping"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that is being stopped."""
    STOPPED = "Stopped"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that has stopped."""
    SKIPPED = "Skipped"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that has been skipped."""
    FAILED = "Failed"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that has failed."""
    COMPLETED = "Completed"
    """The state of an UpdateRun/UpdateStage/UpdateGroup/MemberUpdate that has completed."""
