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


class JobPreparationTaskExecutionInformation(Model):
    """Contains information about the execution of a Job Preparation task on a
    compute node.

    :param start_time: The time at which the task started running. Note that
     every time the task is restarted, this value is updated.
    :type start_time: datetime
    :param end_time: The time at which the Job Preparation task completed.
     This property is set only if the task is in the Completed state.
    :type end_time: datetime
    :param state: The current state of the Job Preparation task. Possible
     values include: 'running', 'completed'
    :type state: str or :class:`JobPreparationTaskState
     <azure.batch.models.JobPreparationTaskState>`
    :param task_root_directory: The root directory of the Job Preparation
     task on the compute node. You can use this path to retrieve files
     created by the task, such as log files.
    :type task_root_directory: str
    :param task_root_directory_url: The URL to the root directory of the Job
     Preparation task on the compute node.
    :type task_root_directory_url: str
    :param exit_code: The exit code of the Job Preparation task. This
     property is set only if the task is in the Completed state.
    :type exit_code: int
    :param scheduling_error: The error encountered by the Batch service when
     starting the task.
    :type scheduling_error: :class:`TaskSchedulingError
     <azure.batch.models.TaskSchedulingError>`
    :param retry_count: The number of times the task has been retried by the
     Batch service. Every time the task exits with a non-zero exit code, it
     is deemed a task failure. The Batch service will retry the task up to
     the limit specified by the constraints.
    :type retry_count: int
    :param last_retry_time: The most recent time at which a retry of the Job
     Preparation task started running. This property is set only if the task
     was retried (i.e. retryCount is nonzero).
    :type last_retry_time: datetime
    """ 

    _validation = {
        'start_time': {'required': True},
        'state': {'required': True},
        'retry_count': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'JobPreparationTaskState'},
        'task_root_directory': {'key': 'taskRootDirectory', 'type': 'str'},
        'task_root_directory_url': {'key': 'taskRootDirectoryUrl', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'TaskSchedulingError'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'last_retry_time': {'key': 'lastRetryTime', 'type': 'iso-8601'},
    }

    def __init__(self, start_time, state, retry_count, end_time=None, task_root_directory=None, task_root_directory_url=None, exit_code=None, scheduling_error=None, last_retry_time=None):
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.task_root_directory = task_root_directory
        self.task_root_directory_url = task_root_directory_url
        self.exit_code = exit_code
        self.scheduling_error = scheduling_error
        self.retry_count = retry_count
        self.last_retry_time = last_retry_time
