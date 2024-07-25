# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementVirtualMachineExtensionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create_or_update(self, resource_group):
        response = self.client.virtual_machine_extensions.begin_create_or_update(
            resource_group_name=resource_group.name,
            vm_name="str",
            vm_extension_name="str",
            extension_parameters={
                "location": "str",
                "autoUpgradeMinorVersion": bool,
                "forceUpdateTag": "str",
                "id": "str",
                "instanceView": {
                    "name": "str",
                    "statuses": [
                        {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    ],
                    "substatuses": [
                        {
                            "code": "str",
                            "displayStatus": "str",
                            "level": "str",
                            "message": "str",
                            "time": "2020-02-20 00:00:00",
                        }
                    ],
                    "type": "str",
                    "typeHandlerVersion": "str",
                },
                "name": "str",
                "protectedSettings": {},
                "provisioningState": "str",
                "publisher": "str",
                "settings": {},
                "tags": {"str": "str"},
                "type": "str",
                "typeHandlerVersion": "str",
            },
            api_version="2015-06-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.virtual_machine_extensions.begin_update(
            resource_group_name=resource_group.name,
            vm_name="str",
            vm_extension_name="str",
            extension_parameters={
                "autoUpgradeMinorVersion": bool,
                "forceUpdateTag": "str",
                "protectedSettings": {},
                "publisher": "str",
                "settings": {},
                "tags": {"str": "str"},
                "type": "str",
                "typeHandlerVersion": "str",
            },
            api_version="2015-06-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.virtual_machine_extensions.begin_delete(
            resource_group_name=resource_group.name,
            vm_name="str",
            vm_extension_name="str",
            api_version="2015-06-15",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.virtual_machine_extensions.get(
            resource_group_name=resource_group.name,
            vm_name="str",
            vm_extension_name="str",
            api_version="2015-06-15",
        )

        # please add some check logic here by yourself
        # ...
