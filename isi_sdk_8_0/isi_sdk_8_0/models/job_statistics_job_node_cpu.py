# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobStatisticsJobNodeCpu(object):
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
        'average': 'float',
        'current': 'float',
        'maximum': 'float',
        'minimum': 'float'
    }

    attribute_map = {
        'average': 'average',
        'current': 'current',
        'maximum': 'maximum',
        'minimum': 'minimum'
    }

    def __init__(self, average=None, current=None, maximum=None, minimum=None):  # noqa: E501
        """JobStatisticsJobNodeCpu - a model defined in Swagger"""  # noqa: E501

        self._average = None
        self._current = None
        self._maximum = None
        self._minimum = None
        self.discriminator = None

        if average is not None:
            self.average = average
        self.current = current
        self.maximum = maximum
        self.minimum = minimum

    @property
    def average(self):
        """Gets the average of this JobStatisticsJobNodeCpu.  # noqa: E501

        The average CPU utilization of the job on this node.  # noqa: E501

        :return: The average of this JobStatisticsJobNodeCpu.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this JobStatisticsJobNodeCpu.

        The average CPU utilization of the job on this node.  # noqa: E501

        :param average: The average of this JobStatisticsJobNodeCpu.  # noqa: E501
        :type: float
        """

        self._average = average

    @property
    def current(self):
        """Gets the current of this JobStatisticsJobNodeCpu.  # noqa: E501

        The current CPU utilization of the job on this node.  # noqa: E501

        :return: The current of this JobStatisticsJobNodeCpu.  # noqa: E501
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this JobStatisticsJobNodeCpu.

        The current CPU utilization of the job on this node.  # noqa: E501

        :param current: The current of this JobStatisticsJobNodeCpu.  # noqa: E501
        :type: float
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def maximum(self):
        """Gets the maximum of this JobStatisticsJobNodeCpu.  # noqa: E501

        The maximum CPU utilization of the job on this node.  # noqa: E501

        :return: The maximum of this JobStatisticsJobNodeCpu.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this JobStatisticsJobNodeCpu.

        The maximum CPU utilization of the job on this node.  # noqa: E501

        :param maximum: The maximum of this JobStatisticsJobNodeCpu.  # noqa: E501
        :type: float
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this JobStatisticsJobNodeCpu.  # noqa: E501

        The minimum CPU utilization of the job on this node.  # noqa: E501

        :return: The minimum of this JobStatisticsJobNodeCpu.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this JobStatisticsJobNodeCpu.

        The minimum CPU utilization of the job on this node.  # noqa: E501

        :param minimum: The minimum of this JobStatisticsJobNodeCpu.  # noqa: E501
        :type: float
        """
        if minimum is None:
            raise ValueError("Invalid value for `minimum`, must not be `None`")  # noqa: E501

        self._minimum = minimum

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
        if not isinstance(other, JobStatisticsJobNodeCpu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
