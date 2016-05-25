# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.classic_administrators_operations import ClassicAdministratorsOperations
from .operations.permissions_operations import PermissionsOperations
from .operations.provider_operations_metadata_operations import ProviderOperationsMetadataOperations
from .operations.role_assignments_operations import RoleAssignmentsOperations
from .operations.role_definitions_operations import RoleDefinitionsOperations
from . import models


class AuthorizationManagementClientConfiguration(AzureConfiguration):
    """Configuration for AuthorizationManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2015-07-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AuthorizationManagementClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('authorizationmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class AuthorizationManagementClient(object):
    """AuthorizationManagementClient

    :ivar config: Configuration for client.
    :vartype config: AuthorizationManagementClientConfiguration

    :ivar classic_administrators: ClassicAdministrators operations
    :vartype classic_administrators: .operations.ClassicAdministratorsOperations
    :ivar permissions: Permissions operations
    :vartype permissions: .operations.PermissionsOperations
    :ivar provider_operations_metadata: ProviderOperationsMetadata operations
    :vartype provider_operations_metadata: .operations.ProviderOperationsMetadataOperations
    :ivar role_assignments: RoleAssignments operations
    :vartype role_assignments: .operations.RoleAssignmentsOperations
    :ivar role_definitions: RoleDefinitions operations
    :vartype role_definitions: .operations.RoleDefinitionsOperations

    :param credentials: Gets Azure subscription credentials.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2015-07-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        self.config = AuthorizationManagementClientConfiguration(credentials, subscription_id, api_version, accept_language, long_running_operation_retry_timeout, generate_client_request_id, base_url, filepath)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.classic_administrators = ClassicAdministratorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.permissions = PermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.provider_operations_metadata = ProviderOperationsMetadataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.role_definitions = RoleDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
