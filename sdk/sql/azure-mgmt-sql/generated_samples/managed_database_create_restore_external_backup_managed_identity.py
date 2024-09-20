# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python managed_database_create_restore_external_backup_managed_identity.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.managed_databases.begin_create_or_update(
        resource_group_name="Default-SQL-SouthEastAsia",
        managed_instance_name="managedInstance",
        database_name="managedDatabase",
        parameters={
            "location": "southeastasia",
            "properties": {
                "autoCompleteRestore": True,
                "collation": "SQL_Latin1_General_CP1_CI_AS",
                "createMode": "RestoreExternalBackup",
                "lastBackupName": "last_backup_name",
                "storageContainerIdentity": "ManagedIdentity",
                "storageContainerUri": "https://myaccountname.blob.core.windows.net/backups",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2022-08-01-preview/examples/ManagedDatabaseCreateRestoreExternalBackupManagedIdentity.json
if __name__ == "__main__":
    main()
