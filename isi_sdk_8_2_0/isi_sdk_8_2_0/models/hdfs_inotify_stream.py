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

from isi_sdk_8_2_0.models.hdfs_inotify_stream_stream import HdfsInotifyStreamStream  # noqa: F401,E501


class HdfsInotifyStream(object):
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
        'stream': 'HdfsInotifyStreamStream'
    }

    attribute_map = {
        'stream': 'stream'
    }

    def __init__(self, stream=None):  # noqa: E501
        """HdfsInotifyStream - a model defined in Swagger"""  # noqa: E501

        self._stream = None
        self.discriminator = None

        if stream is not None:
            self.stream = stream

    @property
    def stream(self):
        """Gets the stream of this HdfsInotifyStream.  # noqa: E501

        Information about HDFS INotify stream.  # noqa: E501

        :return: The stream of this HdfsInotifyStream.  # noqa: E501
        :rtype: HdfsInotifyStreamStream
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this HdfsInotifyStream.

        Information about HDFS INotify stream.  # noqa: E501

        :param stream: The stream of this HdfsInotifyStream.  # noqa: E501
        :type: HdfsInotifyStreamStream
        """

        self._stream = stream

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
        if not isinstance(other, HdfsInotifyStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
