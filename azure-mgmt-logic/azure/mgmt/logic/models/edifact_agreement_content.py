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


class EdifactAgreementContent(Model):
    """EdifactAgreementContent.

    :param receive_agreement: The EDIFACT one-way receive agreement.
    :type receive_agreement: :class:`EdifactOneWayAgreement
     <azure.mgmt.logic.models.EdifactOneWayAgreement>`
    :param send_agreement: The EDIFACT one-way send agreement.
    :type send_agreement: :class:`EdifactOneWayAgreement
     <azure.mgmt.logic.models.EdifactOneWayAgreement>`
    """ 

    _attribute_map = {
        'receive_agreement': {'key': 'receiveAgreement', 'type': 'EdifactOneWayAgreement'},
        'send_agreement': {'key': 'sendAgreement', 'type': 'EdifactOneWayAgreement'},
    }

    def __init__(self, receive_agreement=None, send_agreement=None):
        self.receive_agreement = receive_agreement
        self.send_agreement = send_agreement
