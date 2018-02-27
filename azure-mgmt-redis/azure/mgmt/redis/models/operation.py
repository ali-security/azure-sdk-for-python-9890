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


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that describes the operation.
    :type display: ~azure.mgmt.redis.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, name=None, display=None):
        super(Operation, self).__init__()
        self.name = name
        self.display = display
