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

from msrest.paging import Paged


class ProfilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Profile <azure.mgmt.frontdoor.models.Profile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Profile]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProfilePaged, self).__init__(*args, **kwargs)
class PreconfiguredEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PreconfiguredEndpoint <azure.mgmt.frontdoor.models.PreconfiguredEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PreconfiguredEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(PreconfiguredEndpointPaged, self).__init__(*args, **kwargs)
class ExperimentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Experiment <azure.mgmt.frontdoor.models.Experiment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Experiment]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExperimentPaged, self).__init__(*args, **kwargs)
class FrontDoorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FrontDoor <azure.mgmt.frontdoor.models.FrontDoor>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FrontDoor]'}
    }

    def __init__(self, *args, **kwargs):

        super(FrontDoorPaged, self).__init__(*args, **kwargs)
class FrontendEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FrontendEndpoint <azure.mgmt.frontdoor.models.FrontendEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FrontendEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(FrontendEndpointPaged, self).__init__(*args, **kwargs)
class WebApplicationFirewallPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WebApplicationFirewallPolicy <azure.mgmt.frontdoor.models.WebApplicationFirewallPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WebApplicationFirewallPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(WebApplicationFirewallPolicyPaged, self).__init__(*args, **kwargs)
class ManagedRuleSetDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedRuleSetDefinition <azure.mgmt.frontdoor.models.ManagedRuleSetDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedRuleSetDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedRuleSetDefinitionPaged, self).__init__(*args, **kwargs)
