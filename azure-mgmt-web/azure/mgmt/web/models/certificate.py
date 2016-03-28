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


class Certificate(Resource):
    """
    App certificate

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param friendly_name: Friendly name of the certificate
    :type friendly_name: str
    :param subject_name: Subject name of the certificate
    :type subject_name: str
    :param host_names: Host names the certificate applies to
    :type host_names: list of str
    :param pfx_blob: Pfx blob
    :type pfx_blob: str
    :param site_name: App name
    :type site_name: str
    :param self_link: Self link
    :type self_link: str
    :param issuer: Certificate issuer
    :type issuer: str
    :param issue_date: Certificate issue Date
    :type issue_date: datetime
    :param expiration_date: Certificate expriration date
    :type expiration_date: datetime
    :param password: Certificate password
    :type password: str
    :param thumbprint: Certificate thumbprint
    :type thumbprint: str
    :param valid: Is the certificate valid?
    :type valid: bool
    :param cer_blob: Raw bytes of .cer file
    :type cer_blob: str
    :param public_key_hash: Public key hash
    :type public_key_hash: str
    :param hosting_environment_profile: Specification for the hosting
     environment (App Service Environment) to use for the certificate
    :type hosting_environment_profile: :class:`HostingEnvironmentProfile
     <azure.mgmt.web.models.HostingEnvironmentProfile>`
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'subject_name': {'key': 'properties.subjectName', 'type': 'str'},
        'host_names': {'key': 'properties.hostNames', 'type': '[str]'},
        'pfx_blob': {'key': 'properties.pfxBlob', 'type': 'str'},
        'site_name': {'key': 'properties.siteName', 'type': 'str'},
        'self_link': {'key': 'properties.selfLink', 'type': 'str'},
        'issuer': {'key': 'properties.issuer', 'type': 'str'},
        'issue_date': {'key': 'properties.issueDate', 'type': 'iso-8601'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'valid': {'key': 'properties.valid', 'type': 'bool'},
        'cer_blob': {'key': 'properties.cerBlob', 'type': 'str'},
        'public_key_hash': {'key': 'properties.publicKeyHash', 'type': 'str'},
        'hosting_environment_profile': {'key': 'properties.hostingEnvironmentProfile', 'type': 'HostingEnvironmentProfile'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, friendly_name=None, subject_name=None, host_names=None, pfx_blob=None, site_name=None, self_link=None, issuer=None, issue_date=None, expiration_date=None, password=None, thumbprint=None, valid=None, cer_blob=None, public_key_hash=None, hosting_environment_profile=None, **kwargs):
        super(Certificate, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.friendly_name = friendly_name
        self.subject_name = subject_name
        self.host_names = host_names
        self.pfx_blob = pfx_blob
        self.site_name = site_name
        self.self_link = self_link
        self.issuer = issuer
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.password = password
        self.thumbprint = thumbprint
        self.valid = valid
        self.cer_blob = cer_blob
        self.public_key_hash = public_key_hash
        self.hosting_environment_profile = hosting_environment_profile
