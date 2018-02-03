# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class IntegrationRuntimeState(Enum):

    initial = "Initial"
    stopped = "Stopped"
    started = "Started"
    starting = "Starting"
    stopping = "Stopping"
    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"


class IntegrationRuntimeAutoUpdate(Enum):

    on = "On"
    off = "Off"


class ParameterType(Enum):

    object_enum = "Object"
    string = "String"
    int_enum = "Int"
    float_enum = "Float"
    bool_enum = "Bool"
    array = "Array"


class DependencyCondition(Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    skipped = "Skipped"
    completed = "Completed"


class TriggerRuntimeState(Enum):

    started = "Started"
    stopped = "Stopped"
    disabled = "Disabled"


class PipelineRunQueryFilterOperand(Enum):

    pipeline_name = "PipelineName"
    status = "Status"
    run_start = "RunStart"
    run_end = "RunEnd"


class PipelineRunQueryFilterOperator(Enum):

    equals = "Equals"
    not_equals = "NotEquals"
    in_enum = "In"
    not_in = "NotIn"


class PipelineRunQueryOrderByField(Enum):

    run_start = "RunStart"
    run_end = "RunEnd"


class PipelineRunQueryOrder(Enum):

    asc = "ASC"
    desc = "DESC"


class TriggerRunStatus(Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    inprogress = "Inprogress"


class SparkServerType(Enum):

    shark_server = "SharkServer"
    shark_server2 = "SharkServer2"
    spark_thrift_server = "SparkThriftServer"


class SparkThriftTransportProtocol(Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "


class SparkAuthenticationType(Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class ServiceNowAuthenticationType(Enum):

    basic = "Basic"
    oauth2 = "OAuth2"


class PrestoAuthenticationType(Enum):

    anonymous = "Anonymous"
    ldap = "LDAP"


class PhoenixAuthenticationType(Enum):

    anonymous = "Anonymous"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class ImpalaAuthenticationType(Enum):

    anonymous = "Anonymous"
    sasl_username = "SASLUsername"
    username_and_password = "UsernameAndPassword"


class HiveServerType(Enum):

    hive_server1 = "HiveServer1"
    hive_server2 = "HiveServer2"
    hive_thrift_server = "HiveThriftServer"


class HiveThriftTransportProtocol(Enum):

    binary = "Binary"
    sasl = "SASL"
    http = "HTTP "


class HiveAuthenticationType(Enum):

    anonymous = "Anonymous"
    username = "Username"
    username_and_password = "UsernameAndPassword"
    windows_azure_hd_insight_service = "WindowsAzureHDInsightService"


class HBaseAuthenticationType(Enum):

    anonymous = "Anonymous"
    basic = "Basic"


class GoogleBigQueryAuthenticationType(Enum):

    service_authentication = "ServiceAuthentication"
    user_authentication = "UserAuthentication"


class SapHanaAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class SftpAuthenticationType(Enum):

    basic = "Basic"
    ssh_public_key = "SshPublicKey"


class FtpAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class HttpAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    digest = "Digest"
    windows = "Windows"
    client_certificate = "ClientCertificate"


class MongoDbAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class ODataAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class TeradataAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class Db2AuthenticationType(Enum):

    basic = "Basic"


class SybaseAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class DatasetCompressionLevel(Enum):

    optimal = "Optimal"
    fastest = "Fastest"


class JsonFormatFilePattern(Enum):

    set_of_objects = "setOfObjects"
    array_of_objects = "arrayOfObjects"


class TumblingWindowFrequency(Enum):

    minute = "Minute"
    hour = "Hour"


class DayOfWeek(Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class DaysOfWeek(Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class RecurrenceFrequency(Enum):

    not_specified = "NotSpecified"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"


class WebActivityMethod(Enum):

    get = "GET"
    post = "POST"
    put = "PUT"


class CassandraSourceReadConsistencyLevels(Enum):

    all = "ALL"
    each_quorum = "EACH_QUORUM"
    quorum = "QUORUM"
    local_quorum = "LOCAL_QUORUM"
    one = "ONE"
    two = "TWO"
    three = "THREE"
    local_one = "LOCAL_ONE"
    serial = "SERIAL"
    local_serial = "LOCAL_SERIAL"


class StoredProcedureParameterType(Enum):

    string = "String"
    int_enum = "Int"
    decimal_enum = "Decimal"
    guid = "Guid"
    boolean = "Boolean"
    date_enum = "Date"


class SalesforceSourceReadBehavior(Enum):

    query = "Query"
    query_all = "QueryAll"


class SSISExecutionRuntime(Enum):

    x64 = "x64"
    x86 = "x86"


class HDInsightActivityDebugInfoOption(Enum):

    none = "None"
    always = "Always"
    failure = "Failure"


class SalesforceSinkWriteBehavior(Enum):

    insert = "Insert"
    upsert = "Upsert"


class AzureSearchIndexWriteBehaviorType(Enum):

    merge = "Merge"
    upload = "Upload"


class CopyBehaviorType(Enum):

    preserve_hierarchy = "PreserveHierarchy"
    flatten_hierarchy = "FlattenHierarchy"
    merge_files = "MergeFiles"


class PolybaseSettingsRejectType(Enum):

    value = "value"
    percentage = "percentage"


class SapCloudForCustomerSinkWriteBehavior(Enum):

    insert = "Insert"
    update = "Update"


class IntegrationRuntimeType(Enum):

    managed = "Managed"
    self_hosted = "SelfHosted"


class SelfHostedIntegrationRuntimeNodeStatus(Enum):

    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    upgrading = "Upgrading"
    initializing = "Initializing"
    initialize_failed = "InitializeFailed"


class IntegrationRuntimeUpdateResult(Enum):

    succeed = "Succeed"
    fail = "Fail"


class IntegrationRuntimeInternalChannelEncryptionMode(Enum):

    not_set = "NotSet"
    ssl_encrypted = "SslEncrypted"
    not_encrypted = "NotEncrypted"


class ManagedIntegrationRuntimeNodeStatus(Enum):

    starting = "Starting"
    available = "Available"
    recycling = "Recycling"
    unavailable = "Unavailable"


class IntegrationRuntimeSsisCatalogPricingTier(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"


class IntegrationRuntimeLicenseType(Enum):

    base_price = "BasePrice"
    license_included = "LicenseIncluded"


class IntegrationRuntimeAuthKeyName(Enum):

    auth_key1 = "authKey1"
    auth_key2 = "authKey2"
