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


class RegistryUpdateParameters(Model):
    """The parameters for updating a container registry.

    :param tags: The tags for the container registry.
    :type tags: dict
    :param admin_user_enabled: The value that indicates whether the admin user
     is enabled.
    :type admin_user_enabled: bool
    :param storage_account: The parameters of a storage account for the
     container registry. Only applicable to Basic SKU. If specified, the
     storage account must be in the same physical location as the container
     registry.
    :type storage_account: :class:`StorageAccountProperties
     <azure.mgmt.containerregistry.v2017_06_01_preview.models.StorageAccountProperties>`
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountProperties'},
    }

    def __init__(self, tags=None, admin_user_enabled=None, storage_account=None):
        self.tags = tags
        self.admin_user_enabled = admin_user_enabled
        self.storage_account = storage_account
