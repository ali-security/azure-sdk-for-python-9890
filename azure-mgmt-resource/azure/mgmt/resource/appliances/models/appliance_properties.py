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


class ApplianceProperties(Model):
    """The appliance properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param managed_resource_group_id: The managed resource group Id.
    :type managed_resource_group_id: str
    :param appliance_definition_id: The fully qualified path of appliance
     definition Id.
    :type appliance_definition_id: str
    :param parameters: Name and value pairs that define the appliance
     parameters. It can be a JObject or a well formed JSON string.
    :type parameters: object
    :ivar outputs: Name and value pairs that define the appliance outputs.
    :vartype outputs: object
    :ivar provisioning_state: The appliance provisioning state. Possible
     values include: 'Accepted', 'Running', 'Ready', 'Creating', 'Created',
     'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded', 'Updating'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.resource.appliances.models.ProvisioningState>`
    :param ui_definition_uri: The blob URI where the UI definition file is
     located.
    :type ui_definition_uri: str
    """

    _validation = {
        'managed_resource_group_id': {'required': True},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'managed_resource_group_id': {'key': 'managedResourceGroupId', 'type': 'str'},
        'appliance_definition_id': {'key': 'applianceDefinitionId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'object'},
        'outputs': {'key': 'outputs', 'type': 'object'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'uiDefinitionUri', 'type': 'str'},
    }

    def __init__(self, managed_resource_group_id, appliance_definition_id=None, parameters=None, ui_definition_uri=None):
        self.managed_resource_group_id = managed_resource_group_id
        self.appliance_definition_id = appliance_definition_id
        self.parameters = parameters
        self.outputs = None
        self.provisioning_state = None
        self.ui_definition_uri = ui_definition_uri
