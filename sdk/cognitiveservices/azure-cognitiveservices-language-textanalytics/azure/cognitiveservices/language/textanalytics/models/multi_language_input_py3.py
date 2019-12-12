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


class MultiLanguageInput(Model):
    """MultiLanguageInput.

    :param language: This is the 2 letter ISO 639-1 representation of a
     language. For example, use "en" for English; "es" for Spanish etc.,
    :type language: str
    :param id: Unique, non-empty document identifier.
    :type id: str
    :param text:
    :type text: str
    """

    _attribute_map = {
        'language': {'key': 'language', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
    }

    def __init__(self, *, language: str=None, id: str=None, text: str=None, **kwargs) -> None:
        super(MultiLanguageInput, self).__init__(**kwargs)
        self.language = language
        self.id = id
        self.text = text
