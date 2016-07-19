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


class StartTask(Model):
    """A task which is run when a compute node joins a pool in the Azure Batch
    service, or when the compute node is rebooted or reimaged.

    :param command_line: The command line of the start task.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the start task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param run_elevated: Whether to run the start task in elevated mode. The
     default value is false.
    :type run_elevated: bool
    :param max_task_retry_count: The maximum number of times the task may be
     retried.
    :type max_task_retry_count: int
    :param wait_for_success: Whether the Batch service should wait for the
     start task to complete successfully (that is, to exit with exit code 0)
     before scheduling any tasks on the compute node.
    :type wait_for_success: bool
    """ 

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'max_task_retry_count': {'key': 'maxTaskRetryCount', 'type': 'int'},
        'wait_for_success': {'key': 'waitForSuccess', 'type': 'bool'},
    }

    def __init__(self, command_line=None, resource_files=None, environment_settings=None, run_elevated=None, max_task_retry_count=None, wait_for_success=None):
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.run_elevated = run_elevated
        self.max_task_retry_count = max_task_retry_count
        self.wait_for_success = wait_for_success
