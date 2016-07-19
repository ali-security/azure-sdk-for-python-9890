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


class FirewallRule(Model):
    """Data Lake Store firewall rule information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: the firewall rule's name.
    :type name: str
    :ivar type: the namespace and type of the firewall Rule.
    :vartype type: str
    :param id: the firewall rule's subscription ID.
    :type id: str
    :param location: the firewall rule's regional location.
    :type location: str
    :param properties: the properties of the firewall rule.
    :type properties: :class:`FirewallRuleProperties
     <azure.mgmt.datalake.store.account.models.FirewallRuleProperties>`
    """ 

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'FirewallRuleProperties'},
    }

    def __init__(self, name=None, id=None, location=None, properties=None):
        self.name = name
        self.type = None
        self.id = id
        self.location = location
        self.properties = properties
