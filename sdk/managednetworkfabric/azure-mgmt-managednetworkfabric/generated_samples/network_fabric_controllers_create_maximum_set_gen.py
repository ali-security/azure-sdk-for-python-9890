# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.managednetworkfabric import ManagedNetworkFabricMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managednetworkfabric
# USAGE
    python network_fabric_controllers_create_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedNetworkFabricMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="1234ABCD-0A1B-1234-5678-123456ABCDEF",
    )

    response = client.network_fabric_controllers.begin_create(
        resource_group_name="example-rg",
        network_fabric_controller_name="example-networkController",
        body={
            "location": "eastus",
            "properties": {
                "annotation": "annotation",
                "infrastructureExpressRouteConnections": [
                    {
                        "expressRouteAuthorizationKey": "1234ABCD-0A1B-1234-5678-123456ABCDEF",
                        "expressRouteCircuitId": "/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourceGroups/example-rg/providers/Microsoft.Network/expressRouteCircuits/expressRouteCircuitName",
                    }
                ],
                "ipv4AddressSpace": "172.253.0.0/19",
                "ipv6AddressSpace": "::/60",
                "isWorkloadManagementNetworkEnabled": "True",
                "managedResourceGroupConfiguration": {"location": "eastus", "name": "managedResourceGroupName"},
                "nfcSku": "Standard",
                "workloadExpressRouteConnections": [
                    {
                        "expressRouteAuthorizationKey": "xxxxx",
                        "expressRouteCircuitId": "/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourceGroups/example-rg/providers/Microsoft.Network/expressRouteCircuits/expressRouteCircuitName",
                    }
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/stable/2023-06-15/examples/NetworkFabricControllers_Create_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
