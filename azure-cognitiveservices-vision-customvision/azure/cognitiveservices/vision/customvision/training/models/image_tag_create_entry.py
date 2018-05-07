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


class ImageTagCreateEntry(Model):
    """ImageTagCreateEntry.

    :param image_id:
    :type image_id: str
    :param tag_id:
    :type tag_id: str
    """

    _attribute_map = {
        'image_id': {'key': 'imageId', 'type': 'str'},
        'tag_id': {'key': 'tagId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTagCreateEntry, self).__init__(**kwargs)
        self.image_id = kwargs.get('image_id', None)
        self.tag_id = kwargs.get('tag_id', None)
