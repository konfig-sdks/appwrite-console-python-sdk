# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean.post import CreateBooleanAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections.post import CreateCollection
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime.post import CreateDatetimeAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents.post import CreateDocument
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email.post import CreateEmailAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum.post import CreateEnumAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float.post import CreateFloatAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_indexes.post import CreateIndexOnAttributes
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer.post import CreateIntegerAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip.post import CreateIpAttribute
from appwrite_console_python_sdk.paths.databases.post import CreateNewDatabase
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_relationship.post import CreateRelationshipAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string.post import CreateStringAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url.post import CreateUrlAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.delete import DeleteAttributeById
from appwrite_console_python_sdk.paths.databases_database_id.delete import DeleteById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id.delete import DeleteCollectionById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.delete import DeleteDocumentById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.delete import DeleteIndexByKey
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key.get import GetAttributeById
from appwrite_console_python_sdk.paths.databases_database_id.get import GetById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id.get import GetCollectionById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_usage.get import GetCollectionUsageStats
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.get import GetDocumentById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents.get import GetDocuments
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_indexes_key.get import GetIndexById
from appwrite_console_python_sdk.paths.databases_usage.get import GetUsageStats
from appwrite_console_python_sdk.paths.databases_database_id_usage.get import GetUsageStats0
from appwrite_console_python_sdk.paths.databases.get import ListAllDatabases
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes.get import ListAttributes
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_indexes.get import ListCollectionIndexes
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_logs.get import ListCollectionLogs
from appwrite_console_python_sdk.paths.databases_database_id_collections.get import ListCollections
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id_logs.get import ListDocumentLogs
from appwrite_console_python_sdk.paths.databases_database_id_logs.get import ListLogs
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_datetime_key.patch import PatchDateTimeAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_boolean_key.patch import UpdateBooleanAttribute
from appwrite_console_python_sdk.paths.databases_database_id.put import UpdateById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id.put import UpdateCollectionById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_documents_document_id.patch import UpdateDocumentById
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_email_key.patch import UpdateEmailAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_enum_key.patch import UpdateEnumAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_float_key.patch import UpdateFloatAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_integer_key.patch import UpdateIntegerAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_ip_key.patch import UpdateIpAddressAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_key_relationship.patch import UpdateRelationshipAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_string_key.patch import UpdateStringAttribute
from appwrite_console_python_sdk.paths.databases_database_id_collections_collection_id_attributes_url_key.patch import UpdateUrlAttribute
from appwrite_console_python_sdk.apis.tags.databases_api_raw import DatabasesApiRaw


class DatabasesApi(
    CreateBooleanAttribute,
    CreateCollection,
    CreateDatetimeAttribute,
    CreateDocument,
    CreateEmailAttribute,
    CreateEnumAttribute,
    CreateFloatAttribute,
    CreateIndexOnAttributes,
    CreateIntegerAttribute,
    CreateIpAttribute,
    CreateNewDatabase,
    CreateRelationshipAttribute,
    CreateStringAttribute,
    CreateUrlAttribute,
    DeleteAttributeById,
    DeleteById,
    DeleteCollectionById,
    DeleteDocumentById,
    DeleteIndexByKey,
    GetAttributeById,
    GetById,
    GetCollectionById,
    GetCollectionUsageStats,
    GetDocumentById,
    GetDocuments,
    GetIndexById,
    GetUsageStats,
    GetUsageStats0,
    ListAllDatabases,
    ListAttributes,
    ListCollectionIndexes,
    ListCollectionLogs,
    ListCollections,
    ListDocumentLogs,
    ListLogs,
    PatchDateTimeAttribute,
    UpdateBooleanAttribute,
    UpdateById,
    UpdateCollectionById,
    UpdateDocumentById,
    UpdateEmailAttribute,
    UpdateEnumAttribute,
    UpdateFloatAttribute,
    UpdateIntegerAttribute,
    UpdateIpAddressAttribute,
    UpdateRelationshipAttribute,
    UpdateStringAttribute,
    UpdateUrlAttribute,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DatabasesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DatabasesApiRaw(api_client)
