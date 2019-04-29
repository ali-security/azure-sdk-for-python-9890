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

from msrest.paging import Paged


class PublicIPPrefixPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PublicIPPrefix <azure.mgmt.network.v2019_02_01.models.PublicIPPrefix>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PublicIPPrefix]'}
    }

    def __init__(self, *args, **kwargs):

        super(PublicIPPrefixPaged, self).__init__(*args, **kwargs)
