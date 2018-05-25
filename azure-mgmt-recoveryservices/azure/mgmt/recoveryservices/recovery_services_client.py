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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.vault_certificates_operations import VaultCertificatesOperations
from .operations.registered_identities_operations import RegisteredIdentitiesOperations
from .operations.replication_usages_operations import ReplicationUsagesOperations
from .operations.vaults_operations import VaultsOperations
from .operations.operations import Operations
from .operations.vault_extended_info_operations import VaultExtendedInfoOperations
from .operations.usages_operations import UsagesOperations
from . import models


class RecoveryServicesClientConfiguration(AzureConfiguration):
    """Configuration for RecoveryServicesClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription Id.
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

        super(RecoveryServicesClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-recoveryservices/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class RecoveryServicesClient(SDKClient):
    """Recovery Services Client

    :ivar config: Configuration for client.
    :vartype config: RecoveryServicesClientConfiguration

    :ivar vault_certificates: VaultCertificates operations
    :vartype vault_certificates: azure.mgmt.recoveryservices.operations.VaultCertificatesOperations
    :ivar registered_identities: RegisteredIdentities operations
    :vartype registered_identities: azure.mgmt.recoveryservices.operations.RegisteredIdentitiesOperations
    :ivar replication_usages: ReplicationUsages operations
    :vartype replication_usages: azure.mgmt.recoveryservices.operations.ReplicationUsagesOperations
    :ivar vaults: Vaults operations
    :vartype vaults: azure.mgmt.recoveryservices.operations.VaultsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservices.operations.Operations
    :ivar vault_extended_info: VaultExtendedInfo operations
    :vartype vault_extended_info: azure.mgmt.recoveryservices.operations.VaultExtendedInfoOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.recoveryservices.operations.UsagesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = RecoveryServicesClientConfiguration(credentials, subscription_id, base_url)
        super(RecoveryServicesClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.vault_certificates = VaultCertificatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registered_identities = RegisteredIdentitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replication_usages = ReplicationUsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vaults = VaultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vault_extended_info = VaultExtendedInfoOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
