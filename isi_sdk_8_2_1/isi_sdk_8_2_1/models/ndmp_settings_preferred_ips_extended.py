# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_2_1.models.ndmp_settings_preferred_ips import NdmpSettingsPreferredIps  # noqa: F401,E501
from isi_sdk_8_2_1.models.ndmp_settings_preferred_ips_preference import NdmpSettingsPreferredIpsPreference  # noqa: F401,E501


class NdmpSettingsPreferredIpsExtended(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'preferences': 'list[NdmpSettingsPreferredIpsPreference]',
        'total': 'int',
        'resume': 'str'
    }

    attribute_map = {
        'preferences': 'preferences',
        'total': 'total',
        'resume': 'resume'
    }

    def __init__(self, preferences=None, total=None, resume=None):  # noqa: E501
        """NdmpSettingsPreferredIpsExtended - a model defined in Swagger"""  # noqa: E501

        self._preferences = None
        self._total = None
        self._resume = None
        self.discriminator = None

        if preferences is not None:
            self.preferences = preferences
        if total is not None:
            self.total = total
        if resume is not None:
            self.resume = resume

    @property
    def preferences(self):
        """Gets the preferences of this NdmpSettingsPreferredIpsExtended.  # noqa: E501


        :return: The preferences of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :rtype: list[NdmpSettingsPreferredIpsPreference]
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this NdmpSettingsPreferredIpsExtended.


        :param preferences: The preferences of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :type: list[NdmpSettingsPreferredIpsPreference]
        """

        self._preferences = preferences

    @property
    def total(self):
        """Gets the total of this NdmpSettingsPreferredIpsExtended.  # noqa: E501

        The number of preferences.  # noqa: E501

        :return: The total of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NdmpSettingsPreferredIpsExtended.

        The number of preferences.  # noqa: E501

        :param total: The total of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def resume(self):
        """Gets the resume of this NdmpSettingsPreferredIpsExtended.  # noqa: E501

        Resume string returned by previous query.  # noqa: E501

        :return: The resume of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this NdmpSettingsPreferredIpsExtended.

        Resume string returned by previous query.  # noqa: E501

        :param resume: The resume of this NdmpSettingsPreferredIpsExtended.  # noqa: E501
        :type: str
        """

        self._resume = resume

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NdmpSettingsPreferredIpsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
