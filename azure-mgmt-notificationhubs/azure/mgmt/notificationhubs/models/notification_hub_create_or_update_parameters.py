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


class NotificationHubCreateOrUpdateParameters(Model):
    """Parameters supplied to the CreateOrUpdate NotificationHub operation.

    :param location: Gets or sets NotificationHub data center location.
    :type location: str
    :param tags: Gets or sets NotificationHub tags.
    :type tags: dict
    :param properties: Gets or sets properties of the NotificationHub.
    :type properties: :class:`NotificationHubProperties
     <azure.mgmt.notificationhubs.models.NotificationHubProperties>`
    """ 

    _validation = {
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'NotificationHubProperties'},
    }

    def __init__(self, location, properties, tags=None):
        self.location = location
        self.tags = tags
        self.properties = properties
