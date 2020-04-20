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

from isi_sdk_8_2_0.models.empty import Empty  # noqa: F401,E501


class EventEventlistEvent(object):
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
        'devid': 'int',
        'ended': 'float',
        'event': 'int',
        'id': 'str',
        'lnn': 'int',
        'message': 'str',
        'resolve_time': 'int',
        'severity': 'str',
        'specifier': 'Empty',
        'time': 'int',
        'value': 'float'
    }

    attribute_map = {
        'devid': 'devid',
        'ended': 'ended',
        'event': 'event',
        'id': 'id',
        'lnn': 'lnn',
        'message': 'message',
        'resolve_time': 'resolve_time',
        'severity': 'severity',
        'specifier': 'specifier',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, devid=None, ended=None, event=None, id=None, lnn=None, message=None, resolve_time=None, severity=None, specifier=None, time=None, value=None):  # noqa: E501
        """EventEventlistEvent - a model defined in Swagger"""  # noqa: E501

        self._devid = None
        self._ended = None
        self._event = None
        self._id = None
        self._lnn = None
        self._message = None
        self._resolve_time = None
        self._severity = None
        self._specifier = None
        self._time = None
        self._value = None
        self.discriminator = None

        if devid is not None:
            self.devid = devid
        if ended is not None:
            self.ended = ended
        if event is not None:
            self.event = event
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if message is not None:
            self.message = message
        if resolve_time is not None:
            self.resolve_time = resolve_time
        if severity is not None:
            self.severity = severity
        if specifier is not None:
            self.specifier = specifier
        if time is not None:
            self.time = time
        if value is not None:
            self.value = value

    @property
    def devid(self):
        """Gets the devid of this EventEventlistEvent.  # noqa: E501

        The device id of the node if it is still part of the cluster otherwise None.  # noqa: E501

        :return: The devid of this EventEventlistEvent.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this EventEventlistEvent.

        The device id of the node if it is still part of the cluster otherwise None.  # noqa: E501

        :param devid: The devid of this EventEventlistEvent.  # noqa: E501
        :type: int
        """
        if devid is not None and devid > 65435:  # noqa: E501
            raise ValueError("Invalid value for `devid`, must be a value less than or equal to `65435`")  # noqa: E501
        if devid is not None and devid < 0:  # noqa: E501
            raise ValueError("Invalid value for `devid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._devid = devid

    @property
    def ended(self):
        """Gets the ended of this EventEventlistEvent.  # noqa: E501

        Time event was ended (eventgroup resolved).  # noqa: E501

        :return: The ended of this EventEventlistEvent.  # noqa: E501
        :rtype: float
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this EventEventlistEvent.

        Time event was ended (eventgroup resolved).  # noqa: E501

        :param ended: The ended of this EventEventlistEvent.  # noqa: E501
        :type: float
        """
        if ended is not None and ended > 18446744073709551615:  # noqa: E501
            raise ValueError("Invalid value for `ended`, must be a value less than or equal to `18446744073709551615`")  # noqa: E501
        if ended is not None and ended < 0:  # noqa: E501
            raise ValueError("Invalid value for `ended`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ended = ended

    @property
    def event(self):
        """Gets the event of this EventEventlistEvent.  # noqa: E501

        Integer identifier of the event type.  # noqa: E501

        :return: The event of this EventEventlistEvent.  # noqa: E501
        :rtype: int
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this EventEventlistEvent.

        Integer identifier of the event type.  # noqa: E501

        :param event: The event of this EventEventlistEvent.  # noqa: E501
        :type: int
        """
        if event is not None and event > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `event`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if event is not None and event < 0:  # noqa: E501
            raise ValueError("Invalid value for `event`, must be a value greater than or equal to `0`")  # noqa: E501

        self._event = event

    @property
    def id(self):
        """Gets the id of this EventEventlistEvent.  # noqa: E501

        Unique identifier of event occurrence.  # noqa: E501

        :return: The id of this EventEventlistEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventEventlistEvent.

        Unique identifier of event occurrence.  # noqa: E501

        :param id: The id of this EventEventlistEvent.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this EventEventlistEvent.  # noqa: E501

        The lnn of the node if it is still part of the cluster, otherwise None.  # noqa: E501

        :return: The lnn of this EventEventlistEvent.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this EventEventlistEvent.

        The lnn of the node if it is still part of the cluster, otherwise None.  # noqa: E501

        :param lnn: The lnn of this EventEventlistEvent.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65435:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65435`")  # noqa: E501
        if lnn is not None and lnn < 0:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lnn = lnn

    @property
    def message(self):
        """Gets the message of this EventEventlistEvent.  # noqa: E501

        Human readable description.  # noqa: E501

        :return: The message of this EventEventlistEvent.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EventEventlistEvent.

        Human readable description.  # noqa: E501

        :param message: The message of this EventEventlistEvent.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) > 8192:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `8192`")  # noqa: E501
        if message is not None and len(message) < 0:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")  # noqa: E501

        self._message = message

    @property
    def resolve_time(self):
        """Gets the resolve_time of this EventEventlistEvent.  # noqa: E501

        Time the event was resolved.  # noqa: E501

        :return: The resolve_time of this EventEventlistEvent.  # noqa: E501
        :rtype: int
        """
        return self._resolve_time

    @resolve_time.setter
    def resolve_time(self, resolve_time):
        """Sets the resolve_time of this EventEventlistEvent.

        Time the event was resolved.  # noqa: E501

        :param resolve_time: The resolve_time of this EventEventlistEvent.  # noqa: E501
        :type: int
        """
        if resolve_time is not None and resolve_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `resolve_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if resolve_time is not None and resolve_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `resolve_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._resolve_time = resolve_time

    @property
    def severity(self):
        """Gets the severity of this EventEventlistEvent.  # noqa: E501

        Severity of event occurrence.  # noqa: E501

        :return: The severity of this EventEventlistEvent.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventEventlistEvent.

        Severity of event occurrence.  # noqa: E501

        :param severity: The severity of this EventEventlistEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["information", "warning", "critical", "emergency", "unknown"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def specifier(self):
        """Gets the specifier of this EventEventlistEvent.  # noqa: E501

        A collection of parameters defined per event.  # noqa: E501

        :return: The specifier of this EventEventlistEvent.  # noqa: E501
        :rtype: Empty
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier):
        """Sets the specifier of this EventEventlistEvent.

        A collection of parameters defined per event.  # noqa: E501

        :param specifier: The specifier of this EventEventlistEvent.  # noqa: E501
        :type: Empty
        """

        self._specifier = specifier

    @property
    def time(self):
        """Gets the time of this EventEventlistEvent.  # noqa: E501

        Time event was detected as UNIX timestamp.  # noqa: E501

        :return: The time of this EventEventlistEvent.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EventEventlistEvent.

        Time event was detected as UNIX timestamp.  # noqa: E501

        :param time: The time of this EventEventlistEvent.  # noqa: E501
        :type: int
        """
        if time is not None and time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if time is not None and time < 0:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def value(self):
        """Gets the value of this EventEventlistEvent.  # noqa: E501

        Value of measurement associated with this event.  # noqa: E501

        :return: The value of this EventEventlistEvent.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventEventlistEvent.

        Value of measurement associated with this event.  # noqa: E501

        :param value: The value of this EventEventlistEvent.  # noqa: E501
        :type: float
        """
        if value is not None and value > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if value is not None and value < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

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
        if not isinstance(other, EventEventlistEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
