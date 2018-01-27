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

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StatefulServiceReplicaHealthState,
    StatelessServiceInstanceHealthState

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or ~azure.servicefabric.models.enum
    :param partition_id:
    :type partition_id: str
    :param service_kind: Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
    }

    _subtype_map = {
        'service_kind': {'Stateful': 'StatefulServiceReplicaHealthState', 'Stateless': 'StatelessServiceInstanceHealthState'}
    }

    def __init__(self, aggregated_health_state=None, partition_id=None):
        super(ReplicaHealthState, self).__init__(aggregated_health_state=aggregated_health_state)
        self.partition_id = partition_id
        self.service_kind = None
        self.service_kind = 'ReplicaHealthState'
