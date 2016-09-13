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


class Cost(Model):
    """A cost item.

    :param currency_code: The currency code of the cost.
    :type currency_code: str
    :param costs: The lab cost component of the cost data.
    :type costs: list of :class:`CostPerDayProperties
     <azure.mgmt.devtestlabs.models.CostPerDayProperties>`
    :param resource_costs: The resource cost component of the cost data.
    :type resource_costs: list of :class:`ResourceCostProperties
     <azure.mgmt.devtestlabs.models.ResourceCostProperties>`
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    """ 

    _attribute_map = {
        'currency_code': {'key': 'properties.currencyCode', 'type': 'str'},
        'costs': {'key': 'properties.costs', 'type': '[CostPerDayProperties]'},
        'resource_costs': {'key': 'properties.resourceCosts', 'type': '[ResourceCostProperties]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, currency_code=None, costs=None, resource_costs=None, id=None, name=None, type=None, location=None, tags=None):
        self.currency_code = currency_code
        self.costs = costs
        self.resource_costs = resource_costs
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
