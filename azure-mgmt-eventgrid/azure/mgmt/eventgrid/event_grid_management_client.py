# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.event_subscriptions_operations import EventSubscriptionsOperations
from .operations.operations import Operations
from .operations.topics_operations import TopicsOperations
from .operations.topic_types_operations import TopicTypesOperations
from . import models


class EventGridManagementClientConfiguration(AzureConfiguration):
    """Configuration for EventGridManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials that uniquely identify a
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(EventGridManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-eventgrid/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class EventGridManagementClient(object):
    """Azure EventGrid Management Client

    :ivar config: Configuration for client.
    :vartype config: EventGridManagementClientConfiguration

    :ivar event_subscriptions: EventSubscriptions operations
    :vartype event_subscriptions: azure.mgmt.eventgrid.operations.EventSubscriptionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.eventgrid.operations.Operations
    :ivar topics: Topics operations
    :vartype topics: azure.mgmt.eventgrid.operations.TopicsOperations
    :ivar topic_types: TopicTypes operations
    :vartype topic_types: azure.mgmt.eventgrid.operations.TopicTypesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials that uniquely identify a
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = EventGridManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-06-15-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.event_subscriptions = EventSubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.topic_types = TopicTypesOperations(
            self._client, self.config, self._serialize, self._deserialize)
