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


class NfsSettingsZoneSettings(object):
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
        'nfsv4_allow_numeric_ids': 'bool',
        'nfsv4_domain': 'str',
        'nfsv4_no_domain': 'bool',
        'nfsv4_no_domain_uids': 'bool',
        'nfsv4_no_names': 'bool',
        'nfsv4_replace_domain': 'bool',
        'zone': 'str'
    }

    attribute_map = {
        'nfsv4_allow_numeric_ids': 'nfsv4_allow_numeric_ids',
        'nfsv4_domain': 'nfsv4_domain',
        'nfsv4_no_domain': 'nfsv4_no_domain',
        'nfsv4_no_domain_uids': 'nfsv4_no_domain_uids',
        'nfsv4_no_names': 'nfsv4_no_names',
        'nfsv4_replace_domain': 'nfsv4_replace_domain',
        'zone': 'zone'
    }

    def __init__(self, nfsv4_allow_numeric_ids=None, nfsv4_domain=None, nfsv4_no_domain=None, nfsv4_no_domain_uids=None, nfsv4_no_names=None, nfsv4_replace_domain=None, zone=None):  # noqa: E501
        """NfsSettingsZoneSettings - a model defined in Swagger"""  # noqa: E501

        self._nfsv4_allow_numeric_ids = None
        self._nfsv4_domain = None
        self._nfsv4_no_domain = None
        self._nfsv4_no_domain_uids = None
        self._nfsv4_no_names = None
        self._nfsv4_replace_domain = None
        self._zone = None
        self.discriminator = None

        if nfsv4_allow_numeric_ids is not None:
            self.nfsv4_allow_numeric_ids = nfsv4_allow_numeric_ids
        if nfsv4_domain is not None:
            self.nfsv4_domain = nfsv4_domain
        if nfsv4_no_domain is not None:
            self.nfsv4_no_domain = nfsv4_no_domain
        if nfsv4_no_domain_uids is not None:
            self.nfsv4_no_domain_uids = nfsv4_no_domain_uids
        if nfsv4_no_names is not None:
            self.nfsv4_no_names = nfsv4_no_names
        if nfsv4_replace_domain is not None:
            self.nfsv4_replace_domain = nfsv4_replace_domain
        if zone is not None:
            self.zone = zone

    @property
    def nfsv4_allow_numeric_ids(self):
        """Gets the nfsv4_allow_numeric_ids of this NfsSettingsZoneSettings.  # noqa: E501

        If true, sends owners and groups as UIDs and GIDs when look up fails or if the 'nfsv4_no_name' property is set to 1.  # noqa: E501

        :return: The nfsv4_allow_numeric_ids of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_allow_numeric_ids

    @nfsv4_allow_numeric_ids.setter
    def nfsv4_allow_numeric_ids(self, nfsv4_allow_numeric_ids):
        """Sets the nfsv4_allow_numeric_ids of this NfsSettingsZoneSettings.

        If true, sends owners and groups as UIDs and GIDs when look up fails or if the 'nfsv4_no_name' property is set to 1.  # noqa: E501

        :param nfsv4_allow_numeric_ids: The nfsv4_allow_numeric_ids of this NfsSettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_allow_numeric_ids = nfsv4_allow_numeric_ids

    @property
    def nfsv4_domain(self):
        """Gets the nfsv4_domain of this NfsSettingsZoneSettings.  # noqa: E501

        Specifies the domain or realm through which users and groups are associated.  # noqa: E501

        :return: The nfsv4_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: str
        """
        return self._nfsv4_domain

    @nfsv4_domain.setter
    def nfsv4_domain(self, nfsv4_domain):
        """Sets the nfsv4_domain of this NfsSettingsZoneSettings.

        Specifies the domain or realm through which users and groups are associated.  # noqa: E501

        :param nfsv4_domain: The nfsv4_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :type: str
        """

        self._nfsv4_domain = nfsv4_domain

    @property
    def nfsv4_no_domain(self):
        """Gets the nfsv4_no_domain of this NfsSettingsZoneSettings.  # noqa: E501

        If true, sends owners and groups without a domain name.  # noqa: E501

        :return: The nfsv4_no_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_no_domain

    @nfsv4_no_domain.setter
    def nfsv4_no_domain(self, nfsv4_no_domain):
        """Sets the nfsv4_no_domain of this NfsSettingsZoneSettings.

        If true, sends owners and groups without a domain name.  # noqa: E501

        :param nfsv4_no_domain: The nfsv4_no_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_no_domain = nfsv4_no_domain

    @property
    def nfsv4_no_domain_uids(self):
        """Gets the nfsv4_no_domain_uids of this NfsSettingsZoneSettings.  # noqa: E501

        If true, sends UIDs and GIDs without a domain name.  # noqa: E501

        :return: The nfsv4_no_domain_uids of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_no_domain_uids

    @nfsv4_no_domain_uids.setter
    def nfsv4_no_domain_uids(self, nfsv4_no_domain_uids):
        """Sets the nfsv4_no_domain_uids of this NfsSettingsZoneSettings.

        If true, sends UIDs and GIDs without a domain name.  # noqa: E501

        :param nfsv4_no_domain_uids: The nfsv4_no_domain_uids of this NfsSettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_no_domain_uids = nfsv4_no_domain_uids

    @property
    def nfsv4_no_names(self):
        """Gets the nfsv4_no_names of this NfsSettingsZoneSettings.  # noqa: E501

        If true, sends owners and groups as UIDs and GIDs.  # noqa: E501

        :return: The nfsv4_no_names of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_no_names

    @nfsv4_no_names.setter
    def nfsv4_no_names(self, nfsv4_no_names):
        """Sets the nfsv4_no_names of this NfsSettingsZoneSettings.

        If true, sends owners and groups as UIDs and GIDs.  # noqa: E501

        :param nfsv4_no_names: The nfsv4_no_names of this NfsSettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_no_names = nfsv4_no_names

    @property
    def nfsv4_replace_domain(self):
        """Gets the nfsv4_replace_domain of this NfsSettingsZoneSettings.  # noqa: E501

        If true, replaces the owner or group domain with an NFS domain name.  # noqa: E501

        :return: The nfsv4_replace_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfsv4_replace_domain

    @nfsv4_replace_domain.setter
    def nfsv4_replace_domain(self, nfsv4_replace_domain):
        """Sets the nfsv4_replace_domain of this NfsSettingsZoneSettings.

        If true, replaces the owner or group domain with an NFS domain name.  # noqa: E501

        :param nfsv4_replace_domain: The nfsv4_replace_domain of this NfsSettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._nfsv4_replace_domain = nfsv4_replace_domain

    @property
    def zone(self):
        """Gets the zone of this NfsSettingsZoneSettings.  # noqa: E501

        Specifies the access zones in which these settings apply.  # noqa: E501

        :return: The zone of this NfsSettingsZoneSettings.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this NfsSettingsZoneSettings.

        Specifies the access zones in which these settings apply.  # noqa: E501

        :param zone: The zone of this NfsSettingsZoneSettings.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if not isinstance(other, NfsSettingsZoneSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
