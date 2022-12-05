# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.servicelinker import ServiceLinkerManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicelinker
# USAGE
    python put_linker.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceLinkerManagementClient(
        credential=DefaultAzureCredential(),
    )

    response = client.linker.begin_create_or_update(
        resource_uri="subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.Web/sites/test-app",
        linker_name="linkName",
        parameters={
            "properties": {
                "authInfo": {
                    "authType": "secret",
                    "name": "name",
                    "secretInfo": {"secretType": "rawValue", "value": "secret"},
                },
                "targetService": {
                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.DBforPostgreSQL/servers/test-pg/databases/test-db",
                    "type": "AzureResource",
                },
                "vNetSolution": {"type": "serviceEndpoint"},
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/servicelinker/resource-manager/Microsoft.ServiceLinker/preview/2022-11-01-preview/examples/PutLinker.json
if __name__ == "__main__":
    main()
