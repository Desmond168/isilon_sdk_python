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

from isi_sdk_8_2_2.models.empty import Empty  # noqa: F401,E501


class EventEventgroupOccurrencesEventgroup(object):
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
        'causes': 'list[list[str]]',
        'channels': 'list[str]',
        'event_count': 'int',
        'eventgroup_instance': 'str',
        'id': 'str',
        'ignore': 'bool',
        'ignore_time': 'int',
        'last_event': 'int',
        'resolve_time': 'int',
        'resolved': 'bool',
        'resolver': 'str',
        'sequence': 'int',
        'severity': 'str',
        'specifier': 'Empty',
        'time_noticed': 'int'
    }

    attribute_map = {
        'causes': 'causes',
        'channels': 'channels',
        'event_count': 'event_count',
        'eventgroup_instance': 'eventgroup_instance',
        'id': 'id',
        'ignore': 'ignore',
        'ignore_time': 'ignore_time',
        'last_event': 'last_event',
        'resolve_time': 'resolve_time',
        'resolved': 'resolved',
        'resolver': 'resolver',
        'sequence': 'sequence',
        'severity': 'severity',
        'specifier': 'specifier',
        'time_noticed': 'time_noticed'
    }

    def __init__(self, causes=None, channels=None, event_count=None, eventgroup_instance=None, id=None, ignore=None, ignore_time=None, last_event=None, resolve_time=None, resolved=None, resolver=None, sequence=None, severity=None, specifier=None, time_noticed=None):  # noqa: E501
        """EventEventgroupOccurrencesEventgroup - a model defined in Swagger"""  # noqa: E501

        self._causes = None
        self._channels = None
        self._event_count = None
        self._eventgroup_instance = None
        self._id = None
        self._ignore = None
        self._ignore_time = None
        self._last_event = None
        self._resolve_time = None
        self._resolved = None
        self._resolver = None
        self._sequence = None
        self._severity = None
        self._specifier = None
        self._time_noticed = None
        self.discriminator = None

        if causes is not None:
            self.causes = causes
        if channels is not None:
            self.channels = channels
        if event_count is not None:
            self.event_count = event_count
        if eventgroup_instance is not None:
            self.eventgroup_instance = eventgroup_instance
        if id is not None:
            self.id = id
        if ignore is not None:
            self.ignore = ignore
        if ignore_time is not None:
            self.ignore_time = ignore_time
        if last_event is not None:
            self.last_event = last_event
        if resolve_time is not None:
            self.resolve_time = resolve_time
        if resolved is not None:
            self.resolved = resolved
        if resolver is not None:
            self.resolver = resolver
        if sequence is not None:
            self.sequence = sequence
        if severity is not None:
            self.severity = severity
        if specifier is not None:
            self.specifier = specifier
        if time_noticed is not None:
            self.time_noticed = time_noticed

    @property
    def causes(self):
        """Gets the causes of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        List of eventgroup IDs that may be causes of this occurrence.  # noqa: E501

        :return: The causes of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """Sets the causes of this EventEventgroupOccurrencesEventgroup.

        List of eventgroup IDs that may be causes of this occurrence.  # noqa: E501

        :param causes: The causes of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: list[list[str]]
        """

        self._causes = causes

    @property
    def channels(self):
        """Gets the channels of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        List of channels to which alerts are configured for this eventgroup.  # noqa: E501

        :return: The channels of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this EventEventgroupOccurrencesEventgroup.

        List of channels to which alerts are configured for this eventgroup.  # noqa: E501

        :param channels: The channels of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: list[str]
        """

        self._channels = channels

    @property
    def event_count(self):
        """Gets the event_count of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Number of events linked to this eventgroup.  # noqa: E501

        :return: The event_count of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """Sets the event_count of this EventEventgroupOccurrencesEventgroup.

        Number of events linked to this eventgroup.  # noqa: E501

        :param event_count: The event_count of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._event_count = event_count

    @property
    def eventgroup_instance(self):
        """Gets the eventgroup_instance of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Unique identifier of eventgroup instance.  # noqa: E501

        :return: The eventgroup_instance of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: str
        """
        return self._eventgroup_instance

    @eventgroup_instance.setter
    def eventgroup_instance(self, eventgroup_instance):
        """Sets the eventgroup_instance of this EventEventgroupOccurrencesEventgroup.

        Unique identifier of eventgroup instance.  # noqa: E501

        :param eventgroup_instance: The eventgroup_instance of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: str
        """

        self._eventgroup_instance = eventgroup_instance

    @property
    def id(self):
        """Gets the id of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Same as eventgroup_instance.  # noqa: E501

        :return: The id of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventEventgroupOccurrencesEventgroup.

        Same as eventgroup_instance.  # noqa: E501

        :param id: The id of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ignore(self):
        """Gets the ignore of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        True if eventgroup is marked as 'ignore'.  # noqa: E501

        :return: The ignore of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: bool
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """Sets the ignore of this EventEventgroupOccurrencesEventgroup.

        True if eventgroup is marked as 'ignore'.  # noqa: E501

        :param ignore: The ignore of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: bool
        """

        self._ignore = ignore

    @property
    def ignore_time(self):
        """Gets the ignore_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Time eventgroup was marked as 'ignore'.  # noqa: E501

        :return: The ignore_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._ignore_time

    @ignore_time.setter
    def ignore_time(self, ignore_time):
        """Sets the ignore_time of this EventEventgroupOccurrencesEventgroup.

        Time eventgroup was marked as 'ignore'.  # noqa: E501

        :param ignore_time: The ignore_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._ignore_time = ignore_time

    @property
    def last_event(self):
        """Gets the last_event of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Time the most recent event was added to this eventgroup.  # noqa: E501

        :return: The last_event of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._last_event

    @last_event.setter
    def last_event(self, last_event):
        """Sets the last_event of this EventEventgroupOccurrencesEventgroup.

        Time the most recent event was added to this eventgroup.  # noqa: E501

        :param last_event: The last_event of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._last_event = last_event

    @property
    def resolve_time(self):
        """Gets the resolve_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        When the eventgroup became resolved.  # noqa: E501

        :return: The resolve_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._resolve_time

    @resolve_time.setter
    def resolve_time(self, resolve_time):
        """Sets the resolve_time of this EventEventgroupOccurrencesEventgroup.

        When the eventgroup became resolved.  # noqa: E501

        :param resolve_time: The resolve_time of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._resolve_time = resolve_time

    @property
    def resolved(self):
        """Gets the resolved of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        True if eventgroup is resolved.  # noqa: E501

        :return: The resolved of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this EventEventgroupOccurrencesEventgroup.

        True if eventgroup is resolved.  # noqa: E501

        :param resolved: The resolved of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: bool
        """

        self._resolved = resolved

    @property
    def resolver(self):
        """Gets the resolver of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        'USER' if the eventgroup was marked resolved by the user. '<event_instance>' if eventgroup was marked resolved as a result of an event.  # noqa: E501

        :return: The resolver of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: str
        """
        return self._resolver

    @resolver.setter
    def resolver(self, resolver):
        """Sets the resolver of this EventEventgroupOccurrencesEventgroup.

        'USER' if the eventgroup was marked resolved by the user. '<event_instance>' if eventgroup was marked resolved as a result of an event.  # noqa: E501

        :param resolver: The resolver of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: str
        """

        self._resolver = resolver

    @property
    def sequence(self):
        """Gets the sequence of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Unique sequence number assigned to the eventgroup, by order of creation.  # noqa: E501

        :return: The sequence of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this EventEventgroupOccurrencesEventgroup.

        Unique sequence number assigned to the eventgroup, by order of creation.  # noqa: E501

        :param sequence: The sequence of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def severity(self):
        """Gets the severity of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Event Group severity.  # noqa: E501

        :return: The severity of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventEventgroupOccurrencesEventgroup.

        Event Group severity.  # noqa: E501

        :param severity: The severity of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def specifier(self):
        """Gets the specifier of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        A collection of parameters defined per eventgroup_id.  # noqa: E501

        :return: The specifier of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: Empty
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier):
        """Sets the specifier of this EventEventgroupOccurrencesEventgroup.

        A collection of parameters defined per eventgroup_id.  # noqa: E501

        :param specifier: The specifier of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: Empty
        """

        self._specifier = specifier

    @property
    def time_noticed(self):
        """Gets the time_noticed of this EventEventgroupOccurrencesEventgroup.  # noqa: E501

        Time of first event linked to this eventgroup.  # noqa: E501

        :return: The time_noticed of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :rtype: int
        """
        return self._time_noticed

    @time_noticed.setter
    def time_noticed(self, time_noticed):
        """Sets the time_noticed of this EventEventgroupOccurrencesEventgroup.

        Time of first event linked to this eventgroup.  # noqa: E501

        :param time_noticed: The time_noticed of this EventEventgroupOccurrencesEventgroup.  # noqa: E501
        :type: int
        """

        self._time_noticed = time_noticed

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
        if not isinstance(other, EventEventgroupOccurrencesEventgroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
