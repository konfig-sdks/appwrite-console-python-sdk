# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ConsoleVariables(BaseModel):
    # CNAME target for your Appwrite custom domains.
    __a_p_p__d_o_m_a_i_n__t_a_r_g_e_t: str = Field(alias='_APP_DOMAIN_TARGET')

    # Maximum file size allowed for file upload in bytes.
    __a_p_p__s_t_o_r_a_g_e__l_i_m_i_t: int = Field(alias='_APP_STORAGE_LIMIT')

    # Maximum file size allowed for deployment in bytes.
    __a_p_p__f_u_n_c_t_i_o_n_s__s_i_z_e__l_i_m_i_t: int = Field(alias='_APP_FUNCTIONS_SIZE_LIMIT')

    # Defines if usage stats are enabled. This value is set to 'enabled' by default, to disable the usage stats set the value to 'disabled'.
    __a_p_p__u_s_a_g_e__s_t_a_t_s: str = Field(alias='_APP_USAGE_STATS')

    # Defines if VCS (Version Control System) is enabled.
    __a_p_p__v_c_s__e_n_a_b_l_e_d: bool = Field(alias='_APP_VCS_ENABLED')

    # Defines if main domain is configured. If so, custom domains can be created.
    __a_p_p__d_o_m_a_i_n__e_n_a_b_l_e_d: bool = Field(alias='_APP_DOMAIN_ENABLED')

    # Defines if AI assistant is enabled.
    __a_p_p__a_s_s_i_s_t_a_n_t__e_n_a_b_l_e_d: bool = Field(alias='_APP_ASSISTANT_ENABLED')
    class Config:
        arbitrary_types_allowed = True
