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


class EventHubCreateOrUpdateParameters(Model):
    """Parameters supplied to the Create Or Update Event Hub operation.

    :param location: Location of the resource.
    :type location: str
    :param type: ARM type of the namespace.
    :type type: str
    :param name: Name of the Event Hub.
    :type name: str
    :param properties:
    :type properties: :class:`EventHubProperties
     <azure.mgmt.eventhub.models.EventHubProperties>`
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'EventHubProperties'},
    }

    def __init__(self, location, type=None, name=None, properties=None):
        self.location = location
        self.type = type
        self.name = name
        self.properties = properties
