# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Iterable, Iterator, List, Optional, TypeVar, Union, overload
import urllib.parse
import uuid

from azure.core.exceptions import (ClientAuthenticationError,
                                    HttpResponseError,
                                    ResourceExistsError,
                                    ResourceNotFoundError,
                                    ResourceNotModifiedError,
                                    map_error)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import MessageTemplateClientMixinABC, NotificationMessagesClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any] # pylint: disable=unsubscriptable-object
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_notification_messages_send_request(
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop('content_type', _headers.pop('Content-Type', None))
    api_version: str = kwargs.pop('api_version', _params.pop('api-version', "2024-02-01"))
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/messages/notifications:send"

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if "Repeatability-Request-ID" not in _headers:
        _headers["Repeatability-Request-ID"] = str(uuid.uuid4())
    if "Repeatability-First-Sent" not in _headers:
        _headers["Repeatability-First-Sent"] = _SERIALIZER.serialize_data(
            datetime.datetime.now(datetime.timezone.utc), "rfc-1123")
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_notification_messages_download_media_request(  # pylint: disable=name-too-long
    id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop('api_version', _params.pop('api-version', "2024-02-01"))
    accept = _headers.pop('Accept', "application/octet-stream")

    # Construct URL
    _url = "/messages/streams/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_message_template_list_templates_request(  # pylint: disable=name-too-long
    channel_id: str,
    *,
    maxpagesize: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop('api_version', _params.pop('api-version', "2024-02-01"))
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/messages/channels/{channelId}/templates"
    path_format_arguments = {
        "channelId": _SERIALIZER.url("channel_id", channel_id, 'str'),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if maxpagesize is not None:
        _params['maxpagesize'] = _SERIALIZER.query("maxpagesize", maxpagesize, 'int')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class NotificationMessagesClientOperationsMixin(   # pylint: disable=name-too-long
    NotificationMessagesClientMixinABC
):

    @overload
    def send(
        self,
        body: _models.NotificationContent,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SendMessageResult:
        # pylint: disable=line-too-long
        """Sends a notification message from Business to User.

        :param body: Required.
        :type body: ~azure.communication.messages.models.NotificationContent
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SendMessageResult. The SendMessageResult is compatible with MutableMapping
        :rtype: ~azure.communication.messages.models.SendMessageResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "image":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "kind": "image",
                    "mediaUri": "str",  # A media url for the file. Required if the type is one
                      of the supported media types, e.g. image. Required.
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ],
                    "content": "str"  # Optional. Optional text content.
                }

                # JSON input template for discriminator value "template":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "kind": "template",
                    "template": {
                        "language": "str",  # The template's language, in the ISO 639 format,
                          consist of a two-letter language code followed by an optional two-letter
                          country code, e.g., 'en' or 'en_US'. Required.
                        "name": "str",  # Name of the template. Required.
                        "bindings": message_template_bindings,
                        "values": [
                            message_template_value
                        ]
                    },
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ]
                }

                # JSON input template for discriminator value "whatsApp":
                message_template_bindings = {
                    "kind": "whatsApp",
                    "body": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ],
                    "buttons": [
                        {
                            "refValue": "str",  # The name of the referenced item in the
                              template values. Required.
                            "subType": "str"  # The WhatsApp button sub type. Required.
                              Known values are: "quickReply" and "url".
                        }
                    ],
                    "footer": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ],
                    "header": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ]
                }

                # JSON input template for discriminator value "text":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "content": "str",  # Message content. Required.
                    "kind": "text",
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ]
                }

                # JSON input template you can fill out and use as your body input.
                body = notification_content

                # response body for status code(s): 202
                response == {
                    "receipts": [
                        {
                            "messageId": "str",  # The message id. Required.
                            "to": "str"  # The native external platform user identifier
                              of the recipient. Required.
                        }
                    ]
                }
        """

    @overload
    def send(
        self,
        body: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SendMessageResult:
        """Sends a notification message from Business to User.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SendMessageResult. The SendMessageResult is compatible with MutableMapping
        :rtype: ~azure.communication.messages.models.SendMessageResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 202
                response == {
                    "receipts": [
                        {
                            "messageId": "str",  # The message id. Required.
                            "to": "str"  # The native external platform user identifier
                              of the recipient. Required.
                        }
                    ]
                }
        """

    @overload
    def send(
        self,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SendMessageResult:
        """Sends a notification message from Business to User.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SendMessageResult. The SendMessageResult is compatible with MutableMapping
        :rtype: ~azure.communication.messages.models.SendMessageResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 202
                response == {
                    "receipts": [
                        {
                            "messageId": "str",  # The message id. Required.
                            "to": "str"  # The native external platform user identifier
                              of the recipient. Required.
                        }
                    ]
                }
        """


    @distributed_trace
    def send(
        self,
        body: Union[_models.NotificationContent, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.SendMessageResult:
        # pylint: disable=line-too-long
        """Sends a notification message from Business to User.

        :param body: Is one of the following types: NotificationContent, JSON, IO[bytes] Required.
        :type body: ~azure.communication.messages.models.NotificationContent or JSON or IO[bytes]
        :return: SendMessageResult. The SendMessageResult is compatible with MutableMapping
        :rtype: ~azure.communication.messages.models.SendMessageResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "image":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "kind": "image",
                    "mediaUri": "str",  # A media url for the file. Required if the type is one
                      of the supported media types, e.g. image. Required.
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ],
                    "content": "str"  # Optional. Optional text content.
                }

                # JSON input template for discriminator value "template":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "kind": "template",
                    "template": {
                        "language": "str",  # The template's language, in the ISO 639 format,
                          consist of a two-letter language code followed by an optional two-letter
                          country code, e.g., 'en' or 'en_US'. Required.
                        "name": "str",  # Name of the template. Required.
                        "bindings": message_template_bindings,
                        "values": [
                            message_template_value
                        ]
                    },
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ]
                }

                # JSON input template for discriminator value "whatsApp":
                message_template_bindings = {
                    "kind": "whatsApp",
                    "body": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ],
                    "buttons": [
                        {
                            "refValue": "str",  # The name of the referenced item in the
                              template values. Required.
                            "subType": "str"  # The WhatsApp button sub type. Required.
                              Known values are: "quickReply" and "url".
                        }
                    ],
                    "footer": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ],
                    "header": [
                        {
                            "refValue": "str"  # The name of the referenced item in the
                              template values. Required.
                        }
                    ]
                }

                # JSON input template for discriminator value "text":
                notification_content = {
                    "channelRegistrationId": "str",  # The Channel Registration ID for the
                      Business Identifier. Required.
                    "content": "str",  # Message content. Required.
                    "kind": "text",
                    "to": [
                        "str"  # The native external platform user identifiers of the
                          recipient. Required.
                    ]
                }

                # JSON input template you can fill out and use as your body input.
                body = notification_content

                # response body for status code(s): 202
                response == {
                    "receipts": [
                        {
                            "messageId": "str",  # The message id. Required.
                            "to": "str"  # The native external platform user identifier
                              of the recipient. Required.
                        }
                    ]
                }
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError, 304: ResourceNotModifiedError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop('content_type', _headers.pop('Content-Type', None))
        cls: ClsType[_models.SendMessageResult] = kwargs.pop(
            'cls', None
        )

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_notification_messages_send_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(   # pylint: disable=protected-access
            _request,
            stream=_stream,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Repeatability-Result']=self._deserialize('str', response.headers.get('Repeatability-Result'))
        response_headers['x-ms-client-request-id']=self._deserialize('str', response.headers.get('x-ms-client-request-id'))

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(
                _models.SendMessageResult,
                response.json()
            )

        if cls:
            return cls(pipeline_response, deserialized, response_headers) # type: ignore

        return deserialized  # type: ignore



    @distributed_trace
    def download_media(
        self,
        id: str,
        **kwargs: Any
    ) -> Iterator[bytes]:
        """Download the Media payload from a User to Business message.

        :param id: The stream ID. Required.
        :type id: str
        :return: Iterator[bytes]
        :rtype: Iterator[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Iterator[bytes]] = kwargs.pop(
            'cls', None
        )

        _request = build_notification_messages_download_media_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", True)
        pipeline_response: PipelineResponse = self._client._pipeline.run(   # pylint: disable=protected-access
            _request,
            stream=_stream,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['x-ms-client-request-id']=self._deserialize('str',
                                                                    response.headers.get('x-ms-client-request-id'))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers) # type: ignore

        return deserialized  # type: ignore

class MessageTemplateClientOperationsMixin(
    MessageTemplateClientMixinABC
):

    @distributed_trace
    def list_templates(
        self,
        channel_id: str,
        **kwargs: Any
    ) -> Iterable["_models.MessageTemplateItem"]:
        # pylint: disable=line-too-long
        """List all templates for given Azure Communication Services channel.

        :param channel_id: The registration ID of the channel. Required.
        :type channel_id: str
        :return: An iterator like instance of MessageTemplateItem
        :rtype: ~azure.core.paging.ItemPaged[~azure.communication.messages.models.MessageTemplateItem]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "whatsApp":
                message_template_item = {
                    "kind": "whatsApp",
                    "language": "str",  # The template's language, in the ISO 639 format, consist
                      of a two-letter language code followed by an optional two-letter country code,
                      e.g., 'en' or 'en_US'. Required.
                    "name": "str",  # The template's name. Required.
                    "status": "str",  # The aggregated template status. Required. Known values
                      are: "approved", "rejected", "pending", and "paused".
                    "content": {}  # Optional. WhatsApp platform's template content. This is the
                      payload returned from WhatsApp API.
                }

                # response body for status code(s): 200
                response == message_template_item
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        maxpagesize = kwargs.pop("maxpagesize", None)
        cls: ClsType[List[_models.MessageTemplateItem]] = kwargs.pop(
            'cls', None
        )

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError, 304: ResourceNotModifiedError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                _request = build_message_template_list_templates_request(
                    channel_id=channel_id,
                    maxpagesize=maxpagesize,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict({
                    key: [urllib.parse.quote(v) for v in value]    for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()})
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest("GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.MessageTemplateItem], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem) # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(   # pylint: disable=protected-access
                _request,
                stream=_stream,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
