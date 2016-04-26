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

from .resource import Resource


class RestoreRequest(Resource):
    """
    Description of a restore request

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param storage_account_url: SAS URL to the container
    :type storage_account_url: str
    :param blob_name: Name of a blob which contains the backup
    :type blob_name: str
    :param overwrite: True if the restore operation can overwrite target
     site. "True" needed if trying to restore over an existing site.
    :type overwrite: bool
    :param site_name: Name of a site (Web App)
    :type site_name: str
    :param databases: Collection of databses which should be restored. This
     list has to match the list of databases included in the backup.
    :type databases: list of :class:`DatabaseBackupSetting
     <azure.mgmt.web.models.DatabaseBackupSetting>`
    :param ignore_conflicting_host_names: Changes a logic when restoring a
     site with custom domains. If "true", custom domains are removed
     automatically. If "false", custom domains are added to
     the site object when it is being restored, but that might
     fail due to conflicts during the operation.
    :type ignore_conflicting_host_names: bool
    :param operation_type: Operation type. Possible values include:
     'Default', 'Clone', 'Relocation'
    :type operation_type: str
    :param adjust_connection_strings: Gets or sets a flag showing if
     SiteConfig.ConnectionStrings should be set in new site
    :type adjust_connection_strings: bool
    :param hosting_environment: App Service Environment name, if needed (only
     when restoring a site to an App Service Environment)
    :type hosting_environment: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'storage_account_url': {'key': 'properties.storageAccountUrl', 'type': 'str'},
        'blob_name': {'key': 'properties.blobName', 'type': 'str'},
        'overwrite': {'key': 'properties.overwrite', 'type': 'bool'},
        'site_name': {'key': 'properties.siteName', 'type': 'str'},
        'databases': {'key': 'properties.databases', 'type': '[DatabaseBackupSetting]'},
        'ignore_conflicting_host_names': {'key': 'properties.ignoreConflictingHostNames', 'type': 'bool'},
        'operation_type': {'key': 'properties.operationType', 'type': 'BackupRestoreOperationType'},
        'adjust_connection_strings': {'key': 'properties.adjustConnectionStrings', 'type': 'bool'},
        'hosting_environment': {'key': 'properties.hostingEnvironment', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, storage_account_url=None, blob_name=None, overwrite=None, site_name=None, databases=None, ignore_conflicting_host_names=None, operation_type=None, adjust_connection_strings=None, hosting_environment=None):
        super(RestoreRequest, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.storage_account_url = storage_account_url
        self.blob_name = blob_name
        self.overwrite = overwrite
        self.site_name = site_name
        self.databases = databases
        self.ignore_conflicting_host_names = ignore_conflicting_host_names
        self.operation_type = operation_type
        self.adjust_connection_strings = adjust_connection_strings
        self.hosting_environment = hosting_environment
