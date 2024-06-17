# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.mobilenetwork import MobileNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-mobilenetwork
# USAGE
    python sim_bulk_upload.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MobileNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.sims.begin_bulk_upload(
        resource_group_name="rg1",
        sim_group_name="testSimGroup",
        parameters={
            "sims": [
                {
                    "name": "testSim",
                    "properties": {
                        "authenticationKey": "00000000000000000000000000000000",
                        "deviceType": "Video camera",
                        "integratedCircuitCardIdentifier": "8900000000000000000",
                        "internationalMobileSubscriberIdentity": "00000",
                        "operatorKeyCode": "00000000000000000000000000000000",
                        "simPolicy": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/simPolicies/MySimPolicy"
                        },
                        "staticIpConfiguration": [
                            {
                                "attachedDataNetwork": {
                                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/TestPacketCoreCP/packetCoreDataPlanes/TestPacketCoreDP/attachedDataNetworks/TestAttachedDataNetwork"
                                },
                                "slice": {
                                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                                },
                                "staticIp": {"ipv4Address": "2.4.0.1"},
                            }
                        ],
                    },
                },
                {
                    "name": "testSim2",
                    "properties": {
                        "authenticationKey": "00000000000000000000000000000000",
                        "deviceType": "Video camera",
                        "integratedCircuitCardIdentifier": "8900000000000000001",
                        "internationalMobileSubscriberIdentity": "00000",
                        "operatorKeyCode": "00000000000000000000000000000000",
                        "simPolicy": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/simPolicies/MySimPolicy"
                        },
                        "staticIpConfiguration": [
                            {
                                "attachedDataNetwork": {
                                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/TestPacketCoreCP/packetCoreDataPlanes/TestPacketCoreDP/attachedDataNetworks/TestAttachedDataNetwork"
                                },
                                "slice": {
                                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                                },
                                "staticIp": {"ipv4Address": "2.4.0.2"},
                            }
                        ],
                    },
                },
            ]
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mobilenetwork/resource-manager/Microsoft.MobileNetwork/stable/2024-04-01/examples/SimBulkUpload.json
if __name__ == "__main__":
    main()
