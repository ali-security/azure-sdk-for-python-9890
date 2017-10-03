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


class PrivateRegistryCredentials(Model):
    """Credentials to access a container image in a private repository.

    :param username: User name to login.
    :type username: str
    :param password: Password to login. One of password or
     passwordSecretReference must be specified.
    :type password: str
    :param password_secret_reference: Specifies the location of the password,
     which is a Key Vault Secret. Users can store their secrets in Azure
     KeyVault and pass it to the Batch AI Service to integrate with KeyVault.
     One of password or passwordSecretReference must be specified.
    :type password_secret_reference: :class:`KeyVaultSecretReference
     <azure.mgmt.batchai.models.KeyVaultSecretReference>`
    """

    _validation = {
        'username': {'required': True},
    }

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'password_secret_reference': {'key': 'passwordSecretReference', 'type': 'KeyVaultSecretReference'},
    }

    def __init__(self, username, password=None, password_secret_reference=None):
        self.username = username
        self.password = password
        self.password_secret_reference = password_secret_reference
