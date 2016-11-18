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


class RuleAction(Model):
    """The action that is performed when the alert rule becomes active, and when
    an alert condition is resolved.

    :param odata.type: Polymorphic Discriminator
    :type odata.type: str
    """ 

    _validation = {
        'odata.type': {'required': True},
    }

    _attribute_map = {
        'odata.type': {'key': 'odata.type', 'type': 'str'},
    }

    _subtype_map = {
        'odata.type': {'Microsoft.Azure.Management.Insights.Models.RuleEmailAction': 'RuleEmailAction', 'Microsoft.Azure.Management.Insights.Models.RuleWebhookAction': 'RuleWebhookAction'}
    }

    def __init__(self):
        self.odata.type = None
