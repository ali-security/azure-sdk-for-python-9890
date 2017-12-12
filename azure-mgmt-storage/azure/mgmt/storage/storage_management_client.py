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


class StorageManagementClientConfiguration(AzureConfiguration):
    """Configuration for StorageManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
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

        super(StorageManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-storage/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class StorageManagementClient(object):
    """The Azure Storage Management API.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation 
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: StorageManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A dict using operation group name to API version.
    :type profile: dict[str, str]
    """

    DEFAULT_API_VERSION='2017-10-01'
    DEFAULT_PROFILE = None

    DEFAULT_API_VERSION = '2017-10-01'

    def __init__(self, credentials, subscription_id, api_version=DEFAULT_API_VERSION, base_url=None, profile=DEFAULT_PROFILE):

        self.config = StorageManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        self.api_version = api_version
        self.profile = dict(profile) if profile is not None else {}

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-06-15: :mod:`v2015_06_15.models<azure.mgmt.storage.v2015_06_15.models>`
           * 2016-01-01: :mod:`v2016_01_01.models<azure.mgmt.storage.v2016_01_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.storage.v2016_12_01.models>`
           * 2017-06-01: :mod:`v2017_06_01.models<azure.mgmt.storage.v2017_06_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.storage.v2017_10_01.models>`
        """
        if api_version == '2015-06-15':
            from .v2015_06_15 import models
            return models
        elif api_version == '2016-01-01':
            from .v2016_01_01 import models
            return models
        elif api_version == '2016-12-01':
            from .v2016_12_01 import models
            return models
        elif api_version == '2017-06-01':
            from .v2017_06_01 import models
            return models
        elif api_version == '2017-10-01':
            from .v2017_10_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-06-01: :class:`Operations<azure.mgmt.storage.v2017_06_01.operations.Operations>`
           * 2017-10-01: :class:`Operations<azure.mgmt.storage.v2017_10_01.operations.Operations>`
        """
        api_version = self.profile.get('operations', self.api_version)
        if api_version == '2017-06-01':
            from .v2017_06_01.operations import Operations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def skus(self):
        """Instance depends on the API version:

           * 2017-06-01: :class:`SkusOperations<azure.mgmt.storage.v2017_06_01.operations.SkusOperations>`
           * 2017-10-01: :class:`SkusOperations<azure.mgmt.storage.v2017_10_01.operations.SkusOperations>`
        """
        api_version = self.profile.get('skus', self.api_version)
        if api_version == '2017-06-01':
            from .v2017_06_01.operations import SkusOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import SkusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def storage_accounts(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`StorageAccountsOperations<azure.mgmt.storage.v2015_06_15.operations.StorageAccountsOperations>`
           * 2016-01-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2016_01_01.operations.StorageAccountsOperations>`
           * 2016-12-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2016_12_01.operations.StorageAccountsOperations>`
           * 2017-06-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2017_06_01.operations.StorageAccountsOperations>`
           * 2017-10-01: :class:`StorageAccountsOperations<azure.mgmt.storage.v2017_10_01.operations.StorageAccountsOperations>`
        """
        api_version = self.profile.get('storage_accounts', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2016-01-01':
            from .v2016_01_01.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2017-06-01':
            from .v2017_06_01.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import StorageAccountsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def usage(self):
        """Instance depends on the API version:

           * 2015-06-15: :class:`UsageOperations<azure.mgmt.storage.v2015_06_15.operations.UsageOperations>`
           * 2016-01-01: :class:`UsageOperations<azure.mgmt.storage.v2016_01_01.operations.UsageOperations>`
           * 2016-12-01: :class:`UsageOperations<azure.mgmt.storage.v2016_12_01.operations.UsageOperations>`
           * 2017-06-01: :class:`UsageOperations<azure.mgmt.storage.v2017_06_01.operations.UsageOperations>`
           * 2017-10-01: :class:`UsageOperations<azure.mgmt.storage.v2017_10_01.operations.UsageOperations>`
        """
        api_version = self.profile.get('usage', self.api_version)
        if api_version == '2015-06-15':
            from .v2015_06_15.operations import UsageOperations as OperationClass
        elif api_version == '2016-01-01':
            from .v2016_01_01.operations import UsageOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import UsageOperations as OperationClass
        elif api_version == '2017-06-01':
            from .v2017_06_01.operations import UsageOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import UsageOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
