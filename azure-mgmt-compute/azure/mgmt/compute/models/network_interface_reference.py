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

from .sub_resource import SubResource


class NetworkInterfaceReference(SubResource):
    """Describes a network interface reference.

    :param id: Resource Id
    :type id: str
    :param primary: Specifies the primary network interface in case the
     virtual machine has more than 1 network interface.
    :type primary: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'primary': {'key': 'properties.primary', 'type': 'bool'},
    }

    def __init__(self, id=None, primary=None):
        super(NetworkInterfaceReference, self).__init__(id=id)
        self.primary = primary
