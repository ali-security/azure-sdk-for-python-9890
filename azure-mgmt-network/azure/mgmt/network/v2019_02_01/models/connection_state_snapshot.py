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


class ConnectionStateSnapshot(Model):
    """Connection state snapshot.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param connection_state: The connection state. Possible values include:
     'Reachable', 'Unreachable', 'Unknown'
    :type connection_state: str or
     ~azure.mgmt.network.v2019_02_01.models.ConnectionState
    :param start_time: The start time of the connection snapshot.
    :type start_time: datetime
    :param end_time: The end time of the connection snapshot.
    :type end_time: datetime
    :param evaluation_state: Connectivity analysis evaluation state. Possible
     values include: 'NotStarted', 'InProgress', 'Completed'
    :type evaluation_state: str or
     ~azure.mgmt.network.v2019_02_01.models.EvaluationState
    :param avg_latency_in_ms: Average latency in ms.
    :type avg_latency_in_ms: int
    :param min_latency_in_ms: Minimum latency in ms.
    :type min_latency_in_ms: int
    :param max_latency_in_ms: Maximum latency in ms.
    :type max_latency_in_ms: int
    :param probes_sent: The number of sent probes.
    :type probes_sent: int
    :param probes_failed: The number of failed probes.
    :type probes_failed: int
    :ivar hops: List of hops between the source and the destination.
    :vartype hops:
     list[~azure.mgmt.network.v2019_02_01.models.ConnectivityHop]
    """

    _validation = {
        'hops': {'readonly': True},
    }

    _attribute_map = {
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'evaluation_state': {'key': 'evaluationState', 'type': 'str'},
        'avg_latency_in_ms': {'key': 'avgLatencyInMs', 'type': 'int'},
        'min_latency_in_ms': {'key': 'minLatencyInMs', 'type': 'int'},
        'max_latency_in_ms': {'key': 'maxLatencyInMs', 'type': 'int'},
        'probes_sent': {'key': 'probesSent', 'type': 'int'},
        'probes_failed': {'key': 'probesFailed', 'type': 'int'},
        'hops': {'key': 'hops', 'type': '[ConnectivityHop]'},
    }

    def __init__(self, **kwargs):
        super(ConnectionStateSnapshot, self).__init__(**kwargs)
        self.connection_state = kwargs.get('connection_state', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.evaluation_state = kwargs.get('evaluation_state', None)
        self.avg_latency_in_ms = kwargs.get('avg_latency_in_ms', None)
        self.min_latency_in_ms = kwargs.get('min_latency_in_ms', None)
        self.max_latency_in_ms = kwargs.get('max_latency_in_ms', None)
        self.probes_sent = kwargs.get('probes_sent', None)
        self.probes_failed = kwargs.get('probes_failed', None)
        self.hops = None
