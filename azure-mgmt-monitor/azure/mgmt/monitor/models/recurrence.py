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


class Recurrence(Model):
    """The repeating times at which this profile begins. This element is not used
    if the FixedDate element is used.

    :param frequency: the recurrence frequency. How often the schedule
     profile should take effect. This value must be Week, meaning each week
     will have the same set of profiles. Possible values include: 'None',
     'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year'
    :type frequency: str or :class:`RecurrenceFrequency
     <azure.mgmt.monitor.models.RecurrenceFrequency>`
    :param schedule: the scheduling constraints for when the profile begins.
    :type schedule: :class:`RecurrentSchedule
     <azure.mgmt.monitor.models.RecurrentSchedule>`
    """ 

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'schedule': {'key': 'schedule', 'type': 'RecurrentSchedule'},
    }

    def __init__(self, frequency=None, schedule=None):
        self.frequency = frequency
        self.schedule = schedule
