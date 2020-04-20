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


class SettingsReportsSettings(object):
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
        'live_dir': 'str',
        'live_retain': 'int',
        'schedule': 'str',
        'scheduled_dir': 'str',
        'scheduled_retain': 'int'
    }

    attribute_map = {
        'live_dir': 'live_dir',
        'live_retain': 'live_retain',
        'schedule': 'schedule',
        'scheduled_dir': 'scheduled_dir',
        'scheduled_retain': 'scheduled_retain'
    }

    def __init__(self, live_dir=None, live_retain=None, schedule=None, scheduled_dir=None, scheduled_retain=None):  # noqa: E501
        """SettingsReportsSettings - a model defined in Swagger"""  # noqa: E501

        self._live_dir = None
        self._live_retain = None
        self._schedule = None
        self._scheduled_dir = None
        self._scheduled_retain = None
        self.discriminator = None

        self.live_dir = live_dir
        self.live_retain = live_retain
        self.schedule = schedule
        self.scheduled_dir = scheduled_dir
        self.scheduled_retain = scheduled_retain

    @property
    def live_dir(self):
        """Gets the live_dir of this SettingsReportsSettings.  # noqa: E501

        The directory on /ifs where manual or live reports will be placed.  # noqa: E501

        :return: The live_dir of this SettingsReportsSettings.  # noqa: E501
        :rtype: str
        """
        return self._live_dir

    @live_dir.setter
    def live_dir(self, live_dir):
        """Sets the live_dir of this SettingsReportsSettings.

        The directory on /ifs where manual or live reports will be placed.  # noqa: E501

        :param live_dir: The live_dir of this SettingsReportsSettings.  # noqa: E501
        :type: str
        """
        if live_dir is None:
            raise ValueError("Invalid value for `live_dir`, must not be `None`")  # noqa: E501

        self._live_dir = live_dir

    @property
    def live_retain(self):
        """Gets the live_retain of this SettingsReportsSettings.  # noqa: E501

        The number of manual reports to keep.  # noqa: E501

        :return: The live_retain of this SettingsReportsSettings.  # noqa: E501
        :rtype: int
        """
        return self._live_retain

    @live_retain.setter
    def live_retain(self, live_retain):
        """Sets the live_retain of this SettingsReportsSettings.

        The number of manual reports to keep.  # noqa: E501

        :param live_retain: The live_retain of this SettingsReportsSettings.  # noqa: E501
        :type: int
        """
        if live_retain is None:
            raise ValueError("Invalid value for `live_retain`, must not be `None`")  # noqa: E501
        if live_retain is not None and live_retain < 1:  # noqa: E501
            raise ValueError("Invalid value for `live_retain`, must be a value greater than or equal to `1`")  # noqa: E501

        self._live_retain = live_retain

    @property
    def schedule(self):
        """Gets the schedule of this SettingsReportsSettings.  # noqa: E501

        The isidate schedule used to generate reports.  # noqa: E501

        :return: The schedule of this SettingsReportsSettings.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SettingsReportsSettings.

        The isidate schedule used to generate reports.  # noqa: E501

        :param schedule: The schedule of this SettingsReportsSettings.  # noqa: E501
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def scheduled_dir(self):
        """Gets the scheduled_dir of this SettingsReportsSettings.  # noqa: E501

        The directory on /ifs where schedule reports will be placed.  # noqa: E501

        :return: The scheduled_dir of this SettingsReportsSettings.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_dir

    @scheduled_dir.setter
    def scheduled_dir(self, scheduled_dir):
        """Sets the scheduled_dir of this SettingsReportsSettings.

        The directory on /ifs where schedule reports will be placed.  # noqa: E501

        :param scheduled_dir: The scheduled_dir of this SettingsReportsSettings.  # noqa: E501
        :type: str
        """
        if scheduled_dir is None:
            raise ValueError("Invalid value for `scheduled_dir`, must not be `None`")  # noqa: E501

        self._scheduled_dir = scheduled_dir

    @property
    def scheduled_retain(self):
        """Gets the scheduled_retain of this SettingsReportsSettings.  # noqa: E501

        The number of scheduled reports to keep.  # noqa: E501

        :return: The scheduled_retain of this SettingsReportsSettings.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_retain

    @scheduled_retain.setter
    def scheduled_retain(self, scheduled_retain):
        """Sets the scheduled_retain of this SettingsReportsSettings.

        The number of scheduled reports to keep.  # noqa: E501

        :param scheduled_retain: The scheduled_retain of this SettingsReportsSettings.  # noqa: E501
        :type: int
        """
        if scheduled_retain is None:
            raise ValueError("Invalid value for `scheduled_retain`, must not be `None`")  # noqa: E501
        if scheduled_retain is not None and scheduled_retain < 1:  # noqa: E501
            raise ValueError("Invalid value for `scheduled_retain`, must be a value greater than or equal to `1`")  # noqa: E501

        self._scheduled_retain = scheduled_retain

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
        if not isinstance(other, SettingsReportsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
