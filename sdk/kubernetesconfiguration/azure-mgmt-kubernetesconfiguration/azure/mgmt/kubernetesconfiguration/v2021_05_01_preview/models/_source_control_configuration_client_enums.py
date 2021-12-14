# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ClusterTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Cluster types
    """

    CONNECTED_CLUSTERS = "connectedClusters"
    MANAGED_CLUSTERS = "managedClusters"

class ComplianceStateType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The compliance state of the configuration.
    """

    PENDING = "Pending"
    COMPLIANT = "Compliant"
    NONCOMPLIANT = "Noncompliant"
    INSTALLED = "Installed"
    FAILED = "Failed"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class Enum0(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MICROSOFT_CONTAINER_SERVICE = "Microsoft.ContainerService"
    MICROSOFT_KUBERNETES = "Microsoft.Kubernetes"

class Enum1(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MANAGED_CLUSTERS = "managedClusters"
    CONNECTED_CLUSTERS = "connectedClusters"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MANAGED_CLUSTERS = "managedClusters"
    CONNECTED_CLUSTERS = "connectedClusters"

class LevelType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Level of the status.
    """

    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"

class MessageLevelType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Level of the message.
    """

    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"

class OperatorScopeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Scope at which the operator will be installed.
    """

    CLUSTER = "cluster"
    NAMESPACE = "namespace"

class OperatorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the operator
    """

    FLUX = "Flux"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the extension resource.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"

class ProvisioningStateType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the resource provider.
    """

    ACCEPTED = "Accepted"
    DELETING = "Deleting"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
