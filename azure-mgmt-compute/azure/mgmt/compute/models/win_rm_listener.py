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


class WinRMListener(Model):
    """
    Describes Protocol and thumbprint of Windows Remote Management listener

    :param protocol: Gets or sets the Protocol used by WinRM listener.
     Currently only Http and Https are supported. Possible values include:
     'Http', 'Https'
    :type protocol: str or :class:`ProtocolTypes
     <azure.mgmt.compute.models.ProtocolTypes>`
    :param certificate_url: Gets or sets the Certificate URL in KMS for Https
     listeners. Should be null for Http listeners.
    :type certificate_url: str
    """ 

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'ProtocolTypes'},
        'certificate_url': {'key': 'certificateUrl', 'type': 'str'},
    }

    def __init__(self, protocol=None, certificate_url=None):
        self.protocol = protocol
        self.certificate_url = certificate_url
