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


class ReplicationUsage(Model):
    """Replication usages of a vault.

    :param monitoring_summary: Summary of the replication monitoring data for
     this vault.
    :type monitoring_summary:
     ~azure.mgmt.recoveryservices.models.MonitoringSummary
    :param jobs_summary: Summary of the replication jobs data for this vault.
    :type jobs_summary: ~azure.mgmt.recoveryservices.models.JobsSummary
    :param protected_item_count: Number of replication protected items for
     this vault.
    :type protected_item_count: int
    :param recovery_plan_count: Number of replication recovery plans for this
     vault.
    :type recovery_plan_count: int
    :param registered_servers_count: Number of servers registered to this
     vault.
    :type registered_servers_count: int
    :param recovery_services_provider_auth_type: The authentication type of
     recovery service providers in the vault.
    :type recovery_services_provider_auth_type: int
    """

    _attribute_map = {
        'monitoring_summary': {'key': 'monitoringSummary', 'type': 'MonitoringSummary'},
        'jobs_summary': {'key': 'jobsSummary', 'type': 'JobsSummary'},
        'protected_item_count': {'key': 'protectedItemCount', 'type': 'int'},
        'recovery_plan_count': {'key': 'recoveryPlanCount', 'type': 'int'},
        'registered_servers_count': {'key': 'registeredServersCount', 'type': 'int'},
        'recovery_services_provider_auth_type': {'key': 'recoveryServicesProviderAuthType', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ReplicationUsage, self).__init__(**kwargs)
        self.monitoring_summary = kwargs.get('monitoring_summary', None)
        self.jobs_summary = kwargs.get('jobs_summary', None)
        self.protected_item_count = kwargs.get('protected_item_count', None)
        self.recovery_plan_count = kwargs.get('recovery_plan_count', None)
        self.registered_servers_count = kwargs.get('registered_servers_count', None)
        self.recovery_services_provider_auth_type = kwargs.get('recovery_services_provider_auth_type', None)
