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


class InboundNatPool(SubResource):
    """
    Inbound NAT pool of the loadbalancer

    :param id: Resource Id
    :type id: str
    :param frontend_ip_configuration: Gets or sets a reference to frontend IP
     Addresses
    :type frontend_ip_configuration: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param protocol: Gets or sets the transport potocol for the external
     endpoint. Possible values are Udp or Tcp. Possible values include:
     'Udp', 'Tcp'
    :type protocol: str
    :param frontend_port_range_start: Gets or sets the starting port range
     for the NAT pool. You can spcify any port number you choose, but the
     port numbers specified for each role in the service must be unique.
     Possible values range between 1 and 65535, inclusive
    :type frontend_port_range_start: int
    :param frontend_port_range_end: Gets or sets the ending port range for
     the NAT pool. You can spcify any port number you choose, but the port
     numbers specified for each role in the service must be unique. Possible
     values range between 1 and 65535, inclusive
    :type frontend_port_range_end: int
    :param backend_port: Gets or sets a port used for internal connections on
     the endpoint. The localPort attribute maps the eternal port of the
     endpoint to an internal port on a role. This is useful in scenarios
     where a role must communicate to an internal compotnent on a port that
     is different from the one that is exposed externally. If not specified,
     the value of localPort is the same as the port attribute. Set the value
     of localPort to '*' to automatically assign an unallocated port that is
     discoverable using the runtime API
    :type backend_port: int
    :param provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _validation = {
        'protocol': {'required': True},
        'frontend_port_range_start': {'required': True},
        'frontend_port_range_end': {'required': True},
        'backend_port': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'protocol': {'key': 'properties.protocol', 'type': 'TransportProtocol'},
        'frontend_port_range_start': {'key': 'properties.frontendPortRangeStart', 'type': 'int'},
        'frontend_port_range_end': {'key': 'properties.frontendPortRangeEnd', 'type': 'int'},
        'backend_port': {'key': 'properties.backendPort', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, protocol, frontend_port_range_start, frontend_port_range_end, backend_port, id=None, frontend_ip_configuration=None, provisioning_state=None, name=None, etag=None, **kwargs):
        super(InboundNatPool, self).__init__(id=id, **kwargs)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.protocol = protocol
        self.frontend_port_range_start = frontend_port_range_start
        self.frontend_port_range_end = frontend_port_range_end
        self.backend_port = backend_port
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
