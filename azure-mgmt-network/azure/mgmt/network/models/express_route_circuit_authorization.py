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

from .sub_resource import SubResource


class ExpressRouteCircuitAuthorization(SubResource):
    """Authorization in a ExpressRouteCircuit resource.

    :param id: Resource Id
    :type id: str
    :param authorization_key: Gets or sets the authorization key
    :type authorization_key: str
    :param authorization_use_status: Gets or sets AuthorizationUseStatus.
     Possible values include: 'Available', 'InUse'
    :type authorization_use_status: str or :class:`AuthorizationUseStatus
     <azure.mgmt.network.models.AuthorizationUseStatus>`
    :param provisioning_state: Gets provisioning state of the PublicIP
     resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'authorization_key': {'key': 'properties.authorizationKey', 'type': 'str'},
        'authorization_use_status': {'key': 'properties.authorizationUseStatus', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, authorization_key=None, authorization_use_status=None, provisioning_state=None, name=None, etag=None):
        super(ExpressRouteCircuitAuthorization, self).__init__(id=id)
        self.authorization_key = authorization_key
        self.authorization_use_status = authorization_use_status
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
