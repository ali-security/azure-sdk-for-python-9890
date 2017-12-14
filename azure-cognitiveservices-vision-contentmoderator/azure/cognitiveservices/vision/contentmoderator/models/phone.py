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


class Phone(Model):
    """Phone Property details.

    :param country_code: CountryCode of the detected Phone number.
    :type country_code: str
    :param text: Detected Phone number.
    :type text: str
    :param index: Index(Location) of the Phone number in the input text
     content.
    :type index: int
    """

    _attribute_map = {
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'index': {'key': 'index', 'type': 'int'},
    }

    def __init__(self, country_code=None, text=None, index=None):
        super(Phone, self).__init__()
        self.country_code = country_code
        self.text = text
        self.index = index
