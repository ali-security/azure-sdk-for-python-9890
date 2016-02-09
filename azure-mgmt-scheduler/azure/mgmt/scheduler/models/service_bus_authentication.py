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


class ServiceBusAuthentication(Model):
    """ServiceBusAuthentication

    :param str sas_key: Gets or sets the SAS key.
    :param str sas_key_name: Gets or sets the SAS key name.
    :param str type: Gets or sets the authentication type. Possible values
     include: 'NotSpecified', 'SharedAccessKey'
    """

    _required = []

    _attribute_map = {
        'sas_key': {'key': 'sasKey', 'type': 'str'},
        'sas_key_name': {'key': 'sasKeyName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ServiceBusAuthenticationType'},
    }

    def __init__(self, sas_key=None, sas_key_name=None, type=None):
        self.sas_key = sas_key
        self.sas_key_name = sas_key_name
        self.type = type
