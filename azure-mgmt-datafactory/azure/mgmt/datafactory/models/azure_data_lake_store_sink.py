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

from .copy_sink import CopySink


class AzureDataLakeStoreSink(CopySink):
    """A copy activity Azure Data Lake Store sink.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param type: Constant filled by server.
    :type type: str
    :param copy_behavior: The type of copy behavior for copy sink. Possible
     values include: 'PreserveHierarchy', 'FlattenHierarchy', 'MergeFiles'
    :type copy_behavior: str or
     ~azure.mgmt.datafactory.models.CopyBehaviorType
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'copy_behavior': {'key': 'copyBehavior', 'type': 'str'},
    }

    def __init__(self, additional_properties=None, write_batch_size=None, write_batch_timeout=None, sink_retry_count=None, sink_retry_wait=None, copy_behavior=None):
        super(AzureDataLakeStoreSink, self).__init__(additional_properties=additional_properties, write_batch_size=write_batch_size, write_batch_timeout=write_batch_timeout, sink_retry_count=sink_retry_count, sink_retry_wait=sink_retry_wait)
        self.copy_behavior = copy_behavior
        self.type = 'AzureDataLakeStoreSink'
