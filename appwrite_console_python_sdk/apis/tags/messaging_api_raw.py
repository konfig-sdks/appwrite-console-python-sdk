# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.messaging_providers_apns.post import CreateApnsProviderRaw
from appwrite_console_python_sdk.paths.messaging_messages_email.post import CreateEmailMessageRaw
from appwrite_console_python_sdk.paths.messaging_providers_fcm.post import CreateFcmProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_mailgun.post import CreateMailgunProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_msg91.post import CreateMsgProviderRaw
from appwrite_console_python_sdk.paths.messaging_topics.post import CreateNewTopicRaw
from appwrite_console_python_sdk.paths.messaging_messages_push.post import CreatePushNotificationRaw
from appwrite_console_python_sdk.paths.messaging_providers_sendgrid.post import CreateSendgridProviderRaw
from appwrite_console_python_sdk.paths.messaging_messages_sms.post import CreateSmsMessageRaw
from appwrite_console_python_sdk.paths.messaging_providers_smtp.post import CreateSmtpProviderRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id_subscribers.post import CreateSubscriberRaw
from appwrite_console_python_sdk.paths.messaging_providers_telesign.post import CreateTelesignProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_textmagic.post import CreateTextmagicProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_twilio.post import CreateTwilioProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_vonage.post import CreateVonageProviderRaw
from appwrite_console_python_sdk.paths.messaging_messages_message_id.delete import DeleteMessageRaw
from appwrite_console_python_sdk.paths.messaging_providers_provider_id.delete import DeleteProviderByIdRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id_subscribers_subscriber_id.delete import DeleteSubscriberByIdRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id.delete import DeleteTopicByIdRaw
from appwrite_console_python_sdk.paths.messaging_messages_message_id.get import GetMessageByIdRaw
from appwrite_console_python_sdk.paths.messaging_providers_provider_id.get import GetProviderByIdRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id_subscribers_subscriber_id.get import GetSubscriberByIdRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id.get import GetTopicByIdRaw
from appwrite_console_python_sdk.paths.messaging_messages.get import ListAllMessagesRaw
from appwrite_console_python_sdk.paths.messaging_messages_message_id_logs.get import ListMessageLogsRaw
from appwrite_console_python_sdk.paths.messaging_providers_provider_id_logs.get import ListProviderLogsRaw
from appwrite_console_python_sdk.paths.messaging_providers.get import ListProvidersRaw
from appwrite_console_python_sdk.paths.messaging_subscribers_subscriber_id_logs.get import ListSubscriberLogsRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id_subscribers.get import ListSubscribersRaw
from appwrite_console_python_sdk.paths.messaging_messages_message_id_targets.get import ListTargetsRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id_logs.get import ListTopicLogsRaw
from appwrite_console_python_sdk.paths.messaging_topics.get import ListTopicsRaw
from appwrite_console_python_sdk.paths.messaging_providers_apns_provider_id.patch import UpdateApnsProviderRaw
from appwrite_console_python_sdk.paths.messaging_messages_email_message_id.patch import UpdateEmailByIdRaw
from appwrite_console_python_sdk.paths.messaging_providers_fcm_provider_id.patch import UpdateFcmProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_mailgun_provider_id.patch import UpdateMailgunProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_msg91_provider_id.patch import UpdateProviderByIdRaw
from appwrite_console_python_sdk.paths.messaging_messages_push_message_id.patch import UpdatePushMessageRaw
from appwrite_console_python_sdk.paths.messaging_providers_sendgrid_provider_id.patch import UpdateSendgridProviderRaw
from appwrite_console_python_sdk.paths.messaging_messages_sms_message_id.patch import UpdateSmsMessageByIdRaw
from appwrite_console_python_sdk.paths.messaging_providers_smtp_provider_id.patch import UpdateSmtpProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_telesign_provider_id.patch import UpdateTelesignProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_textmagic_provider_id.patch import UpdateTextmagicProviderRaw
from appwrite_console_python_sdk.paths.messaging_topics_topic_id.patch import UpdateTopicByIdRaw
from appwrite_console_python_sdk.paths.messaging_providers_twilio_provider_id.patch import UpdateTwilioProviderRaw
from appwrite_console_python_sdk.paths.messaging_providers_vonage_provider_id.patch import UpdateVonageProviderByIdRaw


class MessagingApiRaw(
    CreateApnsProviderRaw,
    CreateEmailMessageRaw,
    CreateFcmProviderRaw,
    CreateMailgunProviderRaw,
    CreateMsgProviderRaw,
    CreateNewTopicRaw,
    CreatePushNotificationRaw,
    CreateSendgridProviderRaw,
    CreateSmsMessageRaw,
    CreateSmtpProviderRaw,
    CreateSubscriberRaw,
    CreateTelesignProviderRaw,
    CreateTextmagicProviderRaw,
    CreateTwilioProviderRaw,
    CreateVonageProviderRaw,
    DeleteMessageRaw,
    DeleteProviderByIdRaw,
    DeleteSubscriberByIdRaw,
    DeleteTopicByIdRaw,
    GetMessageByIdRaw,
    GetProviderByIdRaw,
    GetSubscriberByIdRaw,
    GetTopicByIdRaw,
    ListAllMessagesRaw,
    ListMessageLogsRaw,
    ListProviderLogsRaw,
    ListProvidersRaw,
    ListSubscriberLogsRaw,
    ListSubscribersRaw,
    ListTargetsRaw,
    ListTopicLogsRaw,
    ListTopicsRaw,
    UpdateApnsProviderRaw,
    UpdateEmailByIdRaw,
    UpdateFcmProviderRaw,
    UpdateMailgunProviderRaw,
    UpdateProviderByIdRaw,
    UpdatePushMessageRaw,
    UpdateSendgridProviderRaw,
    UpdateSmsMessageByIdRaw,
    UpdateSmtpProviderRaw,
    UpdateTelesignProviderRaw,
    UpdateTextmagicProviderRaw,
    UpdateTopicByIdRaw,
    UpdateTwilioProviderRaw,
    UpdateVonageProviderByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
