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


class ImageUrlCreateBatch(Model):
    """ImageUrlCreateBatch.

    :param images:
    :type images:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageUrlCreateEntry]
    :param tag_ids:
    :type tag_ids: list[str]
    """

    _attribute_map = {
        'images': {'key': 'images', 'type': '[ImageUrlCreateEntry]'},
        'tag_ids': {'key': 'tagIds', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ImageUrlCreateBatch, self).__init__(**kwargs)
        self.images = kwargs.get('images', None)
        self.tag_ids = kwargs.get('tag_ids', None)
