# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class CustomLocation(TrackedResource):  # pylint: disable=too-many-instance-attributes
    """Custom Locations definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.SystemData
    :ivar authentication: This is optional input that contains the authentication that should be
     used to generate the namespace.
    :vartype authentication:
     ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationPropertiesAuthentication
    :ivar cluster_extension_ids: Contains the reference to the add-on that contains charts to
     deploy CRDs and operators.
    :vartype cluster_extension_ids: list[str]
    :ivar display_name: Display name for the Custom Locations location.
    :vartype display_name: str
    :ivar host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform
     a checkAccess API for listAdminCredentials permissions.
    :vartype host_resource_id: str
    :ivar host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
     "Kubernetes"
    :vartype host_type: str or ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.HostType
    :ivar namespace: Kubernetes namespace that will be created on the specified cluster.
    :vartype namespace: str
    :ivar provisioning_state: Provisioning State for the Custom Location.
    :vartype provisioning_state: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "authentication": {"key": "properties.authentication", "type": "CustomLocationPropertiesAuthentication"},
        "cluster_extension_ids": {"key": "properties.clusterExtensionIds", "type": "[str]"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "host_resource_id": {"key": "properties.hostResourceId", "type": "str"},
        "host_type": {"key": "properties.hostType", "type": "str"},
        "namespace": {"key": "properties.namespace", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        authentication: Optional["_models.CustomLocationPropertiesAuthentication"] = None,
        cluster_extension_ids: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        host_resource_id: Optional[str] = None,
        host_type: Optional[Union[str, "_models.HostType"]] = None,
        namespace: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword authentication: This is optional input that contains the authentication that should be
         used to generate the namespace.
        :paramtype authentication:
         ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationPropertiesAuthentication
        :keyword cluster_extension_ids: Contains the reference to the add-on that contains charts to
         deploy CRDs and operators.
        :paramtype cluster_extension_ids: list[str]
        :keyword display_name: Display name for the Custom Locations location.
        :paramtype display_name: str
        :keyword host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will
         perform a checkAccess API for listAdminCredentials permissions.
        :paramtype host_resource_id: str
        :keyword host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
         "Kubernetes"
        :paramtype host_type: str or ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.HostType
        :keyword namespace: Kubernetes namespace that will be created on the specified cluster.
        :paramtype namespace: str
        :keyword provisioning_state: Provisioning State for the Custom Location.
        :paramtype provisioning_state: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.system_data = None
        self.authentication = authentication
        self.cluster_extension_ids = cluster_extension_ids
        self.display_name = display_name
        self.host_resource_id = host_resource_id
        self.host_type = host_type
        self.namespace = namespace
        self.provisioning_state = provisioning_state


class CustomLocationListResult(_serialization.Model):
    """The List Custom Locations operation response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    :ivar value: The list of Custom Locations.
    :vartype value: list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocation]
    """

    _validation = {
        "next_link": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "next_link": {"key": "nextLink", "type": "str"},
        "value": {"key": "value", "type": "[CustomLocation]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.next_link = None
        self.value = None


class CustomLocationOperation(_serialization.Model):
    """Custom Locations operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar is_data_action: Is this Operation a data plane operation.
    :vartype is_data_action: bool
    :ivar name: The name of the compute operation.
    :vartype name: str
    :ivar origin: The origin of the compute operation.
    :vartype origin: str
    :ivar description: The description of the operation.
    :vartype description: str
    :ivar operation: The display name of the compute operation.
    :vartype operation: str
    :ivar provider: The resource provider for the operation.
    :vartype provider: str
    :ivar resource: The display name of the resource the operation applies to.
    :vartype resource: str
    """

    _validation = {
        "is_data_action": {"readonly": True},
        "name": {"readonly": True},
        "origin": {"readonly": True},
        "description": {"readonly": True},
        "operation": {"readonly": True},
        "provider": {"readonly": True},
        "resource": {"readonly": True},
    }

    _attribute_map = {
        "is_data_action": {"key": "isDataAction", "type": "bool"},
        "name": {"key": "name", "type": "str"},
        "origin": {"key": "origin", "type": "str"},
        "description": {"key": "display.description", "type": "str"},
        "operation": {"key": "display.operation", "type": "str"},
        "provider": {"key": "display.provider", "type": "str"},
        "resource": {"key": "display.resource", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.is_data_action = None
        self.name = None
        self.origin = None
        self.description = None
        self.operation = None
        self.provider = None
        self.resource = None


class CustomLocationOperationsList(_serialization.Model):
    """Lists of Custom Locations operations.

    All required parameters must be populated in order to send to Azure.

    :ivar next_link: Next page of operations.
    :vartype next_link: str
    :ivar value: Array of customLocationOperation. Required.
    :vartype value:
     list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationOperation]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "next_link": {"key": "nextLink", "type": "str"},
        "value": {"key": "value", "type": "[CustomLocationOperation]"},
    }

    def __init__(
        self, *, value: List["_models.CustomLocationOperation"], next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword next_link: Next page of operations.
        :paramtype next_link: str
        :keyword value: Array of customLocationOperation. Required.
        :paramtype value:
         list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationOperation]
        """
        super().__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class CustomLocationPropertiesAuthentication(_serialization.Model):
    """This is optional input that contains the authentication that should be used to generate the
    namespace.

    :ivar type: The type of the Custom Locations authentication.
    :vartype type: str
    :ivar value: The kubeconfig value.
    :vartype value: str
    """

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, *, type: Optional[str] = None, value: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword type: The type of the Custom Locations authentication.
        :paramtype type: str
        :keyword value: The kubeconfig value.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.value = value


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have
    tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class EnabledResourceType(ProxyResource):
    """EnabledResourceType definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.SystemData
    :ivar cluster_extension_id: Cluster Extension ID.
    :vartype cluster_extension_id: str
    :ivar extension_type: Cluster Extension Type.
    :vartype extension_type: str
    :ivar types_metadata: Metadata of the Resource Type.
    :vartype types_metadata:
     list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.EnabledResourceTypePropertiesTypesMetadataItem]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "cluster_extension_id": {"key": "properties.clusterExtensionId", "type": "str"},
        "extension_type": {"key": "properties.extensionType", "type": "str"},
        "types_metadata": {
            "key": "properties.typesMetadata",
            "type": "[EnabledResourceTypePropertiesTypesMetadataItem]",
        },
    }

    def __init__(
        self,
        *,
        cluster_extension_id: Optional[str] = None,
        extension_type: Optional[str] = None,
        types_metadata: Optional[List["_models.EnabledResourceTypePropertiesTypesMetadataItem"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword cluster_extension_id: Cluster Extension ID.
        :paramtype cluster_extension_id: str
        :keyword extension_type: Cluster Extension Type.
        :paramtype extension_type: str
        :keyword types_metadata: Metadata of the Resource Type.
        :paramtype types_metadata:
         list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.EnabledResourceTypePropertiesTypesMetadataItem]
        """
        super().__init__(**kwargs)
        self.system_data = None
        self.cluster_extension_id = cluster_extension_id
        self.extension_type = extension_type
        self.types_metadata = types_metadata


class EnabledResourceTypePropertiesTypesMetadataItem(_serialization.Model):
    """Metadata of the Resource Type.

    :ivar api_version: Api Version of Resource Type.
    :vartype api_version: str
    :ivar resource_provider_namespace: Resource Provider Namespace of Resource Type.
    :vartype resource_provider_namespace: str
    :ivar resource_type: Resource Type.
    :vartype resource_type: str
    """

    _attribute_map = {
        "api_version": {"key": "apiVersion", "type": "str"},
        "resource_provider_namespace": {"key": "resourceProviderNamespace", "type": "str"},
        "resource_type": {"key": "resourceType", "type": "str"},
    }

    def __init__(
        self,
        *,
        api_version: Optional[str] = None,
        resource_provider_namespace: Optional[str] = None,
        resource_type: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword api_version: Api Version of Resource Type.
        :paramtype api_version: str
        :keyword resource_provider_namespace: Resource Provider Namespace of Resource Type.
        :paramtype resource_provider_namespace: str
        :keyword resource_type: Resource Type.
        :paramtype resource_type: str
        """
        super().__init__(**kwargs)
        self.api_version = api_version
        self.resource_provider_namespace = resource_provider_namespace
        self.resource_type = resource_type


class EnabledResourceTypesListResult(_serialization.Model):
    """List of EnabledResourceTypes definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    :ivar value: The list of EnabledResourceTypes available for a customLocation.
    :vartype value:
     list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.EnabledResourceType]
    """

    _validation = {
        "next_link": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "next_link": {"key": "nextLink", "type": "str"},
        "value": {"key": "value", "type": "[EnabledResourceType]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.next_link = None
        self.value = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.extendedlocation.v2021_03_15_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class PatchableCustomLocations(_serialization.Model):
    """The Custom Locations patchable resource definition.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar authentication: This is optional input that contains the authentication that should be
     used to generate the namespace.
    :vartype authentication:
     ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationPropertiesAuthentication
    :ivar cluster_extension_ids: Contains the reference to the add-on that contains charts to
     deploy CRDs and operators.
    :vartype cluster_extension_ids: list[str]
    :ivar display_name: Display name for the Custom Locations location.
    :vartype display_name: str
    :ivar host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform
     a checkAccess API for listAdminCredentials permissions.
    :vartype host_resource_id: str
    :ivar host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
     "Kubernetes"
    :vartype host_type: str or ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.HostType
    :ivar namespace: Kubernetes namespace that will be created on the specified cluster.
    :vartype namespace: str
    :ivar provisioning_state: Provisioning State for the Custom Location.
    :vartype provisioning_state: str
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "authentication": {"key": "properties.authentication", "type": "CustomLocationPropertiesAuthentication"},
        "cluster_extension_ids": {"key": "properties.clusterExtensionIds", "type": "[str]"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "host_resource_id": {"key": "properties.hostResourceId", "type": "str"},
        "host_type": {"key": "properties.hostType", "type": "str"},
        "namespace": {"key": "properties.namespace", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        authentication: Optional["_models.CustomLocationPropertiesAuthentication"] = None,
        cluster_extension_ids: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        host_resource_id: Optional[str] = None,
        host_type: Optional[Union[str, "_models.HostType"]] = None,
        namespace: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword authentication: This is optional input that contains the authentication that should be
         used to generate the namespace.
        :paramtype authentication:
         ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CustomLocationPropertiesAuthentication
        :keyword cluster_extension_ids: Contains the reference to the add-on that contains charts to
         deploy CRDs and operators.
        :paramtype cluster_extension_ids: list[str]
        :keyword display_name: Display name for the Custom Locations location.
        :paramtype display_name: str
        :keyword host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will
         perform a checkAccess API for listAdminCredentials permissions.
        :paramtype host_resource_id: str
        :keyword host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
         "Kubernetes"
        :paramtype host_type: str or ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.HostType
        :keyword namespace: Kubernetes namespace that will be created on the specified cluster.
        :paramtype namespace: str
        :keyword provisioning_state: Provisioning State for the Custom Location.
        :paramtype provisioning_state: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.authentication = authentication
        self.cluster_extension_ids = cluster_extension_ids
        self.display_name = display_name
        self.host_resource_id = host_resource_id
        self.host_type = host_type
        self.namespace = namespace
        self.provisioning_state = provisioning_state


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.extendedlocation.v2021_03_15_preview.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
