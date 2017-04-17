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


class StorageProfile(Model):
    """Describes a storage profile.

    :param image_reference: The image reference.
    :type image_reference: :class:`ImageReference
     <azure.mgmt.compute.compute.v2015_06_15.models.ImageReference>`
    :param os_disk: The OS disk.
    :type os_disk: :class:`OSDisk
     <azure.mgmt.compute.compute.v2015_06_15.models.OSDisk>`
    :param data_disks: The data disks.
    :type data_disks: list of :class:`DataDisk
     <azure.mgmt.compute.compute.v2015_06_15.models.DataDisk>`
    """

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'os_disk': {'key': 'osDisk', 'type': 'OSDisk'},
        'data_disks': {'key': 'dataDisks', 'type': '[DataDisk]'},
    }

    def __init__(self, image_reference=None, os_disk=None, data_disks=None):
        self.image_reference = image_reference
        self.os_disk = os_disk
        self.data_disks = data_disks
