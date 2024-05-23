# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.storagecache import StorageCacheManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagecache
# USAGE
    python caches_create_or_update_ldap_only.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageCacheManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.caches.begin_create_or_update(
        resource_group_name="scgroup",
        cache_name="sc1",
        cache={
            "location": "westus",
            "properties": {
                "cacheSizeGB": 3072,
                "directoryServicesSettings": {
                    "usernameDownload": {
                        "credentials": {
                            "bindDn": "cn=ldapadmin,dc=contosoad,dc=contoso,dc=local",
                            "bindPassword": "<bindPassword>",
                        },
                        "extendedGroups": True,
                        "ldapBaseDN": "dc=contosoad,dc=contoso,dc=local",
                        "ldapServer": "192.0.2.12",
                        "usernameSource": "LDAP",
                    }
                },
                "encryptionSettings": {
                    "keyEncryptionKey": {
                        "keyUrl": "https://keyvault-cmk.vault.azure.net/keys/key2048/test",
                        "sourceVault": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.KeyVault/vaults/keyvault-cmk"
                        },
                    }
                },
                "securitySettings": {
                    "accessPolicies": [
                        {
                            "accessRules": [
                                {
                                    "access": "rw",
                                    "rootSquash": False,
                                    "scope": "default",
                                    "submountAccess": True,
                                    "suid": False,
                                }
                            ],
                            "name": "default",
                        }
                    ]
                },
                "subnet": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1",
                "upgradeSettings": {"scheduledTime": "2022-04-26T18:25:43.511Z", "upgradeScheduleEnabled": True},
            },
            "sku": {"name": "Standard_2G"},
            "tags": {"Dept": "Contoso"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/storagecache/resource-manager/Microsoft.StorageCache/stable/2024-03-01/examples/Caches_CreateOrUpdate_ldap_only.json
if __name__ == "__main__":
    main()
