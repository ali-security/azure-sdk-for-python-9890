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


class JobScheduleUpdateParameter(Model):
    """The set of changes to be made to a job schedule.

    :param schedule: The schedule according to which jobs will be created. If
     you do not specify this element, it is equivalent to passing the default
     schedule: that is, a single job scheduled to run immediately.
    :type schedule: ~azure.batch.models.Schedule
    :param job_specification: Details of the jobs to be created on this
     schedule. Updates affect only jobs that are started after the update has
     taken place. Any currently active job continues with the older
     specification.
    :type job_specification: ~azure.batch.models.JobSpecification
    :param metadata: A list of name-value pairs associated with the job
     schedule as metadata. If you do not specify this element, it takes the
     default value of an empty list; in effect, any existing metadata is
     deleted.
    :type metadata: list[~azure.batch.models.MetadataItem]
    """

    _validation = {
        'schedule': {'required': True},
        'job_specification': {'required': True},
    }

    _attribute_map = {
        'schedule': {'key': 'schedule', 'type': 'Schedule'},
        'job_specification': {'key': 'jobSpecification', 'type': 'JobSpecification'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, schedule, job_specification, metadata=None):
        self.schedule = schedule
        self.job_specification = job_specification
        self.metadata = metadata
