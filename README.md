<div align="center">

[![Visit Appwrite](./header.png)](https://appwrite.io)

# Appwrite<a id="appwrite"></a>

Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`appwriteconsole.account.add_authenticator_app`](#appwriteconsoleaccountadd_authenticator_app)
  * [`appwriteconsole.account.complete_email_verification`](#appwriteconsoleaccountcomplete_email_verification)
  * [`appwriteconsole.account.complete_mfa_challenge`](#appwriteconsoleaccountcomplete_mfa_challenge)
  * [`appwriteconsole.account.complete_password_recovery`](#appwriteconsoleaccountcomplete_password_recovery)
  * [`appwriteconsole.account.confirm_phone_verification`](#appwriteconsoleaccountconfirm_phone_verification)
  * [`appwriteconsole.account.create_anonymous_session`](#appwriteconsoleaccountcreate_anonymous_session)
  * [`appwriteconsole.account.create_email_password_session`](#appwriteconsoleaccountcreate_email_password_session)
  * [`appwriteconsole.account.create_email_token`](#appwriteconsoleaccountcreate_email_token)
  * [`appwriteconsole.account.create_email_verification`](#appwriteconsoleaccountcreate_email_verification)
  * [`appwriteconsole.account.create_jwt`](#appwriteconsoleaccountcreate_jwt)
  * [`appwriteconsole.account.create_magic_url_token`](#appwriteconsoleaccountcreate_magic_url_token)
  * [`appwriteconsole.account.create_mfa_challenge`](#appwriteconsoleaccountcreate_mfa_challenge)
  * [`appwriteconsole.account.create_new_user`](#appwriteconsoleaccountcreate_new_user)
  * [`appwriteconsole.account.create_o_auth2_session`](#appwriteconsoleaccountcreate_o_auth2_session)
  * [`appwriteconsole.account.create_o_auth2_token`](#appwriteconsoleaccountcreate_o_auth2_token)
  * [`appwriteconsole.account.create_password_recovery`](#appwriteconsoleaccountcreate_password_recovery)
  * [`appwriteconsole.account.create_phone_token`](#appwriteconsoleaccountcreate_phone_token)
  * [`appwriteconsole.account.create_push_target`](#appwriteconsoleaccountcreate_push_target)
  * [`appwriteconsole.account.create_session_from_token`](#appwriteconsoleaccountcreate_session_from_token)
  * [`appwriteconsole.account.delete_authenticator_by_id`](#appwriteconsoleaccountdelete_authenticator_by_id)
  * [`appwriteconsole.account.delete_identity_by_id`](#appwriteconsoleaccountdelete_identity_by_id)
  * [`appwriteconsole.account.delete_push_target`](#appwriteconsoleaccountdelete_push_target)
  * [`appwriteconsole.account.delete_sessions`](#appwriteconsoleaccountdelete_sessions)
  * [`appwriteconsole.account.delete_user`](#appwriteconsoleaccountdelete_user)
  * [`appwriteconsole.account.extend_session_length`](#appwriteconsoleaccountextend_session_length)
  * [`appwriteconsole.account.generate_recovery_codes`](#appwriteconsoleaccountgenerate_recovery_codes)
  * [`appwriteconsole.account.get_mfa_recovery_codes`](#appwriteconsoleaccountget_mfa_recovery_codes)
  * [`appwriteconsole.account.get_prefs_operation`](#appwriteconsoleaccountget_prefs_operation)
  * [`appwriteconsole.account.get_session`](#appwriteconsoleaccountget_session)
  * [`appwriteconsole.account.get_user`](#appwriteconsoleaccountget_user)
  * [`appwriteconsole.account.list_identities`](#appwriteconsoleaccountlist_identities)
  * [`appwriteconsole.account.list_mfa_factors`](#appwriteconsoleaccountlist_mfa_factors)
  * [`appwriteconsole.account.list_sessions`](#appwriteconsoleaccountlist_sessions)
  * [`appwriteconsole.account.list_user_logs`](#appwriteconsoleaccountlist_user_logs)
  * [`appwriteconsole.account.logout_session`](#appwriteconsoleaccountlogout_session)
  * [`appwriteconsole.account.regenerate_mfa_recovery_codes`](#appwriteconsoleaccountregenerate_mfa_recovery_codes)
  * [`appwriteconsole.account.send_verification_sms`](#appwriteconsoleaccountsend_verification_sms)
  * [`appwriteconsole.account.update_email_address`](#appwriteconsoleaccountupdate_email_address)
  * [`appwriteconsole.account.update_magic_url_session`](#appwriteconsoleaccountupdate_magic_url_session)
  * [`appwriteconsole.account.update_mfa_status`](#appwriteconsoleaccountupdate_mfa_status)
  * [`appwriteconsole.account.update_name`](#appwriteconsoleaccountupdate_name)
  * [`appwriteconsole.account.update_password`](#appwriteconsoleaccountupdate_password)
  * [`appwriteconsole.account.update_phone`](#appwriteconsoleaccountupdate_phone)
  * [`appwriteconsole.account.update_phone_session`](#appwriteconsoleaccountupdate_phone_session)
  * [`appwriteconsole.account.update_prefs_operation`](#appwriteconsoleaccountupdate_prefs_operation)
  * [`appwriteconsole.account.update_push_target`](#appwriteconsoleaccountupdate_push_target)
  * [`appwriteconsole.account.update_status`](#appwriteconsoleaccountupdate_status)
  * [`appwriteconsole.account.verify_authenticator`](#appwriteconsoleaccountverify_authenticator)
  * [`appwriteconsole.assistant.ask_query`](#appwriteconsoleassistantask_query)
  * [`appwriteconsole.avatars.generate_qr_code`](#appwriteconsoleavatarsgenerate_qr_code)
  * [`appwriteconsole.avatars.get_browser_icon`](#appwriteconsoleavatarsget_browser_icon)
  * [`appwriteconsole.avatars.get_credit_card_icon`](#appwriteconsoleavatarsget_credit_card_icon)
  * [`appwriteconsole.avatars.get_favicon`](#appwriteconsoleavatarsget_favicon)
  * [`appwriteconsole.avatars.get_flag_by_code`](#appwriteconsoleavatarsget_flag_by_code)
  * [`appwriteconsole.avatars.get_image_url_and_crop`](#appwriteconsoleavatarsget_image_url_and_crop)
  * [`appwriteconsole.avatars.get_user_initials`](#appwriteconsoleavatarsget_user_initials)
  * [`appwriteconsole.console.list_variables`](#appwriteconsoleconsolelist_variables)
  * [`appwriteconsole.databases.create_boolean_attribute`](#appwriteconsoledatabasescreate_boolean_attribute)
  * [`appwriteconsole.databases.create_collection`](#appwriteconsoledatabasescreate_collection)
  * [`appwriteconsole.databases.create_datetime_attribute`](#appwriteconsoledatabasescreate_datetime_attribute)
  * [`appwriteconsole.databases.create_document`](#appwriteconsoledatabasescreate_document)
  * [`appwriteconsole.databases.create_email_attribute`](#appwriteconsoledatabasescreate_email_attribute)
  * [`appwriteconsole.databases.create_enum_attribute`](#appwriteconsoledatabasescreate_enum_attribute)
  * [`appwriteconsole.databases.create_float_attribute`](#appwriteconsoledatabasescreate_float_attribute)
  * [`appwriteconsole.databases.create_index_on_attributes`](#appwriteconsoledatabasescreate_index_on_attributes)
  * [`appwriteconsole.databases.create_integer_attribute`](#appwriteconsoledatabasescreate_integer_attribute)
  * [`appwriteconsole.databases.create_ip_attribute`](#appwriteconsoledatabasescreate_ip_attribute)
  * [`appwriteconsole.databases.create_new_database`](#appwriteconsoledatabasescreate_new_database)
  * [`appwriteconsole.databases.create_relationship_attribute`](#appwriteconsoledatabasescreate_relationship_attribute)
  * [`appwriteconsole.databases.create_string_attribute`](#appwriteconsoledatabasescreate_string_attribute)
  * [`appwriteconsole.databases.create_url_attribute`](#appwriteconsoledatabasescreate_url_attribute)
  * [`appwriteconsole.databases.delete_attribute_by_id`](#appwriteconsoledatabasesdelete_attribute_by_id)
  * [`appwriteconsole.databases.delete_by_id`](#appwriteconsoledatabasesdelete_by_id)
  * [`appwriteconsole.databases.delete_collection_by_id`](#appwriteconsoledatabasesdelete_collection_by_id)
  * [`appwriteconsole.databases.delete_document_by_id`](#appwriteconsoledatabasesdelete_document_by_id)
  * [`appwriteconsole.databases.delete_index_by_key`](#appwriteconsoledatabasesdelete_index_by_key)
  * [`appwriteconsole.databases.get_attribute_by_id`](#appwriteconsoledatabasesget_attribute_by_id)
  * [`appwriteconsole.databases.get_by_id`](#appwriteconsoledatabasesget_by_id)
  * [`appwriteconsole.databases.get_collection_by_id`](#appwriteconsoledatabasesget_collection_by_id)
  * [`appwriteconsole.databases.get_collection_usage_stats`](#appwriteconsoledatabasesget_collection_usage_stats)
  * [`appwriteconsole.databases.get_document_by_id`](#appwriteconsoledatabasesget_document_by_id)
  * [`appwriteconsole.databases.get_documents`](#appwriteconsoledatabasesget_documents)
  * [`appwriteconsole.databases.get_index_by_id`](#appwriteconsoledatabasesget_index_by_id)
  * [`appwriteconsole.databases.get_usage_stats`](#appwriteconsoledatabasesget_usage_stats)
  * [`appwriteconsole.databases.get_usage_stats_0`](#appwriteconsoledatabasesget_usage_stats_0)
  * [`appwriteconsole.databases.list_all_databases`](#appwriteconsoledatabaseslist_all_databases)
  * [`appwriteconsole.databases.list_attributes`](#appwriteconsoledatabaseslist_attributes)
  * [`appwriteconsole.databases.list_collection_indexes`](#appwriteconsoledatabaseslist_collection_indexes)
  * [`appwriteconsole.databases.list_collection_logs`](#appwriteconsoledatabaseslist_collection_logs)
  * [`appwriteconsole.databases.list_collections`](#appwriteconsoledatabaseslist_collections)
  * [`appwriteconsole.databases.list_document_logs`](#appwriteconsoledatabaseslist_document_logs)
  * [`appwriteconsole.databases.list_logs`](#appwriteconsoledatabaseslist_logs)
  * [`appwriteconsole.databases.patch_date_time_attribute`](#appwriteconsoledatabasespatch_date_time_attribute)
  * [`appwriteconsole.databases.update_boolean_attribute`](#appwriteconsoledatabasesupdate_boolean_attribute)
  * [`appwriteconsole.databases.update_by_id`](#appwriteconsoledatabasesupdate_by_id)
  * [`appwriteconsole.databases.update_collection_by_id`](#appwriteconsoledatabasesupdate_collection_by_id)
  * [`appwriteconsole.databases.update_document_by_id`](#appwriteconsoledatabasesupdate_document_by_id)
  * [`appwriteconsole.databases.update_email_attribute`](#appwriteconsoledatabasesupdate_email_attribute)
  * [`appwriteconsole.databases.update_enum_attribute`](#appwriteconsoledatabasesupdate_enum_attribute)
  * [`appwriteconsole.databases.update_float_attribute`](#appwriteconsoledatabasesupdate_float_attribute)
  * [`appwriteconsole.databases.update_integer_attribute`](#appwriteconsoledatabasesupdate_integer_attribute)
  * [`appwriteconsole.databases.update_ip_address_attribute`](#appwriteconsoledatabasesupdate_ip_address_attribute)
  * [`appwriteconsole.databases.update_relationship_attribute`](#appwriteconsoledatabasesupdate_relationship_attribute)
  * [`appwriteconsole.databases.update_string_attribute`](#appwriteconsoledatabasesupdate_string_attribute)
  * [`appwriteconsole.databases.update_url_attribute`](#appwriteconsoledatabasesupdate_url_attribute)
  * [`appwriteconsole.functions.create_deployment`](#appwriteconsolefunctionscreate_deployment)
  * [`appwriteconsole.functions.create_function`](#appwriteconsolefunctionscreate_function)
  * [`appwriteconsole.functions.create_variable`](#appwriteconsolefunctionscreate_variable)
  * [`appwriteconsole.functions.delete_deployment`](#appwriteconsolefunctionsdelete_deployment)
  * [`appwriteconsole.functions.delete_function_by_id`](#appwriteconsolefunctionsdelete_function_by_id)
  * [`appwriteconsole.functions.delete_variable_by_id`](#appwriteconsolefunctionsdelete_variable_by_id)
  * [`appwriteconsole.functions.download_deployment_contents`](#appwriteconsolefunctionsdownload_deployment_contents)
  * [`appwriteconsole.functions.get_by_id`](#appwriteconsolefunctionsget_by_id)
  * [`appwriteconsole.functions.get_deployment_by_id`](#appwriteconsolefunctionsget_deployment_by_id)
  * [`appwriteconsole.functions.get_execution_log`](#appwriteconsolefunctionsget_execution_log)
  * [`appwriteconsole.functions.get_function_usage`](#appwriteconsolefunctionsget_function_usage)
  * [`appwriteconsole.functions.get_usage_stats`](#appwriteconsolefunctionsget_usage_stats)
  * [`appwriteconsole.functions.get_variable_by_id`](#appwriteconsolefunctionsget_variable_by_id)
  * [`appwriteconsole.functions.list_all`](#appwriteconsolefunctionslist_all)
  * [`appwriteconsole.functions.list_deployments`](#appwriteconsolefunctionslist_deployments)
  * [`appwriteconsole.functions.list_executions`](#appwriteconsolefunctionslist_executions)
  * [`appwriteconsole.functions.list_runtimes`](#appwriteconsolefunctionslist_runtimes)
  * [`appwriteconsole.functions.list_variables`](#appwriteconsolefunctionslist_variables)
  * [`appwriteconsole.functions.retry_build`](#appwriteconsolefunctionsretry_build)
  * [`appwriteconsole.functions.trigger_execution`](#appwriteconsolefunctionstrigger_execution)
  * [`appwriteconsole.functions.update_by_id`](#appwriteconsolefunctionsupdate_by_id)
  * [`appwriteconsole.functions.update_deployment_by_function_and_id`](#appwriteconsolefunctionsupdate_deployment_by_function_and_id)
  * [`appwriteconsole.functions.update_variable_by_id`](#appwriteconsolefunctionsupdate_variable_by_id)
  * [`appwriteconsole.graphql.execute_mutation`](#appwriteconsolegraphqlexecute_mutation)
  * [`appwriteconsole.graphql.execute_mutation_0`](#appwriteconsolegraphqlexecute_mutation_0)
  * [`appwriteconsole.health.certificates_queue_count`](#appwriteconsolehealthcertificates_queue_count)
  * [`appwriteconsole.health.check_appwrite_http_server`](#appwriteconsolehealthcheck_appwrite_http_server)
  * [`appwriteconsole.health.check_av_status`](#appwriteconsolehealthcheck_av_status)
  * [`appwriteconsole.health.check_cache_status`](#appwriteconsolehealthcheck_cache_status)
  * [`appwriteconsole.health.check_database_status`](#appwriteconsolehealthcheck_database_status)
  * [`appwriteconsole.health.check_local_storage`](#appwriteconsolehealthcheck_local_storage)
  * [`appwriteconsole.health.check_queue_status`](#appwriteconsolehealthcheck_queue_status)
  * [`appwriteconsole.health.check_storage_device`](#appwriteconsolehealthcheck_storage_device)
  * [`appwriteconsole.health.functions_queue_count`](#appwriteconsolehealthfunctions_queue_count)
  * [`appwriteconsole.health.get_builds_queue`](#appwriteconsolehealthget_builds_queue)
  * [`appwriteconsole.health.get_databases_queue`](#appwriteconsolehealthget_databases_queue)
  * [`appwriteconsole.health.get_failed_jobs`](#appwriteconsolehealthget_failed_jobs)
  * [`appwriteconsole.health.get_mails_queue`](#appwriteconsolehealthget_mails_queue)
  * [`appwriteconsole.health.get_messaging_queue`](#appwriteconsolehealthget_messaging_queue)
  * [`appwriteconsole.health.get_migrations_queue`](#appwriteconsolehealthget_migrations_queue)
  * [`appwriteconsole.health.get_queue_deletes`](#appwriteconsolehealthget_queue_deletes)
  * [`appwriteconsole.health.get_queue_logs`](#appwriteconsolehealthget_queue_logs)
  * [`appwriteconsole.health.get_queue_usage_metrics`](#appwriteconsolehealthget_queue_usage_metrics)
  * [`appwriteconsole.health.get_ssl_certificate`](#appwriteconsolehealthget_ssl_certificate)
  * [`appwriteconsole.health.get_usage_dump_queue`](#appwriteconsolehealthget_usage_dump_queue)
  * [`appwriteconsole.health.pubsub_get`](#appwriteconsolehealthpubsub_get)
  * [`appwriteconsole.health.sync_time_with_ntp`](#appwriteconsolehealthsync_time_with_ntp)
  * [`appwriteconsole.health.webhooks_queue_count`](#appwriteconsolehealthwebhooks_queue_count)
  * [`appwriteconsole.locale.get_user_locale_details`](#appwriteconsolelocaleget_user_locale_details)
  * [`appwriteconsole.locale.list_codes`](#appwriteconsolelocalelist_codes)
  * [`appwriteconsole.locale.list_continents`](#appwriteconsolelocalelist_continents)
  * [`appwriteconsole.locale.list_countries`](#appwriteconsolelocalelist_countries)
  * [`appwriteconsole.locale.list_countries_phones`](#appwriteconsolelocalelist_countries_phones)
  * [`appwriteconsole.locale.list_currencies`](#appwriteconsolelocalelist_currencies)
  * [`appwriteconsole.locale.list_eu_countries`](#appwriteconsolelocalelist_eu_countries)
  * [`appwriteconsole.locale.list_languages`](#appwriteconsolelocalelist_languages)
  * [`appwriteconsole.messaging.create_apns_provider`](#appwriteconsolemessagingcreate_apns_provider)
  * [`appwriteconsole.messaging.create_email_message`](#appwriteconsolemessagingcreate_email_message)
  * [`appwriteconsole.messaging.create_fcm_provider`](#appwriteconsolemessagingcreate_fcm_provider)
  * [`appwriteconsole.messaging.create_mailgun_provider`](#appwriteconsolemessagingcreate_mailgun_provider)
  * [`appwriteconsole.messaging.create_msg_provider`](#appwriteconsolemessagingcreate_msg_provider)
  * [`appwriteconsole.messaging.create_new_topic`](#appwriteconsolemessagingcreate_new_topic)
  * [`appwriteconsole.messaging.create_push_notification`](#appwriteconsolemessagingcreate_push_notification)
  * [`appwriteconsole.messaging.create_sendgrid_provider`](#appwriteconsolemessagingcreate_sendgrid_provider)
  * [`appwriteconsole.messaging.create_sms_message`](#appwriteconsolemessagingcreate_sms_message)
  * [`appwriteconsole.messaging.create_smtp_provider`](#appwriteconsolemessagingcreate_smtp_provider)
  * [`appwriteconsole.messaging.create_subscriber`](#appwriteconsolemessagingcreate_subscriber)
  * [`appwriteconsole.messaging.create_telesign_provider`](#appwriteconsolemessagingcreate_telesign_provider)
  * [`appwriteconsole.messaging.create_textmagic_provider`](#appwriteconsolemessagingcreate_textmagic_provider)
  * [`appwriteconsole.messaging.create_twilio_provider`](#appwriteconsolemessagingcreate_twilio_provider)
  * [`appwriteconsole.messaging.create_vonage_provider`](#appwriteconsolemessagingcreate_vonage_provider)
  * [`appwriteconsole.messaging.delete_message`](#appwriteconsolemessagingdelete_message)
  * [`appwriteconsole.messaging.delete_provider_by_id`](#appwriteconsolemessagingdelete_provider_by_id)
  * [`appwriteconsole.messaging.delete_subscriber_by_id`](#appwriteconsolemessagingdelete_subscriber_by_id)
  * [`appwriteconsole.messaging.delete_topic_by_id`](#appwriteconsolemessagingdelete_topic_by_id)
  * [`appwriteconsole.messaging.get_message_by_id`](#appwriteconsolemessagingget_message_by_id)
  * [`appwriteconsole.messaging.get_provider_by_id`](#appwriteconsolemessagingget_provider_by_id)
  * [`appwriteconsole.messaging.get_subscriber_by_id`](#appwriteconsolemessagingget_subscriber_by_id)
  * [`appwriteconsole.messaging.get_topic_by_id`](#appwriteconsolemessagingget_topic_by_id)
  * [`appwriteconsole.messaging.list_all_messages`](#appwriteconsolemessaginglist_all_messages)
  * [`appwriteconsole.messaging.list_message_logs`](#appwriteconsolemessaginglist_message_logs)
  * [`appwriteconsole.messaging.list_provider_logs`](#appwriteconsolemessaginglist_provider_logs)
  * [`appwriteconsole.messaging.list_providers`](#appwriteconsolemessaginglist_providers)
  * [`appwriteconsole.messaging.list_subscriber_logs`](#appwriteconsolemessaginglist_subscriber_logs)
  * [`appwriteconsole.messaging.list_subscribers`](#appwriteconsolemessaginglist_subscribers)
  * [`appwriteconsole.messaging.list_targets`](#appwriteconsolemessaginglist_targets)
  * [`appwriteconsole.messaging.list_topic_logs`](#appwriteconsolemessaginglist_topic_logs)
  * [`appwriteconsole.messaging.list_topics`](#appwriteconsolemessaginglist_topics)
  * [`appwriteconsole.messaging.update_apns_provider`](#appwriteconsolemessagingupdate_apns_provider)
  * [`appwriteconsole.messaging.update_email_by_id`](#appwriteconsolemessagingupdate_email_by_id)
  * [`appwriteconsole.messaging.update_fcm_provider`](#appwriteconsolemessagingupdate_fcm_provider)
  * [`appwriteconsole.messaging.update_mailgun_provider`](#appwriteconsolemessagingupdate_mailgun_provider)
  * [`appwriteconsole.messaging.update_provider_by_id`](#appwriteconsolemessagingupdate_provider_by_id)
  * [`appwriteconsole.messaging.update_push_message`](#appwriteconsolemessagingupdate_push_message)
  * [`appwriteconsole.messaging.update_sendgrid_provider`](#appwriteconsolemessagingupdate_sendgrid_provider)
  * [`appwriteconsole.messaging.update_sms_message_by_id`](#appwriteconsolemessagingupdate_sms_message_by_id)
  * [`appwriteconsole.messaging.update_smtp_provider`](#appwriteconsolemessagingupdate_smtp_provider)
  * [`appwriteconsole.messaging.update_telesign_provider`](#appwriteconsolemessagingupdate_telesign_provider)
  * [`appwriteconsole.messaging.update_textmagic_provider`](#appwriteconsolemessagingupdate_textmagic_provider)
  * [`appwriteconsole.messaging.update_topic_by_id`](#appwriteconsolemessagingupdate_topic_by_id)
  * [`appwriteconsole.messaging.update_twilio_provider`](#appwriteconsolemessagingupdate_twilio_provider)
  * [`appwriteconsole.messaging.update_vonage_provider_by_id`](#appwriteconsolemessagingupdate_vonage_provider_by_id)
  * [`appwriteconsole.migrations.create_appwrite_migration`](#appwriteconsolemigrationscreate_appwrite_migration)
  * [`appwriteconsole.migrations.create_n_host_migration`](#appwriteconsolemigrationscreate_n_host_migration)
  * [`appwriteconsole.migrations.delete_migration`](#appwriteconsolemigrationsdelete_migration)
  * [`appwriteconsole.migrations.firebase_data_migration`](#appwriteconsolemigrationsfirebase_data_migration)
  * [`appwriteconsole.migrations.firebase_o_auth_migrate`](#appwriteconsolemigrationsfirebase_o_auth_migrate)
  * [`appwriteconsole.migrations.generate_firebase_report`](#appwriteconsolemigrationsgenerate_firebase_report)
  * [`appwriteconsole.migrations.generate_firebase_report_o_auth`](#appwriteconsolemigrationsgenerate_firebase_report_o_auth)
  * [`appwriteconsole.migrations.generate_nhost_report`](#appwriteconsolemigrationsgenerate_nhost_report)
  * [`appwriteconsole.migrations.generate_report_on_appwrite_data`](#appwriteconsolemigrationsgenerate_report_on_appwrite_data)
  * [`appwriteconsole.migrations.generate_supabase_report`](#appwriteconsolemigrationsgenerate_supabase_report)
  * [`appwriteconsole.migrations.get_by_id`](#appwriteconsolemigrationsget_by_id)
  * [`appwriteconsole.migrations.list_firebase_projects`](#appwriteconsolemigrationslist_firebase_projects)
  * [`appwriteconsole.migrations.list_migrations`](#appwriteconsolemigrationslist_migrations)
  * [`appwriteconsole.migrations.migrate_supabase_data`](#appwriteconsolemigrationsmigrate_supabase_data)
  * [`appwriteconsole.migrations.retry_migration`](#appwriteconsolemigrationsretry_migration)
  * [`appwriteconsole.migrations.revoke_firebase_authorization`](#appwriteconsolemigrationsrevoke_firebase_authorization)
  * [`appwriteconsole.project.create_variable`](#appwriteconsoleprojectcreate_variable)
  * [`appwriteconsole.project.delete_variable_by_id`](#appwriteconsoleprojectdelete_variable_by_id)
  * [`appwriteconsole.project.get_usage_stats`](#appwriteconsoleprojectget_usage_stats)
  * [`appwriteconsole.project.list_variables`](#appwriteconsoleprojectlist_variables)
  * [`appwriteconsole.project.update_variable_by_id`](#appwriteconsoleprojectupdate_variable_by_id)
  * [`appwriteconsole.project.variable_details`](#appwriteconsoleprojectvariable_details)
  * [`appwriteconsole.projects.create_key`](#appwriteconsoleprojectscreate_key)
  * [`appwriteconsole.projects.create_new_project`](#appwriteconsoleprojectscreate_new_project)
  * [`appwriteconsole.projects.create_platform`](#appwriteconsoleprojectscreate_platform)
  * [`appwriteconsole.projects.create_smtp_test`](#appwriteconsoleprojectscreate_smtp_test)
  * [`appwriteconsole.projects.create_webhook`](#appwriteconsoleprojectscreate_webhook)
  * [`appwriteconsole.projects.delete_key`](#appwriteconsoleprojectsdelete_key)
  * [`appwriteconsole.projects.delete_platform`](#appwriteconsoleprojectsdelete_platform)
  * [`appwriteconsole.projects.delete_webhook`](#appwriteconsoleprojectsdelete_webhook)
  * [`appwriteconsole.projects.enable_personal_data_check`](#appwriteconsoleprojectsenable_personal_data_check)
  * [`appwriteconsole.projects.get`](#appwriteconsoleprojectsget)
  * [`appwriteconsole.projects.get_email_template`](#appwriteconsoleprojectsget_email_template)
  * [`appwriteconsole.projects.get_key`](#appwriteconsoleprojectsget_key)
  * [`appwriteconsole.projects.get_platform_by_id`](#appwriteconsoleprojectsget_platform_by_id)
  * [`appwriteconsole.projects.get_sms_template`](#appwriteconsoleprojectsget_sms_template)
  * [`appwriteconsole.projects.get_webhook`](#appwriteconsoleprojectsget_webhook)
  * [`appwriteconsole.projects.list_keys`](#appwriteconsoleprojectslist_keys)
  * [`appwriteconsole.projects.list_platforms`](#appwriteconsoleprojectslist_platforms)
  * [`appwriteconsole.projects.list_projects`](#appwriteconsoleprojectslist_projects)
  * [`appwriteconsole.projects.list_webhooks`](#appwriteconsoleprojectslist_webhooks)
  * [`appwriteconsole.projects.remove_by_id`](#appwriteconsoleprojectsremove_by_id)
  * [`appwriteconsole.projects.reset_email_template`](#appwriteconsoleprojectsreset_email_template)
  * [`appwriteconsole.projects.reset_sms_template`](#appwriteconsoleprojectsreset_sms_template)
  * [`appwriteconsole.projects.update_all_api_status`](#appwriteconsoleprojectsupdate_all_api_status)
  * [`appwriteconsole.projects.update_all_service_status`](#appwriteconsoleprojectsupdate_all_service_status)
  * [`appwriteconsole.projects.update_api_status`](#appwriteconsoleprojectsupdate_api_status)
  * [`appwriteconsole.projects.update_auth_duration`](#appwriteconsoleprojectsupdate_auth_duration)
  * [`appwriteconsole.projects.update_auth_method_status`](#appwriteconsoleprojectsupdate_auth_method_status)
  * [`appwriteconsole.projects.update_auth_password_dictionary`](#appwriteconsoleprojectsupdate_auth_password_dictionary)
  * [`appwriteconsole.projects.update_auth_password_history`](#appwriteconsoleprojectsupdate_auth_password_history)
  * [`appwriteconsole.projects.update_custom_email_templates`](#appwriteconsoleprojectsupdate_custom_email_templates)
  * [`appwriteconsole.projects.update_detail`](#appwriteconsoleprojectsupdate_detail)
  * [`appwriteconsole.projects.update_key`](#appwriteconsoleprojectsupdate_key)
  * [`appwriteconsole.projects.update_max_sessions_limit`](#appwriteconsoleprojectsupdate_max_sessions_limit)
  * [`appwriteconsole.projects.update_o_auth`](#appwriteconsoleprojectsupdate_o_auth)
  * [`appwriteconsole.projects.update_platform_by_id`](#appwriteconsoleprojectsupdate_platform_by_id)
  * [`appwriteconsole.projects.update_service_status`](#appwriteconsoleprojectsupdate_service_status)
  * [`appwriteconsole.projects.update_sms_template`](#appwriteconsoleprojectsupdate_sms_template)
  * [`appwriteconsole.projects.update_smtp`](#appwriteconsoleprojectsupdate_smtp)
  * [`appwriteconsole.projects.update_team`](#appwriteconsoleprojectsupdate_team)
  * [`appwriteconsole.projects.update_user_limit`](#appwriteconsoleprojectsupdate_user_limit)
  * [`appwriteconsole.projects.update_webhook`](#appwriteconsoleprojectsupdate_webhook)
  * [`appwriteconsole.projects.update_webhook_signature`](#appwriteconsoleprojectsupdate_webhook_signature)
  * [`appwriteconsole.proxy.create_new_rule`](#appwriteconsoleproxycreate_new_rule)
  * [`appwriteconsole.proxy.delete_rule_by_id`](#appwriteconsoleproxydelete_rule_by_id)
  * [`appwriteconsole.proxy.get_rule_by_id`](#appwriteconsoleproxyget_rule_by_id)
  * [`appwriteconsole.proxy.list_rules`](#appwriteconsoleproxylist_rules)
  * [`appwriteconsole.proxy.update_rule_verification_status`](#appwriteconsoleproxyupdate_rule_verification_status)
  * [`appwriteconsole.storage.create_bucket`](#appwriteconsolestoragecreate_bucket)
  * [`appwriteconsole.storage.create_file`](#appwriteconsolestoragecreate_file)
  * [`appwriteconsole.storage.delete_bucket_by_id`](#appwriteconsolestoragedelete_bucket_by_id)
  * [`appwriteconsole.storage.delete_file_by_id`](#appwriteconsolestoragedelete_file_by_id)
  * [`appwriteconsole.storage.get_bucket`](#appwriteconsolestorageget_bucket)
  * [`appwriteconsole.storage.get_bucket_usage_stats`](#appwriteconsolestorageget_bucket_usage_stats)
  * [`appwriteconsole.storage.get_download_file`](#appwriteconsolestorageget_download_file)
  * [`appwriteconsole.storage.get_file_by_id`](#appwriteconsolestorageget_file_by_id)
  * [`appwriteconsole.storage.get_file_preview_image`](#appwriteconsolestorageget_file_preview_image)
  * [`appwriteconsole.storage.get_file_view`](#appwriteconsolestorageget_file_view)
  * [`appwriteconsole.storage.get_usage_stats`](#appwriteconsolestorageget_usage_stats)
  * [`appwriteconsole.storage.list_buckets`](#appwriteconsolestoragelist_buckets)
  * [`appwriteconsole.storage.list_files`](#appwriteconsolestoragelist_files)
  * [`appwriteconsole.storage.update_bucket_by_id`](#appwriteconsolestorageupdate_bucket_by_id)
  * [`appwriteconsole.storage.update_file_by_id`](#appwriteconsolestorageupdate_file_by_id)
  * [`appwriteconsole.teams.create_membership`](#appwriteconsoleteamscreate_membership)
  * [`appwriteconsole.teams.create_team`](#appwriteconsoleteamscreate_team)
  * [`appwriteconsole.teams.get_by_id`](#appwriteconsoleteamsget_by_id)
  * [`appwriteconsole.teams.get_filtered_teams`](#appwriteconsoleteamsget_filtered_teams)
  * [`appwriteconsole.teams.get_membership`](#appwriteconsoleteamsget_membership)
  * [`appwriteconsole.teams.get_prefs`](#appwriteconsoleteamsget_prefs)
  * [`appwriteconsole.teams.list_logs`](#appwriteconsoleteamslist_logs)
  * [`appwriteconsole.teams.list_memberships`](#appwriteconsoleteamslist_memberships)
  * [`appwriteconsole.teams.remove_by_id`](#appwriteconsoleteamsremove_by_id)
  * [`appwriteconsole.teams.remove_membership`](#appwriteconsoleteamsremove_membership)
  * [`appwriteconsole.teams.update_membership_roles`](#appwriteconsoleteamsupdate_membership_roles)
  * [`appwriteconsole.teams.update_membership_status`](#appwriteconsoleteamsupdate_membership_status)
  * [`appwriteconsole.teams.update_name_by_id`](#appwriteconsoleteamsupdate_name_by_id)
  * [`appwriteconsole.teams.update_prefs_by_id`](#appwriteconsoleteamsupdate_prefs_by_id)
  * [`appwriteconsole.users.create_argon_user`](#appwriteconsoleuserscreate_argon_user)
  * [`appwriteconsole.users.create_bcrypt_password`](#appwriteconsoleuserscreate_bcrypt_password)
  * [`appwriteconsole.users.create_md5_user`](#appwriteconsoleuserscreate_md5_user)
  * [`appwriteconsole.users.create_messaging_target`](#appwriteconsoleuserscreate_messaging_target)
  * [`appwriteconsole.users.create_mfa_recovery_codes`](#appwriteconsoleuserscreate_mfa_recovery_codes)
  * [`appwriteconsole.users.create_new_user`](#appwriteconsoleuserscreate_new_user)
  * [`appwriteconsole.users.create_scrypt_modified_user`](#appwriteconsoleuserscreate_scrypt_modified_user)
  * [`appwriteconsole.users.create_scrypt_user`](#appwriteconsoleuserscreate_scrypt_user)
  * [`appwriteconsole.users.create_session`](#appwriteconsoleuserscreate_session)
  * [`appwriteconsole.users.create_with_ph_pass`](#appwriteconsoleuserscreate_with_ph_pass)
  * [`appwriteconsole.users.create_with_sha_password`](#appwriteconsoleuserscreate_with_sha_password)
  * [`appwriteconsole.users.delete_authenticator`](#appwriteconsoleusersdelete_authenticator)
  * [`appwriteconsole.users.delete_by_id`](#appwriteconsoleusersdelete_by_id)
  * [`appwriteconsole.users.delete_identity_by_id`](#appwriteconsoleusersdelete_identity_by_id)
  * [`appwriteconsole.users.delete_session_by_user_id_and_session_id`](#appwriteconsoleusersdelete_session_by_user_id_and_session_id)
  * [`appwriteconsole.users.delete_sessions_by_id`](#appwriteconsoleusersdelete_sessions_by_id)
  * [`appwriteconsole.users.delete_target_messaging`](#appwriteconsoleusersdelete_target_messaging)
  * [`appwriteconsole.users.generate_token`](#appwriteconsoleusersgenerate_token)
  * [`appwriteconsole.users.get_logs_by_user_id`](#appwriteconsoleusersget_logs_by_user_id)
  * [`appwriteconsole.users.get_memberships_by_id`](#appwriteconsoleusersget_memberships_by_id)
  * [`appwriteconsole.users.get_mfa_recovery_codes`](#appwriteconsoleusersget_mfa_recovery_codes)
  * [`appwriteconsole.users.get_target`](#appwriteconsoleusersget_target)
  * [`appwriteconsole.users.get_usage_stats`](#appwriteconsoleusersget_usage_stats)
  * [`appwriteconsole.users.get_user_by_id`](#appwriteconsoleusersget_user_by_id)
  * [`appwriteconsole.users.get_user_prefs_by_id`](#appwriteconsoleusersget_user_prefs_by_id)
  * [`appwriteconsole.users.list_filtered_users`](#appwriteconsoleuserslist_filtered_users)
  * [`appwriteconsole.users.list_identities`](#appwriteconsoleuserslist_identities)
  * [`appwriteconsole.users.list_mfa_factors`](#appwriteconsoleuserslist_mfa_factors)
  * [`appwriteconsole.users.list_sessions_by_user_id`](#appwriteconsoleuserslist_sessions_by_user_id)
  * [`appwriteconsole.users.list_targets`](#appwriteconsoleuserslist_targets)
  * [`appwriteconsole.users.regenerate_mfa_recovery_codes_by_user_id`](#appwriteconsoleusersregenerate_mfa_recovery_codes_by_user_id)
  * [`appwriteconsole.users.update_email_by_id`](#appwriteconsoleusersupdate_email_by_id)
  * [`appwriteconsole.users.update_email_verification_status`](#appwriteconsoleusersupdate_email_verification_status)
  * [`appwriteconsole.users.update_labels_by_user_id`](#appwriteconsoleusersupdate_labels_by_user_id)
  * [`appwriteconsole.users.update_messaging_target`](#appwriteconsoleusersupdate_messaging_target)
  * [`appwriteconsole.users.update_mfa_status`](#appwriteconsoleusersupdate_mfa_status)
  * [`appwriteconsole.users.update_name_by_id`](#appwriteconsoleusersupdate_name_by_id)
  * [`appwriteconsole.users.update_password_by_user_id`](#appwriteconsoleusersupdate_password_by_user_id)
  * [`appwriteconsole.users.update_phone_by_user_id`](#appwriteconsoleusersupdate_phone_by_user_id)
  * [`appwriteconsole.users.update_phone_verification`](#appwriteconsoleusersupdate_phone_verification)
  * [`appwriteconsole.users.update_prefs_by_id`](#appwriteconsoleusersupdate_prefs_by_id)
  * [`appwriteconsole.users.update_status_by_user_id`](#appwriteconsoleusersupdate_status_by_user_id)
  * [`appwriteconsole.vcs.authorize_external_deployment`](#appwriteconsolevcsauthorize_external_deployment)
  * [`appwriteconsole.vcs.create_provider_repository`](#appwriteconsolevcscreate_provider_repository)
  * [`appwriteconsole.vcs.delete_installation`](#appwriteconsolevcsdelete_installation)
  * [`appwriteconsole.vcs.detect_runtime_settings`](#appwriteconsolevcsdetect_runtime_settings)
  * [`appwriteconsole.vcs.get_installation_by_id`](#appwriteconsolevcsget_installation_by_id)
  * [`appwriteconsole.vcs.get_repository`](#appwriteconsolevcsget_repository)
  * [`appwriteconsole.vcs.list_installations`](#appwriteconsolevcslist_installations)
  * [`appwriteconsole.vcs.list_provider_repositories`](#appwriteconsolevcslist_provider_repositories)
  * [`appwriteconsole.vcs.list_repository_branches`](#appwriteconsolevcslist_repository_branches)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Appwrite&serviceName=Console&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from appwrite_console_python_sdk import AppwriteConsole, ApiException

appwriteconsole = AppwriteConsole(

        jwt = 'YOUR_API_KEY',

        project = 'YOUR_API_KEY',
)

try:
    # Add Authenticator
    add_authenticator_app_response = appwriteconsole.account.add_authenticator_app(
        type="totp",
    )
    print(add_authenticator_app_response)
except ApiException as e:
    print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from appwrite_console_python_sdk import AppwriteConsole, ApiException

appwriteconsole = AppwriteConsole(

        jwt = 'YOUR_API_KEY',

        project = 'YOUR_API_KEY',
)

async def main():
    try:
        # Add Authenticator
        add_authenticator_app_response = await appwriteconsole.account.aadd_authenticator_app(
            type="totp",
        )
        print(add_authenticator_app_response)
    except ApiException as e:
        print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from appwrite_console_python_sdk import AppwriteConsole, ApiException

appwriteconsole = AppwriteConsole(

        jwt = 'YOUR_API_KEY',

        project = 'YOUR_API_KEY',
)

try:
    # Add Authenticator
    add_authenticator_app_response = appwriteconsole.account.raw.add_authenticator_app(
        type="totp",
    )
    pprint(add_authenticator_app_response.body)
    pprint(add_authenticator_app_response.body["secret"])
    pprint(add_authenticator_app_response.body["uri"])
    pprint(add_authenticator_app_response.headers)
    pprint(add_authenticator_app_response.status)
    pprint(add_authenticator_app_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.add_authenticator_app: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `appwriteconsole.account.add_authenticator_app`<a id="appwriteconsoleaccountadd_authenticator_app"></a>

Add an authenticator app to be used as an MFA factor. Verify the authenticator using the [verify authenticator](/docs/references/cloud/client-web/account#verifyAuthenticator) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_authenticator_app_response = appwriteconsole.account.add_authenticator_app(
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of authenticator. Must be `totp`

#### 🔄 Return<a id="🔄-return"></a>

[`MfaType`](./appwrite_console_python_sdk/pydantic/mfa_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.complete_email_verification`<a id="appwriteconsoleaccountcomplete_email_verification"></a>

Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_email_verification_response = appwriteconsole.account.complete_email_verification(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompleteEmailVerificationRequest`](./appwrite_console_python_sdk/type/account_complete_email_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.complete_mfa_challenge`<a id="appwriteconsoleaccountcomplete_mfa_challenge"></a>

Complete the MFA challenge by providing the one-time password. Finish the process of MFA verification by providing the one-time password. To begin the flow, use [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_mfa_challenge_response = appwriteconsole.account.complete_mfa_challenge(
    challenge_id="<CHALLENGE_ID>",
    otp="<OTP>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### challenge_id: `str`<a id="challenge_id-str"></a>

ID of the challenge.

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompleteMfaChallengeRequest`](./appwrite_console_python_sdk/type/account_complete_mfa_challenge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/challenge` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.complete_password_recovery`<a id="appwriteconsoleaccountcomplete_password_recovery"></a>

Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#createRecovery) endpoint.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_password_recovery_response = appwriteconsole.account.complete_password_recovery(
    user_id="<USER_ID>",
    secret="<SECRET>",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid reset token.

##### password: `str`<a id="password-str"></a>

New user password. Must be between 8 and 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCompletePasswordRecoveryRequest`](./appwrite_console_python_sdk/type/account_complete_password_recovery_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/recovery` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.confirm_phone_verification`<a id="appwriteconsoleaccountconfirm_phone_verification"></a>

Use this endpoint to complete the user phone verification process. Use the **userId** and **secret** that were sent to your user's phone number to verify the user email ownership. If confirmed this route will return a 200 status code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
confirm_phone_verification_response = appwriteconsole.account.confirm_phone_verification(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountConfirmPhoneVerificationRequest`](./appwrite_console_python_sdk/type/account_confirm_phone_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification/phone` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_anonymous_session`<a id="appwriteconsoleaccountcreate_anonymous_session"></a>

Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](https://appwrite.io/docs/references/cloud/client-web/account#updateEmail) or create an [OAuth2 session](https://appwrite.io/docs/references/cloud/client-web/account#CreateOAuth2Session).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_anonymous_session_response = appwriteconsole.account.create_anonymous_session()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/anonymous` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_email_password_session`<a id="appwriteconsoleaccountcreate_email_password_session"></a>

Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_password_session_response = appwriteconsole.account.create_email_password_session(
    email="email@example.com",
    password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailPasswordSessionRequest`](./appwrite_console_python_sdk/type/account_create_email_password_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_email_token`<a id="appwriteconsoleaccountcreate_email_token"></a>

Sends the user an email with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's email is valid for 15 minutes.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_token_response = appwriteconsole.account.create_email_token(
    user_id="<USER_ID>",
    email="email@example.com",
    phrase=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### phrase: `bool`<a id="phrase-bool"></a>

Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailTokenRequest`](./appwrite_console_python_sdk/type/account_create_email_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_email_verification`<a id="appwriteconsoleaccountcreate_email_verification"></a>

Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateVerification). The verification link sent to the user's email address is valid for 7 days.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_verification_response = appwriteconsole.account.create_email_verification(
    url="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateEmailVerificationRequest`](./appwrite_console_python_sdk/type/account_create_email_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_jwt`<a id="appwriteconsoleaccountcreate_jwt"></a>

Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on behalf of the current user when working with the Appwrite server-side API and SDKs. The JWT secret is valid for 15 minutes from its creation and will be invalid if the user will logout in that time frame.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_jwt_response = appwriteconsole.account.create_jwt()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Jwt`](./appwrite_console_python_sdk/pydantic/jwt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/jwt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_magic_url_token`<a id="appwriteconsoleaccountcreate_magic_url_token"></a>

Sends the user an email with a secret key for creating a session. If the provided user ID has not been registered, a new user will be created. When the user clicks the link in the email, the user is redirected back to the URL you provided with the secret key and userId values attached to the URL query string. Use the query string parameters to submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The link sent to the user's email address is valid for 1 hour. If you are on a mobile device you can leave the URL parameter empty, so that the login completion will be handled by your Appwrite instance by default.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_magic_url_token_response = appwriteconsole.account.create_magic_url_token(
    user_id="<USER_ID>",
    email="email@example.com",
    url="https://example.com",
    phrase=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the magic URL login. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### phrase: `bool`<a id="phrase-bool"></a>

Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateMagicUrlTokenRequest`](./appwrite_console_python_sdk/type/account_create_magic_url_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/magic-url` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_mfa_challenge`<a id="appwriteconsoleaccountcreate_mfa_challenge"></a>

Begin the process of MFA verification after sign-in. Finish the flow with [updateMfaChallenge](/docs/references/cloud/client-web/account#updateMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_mfa_challenge_response = appwriteconsole.account.create_mfa_challenge(
    factor="email",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### factor: `str`<a id="factor-str"></a>

Factor used for verification. Must be one of following: `email`, `phone`, `totp`, `recoveryCode`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateMfaChallengeRequest`](./appwrite_console_python_sdk/type/account_create_mfa_challenge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MfaChallenge`](./appwrite_console_python_sdk/pydantic/mfa_challenge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/challenge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_new_user`<a id="appwriteconsoleaccountcreate_new_user"></a>

Use this endpoint to allow a new user to register a new account in your project. After the user registration completes successfully, you can use the [/account/verfication](https://appwrite.io/docs/references/cloud/client-web/account#createVerification) route to start verifying the user email address. To allow the new user to login to their new account, you need to create a new [account session](https://appwrite.io/docs/references/cloud/client-web/account#createEmailSession).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = appwriteconsole.account.create_new_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="string_example",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

New user password. Must be between 8 and 256 chars.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateNewUserRequest`](./appwrite_console_python_sdk/type/account_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_o_auth2_session`<a id="appwriteconsoleaccountcreate_o_auth2_session"></a>

Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed.

If there is already an active session, the new session will be attached to the logged-in account. If there are no active sessions, the server will attempt to look for a user with the same email address as the email received from the OAuth2 provider and attach the new session to the existing user. If no matching user is found - the server will create a new user.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.create_o_auth2_session(
    provider="amazon",
    success="",
    failure="",
    scopes=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

OAuth2 Provider. Currently, supported providers are: amazon, apple, auth0, authentik, autodesk, bitbucket, bitly, box, dailymotion, discord, disqus, dropbox, etsy, facebook, github, gitlab, google, linkedin, microsoft, notion, oidc, okta, paypal, paypalSandbox, podio, salesforce, slack, spotify, stripe, tradeshift, tradeshiftBox, twitch, wordpress, yahoo, yammer, yandex, zoho, zoom.

##### success: `str`<a id="success-str"></a>

URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### failure: `str`<a id="failure-str"></a>

URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### scopes: List[`str`]<a id="scopes-liststr"></a>

A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes. Maximum of 100 scopes are allowed, each 4096 characters long.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/oauth2/{provider}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_o_auth2_token`<a id="appwriteconsoleaccountcreate_o_auth2_token"></a>

Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed. 

If authentication succeeds, `userId` and `secret` of a token will be appended to the success URL as query parameters. These can be used to create a new session using the [Create session](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.create_o_auth2_token(
    provider="amazon",
    success="",
    failure="",
    scopes=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

OAuth2 Provider. Currently, supported providers are: amazon, apple, auth0, authentik, autodesk, bitbucket, bitly, box, dailymotion, discord, disqus, dropbox, etsy, facebook, github, gitlab, google, linkedin, microsoft, notion, oidc, okta, paypal, paypalSandbox, podio, salesforce, slack, spotify, stripe, tradeshift, tradeshiftBox, twitch, wordpress, yahoo, yammer, yandex, zoho, zoom.

##### success: `str`<a id="success-str"></a>

URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### failure: `str`<a id="failure-str"></a>

URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### scopes: List[`str`]<a id="scopes-liststr"></a>

A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes. Maximum of 100 scopes are allowed, each 4096 characters long.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/oauth2/{provider}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_password_recovery`<a id="appwriteconsoleaccountcreate_password_recovery"></a>

Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#updateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_password_recovery_response = appwriteconsole.account.create_password_recovery(
    email="email@example.com",
    url="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreatePasswordRecoveryRequest`](./appwrite_console_python_sdk/type/account_create_password_recovery_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/recovery` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_phone_token`<a id="appwriteconsoleaccountcreate_phone_token"></a>

Sends the user an SMS with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's phone is valid for 15 minutes.

A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phone_token_response = appwriteconsole.account.create_phone_token(
    user_id="<USER_ID>",
    phone="+12065550100",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreatePhoneTokenRequest`](./appwrite_console_python_sdk/type/account_create_phone_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/tokens/phone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_push_target`<a id="appwriteconsoleaccountcreate_push_target"></a>

Create push target

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_push_target_response = appwriteconsole.account.create_push_target(
    target_id="<TARGET_ID>",
    identifier="<IDENTIFIER>",
    provider_id="<PROVIDER_ID>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_id: `str`<a id="target_id-str"></a>

Target ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreatePushTargetRequest`](./appwrite_console_python_sdk/type/account_create_push_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/targets/push` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.create_session_from_token`<a id="appwriteconsoleaccountcreate_session_from_token"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_from_token_response = appwriteconsole.account.create_session_from_token(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Secret of a token generated by login methods. For example, the `createMagicURLToken` or `createPhoneToken` methods.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateSessionFromTokenRequest`](./appwrite_console_python_sdk/type/account_create_session_from_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.delete_authenticator_by_id`<a id="appwriteconsoleaccountdelete_authenticator_by_id"></a>

Delete an authenticator for a user by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_authenticator_by_id_response = appwriteconsole.account.delete_authenticator_by_id(
    otp="<OTP>",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountDeleteAuthenticatorByIdRequest`](./appwrite_console_python_sdk/type/account_delete_authenticator_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.delete_identity_by_id`<a id="appwriteconsoleaccountdelete_identity_by_id"></a>

Delete an identity by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.delete_identity_by_id(
    identity_id="identityId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identity_id: `str`<a id="identity_id-str"></a>

Identity ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/identities/{identityId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.delete_push_target`<a id="appwriteconsoleaccountdelete_push_target"></a>

Delete push target

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_push_target_response = appwriteconsole.account.delete_push_target(
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/targets/{targetId}/push` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.delete_sessions`<a id="appwriteconsoleaccountdelete_sessions"></a>

Delete all sessions from the user account and remove any sessions cookies from the end client.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.delete_sessions()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.delete_user`<a id="appwriteconsoleaccountdelete_user"></a>

Delete the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.delete_user()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.extend_session_length`<a id="appwriteconsoleaccountextend_session_length"></a>

Use this endpoint to extend a session's length. Extending a session is useful when session expiry is short. If the session was created using an OAuth provider, this endpoint refreshes the access token from the provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extend_session_length_response = appwriteconsole.account.extend_session_length(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to update the current device session.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.generate_recovery_codes`<a id="appwriteconsoleaccountgenerate_recovery_codes"></a>

Generate recovery codes as backup for MFA flow. It's recommended to generate and show then immediately after user successfully adds their authehticator. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_recovery_codes_response = appwriteconsole.account.generate_recovery_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.get_mfa_recovery_codes`<a id="appwriteconsoleaccountget_mfa_recovery_codes"></a>

Get recovery codes that can be used as backup for MFA flow. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to read recovery codes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mfa_recovery_codes_response = appwriteconsole.account.get_mfa_recovery_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.get_prefs_operation`<a id="appwriteconsoleaccountget_prefs_operation"></a>

Get the preferences as a key-value object for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_prefs_operation_response = appwriteconsole.account.get_prefs_operation()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_console_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.get_session`<a id="appwriteconsoleaccountget_session"></a>

Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_session_response = appwriteconsole.account.get_session(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to get the current device session.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.get_user`<a id="appwriteconsoleaccountget_user"></a>

Get the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_response = appwriteconsole.account.get_user()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.list_identities`<a id="appwriteconsoleaccountlist_identities"></a>

Get the list of identities for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_identities_response = appwriteconsole.account.list_identities(
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityList`](./appwrite_console_python_sdk/pydantic/identity_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/identities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.list_mfa_factors`<a id="appwriteconsoleaccountlist_mfa_factors"></a>

List the factors available on the account to be used as a MFA challange.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_mfa_factors_response = appwriteconsole.account.list_mfa_factors()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaFactors`](./appwrite_console_python_sdk/pydantic/mfa_factors.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/factors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.list_sessions`<a id="appwriteconsoleaccountlist_sessions"></a>

Get the list of active sessions across different devices for the currently logged in user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sessions_response = appwriteconsole.account.list_sessions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SessionList`](./appwrite_console_python_sdk/pydantic/session_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.list_user_logs`<a id="appwriteconsoleaccountlist_user_logs"></a>

Get the list of latest security activity logs for the currently logged in user. Each log returns user IP address, location and date and time of log.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_logs_response = appwriteconsole.account.list_user_logs(
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.logout_session`<a id="appwriteconsoleaccountlogout_session"></a>

Logout the user. Use 'current' as the session ID to logout on this device, use a session ID to logout on another device. If you're looking to logout the user on all devices, use [Delete Sessions](https://appwrite.io/docs/references/cloud/client-web/account#deleteSessions) instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.account.logout_session(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

Session ID. Use the string 'current' to delete the current device session.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/{sessionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.regenerate_mfa_recovery_codes`<a id="appwriteconsoleaccountregenerate_mfa_recovery_codes"></a>

Regenerate recovery codes that can be used as backup for MFA flow. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to regenreate recovery codes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
regenerate_mfa_recovery_codes_response = appwriteconsole.account.regenerate_mfa_recovery_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/recovery-codes` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.send_verification_sms`<a id="appwriteconsoleaccountsend_verification_sms"></a>

Use this endpoint to send a verification SMS to the currently logged in user. This endpoint is meant for use after updating a user's phone number using the [accountUpdatePhone](https://appwrite.io/docs/references/cloud/client-web/account#updatePhone) endpoint. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updatePhoneVerification). The verification code sent to the user's phone number is valid for 15 minutes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_verification_sms_response = appwriteconsole.account.send_verification_sms()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/verification/phone` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_email_address`<a id="appwriteconsoleaccountupdate_email_address"></a>

Update currently logged in user account email address. After changing user address, the user confirmation status will get reset. A new confirmation email is not sent automatically however you can use the send confirmation email endpoint again to send the confirmation email. For security measures, user password is required to complete this request.
This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_address_response = appwriteconsole.account.update_email_address(
    email="email@example.com",
    password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateEmailAddressRequest`](./appwrite_console_python_sdk/type/account_update_email_address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/email` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_magic_url_session`<a id="appwriteconsoleaccountupdate_magic_url_session"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_magic_url_session_response = appwriteconsole.account.update_magic_url_session(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateMagicUrlSessionRequest`](./appwrite_console_python_sdk/type/account_update_magic_url_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/magic-url` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_mfa_status`<a id="appwriteconsoleaccountupdate_mfa_status"></a>

Enable or disable MFA on an account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mfa_status_response = appwriteconsole.account.update_mfa_status(
    mfa=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mfa: `bool`<a id="mfa-bool"></a>

Enable or disable MFA.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateMfaStatusRequest`](./appwrite_console_python_sdk/type/account_update_mfa_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_name`<a id="appwriteconsoleaccountupdate_name"></a>

Update currently logged in user account name.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_name_response = appwriteconsole.account.update_name(
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdateNameRequest`](./appwrite_console_python_sdk/type/account_update_name_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_password`<a id="appwriteconsoleaccountupdate_password"></a>

Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth, Team Invites and Magic URL, oldPassword is optional.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_password_response = appwriteconsole.account.update_password(
    password="string_example",
    old_password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

New user password. Must be at least 8 chars.

##### old_password: `str`<a id="old_password-str"></a>

Current user password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePasswordRequest`](./appwrite_console_python_sdk/type/account_update_password_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/password` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_phone`<a id="appwriteconsoleaccountupdate_phone"></a>

Update the currently logged in user's phone number. After updating the phone number, the phone verification status will be reset. A confirmation SMS is not sent automatically, however you can use the [POST /account/verification/phone](https://appwrite.io/docs/references/cloud/client-web/account#createPhoneVerification) endpoint to send a confirmation SMS.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_response = appwriteconsole.account.update_phone(
    phone="+12065550100",
    password="password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### password: `str`<a id="password-str"></a>

User password. Must be at least 8 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePhoneRequest`](./appwrite_console_python_sdk/type/account_update_phone_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_phone_session`<a id="appwriteconsoleaccountupdate_phone_session"></a>

Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_session_response = appwriteconsole.account.update_phone_session(
    user_id="<USER_ID>",
    secret="<SECRET>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### secret: `str`<a id="secret-str"></a>

Valid verification token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePhoneSessionRequest`](./appwrite_console_python_sdk/type/account_update_phone_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/sessions/phone` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_prefs_operation`<a id="appwriteconsoleaccountupdate_prefs_operation"></a>

Update currently logged in user account preferences. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_prefs_operation_response = appwriteconsole.account.update_prefs_operation(
    prefs={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePrefsOperationRequest`](./appwrite_console_python_sdk/type/account_update_prefs_operation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/prefs` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_push_target`<a id="appwriteconsoleaccountupdate_push_target"></a>

Update push target

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_push_target_response = appwriteconsole.account.update_push_target(
    identifier="<IDENTIFIER>",
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountUpdatePushTargetRequest`](./appwrite_console_python_sdk/type/account_update_push_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/targets/{targetId}/push` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.update_status`<a id="appwriteconsoleaccountupdate_status"></a>

Block the currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. To completely delete a user, use the Users API instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_response = appwriteconsole.account.update_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.account.verify_authenticator`<a id="appwriteconsoleaccountverify_authenticator"></a>

Verify an authenticator app after adding it using the [add authenticator](/docs/references/cloud/client-web/account#addAuthenticator) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_authenticator_response = appwriteconsole.account.verify_authenticator(
    otp="<OTP>",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### otp: `str`<a id="otp-str"></a>

Valid verification token.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountVerifyAuthenticatorRequest`](./appwrite_console_python_sdk/type/account_verify_authenticator_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account/mfa/authenticators/{type}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.assistant.ask_query`<a id="appwriteconsoleassistantask_query"></a>

Ask Query

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.assistant.ask_query(
    prompt="<PROMPT>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prompt: `str`<a id="prompt-str"></a>

Prompt. A string containing questions asked to the AI assistant.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssistantAskQueryRequest`](./appwrite_console_python_sdk/type/assistant_ask_query_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/console/assistant` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.generate_qr_code`<a id="appwriteconsoleavatarsgenerate_qr_code"></a>

Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.generate_qr_code(
    text="text_example",
    size=400,
    margin=1,
    download=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### text: `str`<a id="text-str"></a>

Plain text to be converted to QR code image.

##### size: `int`<a id="size-int"></a>

QR code size. Pass an integer between 1 to 1000. Defaults to 400.

##### margin: `int`<a id="margin-int"></a>

Margin from edge. Pass an integer between 0 to 10. Defaults to 1.

##### download: `bool`<a id="download-bool"></a>

Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/qr` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_browser_icon`<a id="appwriteconsoleavatarsget_browser_icon"></a>

You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user [GET /account/sessions](https://appwrite.io/docs/references/cloud/client-web/account#getSessions) endpoint. Use width, height and quality arguments to change the output settings.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_browser_icon(
    code="aa",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Browser Code.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/browsers/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_credit_card_icon`<a id="appwriteconsoleavatarsget_credit_card_icon"></a>

The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_credit_card_icon(
    code="amex",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/credit-cards/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_favicon`<a id="appwriteconsoleavatarsget_favicon"></a>

Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_favicon(
    url="url_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Website URL which you want to fetch the favicon from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/favicon` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_flag_by_code`<a id="appwriteconsoleavatarsget_flag_by_code"></a>

You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings. Country codes follow the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) standard.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_flag_by_code(
    code="af",
    width=100,
    height=100,
    quality=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Country Code. ISO Alpha-2 country code format.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### quality: `int`<a id="quality-int"></a>

Image quality. Pass an integer between 0 to 100. Defaults to 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/flags/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_image_url_and_crop`<a id="appwriteconsoleavatarsget_image_url_and_crop"></a>

Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 400x400px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_image_url_and_crop(
    url="url_example",
    width=400,
    height=400,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Image URL which you want to crop.

##### width: `int`<a id="width-int"></a>

Resize preview image width, Pass an integer between 0 to 2000. Defaults to 400.

##### height: `int`<a id="height-int"></a>

Resize preview image height, Pass an integer between 0 to 2000. Defaults to 400.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/image` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.avatars.get_user_initials`<a id="appwriteconsoleavatarsget_user_initials"></a>

Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.

You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.

When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.avatars.get_user_initials(
    name="",
    width=500,
    height=500,
    background="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Full Name. When empty, current user name or email will be used. Max length: 128 chars.

##### width: `int`<a id="width-int"></a>

Image width. Pass an integer between 0 to 2000. Defaults to 100.

##### height: `int`<a id="height-int"></a>

Image height. Pass an integer between 0 to 2000. Defaults to 100.

##### background: `str`<a id="background-str"></a>

Changes background color. By default a random color will be picked and stay will persistent to the given name.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/avatars/initials` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.console.list_variables`<a id="appwriteconsoleconsolelist_variables"></a>

Get all Environment Variables that are relevant for the console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variables_response = appwriteconsole.console.list_variables()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ConsoleVariables`](./appwrite_console_python_sdk/pydantic/console_variables.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/console/variables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_boolean_attribute`<a id="appwriteconsoledatabasescreate_boolean_attribute"></a>

Create a boolean attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_boolean_attribute_response = appwriteconsole.databases.create_boolean_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default=False,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `bool`<a id="default-bool"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateBooleanAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_boolean_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeBoolean`](./appwrite_console_python_sdk/pydantic/attribute_boolean.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/boolean` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_collection`<a id="appwriteconsoledatabasescreate_collection"></a>

Create a new Collection. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_collection_response = appwriteconsole.databases.create_collection(
    collection_id="<COLLECTION_ID>",
    name="<NAME>",
    database_id="databaseId_example",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
    document_security=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Collection name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### permissions: [`DatabasesCreateCollectionRequestPermissions`](./appwrite_console_python_sdk/type/databases_create_collection_request_permissions.py)<a id="permissions-databasescreatecollectionrequestpermissionsappwrite_console_python_sdktypedatabases_create_collection_request_permissionspy"></a>

##### document_security: `bool`<a id="document_security-bool"></a>

Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateCollectionRequest`](./appwrite_console_python_sdk/type/databases_create_collection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_console_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_datetime_attribute`<a id="appwriteconsoledatabasescreate_datetime_attribute"></a>

Create a date time attribute according to the ISO 8601 standard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_datetime_attribute_response = appwriteconsole.databases.create_datetime_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="string_example",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for the attribute in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateDatetimeAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_datetime_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeDatetime`](./appwrite_console_python_sdk/pydantic/attribute_datetime.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/datetime` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_document`<a id="appwriteconsoledatabasescreate_document"></a>

Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_document_response = appwriteconsole.databases.create_document(
    document_id="<DOCUMENT_ID>",
    data={},
    database_id="databaseId_example",
    collection_id="collectionId_example",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### document_id: `str`<a id="document_id-str"></a>

Document ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Document data as JSON object.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection). Make sure to define attributes before creating documents.

##### permissions: [`DatabasesCreateDocumentRequestPermissions`](./appwrite_console_python_sdk/type/databases_create_document_request_permissions.py)<a id="permissions-databasescreatedocumentrequestpermissionsappwrite_console_python_sdktypedatabases_create_document_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateDocumentRequest`](./appwrite_console_python_sdk/type/databases_create_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_console_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_email_attribute`<a id="appwriteconsoledatabasescreate_email_attribute"></a>

Create an email attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_attribute_response = appwriteconsole.databases.create_email_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="email@example.com",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateEmailAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_email_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEmail`](./appwrite_console_python_sdk/pydantic/attribute_email.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_enum_attribute`<a id="appwriteconsoledatabasescreate_enum_attribute"></a>

Create an enumeration attribute. The `elements` param acts as a white-list of accepted values for this attribute. 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_enum_attribute_response = appwriteconsole.databases.create_enum_attribute(
    key="string_example",
    elements=[
        "string_example"
    ],
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="<DEFAULT>",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### elements: [`DatabasesCreateEnumAttributeRequestElements`](./appwrite_console_python_sdk/type/databases_create_enum_attribute_request_elements.py)<a id="elements-databasescreateenumattributerequestelementsappwrite_console_python_sdktypedatabases_create_enum_attribute_request_elementspy"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateEnumAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_enum_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEnum`](./appwrite_console_python_sdk/pydantic/attribute_enum.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/enum` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_float_attribute`<a id="appwriteconsoledatabasescreate_float_attribute"></a>

Create a float attribute. Optionally, minimum and maximum values can be provided.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_float_attribute_response = appwriteconsole.databases.create_float_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    min=3.14,
    max=3.14,
    default=3.14,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### min: `Union[int, float]`<a id="min-unionint-float"></a>

Minimum value to enforce on new documents

##### max: `Union[int, float]`<a id="max-unionint-float"></a>

Maximum value to enforce on new documents

##### default: `Union[int, float]`<a id="default-unionint-float"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateFloatAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_float_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeFloat`](./appwrite_console_python_sdk/pydantic/attribute_float.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/float` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_index_on_attributes`<a id="appwriteconsoledatabasescreate_index_on_attributes"></a>

Creates an index on the attributes listed. Your index should include all the attributes you will query in a single request.
Attributes can be `key`, `fulltext`, and `unique`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_index_on_attributes_response = appwriteconsole.databases.create_index_on_attributes(
    key="string_example",
    type="key",
    attributes=[
        "string_example"
    ],
    database_id="databaseId_example",
    collection_id="collectionId_example",
    orders=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Index Key.

##### type: `str`<a id="type-str"></a>

Index type.

##### attributes: [`DatabasesCreateIndexOnAttributesRequestAttributes`](./appwrite_console_python_sdk/type/databases_create_index_on_attributes_request_attributes.py)<a id="attributes-databasescreateindexonattributesrequestattributesappwrite_console_python_sdktypedatabases_create_index_on_attributes_request_attributespy"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### orders: [`DatabasesCreateIndexOnAttributesRequestOrders`](./appwrite_console_python_sdk/type/databases_create_index_on_attributes_request_orders.py)<a id="orders-databasescreateindexonattributesrequestordersappwrite_console_python_sdktypedatabases_create_index_on_attributes_request_orderspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIndexOnAttributesRequest`](./appwrite_console_python_sdk/type/databases_create_index_on_attributes_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Index`](./appwrite_console_python_sdk/pydantic/index.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_integer_attribute`<a id="appwriteconsoledatabasescreate_integer_attribute"></a>

Create an integer attribute. Optionally, minimum and maximum values can be provided.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_integer_attribute_response = appwriteconsole.databases.create_integer_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    min=1,
    max=1,
    default=1,
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### min: `int`<a id="min-int"></a>

Minimum value to enforce on new documents

##### max: `int`<a id="max-int"></a>

Maximum value to enforce on new documents

##### default: `int`<a id="default-int"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIntegerAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_integer_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeInteger`](./appwrite_console_python_sdk/pydantic/attribute_integer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/integer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_ip_attribute`<a id="appwriteconsoledatabasescreate_ip_attribute"></a>

Create IP address attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ip_attribute_response = appwriteconsole.databases.create_ip_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="string_example",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateIpAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_ip_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeIp`](./appwrite_console_python_sdk/pydantic/attribute_ip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/ip` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_new_database`<a id="appwriteconsoledatabasescreate_new_database"></a>

Create a new Database.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_database_response = appwriteconsole.databases.create_new_database(
    database_id="<DATABASE_ID>",
    name="<NAME>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Database name. Max length: 128 chars.

##### enabled: `bool`<a id="enabled-bool"></a>

Is the database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateNewDatabaseRequest`](./appwrite_console_python_sdk/type/databases_create_new_database_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_console_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_relationship_attribute`<a id="appwriteconsoledatabasescreate_relationship_attribute"></a>

Create relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_relationship_attribute_response = appwriteconsole.databases.create_relationship_attribute(
    related_collection_id="<RELATED_COLLECTION_ID>",
    type="oneToOne",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    two_way=False,
    key="string_example",
    two_way_key="string_example",
    on_delete="cascade",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### related_collection_id: `str`<a id="related_collection_id-str"></a>

Related Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### type: `str`<a id="type-str"></a>

Relation type

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### two_way: `bool`<a id="two_way-bool"></a>

Is Two Way?

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### two_way_key: `str`<a id="two_way_key-str"></a>

Two Way Attribute Key.

##### on_delete: `str`<a id="on_delete-str"></a>

Constraints option

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateRelationshipAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_relationship_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeRelationship`](./appwrite_console_python_sdk/pydantic/attribute_relationship.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/relationship` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_string_attribute`<a id="appwriteconsoledatabasescreate_string_attribute"></a>

Create a string attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_string_attribute_response = appwriteconsole.databases.create_string_attribute(
    key="string_example",
    size=1,
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="<DEFAULT>",
    array=False,
    encrypt=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### size: `int`<a id="size-int"></a>

Attribute size for text attributes, in number of characters.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

##### encrypt: `bool`<a id="encrypt-bool"></a>

Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateStringAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_string_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeString`](./appwrite_console_python_sdk/pydantic/attribute_string.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/string` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.create_url_attribute`<a id="appwriteconsoledatabasescreate_url_attribute"></a>

Create a URL attribute.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_url_attribute_response = appwriteconsole.databases.create_url_attribute(
    key="string_example",
    required=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    default="https://example.com",
    array=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### default: `str`<a id="default-str"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### array: `bool`<a id="array-bool"></a>

Is attribute an array?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesCreateUrlAttributeRequest`](./appwrite_console_python_sdk/type/databases_create_url_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeUrl`](./appwrite_console_python_sdk/pydantic/attribute_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/url` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.delete_attribute_by_id`<a id="appwriteconsoledatabasesdelete_attribute_by_id"></a>

Deletes an attribute.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.databases.delete_attribute_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.delete_by_id`<a id="appwriteconsoledatabasesdelete_by_id"></a>

Delete a database by its unique ID. Only API keys with with databases.write scope can delete a database.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.databases.delete_by_id(
    database_id="databaseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.delete_collection_by_id`<a id="appwriteconsoledatabasesdelete_collection_by_id"></a>

Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.databases.delete_collection_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.delete_document_by_id`<a id="appwriteconsoledatabasesdelete_document_by_id"></a>

Delete a document by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.databases.delete_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.delete_index_by_key`<a id="appwriteconsoledatabasesdelete_index_by_key"></a>

Delete an index.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.databases.delete_index_by_key(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Index Key.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes/{key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_attribute_by_id`<a id="appwriteconsoledatabasesget_attribute_by_id"></a>

Get attribute by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attribute_by_id_response = appwriteconsole.databases.get_attribute_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### 🔄 Return<a id="🔄-return"></a>

[`DatabasesGetAttributeByIdResponse`](./appwrite_console_python_sdk/pydantic/databases_get_attribute_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_by_id`<a id="appwriteconsoledatabasesget_by_id"></a>

Get a database by its unique ID. This endpoint response returns a JSON object with the database metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteconsole.databases.get_by_id(
    database_id="databaseId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_console_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_collection_by_id`<a id="appwriteconsoledatabasesget_collection_by_id"></a>

Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_by_id_response = appwriteconsole.databases.get_collection_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_console_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_collection_usage_stats`<a id="appwriteconsoledatabasesget_collection_usage_stats"></a>

Get collection usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_usage_stats_response = appwriteconsole.databases.get_collection_usage_stats(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageCollection`](./appwrite_console_python_sdk/pydantic/usage_collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_document_by_id`<a id="appwriteconsoledatabasesget_document_by_id"></a>

Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_by_id_response = appwriteconsole.databases.get_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.

#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_console_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_documents`<a id="appwriteconsoledatabasesget_documents"></a>

Get a list of all the user's documents in a given collection. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_documents_response = appwriteconsole.databases.get_documents(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentList`](./appwrite_console_python_sdk/pydantic/document_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_index_by_id`<a id="appwriteconsoledatabasesget_index_by_id"></a>

Get index by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_index_by_id_response = appwriteconsole.databases.get_index_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Index Key.

#### 🔄 Return<a id="🔄-return"></a>

[`Index`](./appwrite_console_python_sdk/pydantic/index.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_usage_stats`<a id="appwriteconsoledatabasesget_usage_stats"></a>

Get databases usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_response = appwriteconsole.databases.get_usage_stats(
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### range: `str`<a id="range-str"></a>

`Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageDatabases`](./appwrite_console_python_sdk/pydantic/usage_databases.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.get_usage_stats_0`<a id="appwriteconsoledatabasesget_usage_stats_0"></a>

Get database usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_0_response = appwriteconsole.databases.get_usage_stats_0(
    database_id="databaseId_example",
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### range: `str`<a id="range-str"></a>

`Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageDatabase`](./appwrite_console_python_sdk/pydantic/usage_database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_all_databases`<a id="appwriteconsoledatabaseslist_all_databases"></a>

Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_databases_response = appwriteconsole.databases.list_all_databases(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`DatabaseList`](./appwrite_console_python_sdk/pydantic/database_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_attributes`<a id="appwriteconsoledatabaseslist_attributes"></a>

List attributes in the collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_attributes_response = appwriteconsole.databases.list_attributes(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, size, required, array, status, error

#### 🔄 Return<a id="🔄-return"></a>

[`AttributeList`](./appwrite_console_python_sdk/pydantic/attribute_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_collection_indexes`<a id="appwriteconsoledatabaseslist_collection_indexes"></a>

List indexes in the collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_indexes_response = appwriteconsole.databases.list_collection_indexes(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, status, attributes, error

#### 🔄 Return<a id="🔄-return"></a>

[`IndexList`](./appwrite_console_python_sdk/pydantic/index_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/indexes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_collection_logs`<a id="appwriteconsoledatabaseslist_collection_logs"></a>

Get the collection activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collection_logs_response = appwriteconsole.databases.list_collection_logs(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_collections`<a id="appwriteconsoledatabaseslist_collections"></a>

Get a list of all collections that belong to the provided databaseId. You can use the search parameter to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_collections_response = appwriteconsole.databases.list_collections(
    database_id="databaseId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, documentSecurity

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionList`](./appwrite_console_python_sdk/pydantic/collection_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_document_logs`<a id="appwriteconsoledatabaseslist_document_logs"></a>

Get the document activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_document_logs_response = appwriteconsole.databases.list_document_logs(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.list_logs`<a id="appwriteconsoledatabaseslist_logs"></a>

Get the database activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_logs_response = appwriteconsole.databases.list_logs(
    database_id="databaseId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.patch_date_time_attribute`<a id="appwriteconsoledatabasespatch_date_time_attribute"></a>

Update a date time attribute. Changing the `default` value will not update already existing documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
patch_date_time_attribute_response = appwriteconsole.databases.patch_date_time_attribute(
    required=False,
    default="string_example",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesPatchDateTimeAttributeRequest`](./appwrite_console_python_sdk/type/databases_patch_date_time_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeDatetime`](./appwrite_console_python_sdk/pydantic/attribute_datetime.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_boolean_attribute`<a id="appwriteconsoledatabasesupdate_boolean_attribute"></a>

Update a boolean attribute. Changing the `default` value will not update already existing documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_boolean_attribute_response = appwriteconsole.databases.update_boolean_attribute(
    required=False,
    default=False,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[bool]`<a id="default-optionalbool"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateBooleanAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_boolean_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeBoolean`](./appwrite_console_python_sdk/pydantic/attribute_boolean.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_by_id`<a id="appwriteconsoledatabasesupdate_by_id"></a>

Update a database by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = appwriteconsole.databases.update_by_id(
    name="<NAME>",
    database_id="databaseId_example",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Database name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### enabled: `bool`<a id="enabled-bool"></a>

Is database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateByIdRequest`](./appwrite_console_python_sdk/type/databases_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Database`](./appwrite_console_python_sdk/pydantic/database.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_collection_by_id`<a id="appwriteconsoledatabasesupdate_collection_by_id"></a>

Update a collection by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_collection_by_id_response = appwriteconsole.databases.update_collection_by_id(
    name="<NAME>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
    document_security=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Collection name. Max length: 128 chars.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### permissions: [`DatabasesUpdateCollectionByIdRequestPermissions`](./appwrite_console_python_sdk/type/databases_update_collection_by_id_request_permissions.py)<a id="permissions-databasesupdatecollectionbyidrequestpermissionsappwrite_console_python_sdktypedatabases_update_collection_by_id_request_permissionspy"></a>

##### document_security: `bool`<a id="document_security-bool"></a>

Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateCollectionByIdRequest`](./appwrite_console_python_sdk/type/databases_update_collection_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collection`](./appwrite_console_python_sdk/pydantic/collection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_document_by_id`<a id="appwriteconsoledatabasesupdate_document_by_id"></a>

Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_document_by_id_response = appwriteconsole.databases.update_document_by_id(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    document_id="documentId_example",
    data={},
    permissions=[
        "[\"read(\"any\")\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID.

##### document_id: `str`<a id="document_id-str"></a>

Document ID.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Document data as JSON object. Include only attribute and value pairs to be updated.

##### permissions: [`DatabasesUpdateDocumentByIdRequestPermissions`](./appwrite_console_python_sdk/type/databases_update_document_by_id_request_permissions.py)<a id="permissions-databasesupdatedocumentbyidrequestpermissionsappwrite_console_python_sdktypedatabases_update_document_by_id_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateDocumentByIdRequest`](./appwrite_console_python_sdk/type/databases_update_document_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Document`](./appwrite_console_python_sdk/pydantic/document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/documents/{documentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_email_attribute`<a id="appwriteconsoledatabasesupdate_email_attribute"></a>

Update an email attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_attribute_response = appwriteconsole.databases.update_email_attribute(
    required=False,
    default="email@example.com",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateEmailAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_email_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEmail`](./appwrite_console_python_sdk/pydantic/attribute_email.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_enum_attribute`<a id="appwriteconsoledatabasesupdate_enum_attribute"></a>

Update an enum attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_enum_attribute_response = appwriteconsole.databases.update_enum_attribute(
    elements=[
        "string_example"
    ],
    required=False,
    default="<DEFAULT>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### elements: [`DatabasesUpdateEnumAttributeRequestElements`](./appwrite_console_python_sdk/type/databases_update_enum_attribute_request_elements.py)<a id="elements-databasesupdateenumattributerequestelementsappwrite_console_python_sdktypedatabases_update_enum_attribute_request_elementspy"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateEnumAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_enum_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeEnum`](./appwrite_console_python_sdk/pydantic/attribute_enum.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_float_attribute`<a id="appwriteconsoledatabasesupdate_float_attribute"></a>

Update a float attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_float_attribute_response = appwriteconsole.databases.update_float_attribute(
    required=False,
    min=3.14,
    max=3.14,
    default=3.14,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### min: `Union[int, float]`<a id="min-unionint-float"></a>

Minimum value to enforce on new documents

##### max: `Union[int, float]`<a id="max-unionint-float"></a>

Maximum value to enforce on new documents

##### default: `Optional[Union[int, float]]`<a id="default-optionalunionint-float"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateFloatAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_float_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeFloat`](./appwrite_console_python_sdk/pydantic/attribute_float.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_integer_attribute`<a id="appwriteconsoledatabasesupdate_integer_attribute"></a>

Update an integer attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_integer_attribute_response = appwriteconsole.databases.update_integer_attribute(
    required=False,
    min=1,
    max=1,
    default=1,
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### min: `int`<a id="min-int"></a>

Minimum value to enforce on new documents

##### max: `int`<a id="max-int"></a>

Maximum value to enforce on new documents

##### default: `Optional[int]`<a id="default-optionalint"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateIntegerAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_integer_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeInteger`](./appwrite_console_python_sdk/pydantic/attribute_integer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_ip_address_attribute`<a id="appwriteconsoledatabasesupdate_ip_address_attribute"></a>

Update an ip attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_ip_address_attribute_response = appwriteconsole.databases.update_ip_address_attribute(
    required=False,
    default="string_example",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateIpAddressAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_ip_address_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeIp`](./appwrite_console_python_sdk/pydantic/attribute_ip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_relationship_attribute`<a id="appwriteconsoledatabasesupdate_relationship_attribute"></a>

Update relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_relationship_attribute_response = appwriteconsole.databases.update_relationship_attribute(
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
    on_delete="cascade",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

##### on_delete: `str`<a id="on_delete-str"></a>

Constraints option

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateRelationshipAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_relationship_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeRelationship`](./appwrite_console_python_sdk/pydantic/attribute_relationship.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_string_attribute`<a id="appwriteconsoledatabasesupdate_string_attribute"></a>

Update a string attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_string_attribute_response = appwriteconsole.databases.update_string_attribute(
    required=False,
    default="<DEFAULT>",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateStringAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_string_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeString`](./appwrite_console_python_sdk/pydantic/attribute_string.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.databases.update_url_attribute`<a id="appwriteconsoledatabasesupdate_url_attribute"></a>

Update an url attribute. Changing the `default` value will not update already existing documents.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_url_attribute_response = appwriteconsole.databases.update_url_attribute(
    required=False,
    default="https://example.com",
    database_id="databaseId_example",
    collection_id="collectionId_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### required: `bool`<a id="required-bool"></a>

Is attribute required?

##### default: `Optional[str]`<a id="default-optionalstr"></a>

Default value for attribute when not provided. Cannot be set when attribute is required.

##### database_id: `str`<a id="database_id-str"></a>

Database ID.

##### collection_id: `str`<a id="collection_id-str"></a>

Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).

##### key: `str`<a id="key-str"></a>

Attribute Key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatabasesUpdateUrlAttributeRequest`](./appwrite_console_python_sdk/type/databases_update_url_attribute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AttributeUrl`](./appwrite_console_python_sdk/pydantic/attribute_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.create_deployment`<a id="appwriteconsolefunctionscreate_deployment"></a>

Create a new function code deployment. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's deployment to use your new deployment UID.

This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](https://appwrite.io/docs/functions).

Use the "command" param to set the entrypoint used to execute your code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_deployment_response = appwriteconsole.functions.create_deployment(
    function_id="functionId_example",
    code="string_example",
    activate=False,
    entrypoint="<ENTRYPOINT>",
    commands="<COMMANDS>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### code: `str`<a id="code-str"></a>

Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

##### activate: `bool`<a id="activate-bool"></a>

Automatically activate the deployment when it is finished building.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File.

##### commands: `str`<a id="commands-str"></a>

Build Commands.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateDeploymentRequest`](./appwrite_console_python_sdk/type/functions_create_deployment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Deployment`](./appwrite_console_python_sdk/pydantic/deployment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.create_function`<a id="appwriteconsolefunctionscreate_function"></a>

Create a new function. You can pass a list of [permissions](https://appwrite.io/docs/permissions) to allow different project users or team with access to execute the function using the client API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_function_response = appwriteconsole.functions.create_function(
    function_id="<FUNCTION_ID>",
    name="<NAME>",
    runtime="node-14.5",
    execute=[
        "[\"any\"]"
    ],
    events=[
        "string_example"
    ],
    schedule="string_example",
    timeout=1,
    enabled=False,
    logging=False,
    entrypoint="<ENTRYPOINT>",
    commands="<COMMANDS>",
    installation_id="<INSTALLATION_ID>",
    provider_repository_id="<PROVIDER_REPOSITORY_ID>",
    provider_branch="<PROVIDER_BRANCH>",
    provider_silent_mode=False,
    provider_root_directory="<PROVIDER_ROOT_DIRECTORY>",
    template_repository="<TEMPLATE_REPOSITORY>",
    template_owner="<TEMPLATE_OWNER>",
    template_root_directory="<TEMPLATE_ROOT_DIRECTORY>",
    template_branch="<TEMPLATE_BRANCH>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Function name. Max length: 128 chars.

##### runtime: `str`<a id="runtime-str"></a>

Execution runtime.

##### execute: [`FunctionsCreateFunctionRequestExecute`](./appwrite_console_python_sdk/type/functions_create_function_request_execute.py)<a id="execute-functionscreatefunctionrequestexecuteappwrite_console_python_sdktypefunctions_create_function_request_executepy"></a>

##### events: [`FunctionsCreateFunctionRequestEvents`](./appwrite_console_python_sdk/type/functions_create_function_request_events.py)<a id="events-functionscreatefunctionrequesteventsappwrite_console_python_sdktypefunctions_create_function_request_eventspy"></a>

##### schedule: `str`<a id="schedule-str"></a>

Schedule CRON syntax.

##### timeout: `int`<a id="timeout-int"></a>

Function maximum execution time in seconds.

##### enabled: `bool`<a id="enabled-bool"></a>

Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.

##### logging: `bool`<a id="logging-bool"></a>

Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File. This path is relative to the \\\"providerRootDirectory\\\".

##### commands: `str`<a id="commands-str"></a>

Build Commands.

##### installation_id: `str`<a id="installation_id-str"></a>

Appwrite Installation ID for VCS (Version Control System) deployment.

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository ID of the repo linked to the function.

##### provider_branch: `str`<a id="provider_branch-str"></a>

Production branch for the repo linked to the function.

##### provider_silent_mode: `bool`<a id="provider_silent_mode-bool"></a>

Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.

##### provider_root_directory: `str`<a id="provider_root_directory-str"></a>

Path to function code in the linked repo.

##### template_repository: `str`<a id="template_repository-str"></a>

Repository name of the template.

##### template_owner: `str`<a id="template_owner-str"></a>

The name of the owner of the template.

##### template_root_directory: `str`<a id="template_root_directory-str"></a>

Path to function code in the template repo.

##### template_branch: `str`<a id="template_branch-str"></a>

Production branch for the repo linked to the function template.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateFunctionRequest`](./appwrite_console_python_sdk/type/functions_create_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_console_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.create_variable`<a id="appwriteconsolefunctionscreate_variable"></a>

Create a new function environment variable. These variables can be accessed in the function at runtime as environment variables.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_variable_response = appwriteconsole.functions.create_variable(
    key="<KEY>",
    value="<VALUE>",
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsCreateVariableRequest`](./appwrite_console_python_sdk/type/functions_create_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.delete_deployment`<a id="appwriteconsolefunctionsdelete_deployment"></a>

Delete a code deployment by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.functions.delete_deployment(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.delete_function_by_id`<a id="appwriteconsolefunctionsdelete_function_by_id"></a>

Delete a function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.functions.delete_function_by_id(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.delete_variable_by_id`<a id="appwriteconsolefunctionsdelete_variable_by_id"></a>

Delete a variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.functions.delete_variable_by_id(
    function_id="functionId_example",
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.download_deployment_contents`<a id="appwriteconsolefunctionsdownload_deployment_contents"></a>

Get a Deployment's contents by its unique ID. This endpoint supports range requests for partial or streaming file download.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.functions.download_deployment_contents(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_by_id`<a id="appwriteconsolefunctionsget_by_id"></a>

Get a function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteconsole.functions.get_by_id(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_console_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_deployment_by_id`<a id="appwriteconsolefunctionsget_deployment_by_id"></a>

Get a code deployment by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deployment_by_id_response = appwriteconsole.functions.get_deployment_by_id(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Deployment`](./appwrite_console_python_sdk/pydantic/deployment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_execution_log`<a id="appwriteconsolefunctionsget_execution_log"></a>

Get a function execution log by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_execution_log_response = appwriteconsole.functions.get_execution_log(
    function_id="functionId_example",
    execution_id="executionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### execution_id: `str`<a id="execution_id-str"></a>

Execution ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Execution`](./appwrite_console_python_sdk/pydantic/execution.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions/{executionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_function_usage`<a id="appwriteconsolefunctionsget_function_usage"></a>

Get function usage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_function_usage_response = appwriteconsole.functions.get_function_usage(
    function_id="functionId_example",
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageFunction`](./appwrite_console_python_sdk/pydantic/usage_function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_usage_stats`<a id="appwriteconsolefunctionsget_usage_stats"></a>

Get functions usage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_response = appwriteconsole.functions.get_usage_stats(
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageFunctions`](./appwrite_console_python_sdk/pydantic/usage_functions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.get_variable_by_id`<a id="appwriteconsolefunctionsget_variable_by_id"></a>

Get a variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_variable_by_id_response = appwriteconsole.functions.get_variable_by_id(
    function_id="functionId_example",
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.list_all`<a id="appwriteconsolefunctionslist_all"></a>

Get a list of all the project's functions. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = appwriteconsole.functions.list_all(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, runtime, deployment, schedule, scheduleNext, schedulePrevious, timeout, entrypoint, commands, installationId

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionList`](./appwrite_console_python_sdk/pydantic/function_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.list_deployments`<a id="appwriteconsolefunctionslist_deployments"></a>

Get a list of all the project's code deployments. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_deployments_response = appwriteconsole.functions.list_deployments(
    function_id="functionId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: size, buildId, activate, entrypoint, commands

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`DeploymentList`](./appwrite_console_python_sdk/pydantic/deployment_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.list_executions`<a id="appwriteconsolefunctionslist_executions"></a>

Get a list of all the current user function execution logs. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_executions_response = appwriteconsole.functions.list_executions(
    function_id="functionId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: trigger, status, responseStatusCode, duration

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ExecutionList`](./appwrite_console_python_sdk/pydantic/execution_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.list_runtimes`<a id="appwriteconsolefunctionslist_runtimes"></a>

Get a list of all runtimes that are currently active on your instance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_runtimes_response = appwriteconsole.functions.list_runtimes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RuntimeList`](./appwrite_console_python_sdk/pydantic/runtime_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/runtimes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.list_variables`<a id="appwriteconsolefunctionslist_variables"></a>

Get a list of all variables of a specific function.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variables_response = appwriteconsole.functions.list_variables(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`VariableList`](./appwrite_console_python_sdk/pydantic/variable_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.retry_build`<a id="appwriteconsolefunctionsretry_build"></a>

Create a new build for an Appwrite Function deployment. This endpoint can be used to retry a failed build.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.functions.retry_build(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
    build_id="buildId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

##### build_id: `str`<a id="build_id-str"></a>

Build unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.trigger_execution`<a id="appwriteconsolefunctionstrigger_execution"></a>

Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_execution_response = appwriteconsole.functions.trigger_execution(
    function_id="functionId_example",
    body="<BODY>",
    _async=False,
    path="<PATH>",
    method="GET",
    headers={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### body: `str`<a id="body-str"></a>

HTTP body of execution. Default value is empty string.

##### _async: `bool`<a id="_async-bool"></a>

Execute code in the background. Default value is false.

##### path: `str`<a id="path-str"></a>

HTTP path of execution. Path can include query params. Default value is /

##### method: `str`<a id="method-str"></a>

HTTP method of execution. Default value is GET.

##### headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

HTTP headers of execution. Defaults to empty.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsTriggerExecutionRequest`](./appwrite_console_python_sdk/type/functions_trigger_execution_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Execution`](./appwrite_console_python_sdk/pydantic/execution.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/executions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.update_by_id`<a id="appwriteconsolefunctionsupdate_by_id"></a>

Update function by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = appwriteconsole.functions.update_by_id(
    name="<NAME>",
    function_id="functionId_example",
    runtime="node-14.5",
    execute=[
        "[\"any\"]"
    ],
    events=[
        "string_example"
    ],
    schedule="string_example",
    timeout=1,
    enabled=False,
    logging=False,
    entrypoint="<ENTRYPOINT>",
    commands="<COMMANDS>",
    installation_id="<INSTALLATION_ID>",
    provider_repository_id="<PROVIDER_REPOSITORY_ID>",
    provider_branch="<PROVIDER_BRANCH>",
    provider_silent_mode=False,
    provider_root_directory="<PROVIDER_ROOT_DIRECTORY>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Function name. Max length: 128 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### runtime: `str`<a id="runtime-str"></a>

Execution runtime.

##### execute: [`FunctionsUpdateByIdRequestExecute`](./appwrite_console_python_sdk/type/functions_update_by_id_request_execute.py)<a id="execute-functionsupdatebyidrequestexecuteappwrite_console_python_sdktypefunctions_update_by_id_request_executepy"></a>

##### events: [`FunctionsUpdateByIdRequestEvents`](./appwrite_console_python_sdk/type/functions_update_by_id_request_events.py)<a id="events-functionsupdatebyidrequesteventsappwrite_console_python_sdktypefunctions_update_by_id_request_eventspy"></a>

##### schedule: `str`<a id="schedule-str"></a>

Schedule CRON syntax.

##### timeout: `int`<a id="timeout-int"></a>

Maximum execution time in seconds.

##### enabled: `bool`<a id="enabled-bool"></a>

Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.

##### logging: `bool`<a id="logging-bool"></a>

Whether executions will be logged. When set to false, executions will not be logged, but will reduce resource used by your Appwrite project.

##### entrypoint: `str`<a id="entrypoint-str"></a>

Entrypoint File. This path is relative to the \\\"providerRootDirectory\\\".

##### commands: `str`<a id="commands-str"></a>

Build Commands.

##### installation_id: `str`<a id="installation_id-str"></a>

Appwrite Installation ID for VCS (Version Controle System) deployment.

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository ID of the repo linked to the function

##### provider_branch: `str`<a id="provider_branch-str"></a>

Production branch for the repo linked to the function

##### provider_silent_mode: `bool`<a id="provider_silent_mode-bool"></a>

Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.

##### provider_root_directory: `str`<a id="provider_root_directory-str"></a>

Path to function code in the linked repo.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsUpdateByIdRequest`](./appwrite_console_python_sdk/type/functions_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_console_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.update_deployment_by_function_and_id`<a id="appwriteconsolefunctionsupdate_deployment_by_function_and_id"></a>

Update the function code deployment ID using the unique function ID. Use this endpoint to switch the code deployment that should be executed by the execution endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_deployment_by_function_and_id_response = appwriteconsole.functions.update_deployment_by_function_and_id(
    function_id="functionId_example",
    deployment_id="deploymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function ID.

##### deployment_id: `str`<a id="deployment_id-str"></a>

Deployment ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Function`](./appwrite_console_python_sdk/pydantic/function.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/deployments/{deploymentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.functions.update_variable_by_id`<a id="appwriteconsolefunctionsupdate_variable_by_id"></a>

Update variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_variable_by_id_response = appwriteconsole.functions.update_variable_by_id(
    key="<KEY>",
    function_id="functionId_example",
    variable_id="variableId_example",
    value="<VALUE>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### function_id: `str`<a id="function_id-str"></a>

Function unique ID.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionsUpdateVariableByIdRequest`](./appwrite_console_python_sdk/type/functions_update_variable_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/functions/{functionId}/variables/{variableId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.graphql.execute_mutation`<a id="appwriteconsolegraphqlexecute_mutation"></a>

Execute a GraphQL mutation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_mutation_response = appwriteconsole.graphql.execute_mutation()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Any`](./appwrite_console_python_sdk/pydantic/any.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/graphql` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.graphql.execute_mutation_0`<a id="appwriteconsolegraphqlexecute_mutation_0"></a>

Execute a GraphQL mutation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_mutation_0_response = appwriteconsole.graphql.execute_mutation_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Any`](./appwrite_console_python_sdk/pydantic/any.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/graphql/mutation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.certificates_queue_count`<a id="appwriteconsolehealthcertificates_queue_count"></a>

Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
certificates_queue_count_response = appwriteconsole.health.certificates_queue_count(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/certificates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_appwrite_http_server`<a id="appwriteconsolehealthcheck_appwrite_http_server"></a>

Check the Appwrite HTTP server is up and responsive.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_appwrite_http_server_response = appwriteconsole.health.check_appwrite_http_server()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_av_status`<a id="appwriteconsolehealthcheck_av_status"></a>

Check the Appwrite Antivirus server is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_av_status_response = appwriteconsole.health.check_av_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthAntivirus`](./appwrite_console_python_sdk/pydantic/health_antivirus.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/anti-virus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_cache_status`<a id="appwriteconsolehealthcheck_cache_status"></a>

Check the Appwrite in-memory cache servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_cache_status_response = appwriteconsole.health.check_cache_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/cache` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_database_status`<a id="appwriteconsolehealthcheck_database_status"></a>

Check the Appwrite database servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_database_status_response = appwriteconsole.health.check_database_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/db` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_local_storage`<a id="appwriteconsolehealthcheck_local_storage"></a>

Check the Appwrite local storage device is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_local_storage_response = appwriteconsole.health.check_local_storage()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/storage/local` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_queue_status`<a id="appwriteconsolehealthcheck_queue_status"></a>

Check the Appwrite queue messaging servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_queue_status_response = appwriteconsole.health.check_queue_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.check_storage_device`<a id="appwriteconsolehealthcheck_storage_device"></a>

Check the Appwrite storage device is up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_storage_device_response = appwriteconsole.health.check_storage_device()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/storage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.functions_queue_count`<a id="appwriteconsolehealthfunctions_queue_count"></a>

Get the number of function executions that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
functions_queue_count_response = appwriteconsole.health.functions_queue_count(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_builds_queue`<a id="appwriteconsolehealthget_builds_queue"></a>

Get the number of builds that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_builds_queue_response = appwriteconsole.health.get_builds_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/builds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_databases_queue`<a id="appwriteconsolehealthget_databases_queue"></a>

Get the number of database changes that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_databases_queue_response = appwriteconsole.health.get_databases_queue(
    name="database_db_main",
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Queue name for which to check the queue size

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/databases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_failed_jobs`<a id="appwriteconsolehealthget_failed_jobs"></a>

Returns the amount of failed jobs in a given queue.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_failed_jobs_response = appwriteconsole.health.get_failed_jobs(
    name="v1-database",
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the queue

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/failed/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_mails_queue`<a id="appwriteconsolehealthget_mails_queue"></a>

Get the number of mails that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mails_queue_response = appwriteconsole.health.get_mails_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/mails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_messaging_queue`<a id="appwriteconsolehealthget_messaging_queue"></a>

Get the number of messages that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_messaging_queue_response = appwriteconsole.health.get_messaging_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/messaging` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_migrations_queue`<a id="appwriteconsolehealthget_migrations_queue"></a>

Get the number of migrations that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_migrations_queue_response = appwriteconsole.health.get_migrations_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/migrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_queue_deletes`<a id="appwriteconsolehealthget_queue_deletes"></a>

Get the number of background destructive changes that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_deletes_response = appwriteconsole.health.get_queue_deletes(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/deletes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_queue_logs`<a id="appwriteconsolehealthget_queue_logs"></a>

Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_logs_response = appwriteconsole.health.get_queue_logs(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_queue_usage_metrics`<a id="appwriteconsolehealthget_queue_usage_metrics"></a>

Get the number of metrics that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_usage_metrics_response = appwriteconsole.health.get_queue_usage_metrics(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_ssl_certificate`<a id="appwriteconsolehealthget_ssl_certificate"></a>

Get the SSL certificate for a domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ssl_certificate_response = appwriteconsole.health.get_ssl_certificate(
    domain="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

string

#### 🔄 Return<a id="🔄-return"></a>

[`HealthCertificate`](./appwrite_console_python_sdk/pydantic/health_certificate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/certificate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.get_usage_dump_queue`<a id="appwriteconsolehealthget_usage_dump_queue"></a>

Get the number of projects containing metrics that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_dump_queue_response = appwriteconsole.health.get_usage_dump_queue(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/usage-dump` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.pubsub_get`<a id="appwriteconsolehealthpubsub_get"></a>

Check the Appwrite pub-sub servers are up and connection is successful.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pubsub_get_response = appwriteconsole.health.pubsub_get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthStatus`](./appwrite_console_python_sdk/pydantic/health_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/pubsub` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.sync_time_with_ntp`<a id="appwriteconsolehealthsync_time_with_ntp"></a>

Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sync_time_with_ntp_response = appwriteconsole.health.sync_time_with_ntp()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthTime`](./appwrite_console_python_sdk/pydantic/health_time.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/time` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.health.webhooks_queue_count`<a id="appwriteconsolehealthwebhooks_queue_count"></a>

Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhooks_queue_count_response = appwriteconsole.health.webhooks_queue_count(
    threshold=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### threshold: `int`<a id="threshold-int"></a>

Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.

#### 🔄 Return<a id="🔄-return"></a>

[`HealthQueue`](./appwrite_console_python_sdk/pydantic/health_queue.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/queue/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.get_user_locale_details`<a id="appwriteconsolelocaleget_user_locale_details"></a>

Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.

([IP Geolocation by DB-IP](https://db-ip.com))

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_locale_details_response = appwriteconsole.locale.get_user_locale_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Locale`](./appwrite_console_python_sdk/pydantic/locale.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_codes`<a id="appwriteconsolelocalelist_codes"></a>

List of all locale codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_codes_response = appwriteconsole.locale.list_codes()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LocaleCodeList`](./appwrite_console_python_sdk/pydantic/locale_code_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_continents`<a id="appwriteconsolelocalelist_continents"></a>

List of all continents. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_continents_response = appwriteconsole.locale.list_continents()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContinentList`](./appwrite_console_python_sdk/pydantic/continent_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/continents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_countries`<a id="appwriteconsolelocalelist_countries"></a>

List of all countries. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_countries_response = appwriteconsole.locale.list_countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CountryList`](./appwrite_console_python_sdk/pydantic/country_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_countries_phones`<a id="appwriteconsolelocalelist_countries_phones"></a>

List of all countries phone codes. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_countries_phones_response = appwriteconsole.locale.list_countries_phones()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneList`](./appwrite_console_python_sdk/pydantic/phone_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries/phones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_currencies`<a id="appwriteconsolelocalelist_currencies"></a>

List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_currencies_response = appwriteconsole.locale.list_currencies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CurrencyList`](./appwrite_console_python_sdk/pydantic/currency_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/currencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_eu_countries`<a id="appwriteconsolelocalelist_eu_countries"></a>

List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_eu_countries_response = appwriteconsole.locale.list_eu_countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CountryList`](./appwrite_console_python_sdk/pydantic/country_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/countries/eu` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.locale.list_languages`<a id="appwriteconsolelocalelist_languages"></a>

List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_languages_response = appwriteconsole.locale.list_languages()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LanguageList`](./appwrite_console_python_sdk/pydantic/language_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locale/languages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_apns_provider`<a id="appwriteconsolemessagingcreate_apns_provider"></a>

Create a new Apple Push Notification service provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_apns_provider_response = appwriteconsole.messaging.create_apns_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    auth_key="<AUTH_KEY>",
    auth_key_id="<AUTH_KEY_ID>",
    team_id="<TEAM_ID>",
    bundle_id="<BUNDLE_ID>",
    sandbox=False,
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### auth_key: `str`<a id="auth_key-str"></a>

APNS authentication key.

##### auth_key_id: `str`<a id="auth_key_id-str"></a>

APNS authentication key ID.

##### team_id: `str`<a id="team_id-str"></a>

APNS team ID.

##### bundle_id: `str`<a id="bundle_id-str"></a>

APNS bundle ID.

##### sandbox: `bool`<a id="sandbox-bool"></a>

Use APNS sandbox environment.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateApnsProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_apns_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/apns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_email_message`<a id="appwriteconsolemessagingcreate_email_message"></a>

Create a new email message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_message_response = appwriteconsole.messaging.create_email_message(
    message_id="<MESSAGE_ID>",
    subject="<SUBJECT>",
    content="<CONTENT>",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    attachments=[
        "string_example"
    ],
    draft=False,
    html=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### subject: `str`<a id="subject-str"></a>

Email Subject.

##### content: `str`<a id="content-str"></a>

Email Content.

##### topics: [`MessagingCreateEmailMessageRequestTopics`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_topics.py)<a id="topics-messagingcreateemailmessagerequesttopicsappwrite_console_python_sdktypemessaging_create_email_message_request_topicspy"></a>

##### users: [`MessagingCreateEmailMessageRequestUsers`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_users.py)<a id="users-messagingcreateemailmessagerequestusersappwrite_console_python_sdktypemessaging_create_email_message_request_userspy"></a>

##### targets: [`MessagingCreateEmailMessageRequestTargets`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_targets.py)<a id="targets-messagingcreateemailmessagerequesttargetsappwrite_console_python_sdktypemessaging_create_email_message_request_targetspy"></a>

##### cc: [`MessagingCreateEmailMessageRequestCc`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_cc.py)<a id="cc-messagingcreateemailmessagerequestccappwrite_console_python_sdktypemessaging_create_email_message_request_ccpy"></a>

##### bcc: [`MessagingCreateEmailMessageRequestBcc`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_bcc.py)<a id="bcc-messagingcreateemailmessagerequestbccappwrite_console_python_sdktypemessaging_create_email_message_request_bccpy"></a>

##### attachments: [`MessagingCreateEmailMessageRequestAttachments`](./appwrite_console_python_sdk/type/messaging_create_email_message_request_attachments.py)<a id="attachments-messagingcreateemailmessagerequestattachmentsappwrite_console_python_sdktypemessaging_create_email_message_request_attachmentspy"></a>

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### html: `bool`<a id="html-bool"></a>

Is content of type HTML

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateEmailMessageRequest`](./appwrite_console_python_sdk/type/messaging_create_email_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_fcm_provider`<a id="appwriteconsolemessagingcreate_fcm_provider"></a>

Create a new Firebase Cloud Messaging provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_fcm_provider_response = appwriteconsole.messaging.create_fcm_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    service_account_json={},
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### service_account_json: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="service_account_json-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

FCM service account JSON.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateFcmProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_fcm_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/fcm` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_mailgun_provider`<a id="appwriteconsolemessagingcreate_mailgun_provider"></a>

Create a new Mailgun provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_mailgun_provider_response = appwriteconsole.messaging.create_mailgun_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    api_key="<API_KEY>",
    domain="<DOMAIN>",
    is_eu_region=False,
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Mailgun API Key.

##### domain: `str`<a id="domain-str"></a>

Mailgun Domain.

##### is_eu_region: `bool`<a id="is_eu_region-bool"></a>

Set as EU region.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateMailgunProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_mailgun_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/mailgun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_msg_provider`<a id="appwriteconsolemessagingcreate_msg_provider"></a>

Create a new MSG91 provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_msg_provider_response = appwriteconsole.messaging.create_msg_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    sender_id="<SENDER_ID>",
    auth_key="<AUTH_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### sender_id: `str`<a id="sender_id-str"></a>

Msg91 Sender ID.

##### auth_key: `str`<a id="auth_key-str"></a>

Msg91 Auth Key.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateMsgProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_msg_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/msg91` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_new_topic`<a id="appwriteconsolemessagingcreate_new_topic"></a>

Create a new topic.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_topic_response = appwriteconsole.messaging.create_new_topic(
    topic_id="<TOPIC_ID>",
    name="<NAME>",
    subscribe=[
        "[\"any\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. Choose a custom Topic ID or a new Topic ID.

##### name: `str`<a id="name-str"></a>

Topic Name.

##### subscribe: [`MessagingCreateNewTopicRequestSubscribe`](./appwrite_console_python_sdk/type/messaging_create_new_topic_request_subscribe.py)<a id="subscribe-messagingcreatenewtopicrequestsubscribeappwrite_console_python_sdktypemessaging_create_new_topic_request_subscribepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateNewTopicRequest`](./appwrite_console_python_sdk/type/messaging_create_new_topic_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_console_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_push_notification`<a id="appwriteconsolemessagingcreate_push_notification"></a>

Create a new push notification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_push_notification_response = appwriteconsole.messaging.create_push_notification(
    title="<TITLE>",
    message_id="<MESSAGE_ID>",
    body="<BODY>",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    data={},
    action="<ACTION>",
    image="[ID1:ID2]",
    icon="<ICON>",
    sound="<SOUND>",
    color="<COLOR>",
    tag="<TAG>",
    badge="<BADGE>",
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title for push notification.

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### body: `str`<a id="body-str"></a>

Body for push notification.

##### topics: [`MessagingCreatePushNotificationRequestTopics`](./appwrite_console_python_sdk/type/messaging_create_push_notification_request_topics.py)<a id="topics-messagingcreatepushnotificationrequesttopicsappwrite_console_python_sdktypemessaging_create_push_notification_request_topicspy"></a>

##### users: [`MessagingCreatePushNotificationRequestUsers`](./appwrite_console_python_sdk/type/messaging_create_push_notification_request_users.py)<a id="users-messagingcreatepushnotificationrequestusersappwrite_console_python_sdktypemessaging_create_push_notification_request_userspy"></a>

##### targets: [`MessagingCreatePushNotificationRequestTargets`](./appwrite_console_python_sdk/type/messaging_create_push_notification_request_targets.py)<a id="targets-messagingcreatepushnotificationrequesttargetsappwrite_console_python_sdktypemessaging_create_push_notification_request_targetspy"></a>

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Additional Data for push notification.

##### action: `str`<a id="action-str"></a>

Action for push notification.

##### image: `str`<a id="image-str"></a>

Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.

##### icon: `str`<a id="icon-str"></a>

Icon for push notification. Available only for Android and Web Platform.

##### sound: `str`<a id="sound-str"></a>

Sound for push notification. Available only for Android and IOS Platform.

##### color: `str`<a id="color-str"></a>

Color for push notification. Available only for Android Platform.

##### tag: `str`<a id="tag-str"></a>

Tag for push notification. Available only for Android Platform.

##### badge: `str`<a id="badge-str"></a>

Badge for push notification. Available only for IOS Platform.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreatePushNotificationRequest`](./appwrite_console_python_sdk/type/messaging_create_push_notification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/push` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_sendgrid_provider`<a id="appwriteconsolemessagingcreate_sendgrid_provider"></a>

Create a new Sendgrid provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sendgrid_provider_response = appwriteconsole.messaging.create_sendgrid_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    api_key="<API_KEY>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Sendgrid API key.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSendgridProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_sendgrid_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/sendgrid` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_sms_message`<a id="appwriteconsolemessagingcreate_sms_message"></a>

Create a new SMS message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sms_message_response = appwriteconsole.messaging.create_sms_message(
    message_id="<MESSAGE_ID>",
    content="<CONTENT>",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### content: `str`<a id="content-str"></a>

SMS Content.

##### topics: [`MessagingCreateSmsMessageRequestTopics`](./appwrite_console_python_sdk/type/messaging_create_sms_message_request_topics.py)<a id="topics-messagingcreatesmsmessagerequesttopicsappwrite_console_python_sdktypemessaging_create_sms_message_request_topicspy"></a>

##### users: [`MessagingCreateSmsMessageRequestUsers`](./appwrite_console_python_sdk/type/messaging_create_sms_message_request_users.py)<a id="users-messagingcreatesmsmessagerequestusersappwrite_console_python_sdktypemessaging_create_sms_message_request_userspy"></a>

##### targets: [`MessagingCreateSmsMessageRequestTargets`](./appwrite_console_python_sdk/type/messaging_create_sms_message_request_targets.py)<a id="targets-messagingcreatesmsmessagerequesttargetsappwrite_console_python_sdktypemessaging_create_sms_message_request_targetspy"></a>

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSmsMessageRequest`](./appwrite_console_python_sdk/type/messaging_create_sms_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/sms` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_smtp_provider`<a id="appwriteconsolemessagingcreate_smtp_provider"></a>

Create a new SMTP provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_smtp_provider_response = appwriteconsole.messaging.create_smtp_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    host="<HOST>",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    encryption="none",
    auto_tls=False,
    mailer="<MAILER>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="email@example.com",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### host: `str`<a id="host-str"></a>

SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\\\"`. Hosts will be tried in order.

##### port: `int`<a id="port-int"></a>

The default SMTP server port.

##### username: `str`<a id="username-str"></a>

Authentication username.

##### password: `str`<a id="password-str"></a>

Authentication password.

##### encryption: `str`<a id="encryption-str"></a>

Encryption type. Can be omitted, 'ssl', or 'tls'

##### auto_tls: `bool`<a id="auto_tls-bool"></a>

Enable SMTP AutoTLS feature.

##### mailer: `str`<a id="mailer-str"></a>

The value to use for the X-Mailer header.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSmtpProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_smtp_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/smtp` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_subscriber`<a id="appwriteconsolemessagingcreate_subscriber"></a>

Create a new subscriber.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subscriber_response = appwriteconsole.messaging.create_subscriber(
    subscriber_id="<SUBSCRIBER_ID>",
    target_id="<TARGET_ID>",
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID. Choose a custom Subscriber ID or a new Subscriber ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID. The target ID to link to the specified Topic ID.

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID to subscribe to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateSubscriberRequest`](./appwrite_console_python_sdk/type/messaging_create_subscriber_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Subscriber`](./appwrite_console_python_sdk/pydantic/subscriber.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_telesign_provider`<a id="appwriteconsolemessagingcreate_telesign_provider"></a>

Create a new Telesign provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_telesign_provider_response = appwriteconsole.messaging.create_telesign_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    customer_id="<CUSTOMER_ID>",
    api_key="<API_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### customer_id: `str`<a id="customer_id-str"></a>

Telesign customer ID.

##### api_key: `str`<a id="api_key-str"></a>

Telesign API key.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTelesignProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_telesign_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/telesign` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_textmagic_provider`<a id="appwriteconsolemessagingcreate_textmagic_provider"></a>

Create a new Textmagic provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_textmagic_provider_response = appwriteconsole.messaging.create_textmagic_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    username="<USERNAME>",
    api_key="<API_KEY>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### username: `str`<a id="username-str"></a>

Textmagic username.

##### api_key: `str`<a id="api_key-str"></a>

Textmagic apiKey.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTextmagicProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_textmagic_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/textmagic` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_twilio_provider`<a id="appwriteconsolemessagingcreate_twilio_provider"></a>

Create a new Twilio provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_twilio_provider_response = appwriteconsole.messaging.create_twilio_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    account_sid="<ACCOUNT_SID>",
    auth_token="<AUTH_TOKEN>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### account_sid: `str`<a id="account_sid-str"></a>

Twilio account secret ID.

##### auth_token: `str`<a id="auth_token-str"></a>

Twilio authentication token.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateTwilioProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_twilio_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/twilio` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.create_vonage_provider`<a id="appwriteconsolemessagingcreate_vonage_provider"></a>

Create a new Vonage provider.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_vonage_provider_response = appwriteconsole.messaging.create_vonage_provider(
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
    _from="+12065550100",
    api_key="<API_KEY>",
    api_secret="<API_SECRET>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Provider name.

##### _from: `str`<a id="_from-str"></a>

Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### api_key: `str`<a id="api_key-str"></a>

Vonage API key.

##### api_secret: `str`<a id="api_secret-str"></a>

Vonage API secret.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingCreateVonageProviderRequest`](./appwrite_console_python_sdk/type/messaging_create_vonage_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/vonage` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.delete_message`<a id="appwriteconsolemessagingdelete_message"></a>

Delete a message. If the message is not a draft or scheduled, but has been sent, this will not recall the message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.messaging.delete_message(
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.delete_provider_by_id`<a id="appwriteconsolemessagingdelete_provider_by_id"></a>

Delete a provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.messaging.delete_provider_by_id(
    provider_id="providerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.delete_subscriber_by_id`<a id="appwriteconsolemessagingdelete_subscriber_by_id"></a>

Delete a subscriber by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.messaging.delete_subscriber_by_id(
    topic_id="topicId_example",
    subscriber_id="subscriberId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers/{subscriberId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.delete_topic_by_id`<a id="appwriteconsolemessagingdelete_topic_by_id"></a>

Delete a topic by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.messaging.delete_topic_by_id(
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.get_message_by_id`<a id="appwriteconsolemessagingget_message_by_id"></a>

Get a message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_message_by_id_response = appwriteconsole.messaging.get_message_by_id(
    message_id="messageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.get_provider_by_id`<a id="appwriteconsolemessagingget_provider_by_id"></a>

Get a provider by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_provider_by_id_response = appwriteconsole.messaging.get_provider_by_id(
    provider_id="providerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.get_subscriber_by_id`<a id="appwriteconsolemessagingget_subscriber_by_id"></a>

Get a subscriber by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscriber_by_id_response = appwriteconsole.messaging.get_subscriber_by_id(
    topic_id="topicId_example",
    subscriber_id="subscriberId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Subscriber`](./appwrite_console_python_sdk/pydantic/subscriber.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers/{subscriberId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.get_topic_by_id`<a id="appwriteconsolemessagingget_topic_by_id"></a>

Get a topic by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_topic_by_id_response = appwriteconsole.messaging.get_topic_by_id(
    topic_id="topicId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_console_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_all_messages`<a id="appwriteconsolemessaginglist_all_messages"></a>

Get a list of all messages from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_messages_response = appwriteconsole.messaging.list_all_messages(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: scheduledAt, deliveredAt, deliveredTotal, status, description, providerType

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageList`](./appwrite_console_python_sdk/pydantic/message_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_message_logs`<a id="appwriteconsolemessaginglist_message_logs"></a>

Get the message activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_message_logs_response = appwriteconsole.messaging.list_message_logs(
    message_id="messageId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_provider_logs`<a id="appwriteconsolemessaginglist_provider_logs"></a>

Get the provider activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_provider_logs_response = appwriteconsole.messaging.list_provider_logs(
    provider_id="providerId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/{providerId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_providers`<a id="appwriteconsolemessaginglist_providers"></a>

Get a list of all providers from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_providers_response = appwriteconsole.messaging.list_providers(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ProviderList`](./appwrite_console_python_sdk/pydantic/provider_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_subscriber_logs`<a id="appwriteconsolemessaginglist_subscriber_logs"></a>

Get the subscriber activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscriber_logs_response = appwriteconsole.messaging.list_subscriber_logs(
    subscriber_id="subscriberId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriber_id: `str`<a id="subscriber_id-str"></a>

Subscriber ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/subscribers/{subscriberId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_subscribers`<a id="appwriteconsolemessaginglist_subscribers"></a>

Get a list of all subscribers from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_subscribers_response = appwriteconsole.messaging.list_subscribers(
    topic_id="topicId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID. The topic ID subscribed to.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`SubscriberList`](./appwrite_console_python_sdk/pydantic/subscriber_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/subscribers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_targets`<a id="appwriteconsolemessaginglist_targets"></a>

Get a list of the targets associated with a message.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_targets_response = appwriteconsole.messaging.list_targets(
    message_id="messageId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, providerId, identifier, providerType

#### 🔄 Return<a id="🔄-return"></a>

[`TargetList`](./appwrite_console_python_sdk/pydantic/target_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/{messageId}/targets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_topic_logs`<a id="appwriteconsolemessaginglist_topic_logs"></a>

Get the topic activity logs listed by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_topic_logs_response = appwriteconsole.messaging.list_topic_logs(
    topic_id="topicId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.list_topics`<a id="appwriteconsolemessaginglist_topics"></a>

Get a list of all topics from the current Appwrite project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_topics_response = appwriteconsole.messaging.list_topics(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, description, emailTotal, smsTotal, pushTotal

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`TopicList`](./appwrite_console_python_sdk/pydantic/topic_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_apns_provider`<a id="appwriteconsolemessagingupdate_apns_provider"></a>

Update a Apple Push Notification service provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_apns_provider_response = appwriteconsole.messaging.update_apns_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    auth_key="<AUTH_KEY>",
    auth_key_id="<AUTH_KEY_ID>",
    team_id="<TEAM_ID>",
    bundle_id="<BUNDLE_ID>",
    sandbox=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### auth_key: `str`<a id="auth_key-str"></a>

APNS authentication key.

##### auth_key_id: `str`<a id="auth_key_id-str"></a>

APNS authentication key ID.

##### team_id: `str`<a id="team_id-str"></a>

APNS team ID.

##### bundle_id: `str`<a id="bundle_id-str"></a>

APNS bundle ID.

##### sandbox: `bool`<a id="sandbox-bool"></a>

Use APNS sandbox environment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateApnsProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_apns_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/apns/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_email_by_id`<a id="appwriteconsolemessagingupdate_email_by_id"></a>

Update an email message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_by_id_response = appwriteconsole.messaging.update_email_by_id(
    message_id="messageId_example",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    subject="<SUBJECT>",
    content="<CONTENT>",
    draft=False,
    html=False,
    cc=[
        "string_example"
    ],
    bcc=[
        "string_example"
    ],
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### topics: [`MessagingUpdateEmailByIdRequestTopics`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request_topics.py)<a id="topics-messagingupdateemailbyidrequesttopicsappwrite_console_python_sdktypemessaging_update_email_by_id_request_topicspy"></a>

##### users: [`MessagingUpdateEmailByIdRequestUsers`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request_users.py)<a id="users-messagingupdateemailbyidrequestusersappwrite_console_python_sdktypemessaging_update_email_by_id_request_userspy"></a>

##### targets: [`MessagingUpdateEmailByIdRequestTargets`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request_targets.py)<a id="targets-messagingupdateemailbyidrequesttargetsappwrite_console_python_sdktypemessaging_update_email_by_id_request_targetspy"></a>

##### subject: `str`<a id="subject-str"></a>

Email Subject.

##### content: `str`<a id="content-str"></a>

Email Content.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### html: `bool`<a id="html-bool"></a>

Is content of type HTML

##### cc: [`MessagingUpdateEmailByIdRequestCc`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request_cc.py)<a id="cc-messagingupdateemailbyidrequestccappwrite_console_python_sdktypemessaging_update_email_by_id_request_ccpy"></a>

##### bcc: [`MessagingUpdateEmailByIdRequestBcc`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request_bcc.py)<a id="bcc-messagingupdateemailbyidrequestbccappwrite_console_python_sdktypemessaging_update_email_by_id_request_bccpy"></a>

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateEmailByIdRequest`](./appwrite_console_python_sdk/type/messaging_update_email_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/email/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_fcm_provider`<a id="appwriteconsolemessagingupdate_fcm_provider"></a>

Update a Firebase Cloud Messaging provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_fcm_provider_response = appwriteconsole.messaging.update_fcm_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    service_account_json={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### service_account_json: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="service_account_json-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

FCM service account JSON.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateFcmProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_fcm_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/fcm/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_mailgun_provider`<a id="appwriteconsolemessagingupdate_mailgun_provider"></a>

Update a Mailgun provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mailgun_provider_response = appwriteconsole.messaging.update_mailgun_provider(
    provider_id="providerId_example",
    name="<NAME>",
    api_key="<API_KEY>",
    domain="<DOMAIN>",
    is_eu_region=False,
    enabled=False,
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### api_key: `str`<a id="api_key-str"></a>

Mailgun API Key.

##### domain: `str`<a id="domain-str"></a>

Mailgun Domain.

##### is_eu_region: `bool`<a id="is_eu_region-bool"></a>

Set as EU region.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the reply to field for the mail. Default value is sender name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the reply to field for the mail. Default value is sender email.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateMailgunProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_mailgun_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/mailgun/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_provider_by_id`<a id="appwriteconsolemessagingupdate_provider_by_id"></a>

Update a MSG91 provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_provider_by_id_response = appwriteconsole.messaging.update_provider_by_id(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    sender_id="<SENDER_ID>",
    auth_key="<AUTH_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### sender_id: `str`<a id="sender_id-str"></a>

Msg91 Sender ID.

##### auth_key: `str`<a id="auth_key-str"></a>

Msg91 Auth Key.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateProviderByIdRequest`](./appwrite_console_python_sdk/type/messaging_update_provider_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/msg91/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_push_message`<a id="appwriteconsolemessagingupdate_push_message"></a>

Update a push notification by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_push_message_response = appwriteconsole.messaging.update_push_message(
    message_id="messageId_example",
    title="<TITLE>",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    body="<BODY>",
    data={},
    action="<ACTION>",
    image="[ID1:ID2]",
    icon="<ICON>",
    sound="<SOUND>",
    color="<COLOR>",
    tag="<TAG>",
    badge=1,
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### title: `str`<a id="title-str"></a>

Title for push notification.

##### topics: [`MessagingUpdatePushMessageRequestTopics`](./appwrite_console_python_sdk/type/messaging_update_push_message_request_topics.py)<a id="topics-messagingupdatepushmessagerequesttopicsappwrite_console_python_sdktypemessaging_update_push_message_request_topicspy"></a>

##### users: [`MessagingUpdatePushMessageRequestUsers`](./appwrite_console_python_sdk/type/messaging_update_push_message_request_users.py)<a id="users-messagingupdatepushmessagerequestusersappwrite_console_python_sdktypemessaging_update_push_message_request_userspy"></a>

##### targets: [`MessagingUpdatePushMessageRequestTargets`](./appwrite_console_python_sdk/type/messaging_update_push_message_request_targets.py)<a id="targets-messagingupdatepushmessagerequesttargetsappwrite_console_python_sdktypemessaging_update_push_message_request_targetspy"></a>

##### body: `str`<a id="body-str"></a>

Body for push notification.

##### data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Additional Data for push notification.

##### action: `str`<a id="action-str"></a>

Action for push notification.

##### image: `str`<a id="image-str"></a>

Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage.

##### icon: `str`<a id="icon-str"></a>

Icon for push notification. Available only for Android and Web platforms.

##### sound: `str`<a id="sound-str"></a>

Sound for push notification. Available only for Android and iOS platforms.

##### color: `str`<a id="color-str"></a>

Color for push notification. Available only for Android platforms.

##### tag: `str`<a id="tag-str"></a>

Tag for push notification. Available only for Android platforms.

##### badge: `int`<a id="badge-int"></a>

Badge for push notification. Available only for iOS platforms.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdatePushMessageRequest`](./appwrite_console_python_sdk/type/messaging_update_push_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/push/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_sendgrid_provider`<a id="appwriteconsolemessagingupdate_sendgrid_provider"></a>

Update a Sendgrid provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sendgrid_provider_response = appwriteconsole.messaging.update_sendgrid_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    api_key="<API_KEY>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### api_key: `str`<a id="api_key-str"></a>

Sendgrid API key.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the Reply To field for the mail. Default value is Sender Name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the Reply To field for the mail. Default value is Sender Email.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateSendgridProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_sendgrid_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/sendgrid/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_sms_message_by_id`<a id="appwriteconsolemessagingupdate_sms_message_by_id"></a>

Update an email message by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sms_message_by_id_response = appwriteconsole.messaging.update_sms_message_by_id(
    message_id="messageId_example",
    topics=[
        "string_example"
    ],
    users=[
        "string_example"
    ],
    targets=[
        "string_example"
    ],
    content="<CONTENT>",
    draft=False,
    scheduled_at="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_id: `str`<a id="message_id-str"></a>

Message ID.

##### topics: [`MessagingUpdateSmsMessageByIdRequestTopics`](./appwrite_console_python_sdk/type/messaging_update_sms_message_by_id_request_topics.py)<a id="topics-messagingupdatesmsmessagebyidrequesttopicsappwrite_console_python_sdktypemessaging_update_sms_message_by_id_request_topicspy"></a>

##### users: [`MessagingUpdateSmsMessageByIdRequestUsers`](./appwrite_console_python_sdk/type/messaging_update_sms_message_by_id_request_users.py)<a id="users-messagingupdatesmsmessagebyidrequestusersappwrite_console_python_sdktypemessaging_update_sms_message_by_id_request_userspy"></a>

##### targets: [`MessagingUpdateSmsMessageByIdRequestTargets`](./appwrite_console_python_sdk/type/messaging_update_sms_message_by_id_request_targets.py)<a id="targets-messagingupdatesmsmessagebyidrequesttargetsappwrite_console_python_sdktypemessaging_update_sms_message_by_id_request_targetspy"></a>

##### content: `str`<a id="content-str"></a>

Email Content.

##### draft: `bool`<a id="draft-bool"></a>

Is message a draft

##### scheduled_at: `str`<a id="scheduled_at-str"></a>

Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateSmsMessageByIdRequest`](./appwrite_console_python_sdk/type/messaging_update_sms_message_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./appwrite_console_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/messages/sms/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_smtp_provider`<a id="appwriteconsolemessagingupdate_smtp_provider"></a>

Update a SMTP provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_smtp_provider_response = appwriteconsole.messaging.update_smtp_provider(
    provider_id="providerId_example",
    name="<NAME>",
    host="<HOST>",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    encryption="none",
    auto_tls=False,
    mailer="<MAILER>",
    from_name="<FROM_NAME>",
    from_email="email@example.com",
    reply_to_name="<REPLY_TO_NAME>",
    reply_to_email="<REPLY_TO_EMAIL>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### host: `str`<a id="host-str"></a>

SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465\\\"`. Hosts will be tried in order.

##### port: `int`<a id="port-int"></a>

SMTP port.

##### username: `str`<a id="username-str"></a>

Authentication username.

##### password: `str`<a id="password-str"></a>

Authentication password.

##### encryption: `str`<a id="encryption-str"></a>

Encryption type. Can be 'ssl' or 'tls'

##### auto_tls: `bool`<a id="auto_tls-bool"></a>

Enable SMTP AutoTLS feature.

##### mailer: `str`<a id="mailer-str"></a>

The value to use for the X-Mailer header.

##### from_name: `str`<a id="from_name-str"></a>

Sender Name.

##### from_email: `str`<a id="from_email-str"></a>

Sender email address.

##### reply_to_name: `str`<a id="reply_to_name-str"></a>

Name set in the Reply To field for the mail. Default value is Sender Name.

##### reply_to_email: `str`<a id="reply_to_email-str"></a>

Email set in the Reply To field for the mail. Default value is Sender Email.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateSmtpProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_smtp_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/smtp/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_telesign_provider`<a id="appwriteconsolemessagingupdate_telesign_provider"></a>

Update a Telesign provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_telesign_provider_response = appwriteconsole.messaging.update_telesign_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    customer_id="<CUSTOMER_ID>",
    api_key="<API_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### customer_id: `str`<a id="customer_id-str"></a>

Telesign customer ID.

##### api_key: `str`<a id="api_key-str"></a>

Telesign API key.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTelesignProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_telesign_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/telesign/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_textmagic_provider`<a id="appwriteconsolemessagingupdate_textmagic_provider"></a>

Update a Textmagic provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_textmagic_provider_response = appwriteconsole.messaging.update_textmagic_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    username="<USERNAME>",
    api_key="<API_KEY>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### username: `str`<a id="username-str"></a>

Textmagic username.

##### api_key: `str`<a id="api_key-str"></a>

Textmagic apiKey.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTextmagicProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_textmagic_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/textmagic/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_topic_by_id`<a id="appwriteconsolemessagingupdate_topic_by_id"></a>

Update a topic by its unique ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_topic_by_id_response = appwriteconsole.messaging.update_topic_by_id(
    topic_id="topicId_example",
    name="<NAME>",
    subscribe=[
        "[\"any\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### topic_id: `str`<a id="topic_id-str"></a>

Topic ID.

##### name: `str`<a id="name-str"></a>

Topic Name.

##### subscribe: [`MessagingUpdateTopicByIdRequestSubscribe`](./appwrite_console_python_sdk/type/messaging_update_topic_by_id_request_subscribe.py)<a id="subscribe-messagingupdatetopicbyidrequestsubscribeappwrite_console_python_sdktypemessaging_update_topic_by_id_request_subscribepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTopicByIdRequest`](./appwrite_console_python_sdk/type/messaging_update_topic_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Topic`](./appwrite_console_python_sdk/pydantic/topic.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/topics/{topicId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_twilio_provider`<a id="appwriteconsolemessagingupdate_twilio_provider"></a>

Update a Twilio provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_twilio_provider_response = appwriteconsole.messaging.update_twilio_provider(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    account_sid="<ACCOUNT_SID>",
    auth_token="<AUTH_TOKEN>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### account_sid: `str`<a id="account_sid-str"></a>

Twilio account secret ID.

##### auth_token: `str`<a id="auth_token-str"></a>

Twilio authentication token.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateTwilioProviderRequest`](./appwrite_console_python_sdk/type/messaging_update_twilio_provider_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/twilio/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.messaging.update_vonage_provider_by_id`<a id="appwriteconsolemessagingupdate_vonage_provider_by_id"></a>

Update a Vonage provider by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_vonage_provider_by_id_response = appwriteconsole.messaging.update_vonage_provider_by_id(
    provider_id="providerId_example",
    name="<NAME>",
    enabled=False,
    api_key="<API_KEY>",
    api_secret="<API_SECRET>",
    _from="<FROM>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID.

##### name: `str`<a id="name-str"></a>

Provider name.

##### enabled: `bool`<a id="enabled-bool"></a>

Set as enabled.

##### api_key: `str`<a id="api_key-str"></a>

Vonage API key.

##### api_secret: `str`<a id="api_secret-str"></a>

Vonage API secret.

##### _from: `str`<a id="_from-str"></a>

Sender number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MessagingUpdateVonageProviderByIdRequest`](./appwrite_console_python_sdk/type/messaging_update_vonage_provider_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Provider`](./appwrite_console_python_sdk/pydantic/provider.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/messaging/providers/vonage/{providerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.create_appwrite_migration`<a id="appwriteconsolemigrationscreate_appwrite_migration"></a>

Migrate Appwrite Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_appwrite_migration_response = appwriteconsole.migrations.create_appwrite_migration(
    resources=[
        "string_example"
    ],
    endpoint="https://example.com",
    project_id="<PROJECT_ID>",
    api_key="<API_KEY>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: [`MigrationsCreateAppwriteMigrationRequestResources`](./appwrite_console_python_sdk/type/migrations_create_appwrite_migration_request_resources.py)<a id="resources-migrationscreateappwritemigrationrequestresourcesappwrite_console_python_sdktypemigrations_create_appwrite_migration_request_resourcespy"></a>

##### endpoint: `str`<a id="endpoint-str"></a>

Source's Appwrite Endpoint

##### project_id: `str`<a id="project_id-str"></a>

Source's Project ID

##### api_key: `str`<a id="api_key-str"></a>

Source's API Key

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsCreateAppwriteMigrationRequest`](./appwrite_console_python_sdk/type/migrations_create_appwrite_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/appwrite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.create_n_host_migration`<a id="appwriteconsolemigrationscreate_n_host_migration"></a>

Migrate NHost Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_n_host_migration_response = appwriteconsole.migrations.create_n_host_migration(
    resources=[
        "string_example"
    ],
    subdomain="<SUBDOMAIN>",
    region="<REGION>",
    admin_secret="<ADMIN_SECRET>",
    database="<DATABASE>",
    username="<USERNAME>",
    password="<PASSWORD>",
    port=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: [`MigrationsCreateNHostMigrationRequestResources`](./appwrite_console_python_sdk/type/migrations_create_n_host_migration_request_resources.py)<a id="resources-migrationscreatenhostmigrationrequestresourcesappwrite_console_python_sdktypemigrations_create_n_host_migration_request_resourcespy"></a>

##### subdomain: `str`<a id="subdomain-str"></a>

Source's Subdomain

##### region: `str`<a id="region-str"></a>

Source's Region

##### admin_secret: `str`<a id="admin_secret-str"></a>

Source's Admin Secret

##### database: `str`<a id="database-str"></a>

Source's Database Name

##### username: `str`<a id="username-str"></a>

Source's Database Username

##### password: `str`<a id="password-str"></a>

Source's Database Password

##### port: `int`<a id="port-int"></a>

Source's Database Port

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsCreateNHostMigrationRequest`](./appwrite_console_python_sdk/type/migrations_create_n_host_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/nhost` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.delete_migration`<a id="appwriteconsolemigrationsdelete_migration"></a>

Delete Migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.migrations.delete_migration(
    migration_id="migrationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### migration_id: `str`<a id="migration_id-str"></a>

Migration ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/{migrationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.firebase_data_migration`<a id="appwriteconsolemigrationsfirebase_data_migration"></a>

Migrate Firebase Data (Service Account)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
firebase_data_migration_response = appwriteconsole.migrations.firebase_data_migration(
    resources=[
        "string_example"
    ],
    service_account="<SERVICE_ACCOUNT>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: [`MigrationsFirebaseDataMigrationRequestResources`](./appwrite_console_python_sdk/type/migrations_firebase_data_migration_request_resources.py)<a id="resources-migrationsfirebasedatamigrationrequestresourcesappwrite_console_python_sdktypemigrations_firebase_data_migration_request_resourcespy"></a>

##### service_account: `str`<a id="service_account-str"></a>

JSON of the Firebase service account credentials

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsFirebaseDataMigrationRequest`](./appwrite_console_python_sdk/type/migrations_firebase_data_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.firebase_o_auth_migrate`<a id="appwriteconsolemigrationsfirebase_o_auth_migrate"></a>

Migrate Firebase Data (OAuth)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
firebase_o_auth_migrate_response = appwriteconsole.migrations.firebase_o_auth_migrate(
    resources=[
        "string_example"
    ],
    project_id="<PROJECT_ID>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: [`MigrationsFirebaseOAuthMigrateRequestResources`](./appwrite_console_python_sdk/type/migrations_firebase_o_auth_migrate_request_resources.py)<a id="resources-migrationsfirebaseoauthmigraterequestresourcesappwrite_console_python_sdktypemigrations_firebase_o_auth_migrate_request_resourcespy"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project ID of the Firebase Project

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsFirebaseOAuthMigrateRequest`](./appwrite_console_python_sdk/type/migrations_firebase_o_auth_migrate_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase/oauth` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.generate_firebase_report`<a id="appwriteconsolemigrationsgenerate_firebase_report"></a>

Generate a report on Firebase Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_firebase_report_response = appwriteconsole.migrations.generate_firebase_report(
    resources=[
        "resources_example"
    ],
    service_account="serviceAccount_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: List[`str`]<a id="resources-liststr"></a>

List of resources to migrate

##### service_account: `str`<a id="service_account-str"></a>

JSON of the Firebase service account credentials

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationReport`](./appwrite_console_python_sdk/pydantic/migration_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.generate_firebase_report_o_auth`<a id="appwriteconsolemigrationsgenerate_firebase_report_o_auth"></a>

Generate a report on Firebase Data using OAuth

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_firebase_report_o_auth_response = appwriteconsole.migrations.generate_firebase_report_o_auth(
    resources=[
        "resources_example"
    ],
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: List[`str`]<a id="resources-liststr"></a>

List of resources to migrate

##### project_id: `str`<a id="project_id-str"></a>

Project ID

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationReport`](./appwrite_console_python_sdk/pydantic/migration_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase/report/oauth` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.generate_nhost_report`<a id="appwriteconsolemigrationsgenerate_nhost_report"></a>

Generate a report on NHost Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_nhost_report_response = appwriteconsole.migrations.generate_nhost_report(
    resources=[
        "resources_example"
    ],
    subdomain="subdomain_example",
    region="region_example",
    admin_secret="adminSecret_example",
    database="database_example",
    username="username_example",
    password="password_example",
    port=5432,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: List[`str`]<a id="resources-liststr"></a>

List of resources to migrate.

##### subdomain: `str`<a id="subdomain-str"></a>

Source's Subdomain.

##### region: `str`<a id="region-str"></a>

Source's Region.

##### admin_secret: `str`<a id="admin_secret-str"></a>

Source's Admin Secret.

##### database: `str`<a id="database-str"></a>

Source's Database Name.

##### username: `str`<a id="username-str"></a>

Source's Database Username.

##### password: `str`<a id="password-str"></a>

Source's Database Password.

##### port: `int`<a id="port-int"></a>

Source's Database Port.

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationReport`](./appwrite_console_python_sdk/pydantic/migration_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/nhost/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.generate_report_on_appwrite_data`<a id="appwriteconsolemigrationsgenerate_report_on_appwrite_data"></a>

Generate a report on Appwrite Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_report_on_appwrite_data_response = appwriteconsole.migrations.generate_report_on_appwrite_data(
    resources=[
        "resources_example"
    ],
    endpoint="endpoint_example",
    project_id="projectID_example",
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: List[`str`]<a id="resources-liststr"></a>

List of resources to migrate

##### endpoint: `str`<a id="endpoint-str"></a>

Source's Appwrite Endpoint

##### project_id: `str`<a id="project_id-str"></a>

Source's Project ID

##### key: `str`<a id="key-str"></a>

Source's API Key

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationReport`](./appwrite_console_python_sdk/pydantic/migration_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/appwrite/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.generate_supabase_report`<a id="appwriteconsolemigrationsgenerate_supabase_report"></a>

Generate a report on Supabase Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_supabase_report_response = appwriteconsole.migrations.generate_supabase_report(
    resources=[
        "resources_example"
    ],
    endpoint="endpoint_example",
    api_key="apiKey_example",
    database_host="databaseHost_example",
    username="username_example",
    password="password_example",
    port=5432,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: List[`str`]<a id="resources-liststr"></a>

List of resources to migrate

##### endpoint: `str`<a id="endpoint-str"></a>

Source's Supabase Endpoint.

##### api_key: `str`<a id="api_key-str"></a>

Source's API Key.

##### database_host: `str`<a id="database_host-str"></a>

Source's Database Host.

##### username: `str`<a id="username-str"></a>

Source's Database Username.

##### password: `str`<a id="password-str"></a>

Source's Database Password.

##### port: `int`<a id="port-int"></a>

Source's Database Port.

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationReport`](./appwrite_console_python_sdk/pydantic/migration_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/supabase/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.get_by_id`<a id="appwriteconsolemigrationsget_by_id"></a>

Get Migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteconsole.migrations.get_by_id(
    migration_id="migrationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### migration_id: `str`<a id="migration_id-str"></a>

Migration unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/{migrationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.list_firebase_projects`<a id="appwriteconsolemigrationslist_firebase_projects"></a>

List Firebase Projects

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_firebase_projects_response = appwriteconsole.migrations.list_firebase_projects()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FirebaseProjectList`](./appwrite_console_python_sdk/pydantic/firebase_project_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.list_migrations`<a id="appwriteconsolemigrationslist_migrations"></a>

List Migrations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_migrations_response = appwriteconsole.migrations.list_migrations(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: status, stage, source, resources, statusCounters, resourceData, errors

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`MigrationList`](./appwrite_console_python_sdk/pydantic/migration_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.migrate_supabase_data`<a id="appwriteconsolemigrationsmigrate_supabase_data"></a>

Migrate Supabase Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
migrate_supabase_data_response = appwriteconsole.migrations.migrate_supabase_data(
    resources=[
        "string_example"
    ],
    endpoint="https://example.com",
    api_key="<API_KEY>",
    database_host="<DATABASE_HOST>",
    username="<USERNAME>",
    password="<PASSWORD>",
    port=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resources: [`MigrationsMigrateSupabaseDataRequestResources`](./appwrite_console_python_sdk/type/migrations_migrate_supabase_data_request_resources.py)<a id="resources-migrationsmigratesupabasedatarequestresourcesappwrite_console_python_sdktypemigrations_migrate_supabase_data_request_resourcespy"></a>

##### endpoint: `str`<a id="endpoint-str"></a>

Source's Supabase Endpoint

##### api_key: `str`<a id="api_key-str"></a>

Source's API Key

##### database_host: `str`<a id="database_host-str"></a>

Source's Database Host

##### username: `str`<a id="username-str"></a>

Source's Database Username

##### password: `str`<a id="password-str"></a>

Source's Database Password

##### port: `int`<a id="port-int"></a>

Source's Database Port

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsMigrateSupabaseDataRequest`](./appwrite_console_python_sdk/type/migrations_migrate_supabase_data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/supabase` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.retry_migration`<a id="appwriteconsolemigrationsretry_migration"></a>

Retry Migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retry_migration_response = appwriteconsole.migrations.retry_migration(
    migration_id="migrationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### migration_id: `str`<a id="migration_id-str"></a>

Migration unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Migration`](./appwrite_console_python_sdk/pydantic/migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/{migrationId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.migrations.revoke_firebase_authorization`<a id="appwriteconsolemigrationsrevoke_firebase_authorization"></a>

Revoke Appwrite's authorization to access Firebase Projects

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.migrations.revoke_firebase_authorization()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/migrations/firebase/deauthorize` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.create_variable`<a id="appwriteconsoleprojectcreate_variable"></a>

Create a new project variable. This variable will be accessible in all Appwrite Functions at runtime.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_variable_response = appwriteconsole.project.create_variable(
    key="<KEY>",
    value="<VALUE>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectCreateVariableRequest`](./appwrite_console_python_sdk/type/project_create_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/variables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.delete_variable_by_id`<a id="appwriteconsoleprojectdelete_variable_by_id"></a>

Delete a project variable by its unique ID. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.project.delete_variable_by_id(
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/variables/{variableId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.get_usage_stats`<a id="appwriteconsoleprojectget_usage_stats"></a>

Get project usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_response = appwriteconsole.project.get_usage_stats(
    start_date="startDate_example",
    end_date="endDate_example",
    period="1d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `str`<a id="start_date-str"></a>

Starting date for the usage

##### end_date: `str`<a id="end_date-str"></a>

End date for the usage

##### period: `str`<a id="period-str"></a>

Period used

#### 🔄 Return<a id="🔄-return"></a>

[`UsageProject`](./appwrite_console_python_sdk/pydantic/usage_project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.list_variables`<a id="appwriteconsoleprojectlist_variables"></a>

Get a list of all project variables. These variables will be accessible in all Appwrite Functions at runtime.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_variables_response = appwriteconsole.project.list_variables()
```

#### 🔄 Return<a id="🔄-return"></a>

[`VariableList`](./appwrite_console_python_sdk/pydantic/variable_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/variables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.update_variable_by_id`<a id="appwriteconsoleprojectupdate_variable_by_id"></a>

Update project variable by its unique ID. This variable will be accessible in all Appwrite Functions at runtime.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_variable_by_id_response = appwriteconsole.project.update_variable_by_id(
    key="<KEY>",
    variable_id="variableId_example",
    value="<VALUE>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

Variable key. Max length: 255 chars.

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

##### value: `str`<a id="value-str"></a>

Variable value. Max length: 8192 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectUpdateVariableByIdRequest`](./appwrite_console_python_sdk/type/project_update_variable_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/variables/{variableId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.project.variable_details`<a id="appwriteconsoleprojectvariable_details"></a>

Get a project variable by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
variable_details_response = appwriteconsole.project.variable_details(
    variable_id="variableId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### variable_id: `str`<a id="variable_id-str"></a>

Variable unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Variable`](./appwrite_console_python_sdk/pydantic/variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/variables/{variableId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.create_key`<a id="appwriteconsoleprojectscreate_key"></a>

Create key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_key_response = appwriteconsole.projects.create_key(
    name="<NAME>",
    scopes=[
        "string_example"
    ],
    project_id="projectId_example",
    expire="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Key name. Max length: 128 chars.

##### scopes: [`ProjectsCreateKeyRequestScopes`](./appwrite_console_python_sdk/type/projects_create_key_request_scopes.py)<a id="scopes-projectscreatekeyrequestscopesappwrite_console_python_sdktypeprojects_create_key_request_scopespy"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### expire: `str`<a id="expire-str"></a>

Expiration time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Use null for unlimited expiration.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateKeyRequest`](./appwrite_console_python_sdk/type/projects_create_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Key`](./appwrite_console_python_sdk/pydantic/key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.create_new_project`<a id="appwriteconsoleprojectscreate_new_project"></a>

Create project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_project_response = appwriteconsole.projects.create_new_project(
    project_id="string_example",
    name="<NAME>",
    team_id="<TEAM_ID>",
    description="<DESCRIPTION>",
    region="default",
    logo="<LOGO>",
    url="https://example.com",
    legal_name="<LEGAL_NAME>",
    legal_country="<LEGAL_COUNTRY>",
    legal_state="<LEGAL_STATE>",
    legal_city="<LEGAL_CITY>",
    legal_address="<LEGAL_ADDRESS>",
    legal_tax_id="<LEGAL_TAX_ID>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, and hyphen. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Project name. Max length: 128 chars.

##### team_id: `str`<a id="team_id-str"></a>

Team unique ID.

##### description: `str`<a id="description-str"></a>

Project description. Max length: 256 chars.

##### region: `str`<a id="region-str"></a>

Project Region.

##### logo: `str`<a id="logo-str"></a>

Project logo.

##### url: `str`<a id="url-str"></a>

Project URL.

##### legal_name: `str`<a id="legal_name-str"></a>

Project legal Name. Max length: 256 chars.

##### legal_country: `str`<a id="legal_country-str"></a>

Project legal Country. Max length: 256 chars.

##### legal_state: `str`<a id="legal_state-str"></a>

Project legal State. Max length: 256 chars.

##### legal_city: `str`<a id="legal_city-str"></a>

Project legal City. Max length: 256 chars.

##### legal_address: `str`<a id="legal_address-str"></a>

Project legal Address. Max length: 256 chars.

##### legal_tax_id: `str`<a id="legal_tax_id-str"></a>

Project legal Tax ID. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateNewProjectRequest`](./appwrite_console_python_sdk/type/projects_create_new_project_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.create_platform`<a id="appwriteconsoleprojectscreate_platform"></a>

Create platform

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_platform_response = appwriteconsole.projects.create_platform(
    type="web",
    name="<NAME>",
    project_id="projectId_example",
    key="<KEY>",
    store="<STORE>",
    hostname="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Platform type.

##### name: `str`<a id="name-str"></a>

Platform name. Max length: 128 chars.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### key: `str`<a id="key-str"></a>

Package name for Android or bundle ID for iOS or macOS. Max length: 256 chars.

##### store: `str`<a id="store-str"></a>

App store or Google Play store ID. Max length: 256 chars.

##### hostname: `str`<a id="hostname-str"></a>

Platform client hostname. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreatePlatformRequest`](./appwrite_console_python_sdk/type/projects_create_platform_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Platform`](./appwrite_console_python_sdk/pydantic/platform.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/platforms` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.create_smtp_test`<a id="appwriteconsoleprojectscreate_smtp_test"></a>

Create SMTP test

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.projects.create_smtp_test(
    emails=[
        "string_example"
    ],
    sender_name="<SENDER_NAME>",
    sender_email="email@example.com",
    host="string_example",
    project_id="projectId_example",
    reply_to="email@example.com",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    secure="tls",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### emails: [`ProjectsCreateSmtpTestRequestEmails`](./appwrite_console_python_sdk/type/projects_create_smtp_test_request_emails.py)<a id="emails-projectscreatesmtptestrequestemailsappwrite_console_python_sdktypeprojects_create_smtp_test_request_emailspy"></a>

##### sender_name: `str`<a id="sender_name-str"></a>

Name of the email sender

##### sender_email: `str`<a id="sender_email-str"></a>

Email of the sender

##### host: `str`<a id="host-str"></a>

SMTP server host name

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### reply_to: `str`<a id="reply_to-str"></a>

Reply to email

##### port: `int`<a id="port-int"></a>

SMTP server port

##### username: `str`<a id="username-str"></a>

SMTP server username

##### password: `str`<a id="password-str"></a>

SMTP server password

##### secure: `str`<a id="secure-str"></a>

Does SMTP server use secure connection

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateSmtpTestRequest`](./appwrite_console_python_sdk/type/projects_create_smtp_test_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/smtp/tests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.create_webhook`<a id="appwriteconsoleprojectscreate_webhook"></a>

Create webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webhook_response = appwriteconsole.projects.create_webhook(
    security=False,
    name="<NAME>",
    events=[
        "string_example"
    ],
    url="string_example",
    project_id="projectId_example",
    enabled=False,
    http_user="<HTTP_USER>",
    http_pass="<HTTP_PASS>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### security: `bool`<a id="security-bool"></a>

Certificate verification, false for disabled or true for enabled.

##### name: `str`<a id="name-str"></a>

Webhook name. Max length: 128 chars.

##### events: [`ProjectsCreateWebhookRequestEvents`](./appwrite_console_python_sdk/type/projects_create_webhook_request_events.py)<a id="events-projectscreatewebhookrequesteventsappwrite_console_python_sdktypeprojects_create_webhook_request_eventspy"></a>

##### url: `str`<a id="url-str"></a>

Webhook URL.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### enabled: `bool`<a id="enabled-bool"></a>

Enable or disable a webhook.

##### http_user: `str`<a id="http_user-str"></a>

Webhook HTTP user. Max length: 256 chars.

##### http_pass: `str`<a id="http_pass-str"></a>

Webhook HTTP password. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateWebhookRequest`](./appwrite_console_python_sdk/type/projects_create_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./appwrite_console_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.delete_key`<a id="appwriteconsoleprojectsdelete_key"></a>

Delete key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.projects.delete_key(
    project_id="projectId_example",
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### key_id: `str`<a id="key_id-str"></a>

Key unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/keys/{keyId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.delete_platform`<a id="appwriteconsoleprojectsdelete_platform"></a>

Delete platform

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.projects.delete_platform(
    project_id="projectId_example",
    platform_id="platformId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### platform_id: `str`<a id="platform_id-str"></a>

Platform unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/platforms/{platformId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.delete_webhook`<a id="appwriteconsoleprojectsdelete_webhook"></a>

Delete webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.projects.delete_webhook(
    project_id="projectId_example",
    webhook_id="webhookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### webhook_id: `str`<a id="webhook_id-str"></a>

Webhook unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks/{webhookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.enable_personal_data_check`<a id="appwriteconsoleprojectsenable_personal_data_check"></a>

Enable or disable checking user passwords for similarity with their personal data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_personal_data_check_response = appwriteconsole.projects.enable_personal_data_check(
    enabled=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enabled: `bool`<a id="enabled-bool"></a>

Set whether or not to check a password for similarity with personal data. Default is false.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsEnablePersonalDataCheckRequest`](./appwrite_console_python_sdk/type/projects_enable_personal_data_check_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/personal-data` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get`<a id="appwriteconsoleprojectsget"></a>

Get project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = appwriteconsole.projects.get(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get_email_template`<a id="appwriteconsoleprojectsget_email_template"></a>

Get custom email template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_template_response = appwriteconsole.projects.get_email_template(
    project_id="projectId_example",
    type="verification",
    locale="af",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplate`](./appwrite_console_python_sdk/pydantic/email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/email/{type}/{locale}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get_key`<a id="appwriteconsoleprojectsget_key"></a>

Get key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_key_response = appwriteconsole.projects.get_key(
    project_id="projectId_example",
    key_id="keyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### key_id: `str`<a id="key_id-str"></a>

Key unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Key`](./appwrite_console_python_sdk/pydantic/key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/keys/{keyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get_platform_by_id`<a id="appwriteconsoleprojectsget_platform_by_id"></a>

Get platform

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_platform_by_id_response = appwriteconsole.projects.get_platform_by_id(
    project_id="projectId_example",
    platform_id="platformId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### platform_id: `str`<a id="platform_id-str"></a>

Platform unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Platform`](./appwrite_console_python_sdk/pydantic/platform.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/platforms/{platformId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get_sms_template`<a id="appwriteconsoleprojectsget_sms_template"></a>

Get custom SMS template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sms_template_response = appwriteconsole.projects.get_sms_template(
    project_id="projectId_example",
    type="verification",
    locale="af",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./appwrite_console_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/sms/{type}/{locale}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.get_webhook`<a id="appwriteconsoleprojectsget_webhook"></a>

Get webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhook_response = appwriteconsole.projects.get_webhook(
    project_id="projectId_example",
    webhook_id="webhookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### webhook_id: `str`<a id="webhook_id-str"></a>

Webhook unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./appwrite_console_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks/{webhookId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.list_keys`<a id="appwriteconsoleprojectslist_keys"></a>

List keys

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_keys_response = appwriteconsole.projects.list_keys(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`KeyList`](./appwrite_console_python_sdk/pydantic/key_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.list_platforms`<a id="appwriteconsoleprojectslist_platforms"></a>

List platforms

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_platforms_response = appwriteconsole.projects.list_platforms(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`PlatformList`](./appwrite_console_python_sdk/pydantic/platform_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/platforms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.list_projects`<a id="appwriteconsoleprojectslist_projects"></a>

List projects

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_projects_response = appwriteconsole.projects.list_projects(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, teamId

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectList`](./appwrite_console_python_sdk/pydantic/project_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.list_webhooks`<a id="appwriteconsoleprojectslist_webhooks"></a>

List webhooks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_webhooks_response = appwriteconsole.projects.list_webhooks(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookList`](./appwrite_console_python_sdk/pydantic/webhook_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.remove_by_id`<a id="appwriteconsoleprojectsremove_by_id"></a>

Delete project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.projects.remove_by_id(
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.reset_email_template`<a id="appwriteconsoleprojectsreset_email_template"></a>

Reset custom email template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_email_template_response = appwriteconsole.projects.reset_email_template(
    project_id="projectId_example",
    type="verification",
    locale="af",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

#### 🔄 Return<a id="🔄-return"></a>

[`EmailTemplate`](./appwrite_console_python_sdk/pydantic/email_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/email/{type}/{locale}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.reset_sms_template`<a id="appwriteconsoleprojectsreset_sms_template"></a>

Reset custom SMS template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_sms_template_response = appwriteconsole.projects.reset_sms_template(
    project_id="projectId_example",
    type="verification",
    locale="af",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./appwrite_console_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/sms/{type}/{locale}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_all_api_status`<a id="appwriteconsoleprojectsupdate_all_api_status"></a>

Update all API status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_all_api_status_response = appwriteconsole.projects.update_all_api_status(
    status=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `bool`<a id="status-bool"></a>

API status.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAllApiStatusRequest`](./appwrite_console_python_sdk/type/projects_update_all_api_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/api/all` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_all_service_status`<a id="appwriteconsoleprojectsupdate_all_service_status"></a>

Update all service status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_all_service_status_response = appwriteconsole.projects.update_all_service_status(
    status=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `bool`<a id="status-bool"></a>

Service status.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAllServiceStatusRequest`](./appwrite_console_python_sdk/type/projects_update_all_service_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/service/all` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_api_status`<a id="appwriteconsoleprojectsupdate_api_status"></a>

Update API status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_api_status_response = appwriteconsole.projects.update_api_status(
    api="rest",
    status=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api: `str`<a id="api-str"></a>

API name.

##### status: `bool`<a id="status-bool"></a>

API status.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateApiStatusRequest`](./appwrite_console_python_sdk/type/projects_update_api_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/api` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_auth_duration`<a id="appwriteconsoleprojectsupdate_auth_duration"></a>

Update project authentication duration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_auth_duration_response = appwriteconsole.projects.update_auth_duration(
    duration=0,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### duration: `int`<a id="duration-int"></a>

Project session length in seconds. Max length: 31536000 seconds.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAuthDurationRequest`](./appwrite_console_python_sdk/type/projects_update_auth_duration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/duration` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_auth_method_status`<a id="appwriteconsoleprojectsupdate_auth_method_status"></a>

Update project auth method status. Use this endpoint to enable or disable a given auth method for this project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_auth_method_status_response = appwriteconsole.projects.update_auth_method_status(
    status=False,
    project_id="projectId_example",
    method="email-password",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `bool`<a id="status-bool"></a>

Set the status of this auth method.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### method: `str`<a id="method-str"></a>

Auth Method. Possible values: email-password,magic-url,email-otp,anonymous,invites,jwt,phone

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAuthMethodStatusRequest`](./appwrite_console_python_sdk/type/projects_update_auth_method_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/{method}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_auth_password_dictionary`<a id="appwriteconsoleprojectsupdate_auth_password_dictionary"></a>

Update authentication password dictionary status. Use this endpoint to enable or disable the dicitonary check for user password

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_auth_password_dictionary_response = appwriteconsole.projects.update_auth_password_dictionary(
    enabled=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enabled: `bool`<a id="enabled-bool"></a>

Set whether or not to enable checking user's password against most commonly used passwords. Default is false.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAuthPasswordDictionaryRequest`](./appwrite_console_python_sdk/type/projects_update_auth_password_dictionary_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/password-dictionary` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_auth_password_history`<a id="appwriteconsoleprojectsupdate_auth_password_history"></a>

Update authentication password history. Use this endpoint to set the number of password history to save and 0 to disable password history.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_auth_password_history_response = appwriteconsole.projects.update_auth_password_history(
    limit=0,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Set the max number of passwords to store in user history. User can't choose a new password that is already stored in the password history list.  Max number of passwords allowed in history is20. Default value is 0

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateAuthPasswordHistoryRequest`](./appwrite_console_python_sdk/type/projects_update_auth_password_history_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/password-history` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_custom_email_templates`<a id="appwriteconsoleprojectsupdate_custom_email_templates"></a>

Update custom email templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_email_templates_response = appwriteconsole.projects.update_custom_email_templates(
    subject="<SUBJECT>",
    message="<MESSAGE>",
    project_id="projectId_example",
    type="verification",
    locale="af",
    sender_name="<SENDER_NAME>",
    sender_email="email@example.com",
    reply_to="email@example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subject: `str`<a id="subject-str"></a>

Email Subject

##### message: `str`<a id="message-str"></a>

Template message

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

##### sender_name: `str`<a id="sender_name-str"></a>

Name of the email sender

##### sender_email: `str`<a id="sender_email-str"></a>

Email of the sender

##### reply_to: `str`<a id="reply_to-str"></a>

Reply to email

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateCustomEmailTemplatesRequest`](./appwrite_console_python_sdk/type/projects_update_custom_email_templates_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/email/{type}/{locale}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_detail`<a id="appwriteconsoleprojectsupdate_detail"></a>

Update project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = appwriteconsole.projects.update_detail(
    name="<NAME>",
    project_id="projectId_example",
    description="<DESCRIPTION>",
    logo="<LOGO>",
    url="https://example.com",
    legal_name="<LEGAL_NAME>",
    legal_country="<LEGAL_COUNTRY>",
    legal_state="<LEGAL_STATE>",
    legal_city="<LEGAL_CITY>",
    legal_address="<LEGAL_ADDRESS>",
    legal_tax_id="<LEGAL_TAX_ID>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Project name. Max length: 128 chars.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### description: `str`<a id="description-str"></a>

Project description. Max length: 256 chars.

##### logo: `str`<a id="logo-str"></a>

Project logo.

##### url: `str`<a id="url-str"></a>

Project URL.

##### legal_name: `str`<a id="legal_name-str"></a>

Project legal name. Max length: 256 chars.

##### legal_country: `str`<a id="legal_country-str"></a>

Project legal country. Max length: 256 chars.

##### legal_state: `str`<a id="legal_state-str"></a>

Project legal state. Max length: 256 chars.

##### legal_city: `str`<a id="legal_city-str"></a>

Project legal city. Max length: 256 chars.

##### legal_address: `str`<a id="legal_address-str"></a>

Project legal address. Max length: 256 chars.

##### legal_tax_id: `str`<a id="legal_tax_id-str"></a>

Project legal tax ID. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateDetailRequest`](./appwrite_console_python_sdk/type/projects_update_detail_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_key`<a id="appwriteconsoleprojectsupdate_key"></a>

Update key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_key_response = appwriteconsole.projects.update_key(
    name="<NAME>",
    scopes=[
        "string_example"
    ],
    project_id="projectId_example",
    key_id="keyId_example",
    expire="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Key name. Max length: 128 chars.

##### scopes: [`ProjectsUpdateKeyRequestScopes`](./appwrite_console_python_sdk/type/projects_update_key_request_scopes.py)<a id="scopes-projectsupdatekeyrequestscopesappwrite_console_python_sdktypeprojects_update_key_request_scopespy"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### key_id: `str`<a id="key_id-str"></a>

Key unique ID.

##### expire: `str`<a id="expire-str"></a>

Expiration time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Use null for unlimited expiration.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateKeyRequest`](./appwrite_console_python_sdk/type/projects_update_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Key`](./appwrite_console_python_sdk/pydantic/key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/keys/{keyId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_max_sessions_limit`<a id="appwriteconsoleprojectsupdate_max_sessions_limit"></a>

Update project user sessions limit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_max_sessions_limit_response = appwriteconsole.projects.update_max_sessions_limit(
    limit=1,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Set the max number of users allowed in this project. Value allowed is between 1-100. Default is 10

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateMaxSessionsLimitRequest`](./appwrite_console_python_sdk/type/projects_update_max_sessions_limit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/max-sessions` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_o_auth`<a id="appwriteconsoleprojectsupdate_o_auth"></a>

Update project OAuth2

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_o_auth_response = appwriteconsole.projects.update_o_auth(
    provider="amazon",
    project_id="projectId_example",
    app_id="<APP_ID>",
    secret="<SECRET>",
    enabled=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider: `str`<a id="provider-str"></a>

Provider Name

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### app_id: `str`<a id="app_id-str"></a>

Provider app ID. Max length: 256 chars.

##### secret: `str`<a id="secret-str"></a>

Provider secret key. Max length: 512 chars.

##### enabled: `bool`<a id="enabled-bool"></a>

Provider status. Set to 'false' to disable new session creation.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateOAuthRequest`](./appwrite_console_python_sdk/type/projects_update_o_auth_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/oauth2` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_platform_by_id`<a id="appwriteconsoleprojectsupdate_platform_by_id"></a>

Update platform

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_platform_by_id_response = appwriteconsole.projects.update_platform_by_id(
    name="<NAME>",
    project_id="projectId_example",
    platform_id="platformId_example",
    key="<KEY>",
    store="<STORE>",
    hostname="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Platform name. Max length: 128 chars.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### platform_id: `str`<a id="platform_id-str"></a>

Platform unique ID.

##### key: `str`<a id="key-str"></a>

Package name for android or bundle ID for iOS. Max length: 256 chars.

##### store: `str`<a id="store-str"></a>

App store or Google Play store ID. Max length: 256 chars.

##### hostname: `str`<a id="hostname-str"></a>

Platform client URL. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdatePlatformByIdRequest`](./appwrite_console_python_sdk/type/projects_update_platform_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Platform`](./appwrite_console_python_sdk/pydantic/platform.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/platforms/{platformId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_service_status`<a id="appwriteconsoleprojectsupdate_service_status"></a>

Update service status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_service_status_response = appwriteconsole.projects.update_service_status(
    service="account",
    status=False,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### service: `str`<a id="service-str"></a>

Service name.

##### status: `bool`<a id="status-bool"></a>

Service status.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateServiceStatusRequest`](./appwrite_console_python_sdk/type/projects_update_service_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/service` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_sms_template`<a id="appwriteconsoleprojectsupdate_sms_template"></a>

Update custom SMS template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_sms_template_response = appwriteconsole.projects.update_sms_template(
    message="<MESSAGE>",
    project_id="projectId_example",
    type="verification",
    locale="af",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message: `str`<a id="message-str"></a>

Template message

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### type: `str`<a id="type-str"></a>

Template type

##### locale: `str`<a id="locale-str"></a>

Template locale

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateSmsTemplateRequest`](./appwrite_console_python_sdk/type/projects_update_sms_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SmsTemplate`](./appwrite_console_python_sdk/pydantic/sms_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/templates/sms/{type}/{locale}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_smtp`<a id="appwriteconsoleprojectsupdate_smtp"></a>

Update SMTP

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_smtp_response = appwriteconsole.projects.update_smtp(
    enabled=False,
    project_id="projectId_example",
    sender_name="<SENDER_NAME>",
    sender_email="email@example.com",
    reply_to="email@example.com",
    host="string_example",
    port=1,
    username="<USERNAME>",
    password="<PASSWORD>",
    secure="tls",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enabled: `bool`<a id="enabled-bool"></a>

Enable custom SMTP service

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### sender_name: `str`<a id="sender_name-str"></a>

Name of the email sender

##### sender_email: `str`<a id="sender_email-str"></a>

Email of the sender

##### reply_to: `str`<a id="reply_to-str"></a>

Reply to email

##### host: `str`<a id="host-str"></a>

SMTP server host name

##### port: `int`<a id="port-int"></a>

SMTP server port

##### username: `str`<a id="username-str"></a>

SMTP server username

##### password: `str`<a id="password-str"></a>

SMTP server password

##### secure: `str`<a id="secure-str"></a>

Does SMTP server use secure connection

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateSmtpRequest`](./appwrite_console_python_sdk/type/projects_update_smtp_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/smtp` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_team`<a id="appwriteconsoleprojectsupdate_team"></a>

Update Project Team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_response = appwriteconsole.projects.update_team(
    team_id="<TEAM_ID>",
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID of the team to transfer project to.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateTeamRequest`](./appwrite_console_python_sdk/type/projects_update_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/team` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_user_limit`<a id="appwriteconsoleprojectsupdate_user_limit"></a>

Update project users limit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_limit_response = appwriteconsole.projects.update_user_limit(
    limit=0,
    project_id="projectId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Set the max number of users allowed in this project. Use 0 for unlimited.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateUserLimitRequest`](./appwrite_console_python_sdk/type/projects_update_user_limit_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Project`](./appwrite_console_python_sdk/pydantic/project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/auth/limit` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_webhook`<a id="appwriteconsoleprojectsupdate_webhook"></a>

Update webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_response = appwriteconsole.projects.update_webhook(
    security=False,
    name="<NAME>",
    events=[
        "string_example"
    ],
    url="string_example",
    project_id="projectId_example",
    webhook_id="webhookId_example",
    enabled=False,
    http_user="<HTTP_USER>",
    http_pass="<HTTP_PASS>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### security: `bool`<a id="security-bool"></a>

Certificate verification, false for disabled or true for enabled.

##### name: `str`<a id="name-str"></a>

Webhook name. Max length: 128 chars.

##### events: [`ProjectsUpdateWebhookRequestEvents`](./appwrite_console_python_sdk/type/projects_update_webhook_request_events.py)<a id="events-projectsupdatewebhookrequesteventsappwrite_console_python_sdktypeprojects_update_webhook_request_eventspy"></a>

##### url: `str`<a id="url-str"></a>

Webhook URL.

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### webhook_id: `str`<a id="webhook_id-str"></a>

Webhook unique ID.

##### enabled: `bool`<a id="enabled-bool"></a>

Enable or disable a webhook.

##### http_user: `str`<a id="http_user-str"></a>

Webhook HTTP user. Max length: 256 chars.

##### http_pass: `str`<a id="http_pass-str"></a>

Webhook HTTP password. Max length: 256 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateWebhookRequest`](./appwrite_console_python_sdk/type/projects_update_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./appwrite_console_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks/{webhookId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.projects.update_webhook_signature`<a id="appwriteconsoleprojectsupdate_webhook_signature"></a>

Update webhook signature key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_signature_response = appwriteconsole.projects.update_webhook_signature(
    project_id="projectId_example",
    webhook_id="webhookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

Project unique ID.

##### webhook_id: `str`<a id="webhook_id-str"></a>

Webhook unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./appwrite_console_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{projectId}/webhooks/{webhookId}/signature` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.proxy.create_new_rule`<a id="appwriteconsoleproxycreate_new_rule"></a>

Create a new proxy rule.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_rule_response = appwriteconsole.proxy.create_new_rule(
    domain="string_example",
    resource_type="api",
    resource_id="<RESOURCE_ID>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain name.

##### resource_type: `str`<a id="resource_type-str"></a>

Action definition for the rule. Possible values are \\\"api\\\", \\\"function\\\"

##### resource_id: `str`<a id="resource_id-str"></a>

ID of resource for the action type. If resourceType is \\\"api\\\", leave empty. If resourceType is \\\"function\\\", provide ID of the function.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProxyCreateNewRuleRequest`](./appwrite_console_python_sdk/type/proxy_create_new_rule_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProxyRule`](./appwrite_console_python_sdk/pydantic/proxy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/proxy/rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.proxy.delete_rule_by_id`<a id="appwriteconsoleproxydelete_rule_by_id"></a>

Delete a proxy rule by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.proxy.delete_rule_by_id(
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

Rule ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/proxy/rules/{ruleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.proxy.get_rule_by_id`<a id="appwriteconsoleproxyget_rule_by_id"></a>

Get a proxy rule by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rule_by_id_response = appwriteconsole.proxy.get_rule_by_id(
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

Rule ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ProxyRule`](./appwrite_console_python_sdk/pydantic/proxy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/proxy/rules/{ruleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.proxy.list_rules`<a id="appwriteconsoleproxylist_rules"></a>

Get a list of all the proxy rules. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_rules_response = appwriteconsole.proxy.list_rules(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: domain, resourceType, resourceId, url

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ProxyRuleList`](./appwrite_console_python_sdk/pydantic/proxy_rule_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/proxy/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.proxy.update_rule_verification_status`<a id="appwriteconsoleproxyupdate_rule_verification_status"></a>

Update Rule Verification Status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_rule_verification_status_response = appwriteconsole.proxy.update_rule_verification_status(
    rule_id="ruleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_id: `str`<a id="rule_id-str"></a>

Rule ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ProxyRule`](./appwrite_console_python_sdk/pydantic/proxy_rule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/proxy/rules/{ruleId}/verification` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.create_bucket`<a id="appwriteconsolestoragecreate_bucket"></a>

Create a new storage bucket.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bucket_response = appwriteconsole.storage.create_bucket(
    bucket_id="<BUCKET_ID>",
    name="<NAME>",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
    file_security=False,
    enabled=False,
    maximum_file_size=1,
    allowed_file_extensions=[
        "string_example"
    ],
    compression="none",
    encryption=False,
    antivirus=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Bucket name

##### permissions: [`StorageCreateBucketRequestPermissions`](./appwrite_console_python_sdk/type/storage_create_bucket_request_permissions.py)<a id="permissions-storagecreatebucketrequestpermissionsappwrite_console_python_sdktypestorage_create_bucket_request_permissionspy"></a>

##### file_security: `bool`<a id="file_security-bool"></a>

Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.

##### maximum_file_size: `int`<a id="maximum_file_size-int"></a>

Maximum file size allowed in bytes. Maximum allowed value is 30MB.

##### allowed_file_extensions: [`StorageCreateBucketRequestAllowedFileExtensions`](./appwrite_console_python_sdk/type/storage_create_bucket_request_allowed_file_extensions.py)<a id="allowed_file_extensions-storagecreatebucketrequestallowedfileextensionsappwrite_console_python_sdktypestorage_create_bucket_request_allowed_file_extensionspy"></a>

##### compression: `str`<a id="compression-str"></a>

Compression algorithm choosen for compression. Can be one of none,  [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled

##### encryption: `bool`<a id="encryption-bool"></a>

Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled

##### antivirus: `bool`<a id="antivirus-bool"></a>

Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageCreateBucketRequest`](./appwrite_console_python_sdk/type/storage_create_bucket_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_console_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.create_file`<a id="appwriteconsolestoragecreate_file"></a>

Create a new file. Before using this route, you should create a new bucket resource using either a [server integration](https://appwrite.io/docs/server/storage#storageCreateBucket) API or directly from your Appwrite console.

Larger files should be uploaded using multiple requests with the [content-range](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range) header to send a partial request with a maximum supported chunk of `5MB`. The `content-range` header values should always be in bytes.

When the first request is sent, the server will return the **File** object, and the subsequent part request must include the file's **id** in `x-appwrite-id` header to allow the server to know that the partial upload is for the existing file and not for a new one.

If you're creating a new file using one of the Appwrite SDKs, all the chunking logic will be managed by the SDK internally.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_file_response = appwriteconsole.storage.create_file(
    bucket_id="bucketId_example",
    file_id="<FILE_ID>",
    file="string_example",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### file: `str`<a id="file-str"></a>

Binary file. Appwrite SDKs provide helpers to handle file input. [Learn about file input](https://appwrite.io/docs/storage#file-input).

##### permissions: [`StorageCreateFileRequestPermissions`](./appwrite_console_python_sdk/type/storage_create_file_request_permissions.py)<a id="permissions-storagecreatefilerequestpermissionsappwrite_console_python_sdktypestorage_create_file_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageCreateFileRequest`](./appwrite_console_python_sdk/type/storage_create_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_console_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.delete_bucket_by_id`<a id="appwriteconsolestoragedelete_bucket_by_id"></a>

Delete a storage bucket by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.storage.delete_bucket_by_id(
    bucket_id="bucketId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.delete_file_by_id`<a id="appwriteconsolestoragedelete_file_by_id"></a>

Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.storage.delete_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_bucket`<a id="appwriteconsolestorageget_bucket"></a>

Get a storage bucket by its unique ID. This endpoint response returns a JSON object with the storage bucket metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bucket_response = appwriteconsole.storage.get_bucket(
    bucket_id="bucketId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_console_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_bucket_usage_stats`<a id="appwriteconsolestorageget_bucket_usage_stats"></a>

Get bucket usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bucket_usage_stats_response = appwriteconsole.storage.get_bucket_usage_stats(
    bucket_id="bucketId_example",
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket ID.

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageBuckets`](./appwrite_console_python_sdk/pydantic/usage_buckets.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/{bucketId}/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_download_file`<a id="appwriteconsolestorageget_download_file"></a>

Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.storage.get_download_file(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_file_by_id`<a id="appwriteconsolestorageget_file_by_id"></a>

Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_by_id_response = appwriteconsole.storage.get_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_console_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_file_preview_image`<a id="appwriteconsolestorageget_file_preview_image"></a>

Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image. Preview is supported only for image files smaller than 10MB.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.storage.get_file_preview_image(
    bucket_id="bucketId_example",
    file_id="fileId_example",
    width=0,
    height=0,
    gravity="center",
    quality=100,
    border_width=0,
    border_color="",
    border_radius=0,
    opacity=1,
    rotation=0,
    background="",
    output="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID

##### width: `int`<a id="width-int"></a>

Resize preview image width, Pass an integer between 0 to 4000.

##### height: `int`<a id="height-int"></a>

Resize preview image height, Pass an integer between 0 to 4000.

##### gravity: `str`<a id="gravity-str"></a>

Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

##### quality: `int`<a id="quality-int"></a>

Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

##### border_width: `int`<a id="border_width-int"></a>

Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

##### border_color: `str`<a id="border_color-str"></a>

Preview image border color. Use a valid HEX color, no # is needed for prefix.

##### border_radius: `int`<a id="border_radius-int"></a>

Preview image border radius in pixels. Pass an integer between 0 to 4000.

##### opacity: `Union[int, float]`<a id="opacity-unionint-float"></a>

Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

##### rotation: `int`<a id="rotation-int"></a>

Preview image rotation in degrees. Pass an integer between -360 and 360.

##### background: `str`<a id="background-str"></a>

Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

##### output: `str`<a id="output-str"></a>

Output format type (jpeg, jpg, png, gif and webp).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/preview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_file_view`<a id="appwriteconsolestorageget_file_view"></a>

Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.storage.get_file_view(
    bucket_id="bucketId_example",
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}/view` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.get_usage_stats`<a id="appwriteconsolestorageget_usage_stats"></a>

Get storage usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_response = appwriteconsole.storage.get_usage_stats(
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageStorage`](./appwrite_console_python_sdk/pydantic/usage_storage.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.list_buckets`<a id="appwriteconsolestoragelist_buckets"></a>

Get a list of all the storage buckets. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_buckets_response = appwriteconsole.storage.list_buckets(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: enabled, name, fileSecurity, maximumFileSize, encryption, antivirus

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`BucketList`](./appwrite_console_python_sdk/pydantic/bucket_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.list_files`<a id="appwriteconsolestoragelist_files"></a>

Get a list of all the user files. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_files_response = appwriteconsole.storage.list_files(
    bucket_id="bucketId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, signature, mimeType, sizeOriginal, chunksTotal, chunksUploaded

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`FileList`](./appwrite_console_python_sdk/pydantic/file_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.update_bucket_by_id`<a id="appwriteconsolestorageupdate_bucket_by_id"></a>

Update a storage bucket by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_bucket_by_id_response = appwriteconsole.storage.update_bucket_by_id(
    name="<NAME>",
    bucket_id="bucketId_example",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
    file_security=False,
    enabled=False,
    maximum_file_size=1,
    allowed_file_extensions=[
        "string_example"
    ],
    compression="none",
    encryption=False,
    antivirus=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Bucket name

##### bucket_id: `str`<a id="bucket_id-str"></a>

Bucket unique ID.

##### permissions: [`StorageUpdateBucketByIdRequestPermissions`](./appwrite_console_python_sdk/type/storage_update_bucket_by_id_request_permissions.py)<a id="permissions-storageupdatebucketbyidrequestpermissionsappwrite_console_python_sdktypestorage_update_bucket_by_id_request_permissionspy"></a>

##### file_security: `bool`<a id="file_security-bool"></a>

Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).

##### enabled: `bool`<a id="enabled-bool"></a>

Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.

##### maximum_file_size: `int`<a id="maximum_file_size-int"></a>

Maximum file size allowed in bytes. Maximum allowed value is 30MB.

##### allowed_file_extensions: [`StorageUpdateBucketByIdRequestAllowedFileExtensions`](./appwrite_console_python_sdk/type/storage_update_bucket_by_id_request_allowed_file_extensions.py)<a id="allowed_file_extensions-storageupdatebucketbyidrequestallowedfileextensionsappwrite_console_python_sdktypestorage_update_bucket_by_id_request_allowed_file_extensionspy"></a>

##### compression: `str`<a id="compression-str"></a>

Compression algorithm choosen for compression. Can be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled

##### encryption: `bool`<a id="encryption-bool"></a>

Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled

##### antivirus: `bool`<a id="antivirus-bool"></a>

Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageUpdateBucketByIdRequest`](./appwrite_console_python_sdk/type/storage_update_bucket_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Bucket`](./appwrite_console_python_sdk/pydantic/bucket.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.storage.update_file_by_id`<a id="appwriteconsolestorageupdate_file_by_id"></a>

Update a file by its unique ID. Only users with write permissions have access to update this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_file_by_id_response = appwriteconsole.storage.update_file_by_id(
    bucket_id="bucketId_example",
    file_id="fileId_example",
    name="<NAME>",
    permissions=[
        "[\"read(\"any\")\"]"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bucket_id: `str`<a id="bucket_id-str"></a>

Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).

##### file_id: `str`<a id="file_id-str"></a>

File unique ID.

##### name: `str`<a id="name-str"></a>

Name of the file

##### permissions: [`StorageUpdateFileByIdRequestPermissions`](./appwrite_console_python_sdk/type/storage_update_file_by_id_request_permissions.py)<a id="permissions-storageupdatefilebyidrequestpermissionsappwrite_console_python_sdktypestorage_update_file_by_id_request_permissionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StorageUpdateFileByIdRequest`](./appwrite_console_python_sdk/type/storage_update_file_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`File`](./appwrite_console_python_sdk/pydantic/file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage/buckets/{bucketId}/files/{fileId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.create_membership`<a id="appwriteconsoleteamscreate_membership"></a>

Invite a new member to join your team. Provide an ID for existing users, or invite unregistered users using an email or phone number. If initiated from a Client SDK, Appwrite will send an email or sms with a link to join the team to the invited user, and an account will be created for them if one doesn't exist. If initiated from a Server SDK, the new member will be added automatically to the team.

You only need to provide one of a user ID, email, or phone number. Appwrite will prioritize accepting the user ID > email > phone number if you provide more than one of these parameters.

Use the `url` parameter to redirect the user from the invitation email to your app. After the user is redirected, use the [Update Team Membership Status](https://appwrite.io/docs/references/cloud/client-web/teams#updateMembershipStatus) endpoint to allow the user to accept the invitation to the team. 

Please note that to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) Appwrite will accept the only redirect URLs under the domains you have added as a platform on the Appwrite Console.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_membership_response = appwriteconsole.teams.create_membership(
    roles=[
        "string_example"
    ],
    team_id="teamId_example",
    email="email@example.com",
    user_id="<USER_ID>",
    phone="+12065550100",
    url="https://example.com",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### roles: [`TeamsCreateMembershipRequestRoles`](./appwrite_console_python_sdk/type/teams_create_membership_request_roles.py)<a id="roles-teamscreatemembershiprequestrolesappwrite_console_python_sdktypeteams_create_membership_request_rolespy"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### email: `str`<a id="email-str"></a>

Email of the new team member.

##### user_id: `str`<a id="user_id-str"></a>

ID of the user to be added to a team.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### url: `str`<a id="url-str"></a>

URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.

##### name: `str`<a id="name-str"></a>

Name of the new team member. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateMembershipRequest`](./appwrite_console_python_sdk/type/teams_create_membership_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_console_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.create_team`<a id="appwriteconsoleteamscreate_team"></a>

Create a new team. The user who creates the team will automatically be assigned as the owner of the team. Only the users with the owner role can invite new members, add new owners and delete or update the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_response = appwriteconsole.teams.create_team(
    team_id="<TEAM_ID>",
    name="<NAME>",
    roles=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### name: `str`<a id="name-str"></a>

Team name. Max length: 128 chars.

##### roles: [`TeamsCreateTeamRequestRoles`](./appwrite_console_python_sdk/type/teams_create_team_request_roles.py)<a id="roles-teamscreateteamrequestrolesappwrite_console_python_sdktypeteams_create_team_request_rolespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateTeamRequest`](./appwrite_console_python_sdk/type/teams_create_team_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_console_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.get_by_id`<a id="appwriteconsoleteamsget_by_id"></a>

Get a team by its ID. All team members have read access for this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = appwriteconsole.teams.get_by_id(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_console_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.get_filtered_teams`<a id="appwriteconsoleteamsget_filtered_teams"></a>

Get a list of all the teams in which the current user is a member. You can use the parameters to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filtered_teams_response = appwriteconsole.teams.get_filtered_teams(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, total, billingPlan

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamList`](./appwrite_console_python_sdk/pydantic/team_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.get_membership`<a id="appwriteconsoleteamsget_membership"></a>

Get a team member by the membership unique id. All team members have read access for this resource.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_membership_response = appwriteconsole.teams.get_membership(
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_console_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.get_prefs`<a id="appwriteconsoleteamsget_prefs"></a>

Get the team's shared preferences by its unique ID. If a preference doesn't need to be shared by all team members, prefer storing them in [user preferences](https://appwrite.io/docs/references/cloud/client-web/account#getPrefs).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_prefs_response = appwriteconsole.teams.get_prefs(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_console_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.list_logs`<a id="appwriteconsoleteamslist_logs"></a>

Get the team activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_logs_response = appwriteconsole.teams.list_logs(
    team_id="teamId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.list_memberships`<a id="appwriteconsoleteamslist_memberships"></a>

Use this endpoint to list a team's members using the team's ID. All team members have read access to this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_memberships_response = appwriteconsole.teams.list_memberships(
    team_id="teamId_example",
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipList`](./appwrite_console_python_sdk/pydantic/membership_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.remove_by_id`<a id="appwriteconsoleteamsremove_by_id"></a>

Delete a team using its ID. Only team members with the owner role can delete the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.teams.remove_by_id(
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.remove_membership`<a id="appwriteconsoleteamsremove_membership"></a>

This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.teams.remove_membership(
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.update_membership_roles`<a id="appwriteconsoleteamsupdate_membership_roles"></a>

Modify the roles of a team member. Only team members with the owner role have access to this endpoint. Learn more about [roles and permissions](https://appwrite.io/docs/permissions).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_membership_roles_response = appwriteconsole.teams.update_membership_roles(
    roles=[
        "string_example"
    ],
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### roles: [`TeamsUpdateMembershipRolesRequestRoles`](./appwrite_console_python_sdk/type/teams_update_membership_roles_request_roles.py)<a id="roles-teamsupdatemembershiprolesrequestrolesappwrite_console_python_sdktypeteams_update_membership_roles_request_rolespy"></a>

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateMembershipRolesRequest`](./appwrite_console_python_sdk/type/teams_update_membership_roles_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_console_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.update_membership_status`<a id="appwriteconsoleteamsupdate_membership_status"></a>

Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email received by the user.

If the request is successful, a session for the user is automatically created.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_membership_status_response = appwriteconsole.teams.update_membership_status(
    user_id="<USER_ID>",
    secret="<SECRET>",
    team_id="teamId_example",
    membership_id="membershipId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### secret: `str`<a id="secret-str"></a>

Secret key.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

##### membership_id: `str`<a id="membership_id-str"></a>

Membership ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateMembershipStatusRequest`](./appwrite_console_python_sdk/type/teams_update_membership_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Membership`](./appwrite_console_python_sdk/pydantic/membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/memberships/{membershipId}/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.update_name_by_id`<a id="appwriteconsoleteamsupdate_name_by_id"></a>

Update the team's name by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_name_by_id_response = appwriteconsole.teams.update_name_by_id(
    name="<NAME>",
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

New team name. Max length: 128 chars.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateNameByIdRequest`](./appwrite_console_python_sdk/type/teams_update_name_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./appwrite_console_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.teams.update_prefs_by_id`<a id="appwriteconsoleteamsupdate_prefs_by_id"></a>

Update the team's preferences by its unique ID. The object you pass is stored as is and replaces any previous value. The maximum allowed prefs size is 64kB and throws an error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_prefs_by_id_response = appwriteconsole.teams.update_prefs_by_id(
    prefs={},
    team_id="teamId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

##### team_id: `str`<a id="team_id-str"></a>

Team ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdatePrefsByIdRequest`](./appwrite_console_python_sdk/type/teams_update_prefs_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_console_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{teamId}/prefs` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_argon_user`<a id="appwriteconsoleuserscreate_argon_user"></a>

Create a new user. Password provided must be hashed with the [Argon2](https://en.wikipedia.org/wiki/Argon2) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_argon_user_response = appwriteconsole.users.create_argon_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Argon2.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateArgonUserRequest`](./appwrite_console_python_sdk/type/users_create_argon_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/argon2` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_bcrypt_password`<a id="appwriteconsoleuserscreate_bcrypt_password"></a>

Create a new user. Password provided must be hashed with the [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bcrypt_password_response = appwriteconsole.users.create_bcrypt_password(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Bcrypt.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateBcryptPasswordRequest`](./appwrite_console_python_sdk/type/users_create_bcrypt_password_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/bcrypt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_md5_user`<a id="appwriteconsoleuserscreate_md5_user"></a>

Create a new user. Password provided must be hashed with the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_md5_user_response = appwriteconsole.users.create_md5_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using MD5.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateMd5UserRequest`](./appwrite_console_python_sdk/type/users_create_md5_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/md5` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_messaging_target`<a id="appwriteconsoleuserscreate_messaging_target"></a>

Create a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_messaging_target_response = appwriteconsole.users.create_messaging_target(
    target_id="<TARGET_ID>",
    provider_type="email",
    identifier="<IDENTIFIER>",
    user_id="userId_example",
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_id: `str`<a id="target_id-str"></a>

Target ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### provider_type: `str`<a id="provider_type-str"></a>

The target provider type. Can be one of the following: `email`, `sms` or `push`.

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.

##### name: `str`<a id="name-str"></a>

Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateMessagingTargetRequest`](./appwrite_console_python_sdk/type/users_create_messaging_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_mfa_recovery_codes`<a id="appwriteconsoleuserscreate_mfa_recovery_codes"></a>

Generate recovery codes used as backup for MFA flow for User ID. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method by client SDK.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_mfa_recovery_codes_response = appwriteconsole.users.create_mfa_recovery_codes(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_new_user`<a id="appwriteconsoleuserscreate_new_user"></a>

Create a new user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = appwriteconsole.users.create_new_user(
    user_id="<USER_ID>",
    email="email@example.com",
    phone="+12065550100",
    password="string_example",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### phone: `str`<a id="phone-str"></a>

Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.

##### password: `str`<a id="password-str"></a>

Plain text user password. Must be at least 8 chars.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateNewUserRequest`](./appwrite_console_python_sdk/type/users_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_scrypt_modified_user`<a id="appwriteconsoleuserscreate_scrypt_modified_user"></a>

Create a new user. Password provided must be hashed with the [Scrypt Modified](https://gist.github.com/Meldiron/eecf84a0225eccb5a378d45bb27462cc) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_scrypt_modified_user_response = appwriteconsole.users.create_scrypt_modified_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_salt="<PASSWORD_SALT>",
    password_salt_separator="<PASSWORD_SALT_SEPARATOR>",
    password_signer_key="<PASSWORD_SIGNER_KEY>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Scrypt Modified.

##### password_salt: `str`<a id="password_salt-str"></a>

Salt used to hash password.

##### password_salt_separator: `str`<a id="password_salt_separator-str"></a>

Salt separator used to hash password.

##### password_signer_key: `str`<a id="password_signer_key-str"></a>

Signer key used to hash password.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateScryptModifiedUserRequest`](./appwrite_console_python_sdk/type/users_create_scrypt_modified_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/scrypt-modified` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_scrypt_user`<a id="appwriteconsoleuserscreate_scrypt_user"></a>

Create a new user. Password provided must be hashed with the [Scrypt](https://github.com/Tarsnap/scrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_scrypt_user_response = appwriteconsole.users.create_scrypt_user(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_salt="<PASSWORD_SALT>",
    password_cpu=1,
    password_memory=1,
    password_parallel=1,
    password_length=1,
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using Scrypt.

##### password_salt: `str`<a id="password_salt-str"></a>

Optional salt used to hash password.

##### password_cpu: `int`<a id="password_cpu-int"></a>

Optional CPU cost used to hash password.

##### password_memory: `int`<a id="password_memory-int"></a>

Optional memory cost used to hash password.

##### password_parallel: `int`<a id="password_parallel-int"></a>

Optional parallelization cost used to hash password.

##### password_length: `int`<a id="password_length-int"></a>

Optional hash length used to hash password.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateScryptUserRequest`](./appwrite_console_python_sdk/type/users_create_scrypt_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/scrypt` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_session`<a id="appwriteconsoleuserscreate_session"></a>

Creates a session for a user. Returns an immediately usable session object.

If you want to generate a token for a custom authentication flow, use the [POST /users/{userId}/tokens](https://appwrite.io/docs/server/users#createToken) endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_response = appwriteconsole.users.create_session(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./appwrite_console_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_with_ph_pass`<a id="appwriteconsoleuserscreate_with_ph_pass"></a>

Create a new user. Password provided must be hashed with the [PHPass](https://www.openwall.com/phpass/) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_with_ph_pass_response = appwriteconsole.users.create_with_ph_pass(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or pass the string `ID.unique()`to auto generate it. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using PHPass.

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateWithPhPassRequest`](./appwrite_console_python_sdk/type/users_create_with_ph_pass_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/phpass` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.create_with_sha_password`<a id="appwriteconsoleuserscreate_with_sha_password"></a>

Create a new user. Password provided must be hashed with the [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_with_sha_password_response = appwriteconsole.users.create_with_sha_password(
    user_id="<USER_ID>",
    email="email@example.com",
    password="password",
    password_version="sha1",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.

##### email: `str`<a id="email-str"></a>

User email.

##### password: `str`<a id="password-str"></a>

User password hashed using SHA.

##### password_version: `str`<a id="password_version-str"></a>

Optional SHA version used to hash password. Allowed values are: 'sha1', 'sha224', 'sha256', 'sha384', 'sha512/224', 'sha512/256', 'sha512', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512'

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateWithShaPasswordRequest`](./appwrite_console_python_sdk/type/users_create_with_sha_password_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/sha` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_authenticator`<a id="appwriteconsoleusersdelete_authenticator"></a>

Delete an authenticator app.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_authenticator_response = appwriteconsole.users.delete_authenticator(
    user_id="userId_example",
    type="totp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### type: `str`<a id="type-str"></a>

Type of authenticator.

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/authenticators/{type}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_by_id`<a id="appwriteconsoleusersdelete_by_id"></a>

Delete a user by its unique ID, thereby releasing it's ID. Since ID is released and can be reused, all user-related resources like documents or storage files should be deleted before user deletion. If you want to keep ID reserved, use the [updateStatus](https://appwrite.io/docs/server/users#usersUpdateStatus) endpoint instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.users.delete_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_identity_by_id`<a id="appwriteconsoleusersdelete_identity_by_id"></a>

Delete an identity by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.users.delete_identity_by_id(
    identity_id="identityId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### identity_id: `str`<a id="identity_id-str"></a>

Identity ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/identities/{identityId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_session_by_user_id_and_session_id`<a id="appwriteconsoleusersdelete_session_by_user_id_and_session_id"></a>

Delete a user sessions by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.users.delete_session_by_user_id_and_session_id(
    user_id="userId_example",
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### session_id: `str`<a id="session_id-str"></a>

Session ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions/{sessionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_sessions_by_id`<a id="appwriteconsoleusersdelete_sessions_by_id"></a>

Delete all user's sessions by using the user's unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.users.delete_sessions_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.delete_target_messaging`<a id="appwriteconsoleusersdelete_target_messaging"></a>

Delete a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.users.delete_target_messaging(
    user_id="userId_example",
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.generate_token`<a id="appwriteconsoleusersgenerate_token"></a>

Returns a token with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [PUT /account/sessions/custom](https://appwrite.io/docs/references/cloud/client-web/account#updateCustomSession) endpoint to complete the login process.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_token_response = appwriteconsole.users.generate_token(
    user_id="userId_example",
    length=4,
    expire=60,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### length: `int`<a id="length-int"></a>

Token length in characters. The default length is 6 characters

##### expire: `int`<a id="expire-int"></a>

Token expiration period in seconds. The default expiration is 15 minutes.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersGenerateTokenRequest`](./appwrite_console_python_sdk/type/users_generate_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./appwrite_console_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_logs_by_user_id`<a id="appwriteconsoleusersget_logs_by_user_id"></a>

Get the user activity logs list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_logs_by_user_id_response = appwriteconsole.users.get_logs_by_user_id(
    user_id="userId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset

#### 🔄 Return<a id="🔄-return"></a>

[`LogList`](./appwrite_console_python_sdk/pydantic/log_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/logs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_memberships_by_id`<a id="appwriteconsoleusersget_memberships_by_id"></a>

Get the user membership list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_memberships_by_id_response = appwriteconsole.users.get_memberships_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipList`](./appwrite_console_python_sdk/pydantic/membership_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_mfa_recovery_codes`<a id="appwriteconsoleusersget_mfa_recovery_codes"></a>

Get recovery codes that can be used as backup for MFA flow by User ID. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mfa_recovery_codes_response = appwriteconsole.users.get_mfa_recovery_codes(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_target`<a id="appwriteconsoleusersget_target"></a>

Get a user's push notification target by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_target_response = appwriteconsole.users.get_target(
    user_id="userId_example",
    target_id="targetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_usage_stats`<a id="appwriteconsoleusersget_usage_stats"></a>

Get users usage stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_stats_response = appwriteconsole.users.get_usage_stats(
    range="30d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### range: `str`<a id="range-str"></a>

Date range.

#### 🔄 Return<a id="🔄-return"></a>

[`UsageUsers`](./appwrite_console_python_sdk/pydantic/usage_users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/usage` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_user_by_id`<a id="appwriteconsoleusersget_user_by_id"></a>

Get a user by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_response = appwriteconsole.users.get_user_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.get_user_prefs_by_id`<a id="appwriteconsoleusersget_user_prefs_by_id"></a>

Get the user preferences by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_prefs_by_id_response = appwriteconsole.users.get_user_prefs_by_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_console_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/prefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.list_filtered_users`<a id="appwriteconsoleuserslist_filtered_users"></a>

Get a list of all the project's users. You can use the query params to filter your results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_filtered_users_response = appwriteconsole.users.list_filtered_users(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`UserList`](./appwrite_console_python_sdk/pydantic/user_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.list_identities`<a id="appwriteconsoleuserslist_identities"></a>

Get identities for all users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_identities_response = appwriteconsole.users.list_identities(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityList`](./appwrite_console_python_sdk/pydantic/identity_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/identities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.list_mfa_factors`<a id="appwriteconsoleuserslist_mfa_factors"></a>

List the factors available on the account to be used as a MFA challange.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_mfa_factors_response = appwriteconsole.users.list_mfa_factors(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaFactors`](./appwrite_console_python_sdk/pydantic/mfa_factors.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/factors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.list_sessions_by_user_id`<a id="appwriteconsoleuserslist_sessions_by_user_id"></a>

Get the user sessions list by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sessions_by_user_id_response = appwriteconsole.users.list_sessions_by_user_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`SessionList`](./appwrite_console_python_sdk/pydantic/session_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.list_targets`<a id="appwriteconsoleuserslist_targets"></a>

List the messaging targets that are associated with a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_targets_response = appwriteconsole.users.list_targets(
    user_id="userId_example",
    queries=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels

#### 🔄 Return<a id="🔄-return"></a>

[`TargetList`](./appwrite_console_python_sdk/pydantic/target_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.regenerate_mfa_recovery_codes_by_user_id`<a id="appwriteconsoleusersregenerate_mfa_recovery_codes_by_user_id"></a>

Regenerate recovery codes that can be used as backup for MFA flow by User ID. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
regenerate_mfa_recovery_codes_by_user_id_response = appwriteconsole.users.regenerate_mfa_recovery_codes_by_user_id(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MfaRecoveryCodes`](./appwrite_console_python_sdk/pydantic/mfa_recovery_codes.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa/recovery-codes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_email_by_id`<a id="appwriteconsoleusersupdate_email_by_id"></a>

Update the user email by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_by_id_response = appwriteconsole.users.update_email_by_id(
    email="email@example.com",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

User email.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateEmailByIdRequest`](./appwrite_console_python_sdk/type/users_update_email_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/email` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_email_verification_status`<a id="appwriteconsoleusersupdate_email_verification_status"></a>

Update the user email verification status by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_verification_status_response = appwriteconsole.users.update_email_verification_status(
    email_verification=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email_verification: `bool`<a id="email_verification-bool"></a>

User email verification status.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateEmailVerificationStatusRequest`](./appwrite_console_python_sdk/type/users_update_email_verification_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/verification` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_labels_by_user_id`<a id="appwriteconsoleusersupdate_labels_by_user_id"></a>

Update the user labels by its unique ID. 

Labels can be used to grant access to resources. While teams are a way for user's to share access to a resource, labels can be defined by the developer to grant access without an invitation. See the [Permissions docs](https://appwrite.io/docs/permissions) for more info.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_labels_by_user_id_response = appwriteconsole.users.update_labels_by_user_id(
    labels=[
        "string_example"
    ],
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### labels: [`UsersUpdateLabelsByUserIdRequestLabels`](./appwrite_console_python_sdk/type/users_update_labels_by_user_id_request_labels.py)<a id="labels-usersupdatelabelsbyuseridrequestlabelsappwrite_console_python_sdktypeusers_update_labels_by_user_id_request_labelspy"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateLabelsByUserIdRequest`](./appwrite_console_python_sdk/type/users_update_labels_by_user_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/labels` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_messaging_target`<a id="appwriteconsoleusersupdate_messaging_target"></a>

Update a messaging target.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_messaging_target_response = appwriteconsole.users.update_messaging_target(
    user_id="userId_example",
    target_id="targetId_example",
    identifier="<IDENTIFIER>",
    provider_id="<PROVIDER_ID>",
    name="<NAME>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID.

##### target_id: `str`<a id="target_id-str"></a>

Target ID.

##### identifier: `str`<a id="identifier-str"></a>

The target identifier (token, email, phone etc.)

##### provider_id: `str`<a id="provider_id-str"></a>

Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.

##### name: `str`<a id="name-str"></a>

Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateMessagingTargetRequest`](./appwrite_console_python_sdk/type/users_update_messaging_target_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Target`](./appwrite_console_python_sdk/pydantic/target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/targets/{targetId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_mfa_status`<a id="appwriteconsoleusersupdate_mfa_status"></a>

Enable or disable MFA on a user account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mfa_status_response = appwriteconsole.users.update_mfa_status(
    mfa=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mfa: `bool`<a id="mfa-bool"></a>

Enable or disable MFA.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateMfaStatusRequest`](./appwrite_console_python_sdk/type/users_update_mfa_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/mfa` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_name_by_id`<a id="appwriteconsoleusersupdate_name_by_id"></a>

Update the user name by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_name_by_id_response = appwriteconsole.users.update_name_by_id(
    name="<NAME>",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

User name. Max length: 128 chars.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateNameByIdRequest`](./appwrite_console_python_sdk/type/users_update_name_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/name` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_password_by_user_id`<a id="appwriteconsoleusersupdate_password_by_user_id"></a>

Update the user password by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_password_by_user_id_response = appwriteconsole.users.update_password_by_user_id(
    password="string_example",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### password: `str`<a id="password-str"></a>

New user password. Must be at least 8 chars.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePasswordByUserIdRequest`](./appwrite_console_python_sdk/type/users_update_password_by_user_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/password` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_phone_by_user_id`<a id="appwriteconsoleusersupdate_phone_by_user_id"></a>

Update the user phone by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_by_user_id_response = appwriteconsole.users.update_phone_by_user_id(
    number="+12065550100",
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### number: `str`<a id="number-str"></a>

User phone number.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePhoneByUserIdRequest`](./appwrite_console_python_sdk/type/users_update_phone_by_user_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_phone_verification`<a id="appwriteconsoleusersupdate_phone_verification"></a>

Update the user phone verification status by its unique ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_verification_response = appwriteconsole.users.update_phone_verification(
    phone_verification=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone_verification: `bool`<a id="phone_verification-bool"></a>

User phone verification status.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePhoneVerificationRequest`](./appwrite_console_python_sdk/type/users_update_phone_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/verification/phone` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_prefs_by_id`<a id="appwriteconsoleusersupdate_prefs_by_id"></a>

Update the user preferences by its unique ID. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_prefs_by_id_response = appwriteconsole.users.update_prefs_by_id(
    prefs={},
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prefs: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="prefs-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Prefs key-value JSON object.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdatePrefsByIdRequest`](./appwrite_console_python_sdk/type/users_update_prefs_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Preferences`](./appwrite_console_python_sdk/pydantic/preferences.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/prefs` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.users.update_status_by_user_id`<a id="appwriteconsoleusersupdate_status_by_user_id"></a>

Update the user status by its unique ID. Use this endpoint as an alternative to deleting a user if you want to keep user's ID reserved.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_by_user_id_response = appwriteconsole.users.update_status_by_user_id(
    status=False,
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `bool`<a id="status-bool"></a>

User Status. To activate the user pass `true` and to block the user pass `false`.

##### user_id: `str`<a id="user_id-str"></a>

User ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateStatusByUserIdRequest`](./appwrite_console_python_sdk/type/users_update_status_by_user_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./appwrite_console_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.authorize_external_deployment`<a id="appwriteconsolevcsauthorize_external_deployment"></a>

Authorize external deployment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.vcs.authorize_external_deployment(
    provider_pull_request_id="<PROVIDER_PULL_REQUEST_ID>",
    installation_id="installationId_example",
    repository_id="repositoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_pull_request_id: `str`<a id="provider_pull_request_id-str"></a>

GitHub Pull Request Id

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

##### repository_id: `str`<a id="repository_id-str"></a>

VCS Repository Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VcsAuthorizeExternalDeploymentRequest`](./appwrite_console_python_sdk/type/vcs_authorize_external_deployment_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/repositories/{repositoryId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.create_provider_repository`<a id="appwriteconsolevcscreate_provider_repository"></a>

Create repository

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_provider_repository_response = appwriteconsole.vcs.create_provider_repository(
    name="<NAME>",
    private=False,
    installation_id="installationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Repository name (slug)

##### private: `bool`<a id="private-bool"></a>

Mark repository public or private

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VcsCreateProviderRepositoryRequest`](./appwrite_console_python_sdk/type/vcs_create_provider_repository_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProviderRepository`](./appwrite_console_python_sdk/pydantic/provider_repository.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/providerRepositories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.delete_installation`<a id="appwriteconsolevcsdelete_installation"></a>

Delete Installation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
appwriteconsole.vcs.delete_installation(
    installation_id="installationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/installations/{installationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.detect_runtime_settings`<a id="appwriteconsolevcsdetect_runtime_settings"></a>

Detect runtime settings from source code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detect_runtime_settings_response = appwriteconsole.vcs.detect_runtime_settings(
    installation_id="installationId_example",
    provider_repository_id="providerRepositoryId_example",
    provider_root_directory="<PROVIDER_ROOT_DIRECTORY>",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository Id

##### provider_root_directory: `str`<a id="provider_root_directory-str"></a>

Path to Root Directory

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VcsDetectRuntimeSettingsRequest`](./appwrite_console_python_sdk/type/vcs_detect_runtime_settings_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Detection`](./appwrite_console_python_sdk/pydantic/detection.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}/detection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.get_installation_by_id`<a id="appwriteconsolevcsget_installation_by_id"></a>

Get installation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_installation_by_id_response = appwriteconsole.vcs.get_installation_by_id(
    installation_id="installationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

#### 🔄 Return<a id="🔄-return"></a>

[`Installation`](./appwrite_console_python_sdk/pydantic/installation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/installations/{installationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.get_repository`<a id="appwriteconsolevcsget_repository"></a>

Get repository

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_repository_response = appwriteconsole.vcs.get_repository(
    installation_id="installationId_example",
    provider_repository_id="providerRepositoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository Id

#### 🔄 Return<a id="🔄-return"></a>

[`ProviderRepository`](./appwrite_console_python_sdk/pydantic/provider_repository.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.list_installations`<a id="appwriteconsolevcslist_installations"></a>

List installations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_installations_response = appwriteconsole.vcs.list_installations(
    queries=[],
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### queries: List[`str`]<a id="queries-liststr"></a>

Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: provider, organization

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`InstallationList`](./appwrite_console_python_sdk/pydantic/installation_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/installations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.list_provider_repositories`<a id="appwriteconsolevcslist_provider_repositories"></a>

List Repositories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_provider_repositories_response = appwriteconsole.vcs.list_provider_repositories(
    installation_id="installationId_example",
    search="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

##### search: `str`<a id="search-str"></a>

Search term to filter your list results. Max length: 256 chars.

#### 🔄 Return<a id="🔄-return"></a>

[`ProviderRepositoryList`](./appwrite_console_python_sdk/pydantic/provider_repository_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/providerRepositories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `appwriteconsole.vcs.list_repository_branches`<a id="appwriteconsolevcslist_repository_branches"></a>

List Repository Branches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_repository_branches_response = appwriteconsole.vcs.list_repository_branches(
    installation_id="installationId_example",
    provider_repository_id="providerRepositoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### installation_id: `str`<a id="installation_id-str"></a>

Installation Id

##### provider_repository_id: `str`<a id="provider_repository_id-str"></a>

Repository Id

#### 🔄 Return<a id="🔄-return"></a>

[`BranchList`](./appwrite_console_python_sdk/pydantic/branch_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}/branches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
