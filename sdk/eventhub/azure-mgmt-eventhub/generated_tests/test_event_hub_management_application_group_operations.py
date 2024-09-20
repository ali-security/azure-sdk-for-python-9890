# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.eventhub import EventHubManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEventHubManagementApplicationGroupOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(EventHubManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_namespace(self, resource_group):
        response = self.client.application_group.list_by_namespace(
            resource_group_name=resource_group.name,
            namespace_name="str",
            api_version="2022-10-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update_application_group(self, resource_group):
        response = self.client.application_group.create_or_update_application_group(
            resource_group_name=resource_group.name,
            namespace_name="str",
            application_group_name="str",
            parameters={
                "clientAppGroupIdentifier": "str",
                "id": "str",
                "isEnabled": bool,
                "location": "str",
                "name": "str",
                "policies": ["application_group_policy"],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2022-10-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_delete(self, resource_group):
        response = self.client.application_group.delete(
            resource_group_name=resource_group.name,
            namespace_name="str",
            application_group_name="str",
            api_version="2022-10-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.application_group.get(
            resource_group_name=resource_group.name,
            namespace_name="str",
            application_group_name="str",
            api_version="2022-10-01-preview",
        )

        # please add some check logic here by yourself
        # ...
