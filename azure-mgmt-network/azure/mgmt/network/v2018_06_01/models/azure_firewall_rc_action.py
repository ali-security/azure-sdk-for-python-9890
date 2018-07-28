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


class AzureFirewallRCAction(Model):
    """Properties of the AzureFirewallRCAction.

    :param type: The type of action. Possible values include: 'Allow', 'Deny'
    :type type: str or
     ~azure.mgmt.network.v2018_06_01.models.AzureFirewallRCActionType
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureFirewallRCAction, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
