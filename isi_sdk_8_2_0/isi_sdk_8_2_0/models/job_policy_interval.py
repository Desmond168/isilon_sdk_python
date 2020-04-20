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


class JobPolicyInterval(object):
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
        'begin': 'str',
        'end': 'str',
        'impact': 'str'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end',
        'impact': 'impact'
    }

    def __init__(self, begin=None, end=None, impact=None):  # noqa: E501
        """JobPolicyInterval - a model defined in Swagger"""  # noqa: E501

        self._begin = None
        self._end = None
        self._impact = None
        self.discriminator = None

        self.begin = begin
        self.end = end
        self.impact = impact

    @property
    def begin(self):
        """Gets the begin of this JobPolicyInterval.  # noqa: E501

        Beginning time for the corresponding impact, in the format 'WWWW HH:MM', where 'WWWW' is the full English name of the day of the week, 'HH' is the hour (00-23), and 'MM' is the minute (00-59).  # noqa: E501

        :return: The begin of this JobPolicyInterval.  # noqa: E501
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this JobPolicyInterval.

        Beginning time for the corresponding impact, in the format 'WWWW HH:MM', where 'WWWW' is the full English name of the day of the week, 'HH' is the hour (00-23), and 'MM' is the minute (00-59).  # noqa: E501

        :param begin: The begin of this JobPolicyInterval.  # noqa: E501
        :type: str
        """
        if begin is None:
            raise ValueError("Invalid value for `begin`, must not be `None`")  # noqa: E501

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this JobPolicyInterval.  # noqa: E501

        Ending time for the corresponding impact, in the format 'WWWW HH:MM', where 'WWWW' is the full English name of the day of the week, 'HH' is the hour (00-23), and 'MM' is the minute (00-59).  # noqa: E501

        :return: The end of this JobPolicyInterval.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this JobPolicyInterval.

        Ending time for the corresponding impact, in the format 'WWWW HH:MM', where 'WWWW' is the full English name of the day of the week, 'HH' is the hour (00-23), and 'MM' is the minute (00-59).  # noqa: E501

        :param end: The end of this JobPolicyInterval.  # noqa: E501
        :type: str
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def impact(self):
        """Gets the impact of this JobPolicyInterval.  # noqa: E501

        Impact for the corresponding time span.  # noqa: E501

        :return: The impact of this JobPolicyInterval.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this JobPolicyInterval.

        Impact for the corresponding time span.  # noqa: E501

        :param impact: The impact of this JobPolicyInterval.  # noqa: E501
        :type: str
        """
        if impact is None:
            raise ValueError("Invalid value for `impact`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Medium", "High", "Paused"]  # noqa: E501
        if impact not in allowed_values:
            raise ValueError(
                "Invalid value for `impact` ({0}), must be one of {1}"  # noqa: E501
                .format(impact, allowed_values)
            )

        self._impact = impact

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
        if not isinstance(other, JobPolicyInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
