# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import QuestionAnsweringClientConfiguration
from .operations import QuestionAnsweringClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import AzureKeyCredential
    from azure.core.rest import HttpRequest, HttpResponse


class QuestionAnsweringClient(QuestionAnsweringClientOperationsMixin):
    """The language service API is a suite of natural language processing (NLP) skills built with best-in-class Microsoft machine learning algorithms.  The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction, language detection and question answering. Further documentation can be found in :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview">https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview</a>`.

    :param endpoint: Supported Cognitive Services endpoint (e.g.,
         https://:code:`<resource-name>`.api.cognitiveservices.azure.com).
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    """

    def __init__(
        self,
        endpoint,  # type: str
        credential,  # type: AzureKeyCredential
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = "{Endpoint}/language"
        self._config = QuestionAnsweringClientConfiguration(credential, endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False

    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.ai.language.questionanswering.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.ai.language.questionanswering.rest import build_query_knowledgebase_request
        >>> request = build_query_knowledgebase_request(project_name=project_name, json=json, content=content, deployment_name=deployment_name, **kwargs)
        <HttpRequest [POST], url: '/:query-knowledgebases'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> QuestionAnsweringClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
