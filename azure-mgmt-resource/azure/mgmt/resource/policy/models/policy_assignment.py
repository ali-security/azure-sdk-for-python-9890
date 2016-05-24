# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PolicyAssignment(Model):
    """
    The policy definition.

    :param display_name: Gets or sets the policy assignment display name.
    :type display_name: str
    :param policy_definition_id: Gets or sets the policy definition Id.
    :type policy_definition_id: str
    :param scope: Gets or sets the scope at which the policy assignment
     exists.
    :type scope: str
    :param id: Gets or sets the Id of the policy assignment.
    :type id: str
    :param type: Gets or sets the type of the policy assignment.
    :type type: str
    :param name: Gets or sets the name of the policy assignment.
    :type name: str
    """ 

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, display_name=None, policy_definition_id=None, scope=None, id=None, type=None, name=None):
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.id = id
        self.type = type
        self.name = name
