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


class AutoscaleProfile(Model):
    """Autoscale profile.

    :param name: the name of the profile.
    :type name: str
    :param capacity: the number of instances that can be used during this
     profile.
    :type capacity: :class:`ScaleCapacity
     <azure.monitor.models.ScaleCapacity>`
    :param rules: the collection of rules that provide the triggers and
     parameters for the scaling action. A maximum of 10 rules can be specified.
    :type rules: list of :class:`ScaleRule <azure.monitor.models.ScaleRule>`
    :param fixed_date: the specific date-time for the profile. This element is
     not used if the Recurrence element is used.
    :type fixed_date: :class:`TimeWindow <azure.monitor.models.TimeWindow>`
    :param recurrence: the repeating times at which this profile begins. This
     element is not used if the FixedDate element is used.
    :type recurrence: :class:`Recurrence <azure.monitor.models.Recurrence>`
    """

    _validation = {
        'name': {'required': True},
        'capacity': {'required': True},
        'rules': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'ScaleCapacity'},
        'rules': {'key': 'rules', 'type': '[ScaleRule]'},
        'fixed_date': {'key': 'fixedDate', 'type': 'TimeWindow'},
        'recurrence': {'key': 'recurrence', 'type': 'Recurrence'},
    }

    def __init__(self, name, capacity, rules, fixed_date=None, recurrence=None):
        self.name = name
        self.capacity = capacity
        self.rules = rules
        self.fixed_date = fixed_date
        self.recurrence = recurrence
