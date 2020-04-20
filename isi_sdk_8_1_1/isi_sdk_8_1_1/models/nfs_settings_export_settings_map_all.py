# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_1_1.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isi_sdk_8_1_1.models.nfs_settings_export_settings_map_all_secondary_groups import NfsSettingsExportSettingsMapAllSecondaryGroups  # noqa: F401,E501


class NfsSettingsExportSettingsMapAll(object):
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
        'enabled': 'bool',
        'primary_group': 'AuthAccessAccessItemFileGroup',
        'secondary_groups': 'list[NfsSettingsExportSettingsMapAllSecondaryGroups]',
        'user': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        'enabled': 'enabled',
        'primary_group': 'primary_group',
        'secondary_groups': 'secondary_groups',
        'user': 'user'
    }

    def __init__(self, enabled=None, primary_group=None, secondary_groups=None, user=None):  # noqa: E501
        """NfsSettingsExportSettingsMapAll - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._primary_group = None
        self._secondary_groups = None
        self._user = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if primary_group is not None:
            self.primary_group = primary_group
        if secondary_groups is not None:
            self.secondary_groups = secondary_groups
        if user is not None:
            self.user = user

    @property
    def enabled(self):
        """Gets the enabled of this NfsSettingsExportSettingsMapAll.  # noqa: E501

        True if the user mapping is applied.  # noqa: E501

        :return: The enabled of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NfsSettingsExportSettingsMapAll.

        True if the user mapping is applied.  # noqa: E501

        :param enabled: The enabled of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def primary_group(self):
        """Gets the primary_group of this NfsSettingsExportSettingsMapAll.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The primary_group of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._primary_group

    @primary_group.setter
    def primary_group(self, primary_group):
        """Sets the primary_group of this NfsSettingsExportSettingsMapAll.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param primary_group: The primary_group of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._primary_group = primary_group

    @property
    def secondary_groups(self):
        """Gets the secondary_groups of this NfsSettingsExportSettingsMapAll.  # noqa: E501

        Specifies persona properties for the secondary user group. A persona consists of either a type and name, or an ID.  # noqa: E501

        :return: The secondary_groups of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :rtype: list[NfsSettingsExportSettingsMapAllSecondaryGroups]
        """
        return self._secondary_groups

    @secondary_groups.setter
    def secondary_groups(self, secondary_groups):
        """Sets the secondary_groups of this NfsSettingsExportSettingsMapAll.

        Specifies persona properties for the secondary user group. A persona consists of either a type and name, or an ID.  # noqa: E501

        :param secondary_groups: The secondary_groups of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :type: list[NfsSettingsExportSettingsMapAllSecondaryGroups]
        """

        self._secondary_groups = secondary_groups

    @property
    def user(self):
        """Gets the user of this NfsSettingsExportSettingsMapAll.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The user of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this NfsSettingsExportSettingsMapAll.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param user: The user of this NfsSettingsExportSettingsMapAll.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
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
        if not isinstance(other, NfsSettingsExportSettingsMapAll):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
