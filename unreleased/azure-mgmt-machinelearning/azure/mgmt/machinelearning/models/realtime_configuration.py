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


class RealtimeConfiguration(Model):
    """Holds the available configuration options for an Azure ML web service
    endpoint.

    :param max_concurrent_calls: Maximum number of concurrent calls allowed
     on the realtime endpoint.
    :type max_concurrent_calls: int
    """ 

    _validation = {
        'max_concurrent_calls': {'maximum': 200, 'minimum': 4},
    }

    _attribute_map = {
        'max_concurrent_calls': {'key': 'maxConcurrentCalls', 'type': 'int'},
    }

    def __init__(self, max_concurrent_calls=None):
        self.max_concurrent_calls = max_concurrent_calls
