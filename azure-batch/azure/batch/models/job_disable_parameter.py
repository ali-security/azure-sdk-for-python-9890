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


class JobDisableParameter(Model):
    """Options when disabling a job.

    :param disable_tasks: What to do with active tasks associated with the
     job. Values are:
     requeue - Terminate running tasks and requeue them. The tasks will run
     again when the job is enabled.
     terminate - Terminate running tasks. The tasks will not run again.
     wait - Allow currently running tasks to complete. Possible values include:
     'requeue', 'terminate', 'wait'
    :type disable_tasks: str or :class:`DisableJobOption
     <azure.batch.models.DisableJobOption>`
    """

    _validation = {
        'disable_tasks': {'required': True},
    }

    _attribute_map = {
        'disable_tasks': {'key': 'disableTasks', 'type': 'DisableJobOption'},
    }

    def __init__(self, disable_tasks):
        self.disable_tasks = disable_tasks
