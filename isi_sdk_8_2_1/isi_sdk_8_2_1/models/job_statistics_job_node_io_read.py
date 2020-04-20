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


class JobStatisticsJobNodeIoRead(object):
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
        'bytes': 'int',
        'ops': 'int'
    }

    attribute_map = {
        'bytes': 'bytes',
        'ops': 'ops'
    }

    def __init__(self, bytes=None, ops=None):  # noqa: E501
        """JobStatisticsJobNodeIoRead - a model defined in Swagger"""  # noqa: E501

        self._bytes = None
        self._ops = None
        self.discriminator = None

        self.bytes = bytes
        self.ops = ops

    @property
    def bytes(self):
        """Gets the bytes of this JobStatisticsJobNodeIoRead.  # noqa: E501

        The number of bytes recently read by this job on this node.  # noqa: E501

        :return: The bytes of this JobStatisticsJobNodeIoRead.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this JobStatisticsJobNodeIoRead.

        The number of bytes recently read by this job on this node.  # noqa: E501

        :param bytes: The bytes of this JobStatisticsJobNodeIoRead.  # noqa: E501
        :type: int
        """
        if bytes is None:
            raise ValueError("Invalid value for `bytes`, must not be `None`")  # noqa: E501

        self._bytes = bytes

    @property
    def ops(self):
        """Gets the ops of this JobStatisticsJobNodeIoRead.  # noqa: E501

        The number of read operations recently performed by this job on this node.  # noqa: E501

        :return: The ops of this JobStatisticsJobNodeIoRead.  # noqa: E501
        :rtype: int
        """
        return self._ops

    @ops.setter
    def ops(self, ops):
        """Sets the ops of this JobStatisticsJobNodeIoRead.

        The number of read operations recently performed by this job on this node.  # noqa: E501

        :param ops: The ops of this JobStatisticsJobNodeIoRead.  # noqa: E501
        :type: int
        """
        if ops is None:
            raise ValueError("Invalid value for `ops`, must not be `None`")  # noqa: E501

        self._ops = ops

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
        if not isinstance(other, JobStatisticsJobNodeIoRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
