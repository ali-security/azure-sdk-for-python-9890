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


class Match(Model):
    """The match details.

    :param score: Confidence score of the image match.
    :type score: float
    :param match_id: The match id.
    :type match_id: int
    :param source: The source.
    :type source: str
    :param tags: The tags for match details.
    :type tags: list[int]
    :param label: The label.
    :type label: str
    """

    _attribute_map = {
        'score': {'key': 'score', 'type': 'float'},
        'match_id': {'key': 'matchId', 'type': 'int'},
        'source': {'key': 'source', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[int]'},
        'label': {'key': 'label', 'type': 'str'},
    }

    def __init__(self, score=None, match_id=None, source=None, tags=None, label=None):
        super(Match, self).__init__()
        self.score = score
        self.match_id = match_id
        self.source = source
        self.tags = tags
        self.label = label
