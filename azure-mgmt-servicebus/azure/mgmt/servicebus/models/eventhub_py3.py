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

from .resource import Resource


class Eventhub(Resource):
    """Single item in List or Get Event Hub operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar partition_ids: Current number of shards on the Event Hub.
    :vartype partition_ids: list[str]
    :ivar created_at: Exact time the Event Hub was created.
    :vartype created_at: datetime
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    :param message_retention_in_days: Number of days to retain the events for
     this Event Hub, value should be 1 to 7 days
    :type message_retention_in_days: long
    :param partition_count: Number of partitions created for the Event Hub,
     allowed values are from 1 to 32 partitions.
    :type partition_count: long
    :param status: Enumerates the possible values for the status of the Event
     Hub. Possible values include: 'Active', 'Disabled', 'Restoring',
     'SendDisabled', 'ReceiveDisabled', 'Creating', 'Deleting', 'Renaming',
     'Unknown'
    :type status: str or ~azure.mgmt.servicebus.models.EntityStatus
    :param capture_description: Properties of capture description
    :type capture_description:
     ~azure.mgmt.servicebus.models.CaptureDescription
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'partition_ids': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'message_retention_in_days': {'maximum': 7, 'minimum': 1},
        'partition_count': {'maximum': 32, 'minimum': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'partition_ids': {'key': 'properties.partitionIds', 'type': '[str]'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'message_retention_in_days': {'key': 'properties.messageRetentionInDays', 'type': 'long'},
        'partition_count': {'key': 'properties.partitionCount', 'type': 'long'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'capture_description': {'key': 'properties.captureDescription', 'type': 'CaptureDescription'},
    }

    def __init__(self, *, message_retention_in_days: int=None, partition_count: int=None, status=None, capture_description=None, **kwargs) -> None:
        super(Eventhub, self).__init__(**kwargs)
        self.partition_ids = None
        self.created_at = None
        self.updated_at = None
        self.message_retention_in_days = message_retention_in_days
        self.partition_count = partition_count
        self.status = status
        self.capture_description = capture_description
