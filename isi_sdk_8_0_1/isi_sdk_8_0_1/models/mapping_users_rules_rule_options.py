# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_0_1.models.mapping_users_rules_rule_user2 import MappingUsersRulesRuleUser2  # noqa: F401,E501


class MappingUsersRulesRuleOptions(object):
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
        '_break': 'bool',
        'default_user': 'MappingUsersRulesRuleUser2',
        'group': 'bool',
        'groups': 'bool',
        'user': 'bool'
    }

    attribute_map = {
        '_break': 'break',
        'default_user': 'default_user',
        'group': 'group',
        'groups': 'groups',
        'user': 'user'
    }

    def __init__(self, _break=None, default_user=None, group=None, groups=None, user=None):  # noqa: E501
        """MappingUsersRulesRuleOptions - a model defined in Swagger"""  # noqa: E501

        self.__break = None
        self._default_user = None
        self._group = None
        self._groups = None
        self._user = None
        self.discriminator = None

        if _break is not None:
            self._break = _break
        if default_user is not None:
            self.default_user = default_user
        if group is not None:
            self.group = group
        if groups is not None:
            self.groups = groups
        if user is not None:
            self.user = user

    @property
    def _break(self):
        """Gets the _break of this MappingUsersRulesRuleOptions.  # noqa: E501

        If true, and the rule was applied successfully, stop processing further.  # noqa: E501

        :return: The _break of this MappingUsersRulesRuleOptions.  # noqa: E501
        :rtype: bool
        """
        return self.__break

    @_break.setter
    def _break(self, _break):
        """Sets the _break of this MappingUsersRulesRuleOptions.

        If true, and the rule was applied successfully, stop processing further.  # noqa: E501

        :param _break: The _break of this MappingUsersRulesRuleOptions.  # noqa: E501
        :type: bool
        """

        self.__break = _break

    @property
    def default_user(self):
        """Gets the default_user of this MappingUsersRulesRuleOptions.  # noqa: E501

          # noqa: E501

        :return: The default_user of this MappingUsersRulesRuleOptions.  # noqa: E501
        :rtype: MappingUsersRulesRuleUser2
        """
        return self._default_user

    @default_user.setter
    def default_user(self, default_user):
        """Sets the default_user of this MappingUsersRulesRuleOptions.

          # noqa: E501

        :param default_user: The default_user of this MappingUsersRulesRuleOptions.  # noqa: E501
        :type: MappingUsersRulesRuleUser2
        """

        self._default_user = default_user

    @property
    def group(self):
        """Gets the group of this MappingUsersRulesRuleOptions.  # noqa: E501

        If true, the primary GID and primary group SID should be copied to the existing credential.  # noqa: E501

        :return: The group of this MappingUsersRulesRuleOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this MappingUsersRulesRuleOptions.

        If true, the primary GID and primary group SID should be copied to the existing credential.  # noqa: E501

        :param group: The group of this MappingUsersRulesRuleOptions.  # noqa: E501
        :type: bool
        """

        self._group = group

    @property
    def groups(self):
        """Gets the groups of this MappingUsersRulesRuleOptions.  # noqa: E501

        If true, all additional identifiers should be copied to the existing credential.  # noqa: E501

        :return: The groups of this MappingUsersRulesRuleOptions.  # noqa: E501
        :rtype: bool
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this MappingUsersRulesRuleOptions.

        If true, all additional identifiers should be copied to the existing credential.  # noqa: E501

        :param groups: The groups of this MappingUsersRulesRuleOptions.  # noqa: E501
        :type: bool
        """

        self._groups = groups

    @property
    def user(self):
        """Gets the user of this MappingUsersRulesRuleOptions.  # noqa: E501

        If true, the primary UID and primary user SID should be copied to the existing credential.  # noqa: E501

        :return: The user of this MappingUsersRulesRuleOptions.  # noqa: E501
        :rtype: bool
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MappingUsersRulesRuleOptions.

        If true, the primary UID and primary user SID should be copied to the existing credential.  # noqa: E501

        :param user: The user of this MappingUsersRulesRuleOptions.  # noqa: E501
        :type: bool
        """

        self._user = user

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
        if not isinstance(other, MappingUsersRulesRuleOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
