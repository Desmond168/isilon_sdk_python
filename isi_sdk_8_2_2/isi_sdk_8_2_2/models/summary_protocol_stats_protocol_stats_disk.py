# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SummaryProtocolStatsProtocolStatsDisk(object):
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
        'iops': 'float',
        'read': 'float',
        'write': 'float'
    }

    attribute_map = {
        'iops': 'iops',
        'read': 'read',
        'write': 'write'
    }

    def __init__(self, iops=None, read=None, write=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsDisk - a model defined in Swagger"""  # noqa: E501

        self._iops = None
        self._read = None
        self._write = None
        self.discriminator = None

        self.iops = iops
        self.read = read
        self.write = write

    @property
    def iops(self):
        """Gets the iops of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501

        Disk iops  # noqa: E501

        :return: The iops of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :rtype: float
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this SummaryProtocolStatsProtocolStatsDisk.

        Disk iops  # noqa: E501

        :param iops: The iops of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :type: float
        """
        if iops is None:
            raise ValueError("Invalid value for `iops`, must not be `None`")  # noqa: E501

        self._iops = iops

    @property
    def read(self):
        """Gets the read of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501

        Disk reads  # noqa: E501

        :return: The read of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :rtype: float
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this SummaryProtocolStatsProtocolStatsDisk.

        Disk reads  # noqa: E501

        :param read: The read of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :type: float
        """
        if read is None:
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

    @property
    def write(self):
        """Gets the write of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501

        Disk writes  # noqa: E501

        :return: The write of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :rtype: float
        """
        return self._write

    @write.setter
    def write(self, write):
        """Sets the write of this SummaryProtocolStatsProtocolStatsDisk.

        Disk writes  # noqa: E501

        :param write: The write of this SummaryProtocolStatsProtocolStatsDisk.  # noqa: E501
        :type: float
        """
        if write is None:
            raise ValueError("Invalid value for `write`, must not be `None`")  # noqa: E501

        self._write = write

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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
