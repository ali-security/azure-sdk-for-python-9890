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

from .resource import Resource


class AvailabilitySet(Resource):
    """Create or update Availability Set parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :param platform_update_domain_count: Update Domain count.
    :type platform_update_domain_count: int
    :param platform_fault_domain_count: Fault Domain count.
    :type platform_fault_domain_count: int
    :param virtual_machines: A list of references to all virtual machines in
     the availability set.
    :type virtual_machines: list of :class:`SubResource
     <azure.mgmt.compute.models.SubResource>`
    :ivar statuses: the resource status information.
    :vartype statuses: list of :class:`InstanceViewStatus
     <azure.mgmt.compute.models.InstanceViewStatus>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'statuses': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'platform_update_domain_count': {'key': 'properties.platformUpdateDomainCount', 'type': 'int'},
        'platform_fault_domain_count': {'key': 'properties.platformFaultDomainCount', 'type': 'int'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[SubResource]'},
        'statuses': {'key': 'properties.statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, location, tags=None, platform_update_domain_count=None, platform_fault_domain_count=None, virtual_machines=None):
        super(AvailabilitySet, self).__init__(location=location, tags=tags)
        self.platform_update_domain_count = platform_update_domain_count
        self.platform_fault_domain_count = platform_fault_domain_count
        self.virtual_machines = virtual_machines
        self.statuses = None
