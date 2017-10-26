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


class Sku(Model):
    """The SKU of the cognitive services account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Gets or sets the sku name. Required for account creation,
     optional for update. Possible values include: 'F0', 'P0', 'P1', 'P2',
     'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6'
    :type name: str or ~azure.mgmt.cognitiveservices.models.SkuName
    :ivar tier: Gets the sku tier. This is based on the SKU name. Possible
     values include: 'Free', 'Standard', 'Premium'
    :vartype tier: str or ~azure.mgmt.cognitiveservices.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
    }

    def __init__(self, name):
        self.name = name
        self.tier = None
