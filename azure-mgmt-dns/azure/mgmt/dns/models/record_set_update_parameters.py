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


class RecordSetUpdateParameters(Model):
    """Parameters supplied to update a Recordset.

    :param record_set: Gets or sets information about the Recordset being
     updated.
    :type record_set: :class:`RecordSet <azure.mgmt.dns.models.RecordSet>`
    """ 

    _attribute_map = {
        'record_set': {'key': 'RecordSet', 'type': 'RecordSet'},
    }

    def __init__(self, record_set=None):
        self.record_set = record_set
