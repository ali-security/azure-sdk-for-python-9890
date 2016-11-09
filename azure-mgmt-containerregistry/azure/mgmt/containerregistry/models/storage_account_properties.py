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


class StorageAccountProperties(Model):
    """The properties of a storage account for a container registry.

    :param name: The name of the storage account.
    :type name: str
    :param access_key: The access key to the storage account.
    :type access_key: str
    """ 

    _validation = {
        'name': {'required': True},
        'access_key': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'access_key': {'key': 'accessKey', 'type': 'str'},
    }

    def __init__(self, name, access_key):
        self.name = name
        self.access_key = access_key
