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


class QuotaQuotasSummarySummary(object):
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
        'count': 'int',
        'default_group_quotas_count': 'int',
        'default_user_quotas_count': 'int',
        'directory_quotas_count': 'int',
        'group_quotas_count': 'int',
        'linked_quotas_count': 'int',
        'user_quotas_count': 'int'
    }

    attribute_map = {
        'count': 'count',
        'default_group_quotas_count': 'default_group_quotas_count',
        'default_user_quotas_count': 'default_user_quotas_count',
        'directory_quotas_count': 'directory_quotas_count',
        'group_quotas_count': 'group_quotas_count',
        'linked_quotas_count': 'linked_quotas_count',
        'user_quotas_count': 'user_quotas_count'
    }

    def __init__(self, count=None, default_group_quotas_count=None, default_user_quotas_count=None, directory_quotas_count=None, group_quotas_count=None, linked_quotas_count=None, user_quotas_count=None):  # noqa: E501
        """QuotaQuotasSummarySummary - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._default_group_quotas_count = None
        self._default_user_quotas_count = None
        self._directory_quotas_count = None
        self._group_quotas_count = None
        self._linked_quotas_count = None
        self._user_quotas_count = None
        self.discriminator = None

        self.count = count
        self.default_group_quotas_count = default_group_quotas_count
        self.default_user_quotas_count = default_user_quotas_count
        self.directory_quotas_count = directory_quotas_count
        self.group_quotas_count = group_quotas_count
        self.linked_quotas_count = linked_quotas_count
        self.user_quotas_count = user_quotas_count

    @property
    def count(self):
        """Gets the count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of quotas.  # noqa: E501

        :return: The count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this QuotaQuotasSummarySummary.

        Total number of quotas.  # noqa: E501

        :param count: The count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def default_group_quotas_count(self):
        """Gets the default_group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of default-group quotas.  # noqa: E501

        :return: The default_group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._default_group_quotas_count

    @default_group_quotas_count.setter
    def default_group_quotas_count(self, default_group_quotas_count):
        """Sets the default_group_quotas_count of this QuotaQuotasSummarySummary.

        Total number of default-group quotas.  # noqa: E501

        :param default_group_quotas_count: The default_group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if default_group_quotas_count is None:
            raise ValueError("Invalid value for `default_group_quotas_count`, must not be `None`")  # noqa: E501

        self._default_group_quotas_count = default_group_quotas_count

    @property
    def default_user_quotas_count(self):
        """Gets the default_user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of default-user quotas.  # noqa: E501

        :return: The default_user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._default_user_quotas_count

    @default_user_quotas_count.setter
    def default_user_quotas_count(self, default_user_quotas_count):
        """Sets the default_user_quotas_count of this QuotaQuotasSummarySummary.

        Total number of default-user quotas.  # noqa: E501

        :param default_user_quotas_count: The default_user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if default_user_quotas_count is None:
            raise ValueError("Invalid value for `default_user_quotas_count`, must not be `None`")  # noqa: E501

        self._default_user_quotas_count = default_user_quotas_count

    @property
    def directory_quotas_count(self):
        """Gets the directory_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of directory quotas.  # noqa: E501

        :return: The directory_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._directory_quotas_count

    @directory_quotas_count.setter
    def directory_quotas_count(self, directory_quotas_count):
        """Sets the directory_quotas_count of this QuotaQuotasSummarySummary.

        Total number of directory quotas.  # noqa: E501

        :param directory_quotas_count: The directory_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if directory_quotas_count is None:
            raise ValueError("Invalid value for `directory_quotas_count`, must not be `None`")  # noqa: E501

        self._directory_quotas_count = directory_quotas_count

    @property
    def group_quotas_count(self):
        """Gets the group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of -group quotas.  # noqa: E501

        :return: The group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._group_quotas_count

    @group_quotas_count.setter
    def group_quotas_count(self, group_quotas_count):
        """Sets the group_quotas_count of this QuotaQuotasSummarySummary.

        Total number of -group quotas.  # noqa: E501

        :param group_quotas_count: The group_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if group_quotas_count is None:
            raise ValueError("Invalid value for `group_quotas_count`, must not be `None`")  # noqa: E501

        self._group_quotas_count = group_quotas_count

    @property
    def linked_quotas_count(self):
        """Gets the linked_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of user and group totals that are linked.  # noqa: E501

        :return: The linked_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._linked_quotas_count

    @linked_quotas_count.setter
    def linked_quotas_count(self, linked_quotas_count):
        """Sets the linked_quotas_count of this QuotaQuotasSummarySummary.

        Total number of user and group totals that are linked.  # noqa: E501

        :param linked_quotas_count: The linked_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if linked_quotas_count is None:
            raise ValueError("Invalid value for `linked_quotas_count`, must not be `None`")  # noqa: E501

        self._linked_quotas_count = linked_quotas_count

    @property
    def user_quotas_count(self):
        """Gets the user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501

        Total number of user quotas.  # noqa: E501

        :return: The user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._user_quotas_count

    @user_quotas_count.setter
    def user_quotas_count(self, user_quotas_count):
        """Sets the user_quotas_count of this QuotaQuotasSummarySummary.

        Total number of user quotas.  # noqa: E501

        :param user_quotas_count: The user_quotas_count of this QuotaQuotasSummarySummary.  # noqa: E501
        :type: int
        """
        if user_quotas_count is None:
            raise ValueError("Invalid value for `user_quotas_count`, must not be `None`")  # noqa: E501

        self._user_quotas_count = user_quotas_count

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
        if not isinstance(other, QuotaQuotasSummarySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
