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


class SyncRuleSchedule(object):
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
        'friday': 'bool',
        'monday': 'bool',
        'saturday': 'bool',
        'sunday': 'bool',
        'thursday': 'bool',
        'tuesday': 'bool',
        'wednesday': 'bool'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end',
        'friday': 'friday',
        'monday': 'monday',
        'saturday': 'saturday',
        'sunday': 'sunday',
        'thursday': 'thursday',
        'tuesday': 'tuesday',
        'wednesday': 'wednesday'
    }

    def __init__(self, begin=None, end=None, friday=None, monday=None, saturday=None, sunday=None, thursday=None, tuesday=None, wednesday=None):  # noqa: E501
        """SyncRuleSchedule - a model defined in Swagger"""  # noqa: E501

        self._begin = None
        self._end = None
        self._friday = None
        self._monday = None
        self._saturday = None
        self._sunday = None
        self._thursday = None
        self._tuesday = None
        self._wednesday = None
        self.discriminator = None

        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end
        if friday is not None:
            self.friday = friday
        if monday is not None:
            self.monday = monday
        if saturday is not None:
            self.saturday = saturday
        if sunday is not None:
            self.sunday = sunday
        if thursday is not None:
            self.thursday = thursday
        if tuesday is not None:
            self.tuesday = tuesday
        if wednesday is not None:
            self.wednesday = wednesday

    @property
    def begin(self):
        """Gets the begin of this SyncRuleSchedule.  # noqa: E501

        Start time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (24h format hour, and minute).  A null value indicates the beginning of the day (\"00:00\").  # noqa: E501

        :return: The begin of this SyncRuleSchedule.  # noqa: E501
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this SyncRuleSchedule.

        Start time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (24h format hour, and minute).  A null value indicates the beginning of the day (\"00:00\").  # noqa: E501

        :param begin: The begin of this SyncRuleSchedule.  # noqa: E501
        :type: str
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this SyncRuleSchedule.  # noqa: E501

        End time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (three-letter weekday name abbreviation, 24h format hour, and minute).  A null value indicates the end of the day (\"23:59\").  # noqa: E501

        :return: The end of this SyncRuleSchedule.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SyncRuleSchedule.

        End time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (three-letter weekday name abbreviation, 24h format hour, and minute).  A null value indicates the end of the day (\"23:59\").  # noqa: E501

        :param end: The end of this SyncRuleSchedule.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def friday(self):
        """Gets the friday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Friday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The friday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._friday

    @friday.setter
    def friday(self, friday):
        """Sets the friday of this SyncRuleSchedule.

        If true, this rule is in effect on Friday.  If false, or unspecified, it is not.  # noqa: E501

        :param friday: The friday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._friday = friday

    @property
    def monday(self):
        """Gets the monday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Monday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The monday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._monday

    @monday.setter
    def monday(self, monday):
        """Sets the monday of this SyncRuleSchedule.

        If true, this rule is in effect on Monday.  If false, or unspecified, it is not.  # noqa: E501

        :param monday: The monday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._monday = monday

    @property
    def saturday(self):
        """Gets the saturday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Saturday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The saturday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        """Sets the saturday of this SyncRuleSchedule.

        If true, this rule is in effect on Saturday.  If false, or unspecified, it is not.  # noqa: E501

        :param saturday: The saturday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._saturday = saturday

    @property
    def sunday(self):
        """Gets the sunday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Sunday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The sunday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        """Sets the sunday of this SyncRuleSchedule.

        If true, this rule is in effect on Sunday.  If false, or unspecified, it is not.  # noqa: E501

        :param sunday: The sunday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._sunday = sunday

    @property
    def thursday(self):
        """Gets the thursday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Thursday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The thursday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        """Sets the thursday of this SyncRuleSchedule.

        If true, this rule is in effect on Thursday.  If false, or unspecified, it is not.  # noqa: E501

        :param thursday: The thursday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._thursday = thursday

    @property
    def tuesday(self):
        """Gets the tuesday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Tuesday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The tuesday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        """Sets the tuesday of this SyncRuleSchedule.

        If true, this rule is in effect on Tuesday.  If false, or unspecified, it is not.  # noqa: E501

        :param tuesday: The tuesday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._tuesday = tuesday

    @property
    def wednesday(self):
        """Gets the wednesday of this SyncRuleSchedule.  # noqa: E501

        If true, this rule is in effect on Wednesday.  If false, or unspecified, it is not.  # noqa: E501

        :return: The wednesday of this SyncRuleSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        """Sets the wednesday of this SyncRuleSchedule.

        If true, this rule is in effect on Wednesday.  If false, or unspecified, it is not.  # noqa: E501

        :param wednesday: The wednesday of this SyncRuleSchedule.  # noqa: E501
        :type: bool
        """

        self._wednesday = wednesday

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
        if not isinstance(other, SyncRuleSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
