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


class SettingsKrb5Realm(object):
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
        'admin_server': 'str',
        'default_domain': 'str',
        'is_default_realm': 'bool',
        'kdc': 'list[str]'
    }

    attribute_map = {
        'admin_server': 'admin_server',
        'default_domain': 'default_domain',
        'is_default_realm': 'is_default_realm',
        'kdc': 'kdc'
    }

    def __init__(self, admin_server=None, default_domain=None, is_default_realm=None, kdc=None):  # noqa: E501
        """SettingsKrb5Realm - a model defined in Swagger"""  # noqa: E501

        self._admin_server = None
        self._default_domain = None
        self._is_default_realm = None
        self._kdc = None
        self.discriminator = None

        if admin_server is not None:
            self.admin_server = admin_server
        if default_domain is not None:
            self.default_domain = default_domain
        if is_default_realm is not None:
            self.is_default_realm = is_default_realm
        if kdc is not None:
            self.kdc = kdc

    @property
    def admin_server(self):
        """Gets the admin_server of this SettingsKrb5Realm.  # noqa: E501

        Specifies the administrative server hostname.  # noqa: E501

        :return: The admin_server of this SettingsKrb5Realm.  # noqa: E501
        :rtype: str
        """
        return self._admin_server

    @admin_server.setter
    def admin_server(self, admin_server):
        """Sets the admin_server of this SettingsKrb5Realm.

        Specifies the administrative server hostname.  # noqa: E501

        :param admin_server: The admin_server of this SettingsKrb5Realm.  # noqa: E501
        :type: str
        """
        if admin_server is not None and len(admin_server) > 255:
            raise ValueError("Invalid value for `admin_server`, length must be less than or equal to `255`")  # noqa: E501
        if admin_server is not None and len(admin_server) < 0:
            raise ValueError("Invalid value for `admin_server`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_server = admin_server

    @property
    def default_domain(self):
        """Gets the default_domain of this SettingsKrb5Realm.  # noqa: E501

        Specifies the default domain mapped to the realm.  # noqa: E501

        :return: The default_domain of this SettingsKrb5Realm.  # noqa: E501
        :rtype: str
        """
        return self._default_domain

    @default_domain.setter
    def default_domain(self, default_domain):
        """Sets the default_domain of this SettingsKrb5Realm.

        Specifies the default domain mapped to the realm.  # noqa: E501

        :param default_domain: The default_domain of this SettingsKrb5Realm.  # noqa: E501
        :type: str
        """
        if default_domain is not None and len(default_domain) > 255:
            raise ValueError("Invalid value for `default_domain`, length must be less than or equal to `255`")  # noqa: E501
        if default_domain is not None and len(default_domain) < 0:
            raise ValueError("Invalid value for `default_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._default_domain = default_domain

    @property
    def is_default_realm(self):
        """Gets the is_default_realm of this SettingsKrb5Realm.  # noqa: E501

        If true, indicates that the realm is the default.  # noqa: E501

        :return: The is_default_realm of this SettingsKrb5Realm.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_realm

    @is_default_realm.setter
    def is_default_realm(self, is_default_realm):
        """Sets the is_default_realm of this SettingsKrb5Realm.

        If true, indicates that the realm is the default.  # noqa: E501

        :param is_default_realm: The is_default_realm of this SettingsKrb5Realm.  # noqa: E501
        :type: bool
        """

        self._is_default_realm = is_default_realm

    @property
    def kdc(self):
        """Gets the kdc of this SettingsKrb5Realm.  # noqa: E501

        Specifies the list of KDC hostnames.  # noqa: E501

        :return: The kdc of this SettingsKrb5Realm.  # noqa: E501
        :rtype: list[str]
        """
        return self._kdc

    @kdc.setter
    def kdc(self, kdc):
        """Sets the kdc of this SettingsKrb5Realm.

        Specifies the list of KDC hostnames.  # noqa: E501

        :param kdc: The kdc of this SettingsKrb5Realm.  # noqa: E501
        :type: list[str]
        """

        self._kdc = kdc

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
        if not isinstance(other, SettingsKrb5Realm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
