# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubtaskInformation(Model):
    """
    Information about an Azure Batch subtask.

    :param id: The id of the subtask.
    :type id: int
    :param node_info: Information about the compute node on which the subtask
     ran.
    :type node_info: :class:`ComputeNodeInformation
     <azure.batch.models.ComputeNodeInformation>`
    :param start_time: The time at which the subtask started running. If the
     subtask has been restarted or retried, this is the most recent time at
     which the subtask started running.
    :type start_time: datetime
    :param end_time: The time at which the subtask completed. This property
     is set only if the subtask is in the Completed state.
    :type end_time: datetime
    :param exit_code: The exit code of the subtask. This property is set only
     if the subtask is in the Completed state.
    :type exit_code: int
    :param scheduling_error: Details of any error encountered scheduling the
     subtask.
    :type scheduling_error: :class:`TaskSchedulingError
     <azure.batch.models.TaskSchedulingError>`
    :param state: The current state of the subtask. Possible values include:
     'active', 'preparing', 'running', 'completed'
    :type state: str or :class:`TaskState <azure.batch.models.TaskState>`
    :param state_transition_time: The time at which the subtask entered its
     current state.
    :type state_transition_time: datetime
    :param previous_state: The previous state of the subtask. This property
     is not set if the subtask is in its initial Active state. Possible
     values include: 'active', 'preparing', 'running', 'completed'
    :type previous_state: str or :class:`TaskState
     <azure.batch.models.TaskState>`
    :param previous_state_transition_time: The time at which the subtask
     entered its previous state. This property is not set if the subtask is
     in its initial Active state.
    :type previous_state_transition_time: datetime
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'node_info': {'key': 'nodeInfo', 'type': 'ComputeNodeInformation'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'TaskSchedulingError'},
        'state': {'key': 'state', 'type': 'TaskState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'TaskState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
    }

    def __init__(self, id=None, node_info=None, start_time=None, end_time=None, exit_code=None, scheduling_error=None, state=None, state_transition_time=None, previous_state=None, previous_state_transition_time=None):
        self.id = id
        self.node_info = node_info
        self.start_time = start_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.scheduling_error = scheduling_error
        self.state = state
        self.state_transition_time = state_transition_time
        self.previous_state = previous_state
        self.previous_state_transition_time = previous_state_transition_time
