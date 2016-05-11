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


class JobManagerTask(Model):
    """
    Specifies details of a Job Manager task.

    :param id: A string that uniquely identifies the Job Manager task. A GUID
     is recommended.
    :type id: str
    :param display_name: The display name of the Job Manager task.
    :type display_name: str
    :param command_line: The command line of the Job Manager task.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the Job Manager task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param constraints: Constraints that apply to the Job Manager task.
    :type constraints: :class:`TaskConstraints
     <azure.batch.models.TaskConstraints>`
    :param kill_job_on_completion: Whether completion of the Job Manager task
     signifies completion of the entire job.
    :type kill_job_on_completion: bool
    :param run_elevated: Whether to run the Job Manager task in elevated
     mode. The default value is false.
    :type run_elevated: bool
    :param run_exclusive: Whether the Job Manager task requires exclusive use
     of the compute node where it runs. If true, no other tasks will run on
     the same compute node for as long as the Job Manager is running. If
     false, other tasks can run simultaneously with the Job Manager on a
     compute node. (The Job Manager task counts normally against the node’s
     concurrent task limit, so this is only relevant if the node allows
     multiple concurrent tasks.)
    :type run_exclusive: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'kill_job_on_completion': {'key': 'killJobOnCompletion', 'type': 'bool'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'run_exclusive': {'key': 'runExclusive', 'type': 'bool'},
    }

    def __init__(self, id=None, display_name=None, command_line=None, resource_files=None, environment_settings=None, constraints=None, kill_job_on_completion=None, run_elevated=None, run_exclusive=None):
        self.id = id
        self.display_name = display_name
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.constraints = constraints
        self.kill_job_on_completion = kill_job_on_completion
        self.run_elevated = run_elevated
        self.run_exclusive = run_exclusive
