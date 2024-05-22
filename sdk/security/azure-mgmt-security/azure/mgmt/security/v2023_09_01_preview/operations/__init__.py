# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._azure_dev_ops_orgs_operations import AzureDevOpsOrgsOperations
from ._azure_dev_ops_projects_operations import AzureDevOpsProjectsOperations
from ._azure_dev_ops_repos_operations import AzureDevOpsReposOperations
from ._dev_ops_configurations_operations import DevOpsConfigurationsOperations
from ._git_hub_owners_operations import GitHubOwnersOperations
from ._git_hub_repos_operations import GitHubReposOperations
from ._git_lab_groups_operations import GitLabGroupsOperations
from ._git_lab_subgroups_operations import GitLabSubgroupsOperations
from ._git_lab_projects_operations import GitLabProjectsOperations
from ._dev_ops_operation_results_operations import DevOpsOperationResultsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureDevOpsOrgsOperations",
    "AzureDevOpsProjectsOperations",
    "AzureDevOpsReposOperations",
    "DevOpsConfigurationsOperations",
    "GitHubOwnersOperations",
    "GitHubReposOperations",
    "GitLabGroupsOperations",
    "GitLabSubgroupsOperations",
    "GitLabProjectsOperations",
    "DevOpsOperationResultsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
