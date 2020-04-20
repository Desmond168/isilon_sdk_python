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

from isi_sdk_8_2_1.models.ndmp_settings_variable import NdmpSettingsVariable  # noqa: F401,E501


class NdmpSettingsVariableCreateParams(object):
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
        'value': 'str',
        'name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'value': 'value',
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, value=None, name=None, path=None):  # noqa: E501
        """NdmpSettingsVariableCreateParams - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._name = None
        self._path = None
        self.discriminator = None

        self.value = value
        self.name = name
        self.path = path

    @property
    def value(self):
        """Gets the value of this NdmpSettingsVariableCreateParams.  # noqa: E501

        The value of environment variable.  # noqa: E501

        :return: The value of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NdmpSettingsVariableCreateParams.

        The value of environment variable.  # noqa: E501

        :param value: The value of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def name(self):
        """Gets the name of this NdmpSettingsVariableCreateParams.  # noqa: E501

        The name of environment variable.  # noqa: E501

        :return: The name of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NdmpSettingsVariableCreateParams.

        The name of environment variable.  # noqa: E501

        :param name: The name of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this NdmpSettingsVariableCreateParams.  # noqa: E501

        The backup path.  # noqa: E501

        :return: The path of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NdmpSettingsVariableCreateParams.

        The backup path.  # noqa: E501

        :param path: The path of this NdmpSettingsVariableCreateParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, NdmpSettingsVariableCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
