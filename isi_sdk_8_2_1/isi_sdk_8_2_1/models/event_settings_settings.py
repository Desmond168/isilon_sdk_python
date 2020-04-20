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

from isi_sdk_8_2_1.models.event_settings_settings_maintenance import EventSettingsSettingsMaintenance  # noqa: F401,E501


class EventSettingsSettings(object):
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
        'heartbeat_interval': 'str',
        'maintenance': 'EventSettingsSettingsMaintenance',
        'retention_days': 'int',
        'storage_limit': 'int'
    }

    attribute_map = {
        'heartbeat_interval': 'heartbeat_interval',
        'maintenance': 'maintenance',
        'retention_days': 'retention_days',
        'storage_limit': 'storage_limit'
    }

    def __init__(self, heartbeat_interval=None, maintenance=None, retention_days=None, storage_limit=None):  # noqa: E501
        """EventSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._heartbeat_interval = None
        self._maintenance = None
        self._retention_days = None
        self._storage_limit = None
        self.discriminator = None

        if heartbeat_interval is not None:
            self.heartbeat_interval = heartbeat_interval
        if maintenance is not None:
            self.maintenance = maintenance
        if retention_days is not None:
            self.retention_days = retention_days
        if storage_limit is not None:
            self.storage_limit = storage_limit

    @property
    def heartbeat_interval(self):
        """Gets the heartbeat_interval of this EventSettingsSettings.  # noqa: E501

        Interval between heartbeat events. \"daily\", \"weekly\", or \"monthly\".  # noqa: E501

        :return: The heartbeat_interval of this EventSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._heartbeat_interval

    @heartbeat_interval.setter
    def heartbeat_interval(self, heartbeat_interval):
        """Sets the heartbeat_interval of this EventSettingsSettings.

        Interval between heartbeat events. \"daily\", \"weekly\", or \"monthly\".  # noqa: E501

        :param heartbeat_interval: The heartbeat_interval of this EventSettingsSettings.  # noqa: E501
        :type: str
        """

        self._heartbeat_interval = heartbeat_interval

    @property
    def maintenance(self):
        """Gets the maintenance of this EventSettingsSettings.  # noqa: E501

        Specifies start and duration of maintenance period during which no alerts will be sent for new eventgroups.  # noqa: E501

        :return: The maintenance of this EventSettingsSettings.  # noqa: E501
        :rtype: EventSettingsSettingsMaintenance
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """Sets the maintenance of this EventSettingsSettings.

        Specifies start and duration of maintenance period during which no alerts will be sent for new eventgroups.  # noqa: E501

        :param maintenance: The maintenance of this EventSettingsSettings.  # noqa: E501
        :type: EventSettingsSettingsMaintenance
        """

        self._maintenance = maintenance

    @property
    def retention_days(self):
        """Gets the retention_days of this EventSettingsSettings.  # noqa: E501

        Retention period in days.  # noqa: E501

        :return: The retention_days of this EventSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this EventSettingsSettings.

        Retention period in days.  # noqa: E501

        :param retention_days: The retention_days of this EventSettingsSettings.  # noqa: E501
        :type: int
        """

        self._retention_days = retention_days

    @property
    def storage_limit(self):
        """Gets the storage_limit of this EventSettingsSettings.  # noqa: E501

        Storage limit in megabytes per terabyte of available storage.  # noqa: E501

        :return: The storage_limit of this EventSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._storage_limit

    @storage_limit.setter
    def storage_limit(self, storage_limit):
        """Sets the storage_limit of this EventSettingsSettings.

        Storage limit in megabytes per terabyte of available storage.  # noqa: E501

        :param storage_limit: The storage_limit of this EventSettingsSettings.  # noqa: E501
        :type: int
        """

        self._storage_limit = storage_limit

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
        if not isinstance(other, EventSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
