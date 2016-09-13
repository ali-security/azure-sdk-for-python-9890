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


class AssetLocation(Model):
    """Describes the access location for a web service asset.

    :param uri: The URI where the asset is accessible from, (e.g. aml://abc
     for system assets or https://xyz for user asets
    :type uri: str
    :param credentials: Access credentials for the asset, if applicable (e.g.
     asset specified by storage account connection string + blob URI)
    :type credentials: str
    """ 

    _validation = {
        'uri': {'required': True},
    }

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'str'},
    }

    def __init__(self, uri, credentials=None):
        self.uri = uri
        self.credentials = credentials
