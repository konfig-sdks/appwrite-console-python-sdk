# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_console_python_sdk.paths.avatars_qr.get import GenerateQrCodeRaw
from appwrite_console_python_sdk.paths.avatars_browsers_code.get import GetBrowserIconRaw
from appwrite_console_python_sdk.paths.avatars_credit_cards_code.get import GetCreditCardIconRaw
from appwrite_console_python_sdk.paths.avatars_favicon.get import GetFaviconRaw
from appwrite_console_python_sdk.paths.avatars_flags_code.get import GetFlagByCodeRaw
from appwrite_console_python_sdk.paths.avatars_image.get import GetImageUrlAndCropRaw
from appwrite_console_python_sdk.paths.avatars_initials.get import GetUserInitialsRaw


class AvatarsApiRaw(
    GenerateQrCodeRaw,
    GetBrowserIconRaw,
    GetCreditCardIconRaw,
    GetFaviconRaw,
    GetFlagByCodeRaw,
    GetImageUrlAndCropRaw,
    GetUserInitialsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
