# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HistogramStatByBreakout(object):
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
        'data': 'list[list[int]]',
        'key': 'str'
    }

    attribute_map = {
        'data': 'data',
        'key': 'key'
    }

    def __init__(self, data=None, key=None):  # noqa: E501
        """HistogramStatByBreakout - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._key = None
        self.discriminator = None

        self.data = data
        self.key = key

    @property
    def data(self):
        """Gets the data of this HistogramStatByBreakout.  # noqa: E501

        List of bucket, file count pairs.  # noqa: E501

        :return: The data of this HistogramStatByBreakout.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this HistogramStatByBreakout.

        List of bucket, file count pairs.  # noqa: E501

        :param data: The data of this HistogramStatByBreakout.  # noqa: E501
        :type: list[list[int]]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def key(self):
        """Gets the key of this HistogramStatByBreakout.  # noqa: E501

        Breakout key by which results are filtered.  # noqa: E501

        :return: The key of this HistogramStatByBreakout.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this HistogramStatByBreakout.

        Breakout key by which results are filtered.  # noqa: E501

        :param key: The key of this HistogramStatByBreakout.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, HistogramStatByBreakout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
