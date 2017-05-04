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

from .entity_health_state import EntityHealthState


class ReplicaHealthState(EntityHealthState):
    """Represents a base class for stateful service replica or stateless service
    instance health state.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param partition_id: The ID of the partition to which this replica
     belongs.
    :type partition_id: str
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    """ 

    _validation = {
        'ServiceKind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'ServiceKind': {'key': 'ServiceKind', 'type': 'str'},
    }

    _subtype_map = {
        'ServiceKind': {'Stateful': 'StatefulServiceReplicaHealthState', 'Stateless': 'StatelessServiceInstanceHealthState'}
    }

    def __init__(self, aggregated_health_state=None, partition_id=None):
        super(ReplicaHealthState, self).__init__(aggregated_health_state=aggregated_health_state)
        self.partition_id = partition_id
        self.ServiceKind = None
        self.ServiceKind = 'ReplicaHealthState'
