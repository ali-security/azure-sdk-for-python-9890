# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AgentPoolMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """A cluster must have at least one 'System' Agent Pool at all times. For additional information
    on agent pool restrictions and best practices, see:
    https://docs.microsoft.com/azure/aks/use-system-pools
    """

    #: System agent pools are primarily for hosting critical system pods such as CoreDNS and
    #: metrics-server. System agent pools osType must be Linux. System agent pools VM SKU must have at
    #: least 2vCPUs and 4GB of memory.
    SYSTEM = "System"
    #: User agent pools are primarily for hosting your application pods.
    USER = "User"

class AgentPoolType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Agent Pool.
    """

    #: Create an Agent Pool backed by a Virtual Machine Scale Set.
    VIRTUAL_MACHINE_SCALE_SETS = "VirtualMachineScaleSets"
    #: Use of this is strongly discouraged.
    AVAILABILITY_SET = "AvailabilitySet"

class Code(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Tells whether the cluster is Running or Stopped
    """

    #: The cluster is running.
    RUNNING = "Running"
    #: The cluster is stopped.
    STOPPED = "Stopped"

class ConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private link service connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class ContainerServiceStorageProfileTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies what kind of storage to use. If omitted, the default will be chosen on your behalf
    based on the choice of orchestrator.
    """

    STORAGE_ACCOUNT = "StorageAccount"
    MANAGED_DISKS = "ManagedDisks"

class ContainerServiceVMSizeTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Size of agent VMs. Note: This is no longer maintained.
    """

    STANDARD_A1 = "Standard_A1"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_A1_V2 = "Standard_A1_v2"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A2_V2 = "Standard_A2_v2"
    STANDARD_A2_M_V2 = "Standard_A2m_v2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A4_V2 = "Standard_A4_v2"
    STANDARD_A4_M_V2 = "Standard_A4m_v2"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A8_V2 = "Standard_A8_v2"
    STANDARD_A8_M_V2 = "Standard_A8m_v2"
    STANDARD_A9 = "Standard_A9"
    STANDARD_B2_MS = "Standard_B2ms"
    STANDARD_B2_S = "Standard_B2s"
    STANDARD_B4_MS = "Standard_B4ms"
    STANDARD_B8_MS = "Standard_B8ms"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D11_V2_PROMO = "Standard_D11_v2_Promo"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D12_V2_PROMO = "Standard_D12_v2_Promo"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D13_V2_PROMO = "Standard_D13_v2_Promo"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D14_V2_PROMO = "Standard_D14_v2_Promo"
    STANDARD_D15_V2 = "Standard_D15_v2"
    STANDARD_D16_V3 = "Standard_D16_v3"
    STANDARD_D16_S_V3 = "Standard_D16s_v3"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D2_V2_PROMO = "Standard_D2_v2_Promo"
    STANDARD_D2_V3 = "Standard_D2_v3"
    STANDARD_D2_S_V3 = "Standard_D2s_v3"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D32_V3 = "Standard_D32_v3"
    STANDARD_D32_S_V3 = "Standard_D32s_v3"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D3_V2_PROMO = "Standard_D3_v2_Promo"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D4_V2_PROMO = "Standard_D4_v2_Promo"
    STANDARD_D4_V3 = "Standard_D4_v3"
    STANDARD_D4_S_V3 = "Standard_D4s_v3"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D5_V2_PROMO = "Standard_D5_v2_Promo"
    STANDARD_D64_V3 = "Standard_D64_v3"
    STANDARD_D64_S_V3 = "Standard_D64s_v3"
    STANDARD_D8_V3 = "Standard_D8_v3"
    STANDARD_D8_S_V3 = "Standard_D8s_v3"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS11_V2_PROMO = "Standard_DS11_v2_Promo"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS12_V2_PROMO = "Standard_DS12_v2_Promo"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS13_2_V2 = "Standard_DS13-2_v2"
    STANDARD_DS13_4_V2 = "Standard_DS13-4_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS13_V2_PROMO = "Standard_DS13_v2_Promo"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_DS14_4_V2 = "Standard_DS14-4_v2"
    STANDARD_DS14_8_V2 = "Standard_DS14-8_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS14_V2_PROMO = "Standard_DS14_v2_Promo"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS2_V2_PROMO = "Standard_DS2_v2_Promo"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS3_V2_PROMO = "Standard_DS3_v2_Promo"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS4_V2_PROMO = "Standard_DS4_v2_Promo"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS5_V2_PROMO = "Standard_DS5_v2_Promo"
    STANDARD_E16_V3 = "Standard_E16_v3"
    STANDARD_E16_S_V3 = "Standard_E16s_v3"
    STANDARD_E2_V3 = "Standard_E2_v3"
    STANDARD_E2_S_V3 = "Standard_E2s_v3"
    STANDARD_E32_16_S_V3 = "Standard_E32-16s_v3"
    STANDARD_E32_8_S_V3 = "Standard_E32-8s_v3"
    STANDARD_E32_V3 = "Standard_E32_v3"
    STANDARD_E32_S_V3 = "Standard_E32s_v3"
    STANDARD_E4_V3 = "Standard_E4_v3"
    STANDARD_E4_S_V3 = "Standard_E4s_v3"
    STANDARD_E64_16_S_V3 = "Standard_E64-16s_v3"
    STANDARD_E64_32_S_V3 = "Standard_E64-32s_v3"
    STANDARD_E64_V3 = "Standard_E64_v3"
    STANDARD_E64_S_V3 = "Standard_E64s_v3"
    STANDARD_E8_V3 = "Standard_E8_v3"
    STANDARD_E8_S_V3 = "Standard_E8s_v3"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F16_S = "Standard_F16s"
    STANDARD_F16_S_V2 = "Standard_F16s_v2"
    STANDARD_F1_S = "Standard_F1s"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F2_S = "Standard_F2s"
    STANDARD_F2_S_V2 = "Standard_F2s_v2"
    STANDARD_F32_S_V2 = "Standard_F32s_v2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F4_S = "Standard_F4s"
    STANDARD_F4_S_V2 = "Standard_F4s_v2"
    STANDARD_F64_S_V2 = "Standard_F64s_v2"
    STANDARD_F72_S_V2 = "Standard_F72s_v2"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F8_S = "Standard_F8s"
    STANDARD_F8_S_V2 = "Standard_F8s_v2"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS4_4 = "Standard_GS4-4"
    STANDARD_GS4_8 = "Standard_GS4-8"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_GS5_16 = "Standard_GS5-16"
    STANDARD_GS5_8 = "Standard_GS5-8"
    STANDARD_H16 = "Standard_H16"
    STANDARD_H16_M = "Standard_H16m"
    STANDARD_H16_MR = "Standard_H16mr"
    STANDARD_H16_R = "Standard_H16r"
    STANDARD_H8 = "Standard_H8"
    STANDARD_H8_M = "Standard_H8m"
    STANDARD_L16_S = "Standard_L16s"
    STANDARD_L32_S = "Standard_L32s"
    STANDARD_L4_S = "Standard_L4s"
    STANDARD_L8_S = "Standard_L8s"
    STANDARD_M128_32_MS = "Standard_M128-32ms"
    STANDARD_M128_64_MS = "Standard_M128-64ms"
    STANDARD_M128_MS = "Standard_M128ms"
    STANDARD_M128_S = "Standard_M128s"
    STANDARD_M64_16_MS = "Standard_M64-16ms"
    STANDARD_M64_32_MS = "Standard_M64-32ms"
    STANDARD_M64_MS = "Standard_M64ms"
    STANDARD_M64_S = "Standard_M64s"
    STANDARD_NC12 = "Standard_NC12"
    STANDARD_NC12_S_V2 = "Standard_NC12s_v2"
    STANDARD_NC12_S_V3 = "Standard_NC12s_v3"
    STANDARD_NC24 = "Standard_NC24"
    STANDARD_NC24_R = "Standard_NC24r"
    STANDARD_NC24_RS_V2 = "Standard_NC24rs_v2"
    STANDARD_NC24_RS_V3 = "Standard_NC24rs_v3"
    STANDARD_NC24_S_V2 = "Standard_NC24s_v2"
    STANDARD_NC24_S_V3 = "Standard_NC24s_v3"
    STANDARD_NC6 = "Standard_NC6"
    STANDARD_NC6_S_V2 = "Standard_NC6s_v2"
    STANDARD_NC6_S_V3 = "Standard_NC6s_v3"
    STANDARD_ND12_S = "Standard_ND12s"
    STANDARD_ND24_RS = "Standard_ND24rs"
    STANDARD_ND24_S = "Standard_ND24s"
    STANDARD_ND6_S = "Standard_ND6s"
    STANDARD_NV12 = "Standard_NV12"
    STANDARD_NV24 = "Standard_NV24"
    STANDARD_NV6 = "Standard_NV6"

class Count(with_metaclass(CaseInsensitiveEnumMeta, int, Enum)):
    """Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The
    default value is 1.
    """

    ONE = 1
    THREE = 3
    FIVE = 5

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class Expander(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """If not specified, the default is 'random'. See `expanders
    <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders>`_
    for more information.
    """

    #: Selects the node group that will have the least idle CPU (if tied, unused memory) after
    #: scale-up. This is useful when you have different classes of nodes, for example, high CPU or
    #: high memory nodes, and only want to expand those when there are pending pods that need a lot of
    #: those resources.
    LEAST_WASTE = "least-waste"
    #: Selects the node group that would be able to schedule the most pods when scaling up. This is
    #: useful when you are using nodeSelector to make sure certain pods land on certain nodes. Note
    #: that this won't cause the autoscaler to select bigger nodes vs. smaller, as it can add multiple
    #: smaller nodes at once.
    MOST_PODS = "most-pods"
    #: Selects the node group that has the highest priority assigned by the user. It's configuration
    #: is described in more details `here
    #: <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md>`_.
    PRIORITY = "priority"
    #: Used when you don't have a particular need for the node groups to scale differently.
    RANDOM = "random"

class ExtendedLocationTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of extendedLocation.
    """

    EDGE_ZONE = "EdgeZone"

class Format(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    #: Return azure auth-provider kubeconfig. This format is deprecated in 1.22 and will be fully
    #: removed in 1.25.
    AZURE = "azure"
    #: Return exec format kubeconfig. This format requires kubelogin binary in the path.
    EXEC_ENUM = "exec"

class GPUInstanceProfile(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU.
    """

    MIG1_G = "MIG1g"
    MIG2_G = "MIG2g"
    MIG3_G = "MIG3g"
    MIG4_G = "MIG4g"
    MIG7_G = "MIG7g"

class IpFamily(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The IP version to use for cluster networking and IP assignment.
    """

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

class KubeletDiskType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Determines the placement of emptyDir volumes, container runtime data root, and Kubelet
    ephemeral storage.
    """

    #: Kubelet will use the OS disk for its data.
    OS = "OS"
    #: Kubelet will use the temporary disk for its data.
    TEMPORARY = "Temporary"

class LicenseType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The license type to use for Windows VMs. See `Azure Hybrid User Benefits
    <https://azure.microsoft.com/pricing/hybrid-benefit/faq/>`_ for more details.
    """

    #: No additional licensing is applied.
    NONE = "None"
    #: Enables Azure Hybrid User Benefits for Windows VMs.
    WINDOWS_SERVER = "Windows_Server"

class LoadBalancerSku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default is 'standard'. See `Azure Load Balancer SKUs
    <https://docs.microsoft.com/azure/load-balancer/skus>`_ for more information about the
    differences between load balancer SKUs.
    """

    #: Use a a standard Load Balancer. This is the recommended Load Balancer SKU. For more information
    #: about on working with the load balancer in the managed cluster, see the `standard Load Balancer
    #: <https://docs.microsoft.com/azure/aks/load-balancer-standard>`_ article.
    STANDARD = "standard"
    #: Use a basic Load Balancer with limited functionality.
    BASIC = "basic"

class ManagedClusterPodIdentityProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state of the pod identity.
    """

    ASSIGNED = "Assigned"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"

class ManagedClusterSKUName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of a managed cluster SKU.
    """

    BASIC = "Basic"

class ManagedClusterSKUTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """If not specified, the default is 'Free'. See `uptime SLA
    <https://docs.microsoft.com/azure/aks/uptime-sla>`_ for more details.
    """

    #: Guarantees 99.95% availability of the Kubernetes API server endpoint for clusters that use
    #: Availability Zones and 99.9% of availability for clusters that don't use Availability Zones.
    PAID = "Paid"
    #: No guaranteed SLA, no additional charges. Free tier clusters have an SLO of 99.5%.
    FREE = "Free"

class NetworkMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This cannot be specified if networkPlugin is anything other than 'azure'.
    """

    #: No bridge is created. Intra-VM Pod to Pod communication is through IP routes created by Azure
    #: CNI. See `Transparent Mode <https://docs.microsoft.com/azure/aks/faq#transparent-mode>`_ for
    #: more information.
    TRANSPARENT = "transparent"
    #: This is no longer supported.
    BRIDGE = "bridge"

class NetworkPlugin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Network plugin used for building the Kubernetes network.
    """

    #: Use the Azure CNI network plugin. See `Azure CNI (advanced) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking>`_ for
    #: more information.
    AZURE = "azure"
    #: Use the Kubenet network plugin. See `Kubenet (basic) networking
    #: <https://docs.microsoft.com/azure/aks/concepts-network#kubenet-basic-networking>`_ for more
    #: information.
    KUBENET = "kubenet"

class NetworkPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Network policy used for building the Kubernetes network.
    """

    #: Use Calico network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information.
    CALICO = "calico"
    #: Use Azure network policies. See `differences between Azure and Calico policies
    #: <https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities>`_
    #: for more information.
    AZURE = "azure"

class OSDiskType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested
    OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more
    information see `Ephemeral OS
    <https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os>`_.
    """

    #: Azure replicates the operating system disk for a virtual machine to Azure storage to avoid data
    #: loss should the VM need to be relocated to another host. Since containers aren't designed to
    #: have local state persisted, this behavior offers limited value while providing some drawbacks,
    #: including slower node provisioning and higher read/write latency.
    MANAGED = "Managed"
    #: Ephemeral OS disks are stored only on the host machine, just like a temporary disk. This
    #: provides lower read/write latency, along with faster node scaling and cluster upgrades.
    EPHEMERAL = "Ephemeral"

class OSSKU(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies an OS SKU. This value must not be specified if OSType is Windows.
    """

    UBUNTU = "Ubuntu"
    CBL_MARINER = "CBLMariner"

class OSType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operating system type. The default is Linux.
    """

    #: Use Linux.
    LINUX = "Linux"
    #: Use Windows.
    WINDOWS = "Windows"

class OutboundType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This can only be set at cluster creation time and cannot be changed later. For more information
    see `egress outbound type <https://docs.microsoft.com/azure/aks/egress-outboundtype>`_.
    """

    #: The load balancer is used for egress through an AKS assigned public IP. This supports
    #: Kubernetes services of type 'loadBalancer'. For more information see `outbound type
    #: loadbalancer
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-loadbalancer>`_.
    LOAD_BALANCER = "loadBalancer"
    #: Egress paths must be defined by the user. This is an advanced scenario and requires proper
    #: network configuration. For more information see `outbound type userDefinedRouting
    #: <https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-userdefinedrouting>`_.
    USER_DEFINED_ROUTING = "userDefinedRouting"
    #: The AKS-managed NAT gateway is used for egress.
    MANAGED_NAT_GATEWAY = "managedNATGateway"
    #: The user-assigned NAT gateway associated to the cluster subnet is used for egress. This is an
    #: advanced scenario and requires proper network configuration.
    USER_ASSIGNED_NAT_GATEWAY = "userAssignedNATGateway"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Allow or deny public network access for AKS
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """For more information see `use managed identities in AKS
    <https://docs.microsoft.com/azure/aks/use-managed-identity>`_.
    """

    #: Use an implicitly created system assigned managed identity to manage cluster resources. Master
    #: components in the control plane such as kube-controller-manager will use the system assigned
    #: managed identity to manipulate Azure resources.
    SYSTEM_ASSIGNED = "SystemAssigned"
    #: Use a user-specified identity to manage cluster resources. Master components in the control
    #: plane such as kube-controller-manager will use the specified user assigned managed identity to
    #: manipulate Azure resources.
    USER_ASSIGNED = "UserAssigned"
    #: Do not use a managed identity for the Managed Cluster, service principal will be used instead.
    NONE = "None"

class ScaleDownMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes how VMs are added to or removed from Agent Pools. See `billing states
    <https://docs.microsoft.com/azure/virtual-machines/states-billing>`_.
    """

    #: Create new instances during scale up and remove instances during scale down.
    DELETE = "Delete"
    #: Attempt to start deallocated instances (if they exist) during scale up and deallocate instances
    #: during scale down.
    DEALLOCATE = "Deallocate"

class ScaleSetEvictionPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The eviction policy specifies what to do with the VM when it is evicted. The default is Delete.
    For more information about eviction see `spot VMs
    <https://docs.microsoft.com/azure/virtual-machines/spot-vms>`_
    """

    #: Nodes in the underlying Scale Set of the node pool are deleted when they're evicted.
    DELETE = "Delete"
    #: Nodes in the underlying Scale Set of the node pool are set to the stopped-deallocated state
    #: upon eviction. Nodes in the stopped-deallocated state count against your compute quota and can
    #: cause issues with cluster scaling or upgrading.
    DEALLOCATE = "Deallocate"

class ScaleSetPriority(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Virtual Machine Scale Set priority.
    """

    #: Spot priority VMs will be used. There is no SLA for spot nodes. See `spot on AKS
    #: <https://docs.microsoft.com/azure/aks/spot-node-pool>`_ for more information.
    SPOT = "Spot"
    #: Regular VMs will be used.
    REGULAR = "Regular"

class SnapshotType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of a snapshot. The default is NodePool.
    """

    #: The snapshot is a snapshot of a node pool.
    NODE_POOL = "NodePool"

class UpgradeChannel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """For more information see `setting the AKS cluster auto-upgrade channel
    <https://docs.microsoft.com/azure/aks/upgrade-cluster#set-auto-upgrade-channel>`_.
    """

    #: Automatically upgrade the cluster to the latest supported patch release on the latest supported
    #: minor version. In cases where the cluster is at a version of Kubernetes that is at an N-2 minor
    #: version where N is the latest supported minor version, the cluster first upgrades to the latest
    #: supported patch version on N-1 minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster first is
    #: upgraded to 1.18.6, then is upgraded to 1.19.1.
    RAPID = "rapid"
    #: Automatically upgrade the cluster to the latest supported patch release on minor version N-1,
    #: where N is the latest supported minor version. For example, if a cluster is running version
    #: 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is upgraded
    #: to 1.18.6.
    STABLE = "stable"
    #: Automatically upgrade the cluster to the latest supported patch version when it becomes
    #: available while keeping the minor version the same. For example, if a cluster is running
    #: version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is
    #: upgraded to 1.17.9.
    PATCH = "patch"
    #: Automatically upgrade the node image to the latest version available. Microsoft provides
    #: patches and new images for image nodes frequently (usually weekly), but your running nodes
    #: won't get the new images unless you do a node image upgrade. Turning on the node-image channel
    #: will automatically update your node images whenever a new version is available.
    NODE_IMAGE = "node-image"
    #: Disables auto-upgrades and keeps the cluster at its current version of Kubernetes.
    NONE = "none"

class WeekDay(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The weekday enum.
    """

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class WorkloadRuntime(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Determines the type of workload a node can run.
    """

    #: Nodes will use Kubelet to run standard OCI container workloads.
    OCI_CONTAINER = "OCIContainer"
    #: Nodes will use Krustlet to run WASM workloads using the WASI provider (Preview).
    WASM_WASI = "WasmWasi"
