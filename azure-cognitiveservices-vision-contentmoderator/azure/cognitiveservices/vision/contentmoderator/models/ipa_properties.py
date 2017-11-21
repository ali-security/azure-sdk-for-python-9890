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


class IPAProperties(Model):
    """IP Address details.

    :param sub_type: Subtype of the detected IP Address.
    :type sub_type: str
    :param text: Detected IP Address.
    :type text: str
    :param index: Index(Location) of the IP Address in the input text content.
    :type index: float
    """

    _attribute_map = {
        'sub_type': {'key': 'subType', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'index': {'key': 'index', 'type': 'float'},
    }

    def __init__(self, sub_type=None, text=None, index=None):
        self.sub_type = sub_type
        self.text = text
        self.index = index
