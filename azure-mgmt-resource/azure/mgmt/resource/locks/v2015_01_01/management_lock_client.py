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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.management_locks_operations import ManagementLocksOperations
from . import models


class ManagementLockClientConfiguration(AzureConfiguration):
    """Configuration for ManagementLockClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ManagementLockClientConfiguration, self).__init__(base_url)

        self.add_user_agent('managementlockclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ManagementLockClient(object):
    """ManagementLockClient

    :ivar config: Configuration for client.
    :vartype config: ManagementLockClientConfiguration

    :ivar management_locks: ManagementLocks operations
    :vartype management_locks: azure.mgmt.resource.locks.v2015_01_01.operations.ManagementLocksOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ManagementLockClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.management_locks = ManagementLocksOperations(
            self._client, self.config, self._serialize, self._deserialize)
