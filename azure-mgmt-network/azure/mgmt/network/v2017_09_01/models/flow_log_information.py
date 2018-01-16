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


class FlowLogInformation(Model):
    """Information on the configuration of flow log.

    :param target_resource_id: The ID of the resource to configure for flow
     logging.
    :type target_resource_id: str
    :param storage_id: ID of the storage account which is used to store the
     flow log.
    :type storage_id: str
    :param enabled: Flag to enable/disable flow logging.
    :type enabled: bool
    :param retention_policy:
    :type retention_policy:
     ~azure.mgmt.network.v2017_09_01.models.RetentionPolicyParameters
    """

    _validation = {
        'target_resource_id': {'required': True},
        'storage_id': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'storage_id': {'key': 'properties.storageId', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'retention_policy': {'key': 'properties.retentionPolicy', 'type': 'RetentionPolicyParameters'},
    }

    def __init__(self, target_resource_id, storage_id, enabled, retention_policy=None):
        super(FlowLogInformation, self).__init__()
        self.target_resource_id = target_resource_id
        self.storage_id = storage_id
        self.enabled = enabled
        self.retention_policy = retention_policy
