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

from isi_sdk_8_2_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501


class AuthGroupObjectHistoryItem(object):
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
        'gid': 'AuthAccessAccessItemFileGroup',
        'sid': 'AuthAccessAccessItemFileGroup',
        'uid': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        'gid': 'gid',
        'sid': 'sid',
        'uid': 'uid'
    }

    def __init__(self, gid=None, sid=None, uid=None):  # noqa: E501
        """AuthGroupObjectHistoryItem - a model defined in Swagger"""  # noqa: E501

        self._gid = None
        self._sid = None
        self._uid = None
        self.discriminator = None

        if gid is not None:
            self.gid = gid
        if sid is not None:
            self.sid = sid
        if uid is not None:
            self.uid = uid

    @property
    def gid(self):
        """Gets the gid of this AuthGroupObjectHistoryItem.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The gid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthGroupObjectHistoryItem.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param gid: The gid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._gid = gid

    @property
    def sid(self):
        """Gets the sid of this AuthGroupObjectHistoryItem.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The sid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthGroupObjectHistoryItem.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param sid: The sid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._sid = sid

    @property
    def uid(self):
        """Gets the uid of this AuthGroupObjectHistoryItem.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The uid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AuthGroupObjectHistoryItem.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param uid: The uid of this AuthGroupObjectHistoryItem.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._uid = uid

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
        if not isinstance(other, AuthGroupObjectHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
