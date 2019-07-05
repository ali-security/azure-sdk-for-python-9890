# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegistrationAssignmentPropertiesRegistrationDefinitionProperties(Model):
    """Properties of registration definition inside registration assignment.

    :param description: Description of the registration definition.
    :type description: str
    :param authorizations: Authorization tuple containing principal id of the
     user/security group or service principal and id of the build-in role.
    :type authorizations:
     list[~azure.mgmt.managedservices.models.Authorization]
    :param registration_definition_name: Name of the registration definition.
    :type registration_definition_name: str
    :param provisioning_state: Current state of the registration definition.
     Possible values include: 'NotSpecified', 'Accepted', 'Running', 'Ready',
     'Creating', 'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed',
     'Succeeded', 'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.managedservices.models.ProvisioningState
    :param managee_tenant_id: Id of the home tenant.
    :type managee_tenant_id: str
    :param managee_tenant_name: Name of the home tenant.
    :type managee_tenant_name: str
    :param managed_by_tenant_id: Id of the managedBy tenant.
    :type managed_by_tenant_id: str
    :param managed_by_tenant_name: Name of the managedBy tenant.
    :type managed_by_tenant_name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'authorizations': {'key': 'authorizations', 'type': '[Authorization]'},
        'registration_definition_name': {'key': 'registrationDefinitionName', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'managee_tenant_id': {'key': 'manageeTenantId', 'type': 'str'},
        'managee_tenant_name': {'key': 'manageeTenantName', 'type': 'str'},
        'managed_by_tenant_id': {'key': 'managedByTenantId', 'type': 'str'},
        'managed_by_tenant_name': {'key': 'managedByTenantName', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, authorizations=None, registration_definition_name: str=None, provisioning_state=None, managee_tenant_id: str=None, managee_tenant_name: str=None, managed_by_tenant_id: str=None, managed_by_tenant_name: str=None, **kwargs) -> None:
        super(RegistrationAssignmentPropertiesRegistrationDefinitionProperties, self).__init__(**kwargs)
        self.description = description
        self.authorizations = authorizations
        self.registration_definition_name = registration_definition_name
        self.provisioning_state = provisioning_state
        self.managee_tenant_id = managee_tenant_id
        self.managee_tenant_name = managee_tenant_name
        self.managed_by_tenant_id = managed_by_tenant_id
        self.managed_by_tenant_name = managed_by_tenant_name
