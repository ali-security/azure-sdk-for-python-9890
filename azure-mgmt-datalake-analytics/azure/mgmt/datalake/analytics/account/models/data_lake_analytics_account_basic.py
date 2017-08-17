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


class DataLakeAnalyticsAccountBasic(Resource):
    """A Data Lake Analytics account object, containing all information associated
    with the named Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :ivar provisioning_state: the provisioning status of the Data Lake
     Analytics account. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting',
     'Deleted'
    :vartype provisioning_state: str or :class:`DataLakeAnalyticsAccountStatus
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountStatus>`
    :ivar state: the state of the Data Lake Analytics account. Possible values
     include: 'Active', 'Suspended'
    :vartype state: str or :class:`DataLakeAnalyticsAccountState
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountState>`
    :ivar creation_time: the account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: the account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: the full CName endpoint for this account.
    :vartype endpoint: str
    :ivar account_id: The unique identifier associated with this Data Lake
     Analytics account.
    :vartype account_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'account_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'DataLakeAnalyticsAccountStatus'},
        'state': {'key': 'properties.state', 'type': 'DataLakeAnalyticsAccountState'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
    }

    def __init__(self, location, tags=None):
        super(DataLakeAnalyticsAccountBasic, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
        self.account_id = None
