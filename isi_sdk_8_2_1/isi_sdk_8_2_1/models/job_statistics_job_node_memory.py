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

from isi_sdk_8_2_1.models.job_statistics_job_node_memory_physical import JobStatisticsJobNodeMemoryPhysical  # noqa: F401,E501
from isi_sdk_8_2_1.models.job_statistics_job_node_memory_virtual import JobStatisticsJobNodeMemoryVirtual  # noqa: F401,E501


class JobStatisticsJobNodeMemory(object):
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
        'physical': 'JobStatisticsJobNodeMemoryPhysical',
        'virtual': 'JobStatisticsJobNodeMemoryVirtual'
    }

    attribute_map = {
        'physical': 'physical',
        'virtual': 'virtual'
    }

    def __init__(self, physical=None, virtual=None):  # noqa: E501
        """JobStatisticsJobNodeMemory - a model defined in Swagger"""  # noqa: E501

        self._physical = None
        self._virtual = None
        self.discriminator = None

        self.physical = physical
        self.virtual = virtual

    @property
    def physical(self):
        """Gets the physical of this JobStatisticsJobNodeMemory.  # noqa: E501

          # noqa: E501

        :return: The physical of this JobStatisticsJobNodeMemory.  # noqa: E501
        :rtype: JobStatisticsJobNodeMemoryPhysical
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """Sets the physical of this JobStatisticsJobNodeMemory.

          # noqa: E501

        :param physical: The physical of this JobStatisticsJobNodeMemory.  # noqa: E501
        :type: JobStatisticsJobNodeMemoryPhysical
        """
        if physical is None:
            raise ValueError("Invalid value for `physical`, must not be `None`")  # noqa: E501

        self._physical = physical

    @property
    def virtual(self):
        """Gets the virtual of this JobStatisticsJobNodeMemory.  # noqa: E501

          # noqa: E501

        :return: The virtual of this JobStatisticsJobNodeMemory.  # noqa: E501
        :rtype: JobStatisticsJobNodeMemoryVirtual
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """Sets the virtual of this JobStatisticsJobNodeMemory.

          # noqa: E501

        :param virtual: The virtual of this JobStatisticsJobNodeMemory.  # noqa: E501
        :type: JobStatisticsJobNodeMemoryVirtual
        """
        if virtual is None:
            raise ValueError("Invalid value for `virtual`, must not be `None`")  # noqa: E501

        self._virtual = virtual

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
        if not isinstance(other, JobStatisticsJobNodeMemory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
