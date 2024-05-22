# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AssessmentStatusCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Programmatic code for the status of the assessment."""

    HEALTHY = "Healthy"
    """The resource is healthy"""
    UNHEALTHY = "Unhealthy"
    """The resource has a security issue that needs to be addressed"""
    NOT_APPLICABLE = "NotApplicable"
    """Assessment for this resource did not happen"""


class AssessmentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment
    based on custom Azure Policy definition.
    """

    BUILT_IN = "BuiltIn"
    """Microsoft Defender for Cloud managed assessments"""
    CUSTOM_POLICY = "CustomPolicy"
    """User defined policies that are automatically ingested from Azure Policy to Microsoft Defender
    for Cloud"""
    CUSTOMER_MANAGED = "CustomerManaged"
    """User assessments pushed directly by the user or other third party to Microsoft Defender for
    Cloud"""
    VERIFIED_PARTNER = "VerifiedPartner"
    """An assessment that was created by a verified 3rd party if the user connected it to ASC"""


class Categories(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The categories of resource that is at risk when the assessment is unhealthy."""

    COMPUTE = "Compute"
    NETWORKING = "Networking"
    DATA = "Data"
    IDENTITY_AND_ACCESS = "IdentityAndAccess"
    IO_T = "IoT"


class Enum12(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum12."""

    MCAS = "MCAS"
    WDATP = "WDATP"
    SENTINEL = "Sentinel"


class ExpandEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ExpandEnum."""

    LINKS = "links"
    """All links associated with an assessment"""
    METADATA = "metadata"
    """Assessment metadata"""


class ImplementationEffort(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The implementation effort required to remediate this assessment."""

    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"


class SettingKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """the kind of the settings string."""

    DATA_EXPORT_SETTINGS = "DataExportSettings"
    ALERT_SUPPRESSION_SETTING = "AlertSuppressionSetting"
    ALERT_SYNC_SETTINGS = "AlertSyncSettings"


class Severity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The severity level of the assessment."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Source(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The platform where the assessed resource resides."""

    AZURE = "Azure"
    """Resource is in Azure"""
    ON_PREMISE = "OnPremise"
    """Resource in an on premise machine connected to Azure cloud"""
    ON_PREMISE_SQL = "OnPremiseSql"
    """SQL Resource in an on premise machine connected to Azure cloud"""


class Tactics(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tactic of the assessment."""

    RECONNAISSANCE = "Reconnaissance"
    RESOURCE_DEVELOPMENT = "Resource Development"
    INITIAL_ACCESS = "Initial Access"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "Privilege Escalation"
    DEFENSE_EVASION = "Defense Evasion"
    CREDENTIAL_ACCESS = "Credential Access"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "Lateral Movement"
    COLLECTION = "Collection"
    COMMAND_AND_CONTROL = "Command and Control"
    EXFILTRATION = "Exfiltration"
    IMPACT = "Impact"


class Techniques(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Techniques of the assessment."""

    ABUSE_ELEVATION_CONTROL_MECHANISM = "Abuse Elevation Control Mechanism"
    ACCESS_TOKEN_MANIPULATION = "Access Token Manipulation"
    ACCOUNT_DISCOVERY = "Account Discovery"
    ACCOUNT_MANIPULATION = "Account Manipulation"
    ACTIVE_SCANNING = "Active Scanning"
    APPLICATION_LAYER_PROTOCOL = "Application Layer Protocol"
    AUDIO_CAPTURE = "Audio Capture"
    BOOT_OR_LOGON_AUTOSTART_EXECUTION = "Boot or Logon Autostart Execution"
    BOOT_OR_LOGON_INITIALIZATION_SCRIPTS = "Boot or Logon Initialization Scripts"
    BRUTE_FORCE = "Brute Force"
    CLOUD_INFRASTRUCTURE_DISCOVERY = "Cloud Infrastructure Discovery"
    CLOUD_SERVICE_DASHBOARD = "Cloud Service Dashboard"
    CLOUD_SERVICE_DISCOVERY = "Cloud Service Discovery"
    COMMAND_AND_SCRIPTING_INTERPRETER = "Command and Scripting Interpreter"
    COMPROMISE_CLIENT_SOFTWARE_BINARY = "Compromise Client Software Binary"
    COMPROMISE_INFRASTRUCTURE = "Compromise Infrastructure"
    CONTAINER_AND_RESOURCE_DISCOVERY = "Container and Resource Discovery"
    CREATE_ACCOUNT = "Create Account"
    CREATE_OR_MODIFY_SYSTEM_PROCESS = "Create or Modify System Process"
    CREDENTIALS_FROM_PASSWORD_STORES = "Credentials from Password Stores"
    DATA_DESTRUCTION = "Data Destruction"
    DATA_ENCRYPTED_FOR_IMPACT = "Data Encrypted for Impact"
    DATA_FROM_CLOUD_STORAGE_OBJECT = "Data from Cloud Storage Object"
    DATA_FROM_CONFIGURATION_REPOSITORY = "Data from Configuration Repository"
    DATA_FROM_INFORMATION_REPOSITORIES = "Data from Information Repositories"
    DATA_FROM_LOCAL_SYSTEM = "Data from Local System"
    DATA_MANIPULATION = "Data Manipulation"
    DATA_STAGED = "Data Staged"
    DEFACEMENT = "Defacement"
    DEOBFUSCATE_DECODE_FILES_OR_INFORMATION = "Deobfuscate/Decode Files or Information"
    DISK_WIPE = "Disk Wipe"
    DOMAIN_TRUST_DISCOVERY = "Domain Trust Discovery"
    DRIVE_BY_COMPROMISE = "Drive-by Compromise"
    DYNAMIC_RESOLUTION = "Dynamic Resolution"
    ENDPOINT_DENIAL_OF_SERVICE = "Endpoint Denial of Service"
    EVENT_TRIGGERED_EXECUTION = "Event Triggered Execution"
    EXFILTRATION_OVER_ALTERNATIVE_PROTOCOL = "Exfiltration Over Alternative Protocol"
    EXPLOIT_PUBLIC_FACING_APPLICATION = "Exploit Public-Facing Application"
    EXPLOITATION_FOR_CLIENT_EXECUTION = "Exploitation for Client Execution"
    EXPLOITATION_FOR_CREDENTIAL_ACCESS = "Exploitation for Credential Access"
    EXPLOITATION_FOR_DEFENSE_EVASION = "Exploitation for Defense Evasion"
    EXPLOITATION_FOR_PRIVILEGE_ESCALATION = "Exploitation for Privilege Escalation"
    EXPLOITATION_OF_REMOTE_SERVICES = "Exploitation of Remote Services"
    EXTERNAL_REMOTE_SERVICES = "External Remote Services"
    FALLBACK_CHANNELS = "Fallback Channels"
    FILE_AND_DIRECTORY_DISCOVERY = "File and Directory Discovery"
    GATHER_VICTIM_NETWORK_INFORMATION = "Gather Victim Network Information"
    HIDE_ARTIFACTS = "Hide Artifacts"
    HIJACK_EXECUTION_FLOW = "Hijack Execution Flow"
    IMPAIR_DEFENSES = "Impair Defenses"
    IMPLANT_CONTAINER_IMAGE = "Implant Container Image"
    INDICATOR_REMOVAL_ON_HOST = "Indicator Removal on Host"
    INDIRECT_COMMAND_EXECUTION = "Indirect Command Execution"
    INGRESS_TOOL_TRANSFER = "Ingress Tool Transfer"
    INPUT_CAPTURE = "Input Capture"
    INTER_PROCESS_COMMUNICATION = "Inter-Process Communication"
    LATERAL_TOOL_TRANSFER = "Lateral Tool Transfer"
    MAN_IN_THE_MIDDLE = "Man-in-the-Middle"
    MASQUERADING = "Masquerading"
    MODIFY_AUTHENTICATION_PROCESS = "Modify Authentication Process"
    MODIFY_REGISTRY = "Modify Registry"
    NETWORK_DENIAL_OF_SERVICE = "Network Denial of Service"
    NETWORK_SERVICE_SCANNING = "Network Service Scanning"
    NETWORK_SNIFFING = "Network Sniffing"
    NON_APPLICATION_LAYER_PROTOCOL = "Non-Application Layer Protocol"
    NON_STANDARD_PORT = "Non-Standard Port"
    OBTAIN_CAPABILITIES = "Obtain Capabilities"
    OBFUSCATED_FILES_OR_INFORMATION = "Obfuscated Files or Information"
    OFFICE_APPLICATION_STARTUP = "Office Application Startup"
    OS_CREDENTIAL_DUMPING = "OS Credential Dumping"
    PERMISSION_GROUPS_DISCOVERY = "Permission Groups Discovery"
    PHISHING = "Phishing"
    PRE_OS_BOOT = "Pre-OS Boot"
    PROCESS_DISCOVERY = "Process Discovery"
    PROCESS_INJECTION = "Process Injection"
    PROTOCOL_TUNNELING = "Protocol Tunneling"
    PROXY = "Proxy"
    QUERY_REGISTRY = "Query Registry"
    REMOTE_ACCESS_SOFTWARE = "Remote Access Software"
    REMOTE_SERVICE_SESSION_HIJACKING = "Remote Service Session Hijacking"
    REMOTE_SERVICES = "Remote Services"
    REMOTE_SYSTEM_DISCOVERY = "Remote System Discovery"
    RESOURCE_HIJACKING = "Resource Hijacking"
    SCHEDULED_TASK_JOB = "Scheduled Task/Job"
    SCREEN_CAPTURE = "Screen Capture"
    SEARCH_VICTIM_OWNED_WEBSITES = "Search Victim-Owned Websites"
    SERVER_SOFTWARE_COMPONENT = "Server Software Component"
    SERVICE_STOP = "Service Stop"
    SIGNED_BINARY_PROXY_EXECUTION = "Signed Binary Proxy Execution"
    SOFTWARE_DEPLOYMENT_TOOLS = "Software Deployment Tools"
    SQL_STORED_PROCEDURES = "SQL Stored Procedures"
    STEAL_OR_FORGE_KERBEROS_TICKETS = "Steal or Forge Kerberos Tickets"
    SUBVERT_TRUST_CONTROLS = "Subvert Trust Controls"
    SUPPLY_CHAIN_COMPROMISE = "Supply Chain Compromise"
    SYSTEM_INFORMATION_DISCOVERY = "System Information Discovery"
    TAINT_SHARED_CONTENT = "Taint Shared Content"
    TRAFFIC_SIGNALING = "Traffic Signaling"
    TRANSFER_DATA_TO_CLOUD_ACCOUNT = "Transfer Data to Cloud Account"
    TRUSTED_RELATIONSHIP = "Trusted Relationship"
    UNSECURED_CREDENTIALS = "Unsecured Credentials"
    USER_EXECUTION = "User Execution"
    VALID_ACCOUNTS = "Valid Accounts"
    WINDOWS_MANAGEMENT_INSTRUMENTATION = "Windows Management Instrumentation"
    FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION = "File and Directory Permissions Modification"


class Threats(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Threats impact of the assessment."""

    ACCOUNT_BREACH = "accountBreach"
    DATA_EXFILTRATION = "dataExfiltration"
    DATA_SPILLAGE = "dataSpillage"
    MALICIOUS_INSIDER = "maliciousInsider"
    ELEVATION_OF_PRIVILEGE = "elevationOfPrivilege"
    THREAT_RESISTANCE = "threatResistance"
    MISSING_COVERAGE = "missingCoverage"
    DENIAL_OF_SERVICE = "denialOfService"


class UserImpact(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The user impact of the assessment."""

    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
