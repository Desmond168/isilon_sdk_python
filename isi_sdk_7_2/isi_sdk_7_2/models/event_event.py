# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_7_2.models.empty import Empty  # noqa: F401,E501


class EventEvent(object):
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
        'acknowledged_time': 'int',
        'coalesced_by_id': 'str',
        'devid': 'int',
        'end': 'int',
        'event_type': 'int',
        'extreme_severity': 'str',
        'extreme_value': 'float',
        'id': 'str',
        'is_coalescing': 'int',
        'message': 'str',
        'severity': 'str',
        'specifiers': 'Empty',
        'start': 'int',
        'update_count': 'int',
        'value': 'float'
    }

    attribute_map = {
        'acknowledged_time': 'acknowledged_time',
        'coalesced_by_id': 'coalesced_by_id',
        'devid': 'devid',
        'end': 'end',
        'event_type': 'event_type',
        'extreme_severity': 'extreme_severity',
        'extreme_value': 'extreme_value',
        'id': 'id',
        'is_coalescing': 'is_coalescing',
        'message': 'message',
        'severity': 'severity',
        'specifiers': 'specifiers',
        'start': 'start',
        'update_count': 'update_count',
        'value': 'value'
    }

    def __init__(self, acknowledged_time=None, coalesced_by_id=None, devid=None, end=None, event_type=None, extreme_severity=None, extreme_value=None, id=None, is_coalescing=None, message=None, severity=None, specifiers=None, start=None, update_count=None, value=None):  # noqa: E501
        """EventEvent - a model defined in Swagger"""  # noqa: E501

        self._acknowledged_time = None
        self._coalesced_by_id = None
        self._devid = None
        self._end = None
        self._event_type = None
        self._extreme_severity = None
        self._extreme_value = None
        self._id = None
        self._is_coalescing = None
        self._message = None
        self._severity = None
        self._specifiers = None
        self._start = None
        self._update_count = None
        self._value = None
        self.discriminator = None

        if acknowledged_time is not None:
            self.acknowledged_time = acknowledged_time
        if coalesced_by_id is not None:
            self.coalesced_by_id = coalesced_by_id
        self.devid = devid
        if end is not None:
            self.end = end
        self.event_type = event_type
        self.extreme_severity = extreme_severity
        self.extreme_value = extreme_value
        self.id = id
        self.is_coalescing = is_coalescing
        self.message = message
        self.severity = severity
        self.specifiers = specifiers
        self.start = start
        if update_count is not None:
            self.update_count = update_count
        self.value = value

    @property
    def acknowledged_time(self):
        """Gets the acknowledged_time of this EventEvent.  # noqa: E501

        The time in epoch seconds at which the event was acknowledged. Set to null when event has not been acknowledged.  # noqa: E501

        :return: The acknowledged_time of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._acknowledged_time

    @acknowledged_time.setter
    def acknowledged_time(self, acknowledged_time):
        """Sets the acknowledged_time of this EventEvent.

        The time in epoch seconds at which the event was acknowledged. Set to null when event has not been acknowledged.  # noqa: E501

        :param acknowledged_time: The acknowledged_time of this EventEvent.  # noqa: E501
        :type: int
        """

        self._acknowledged_time = acknowledged_time

    @property
    def coalesced_by_id(self):
        """Gets the coalesced_by_id of this EventEvent.  # noqa: E501

        The ID of the parent event that coalesced this event. Set to null when event has not been coalesced.  # noqa: E501

        :return: The coalesced_by_id of this EventEvent.  # noqa: E501
        :rtype: str
        """
        return self._coalesced_by_id

    @coalesced_by_id.setter
    def coalesced_by_id(self, coalesced_by_id):
        """Sets the coalesced_by_id of this EventEvent.

        The ID of the parent event that coalesced this event. Set to null when event has not been coalesced.  # noqa: E501

        :param coalesced_by_id: The coalesced_by_id of this EventEvent.  # noqa: E501
        :type: str
        """

        self._coalesced_by_id = coalesced_by_id

    @property
    def devid(self):
        """Gets the devid of this EventEvent.  # noqa: E501

        The ID of the device the event refers to. When set to 0, indicates a cluster event.  # noqa: E501

        :return: The devid of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this EventEvent.

        The ID of the device the event refers to. When set to 0, indicates a cluster event.  # noqa: E501

        :param devid: The devid of this EventEvent.  # noqa: E501
        :type: int
        """
        if devid is None:
            raise ValueError("Invalid value for `devid`, must not be `None`")  # noqa: E501

        self._devid = devid

    @property
    def end(self):
        """Gets the end of this EventEvent.  # noqa: E501

        The time in epoch seconds at which the event's lifetime ended. Set to null when the event is still alive.  # noqa: E501

        :return: The end of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EventEvent.

        The time in epoch seconds at which the event's lifetime ended. Set to null when the event is still alive.  # noqa: E501

        :param end: The end of this EventEvent.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def event_type(self):
        """Gets the event_type of this EventEvent.  # noqa: E501

        A number indicating the class or type of the event.  # noqa: E501

        :return: The event_type of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventEvent.

        A number indicating the class or type of the event.  # noqa: E501

        :param event_type: The event_type of this EventEvent.  # noqa: E501
        :type: int
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def extreme_severity(self):
        """Gets the extreme_severity of this EventEvent.  # noqa: E501

        A severity assigned to events that can change severity during their lifetime.  # noqa: E501

        :return: The extreme_severity of this EventEvent.  # noqa: E501
        :rtype: str
        """
        return self._extreme_severity

    @extreme_severity.setter
    def extreme_severity(self, extreme_severity):
        """Sets the extreme_severity of this EventEvent.

        A severity assigned to events that can change severity during their lifetime.  # noqa: E501

        :param extreme_severity: The extreme_severity of this EventEvent.  # noqa: E501
        :type: str
        """
        if extreme_severity is None:
            raise ValueError("Invalid value for `extreme_severity`, must not be `None`")  # noqa: E501

        self._extreme_severity = extreme_severity

    @property
    def extreme_value(self):
        """Gets the extreme_value of this EventEvent.  # noqa: E501

        A value corresponding to extreme_severity assignment.  # noqa: E501

        :return: The extreme_value of this EventEvent.  # noqa: E501
        :rtype: float
        """
        return self._extreme_value

    @extreme_value.setter
    def extreme_value(self, extreme_value):
        """Sets the extreme_value of this EventEvent.

        A value corresponding to extreme_severity assignment.  # noqa: E501

        :param extreme_value: The extreme_value of this EventEvent.  # noqa: E501
        :type: float
        """
        if extreme_value is None:
            raise ValueError("Invalid value for `extreme_value`, must not be `None`")  # noqa: E501

        self._extreme_value = extreme_value

    @property
    def id(self):
        """Gets the id of this EventEvent.  # noqa: E501

        A unique (across all event_types and instances) identifier for an event.  # noqa: E501

        :return: The id of this EventEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventEvent.

        A unique (across all event_types and instances) identifier for an event.  # noqa: E501

        :param id: The id of this EventEvent.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_coalescing(self):
        """Gets the is_coalescing of this EventEvent.  # noqa: E501

        If non-zero this field represents the coalescer type.  # noqa: E501

        :return: The is_coalescing of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._is_coalescing

    @is_coalescing.setter
    def is_coalescing(self, is_coalescing):
        """Sets the is_coalescing of this EventEvent.

        If non-zero this field represents the coalescer type.  # noqa: E501

        :param is_coalescing: The is_coalescing of this EventEvent.  # noqa: E501
        :type: int
        """
        if is_coalescing is None:
            raise ValueError("Invalid value for `is_coalescing`, must not be `None`")  # noqa: E501

        self._is_coalescing = is_coalescing

    @property
    def message(self):
        """Gets the message of this EventEvent.  # noqa: E501

        A message containing information about the event.  # noqa: E501

        :return: The message of this EventEvent.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EventEvent.

        A message containing information about the event.  # noqa: E501

        :param message: The message of this EventEvent.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def severity(self):
        """Gets the severity of this EventEvent.  # noqa: E501

        The current severity of the event.  # noqa: E501

        :return: The severity of this EventEvent.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventEvent.

        The current severity of the event.  # noqa: E501

        :param severity: The severity of this EventEvent.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def specifiers(self):
        """Gets the specifiers of this EventEvent.  # noqa: E501

        Key-value pairs containing information specific to this event.  # noqa: E501

        :return: The specifiers of this EventEvent.  # noqa: E501
        :rtype: Empty
        """
        return self._specifiers

    @specifiers.setter
    def specifiers(self, specifiers):
        """Sets the specifiers of this EventEvent.

        Key-value pairs containing information specific to this event.  # noqa: E501

        :param specifiers: The specifiers of this EventEvent.  # noqa: E501
        :type: Empty
        """
        if specifiers is None:
            raise ValueError("Invalid value for `specifiers`, must not be `None`")  # noqa: E501

        self._specifiers = specifiers

    @property
    def start(self):
        """Gets the start of this EventEvent.  # noqa: E501

        The time in epoch seconds at which the event's lifetime begins.  # noqa: E501

        :return: The start of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventEvent.

        The time in epoch seconds at which the event's lifetime begins.  # noqa: E501

        :param start: The start of this EventEvent.  # noqa: E501
        :type: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def update_count(self):
        """Gets the update_count of this EventEvent.  # noqa: E501

        The number of times (some parameter of) the event was updated during its lifetime.  # noqa: E501

        :return: The update_count of this EventEvent.  # noqa: E501
        :rtype: int
        """
        return self._update_count

    @update_count.setter
    def update_count(self, update_count):
        """Sets the update_count of this EventEvent.

        The number of times (some parameter of) the event was updated during its lifetime.  # noqa: E501

        :param update_count: The update_count of this EventEvent.  # noqa: E501
        :type: int
        """

        self._update_count = update_count

    @property
    def value(self):
        """Gets the value of this EventEvent.  # noqa: E501

        A value associated with the event.  # noqa: E501

        :return: The value of this EventEvent.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventEvent.

        A value associated with the event.  # noqa: E501

        :param value: The value of this EventEvent.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EventEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
