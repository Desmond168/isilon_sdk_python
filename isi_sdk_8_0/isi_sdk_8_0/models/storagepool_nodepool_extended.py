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

from isi_sdk_8_0.models.storagepool_tier_usage import StoragepoolTierUsage  # noqa: F401,E501


class StoragepoolNodepoolExtended(object):
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
        'can_enable_l3': 'bool',
        'health_flags': 'list[str]',
        'id': 'int',
        'l3': 'bool',
        'l3_status': 'str',
        'lnns': 'list[int]',
        'manual': 'bool',
        'name': 'str',
        'protection_policy': 'str',
        'tier': 'str',
        'usage': 'StoragepoolTierUsage'
    }

    attribute_map = {
        'can_enable_l3': 'can_enable_l3',
        'health_flags': 'health_flags',
        'id': 'id',
        'l3': 'l3',
        'l3_status': 'l3_status',
        'lnns': 'lnns',
        'manual': 'manual',
        'name': 'name',
        'protection_policy': 'protection_policy',
        'tier': 'tier',
        'usage': 'usage'
    }

    def __init__(self, can_enable_l3=None, health_flags=None, id=None, l3=None, l3_status=None, lnns=None, manual=None, name=None, protection_policy=None, tier=None, usage=None):  # noqa: E501
        """StoragepoolNodepoolExtended - a model defined in Swagger"""  # noqa: E501

        self._can_enable_l3 = None
        self._health_flags = None
        self._id = None
        self._l3 = None
        self._l3_status = None
        self._lnns = None
        self._manual = None
        self._name = None
        self._protection_policy = None
        self._tier = None
        self._usage = None
        self.discriminator = None

        self.can_enable_l3 = can_enable_l3
        if health_flags is not None:
            self.health_flags = health_flags
        self.id = id
        self.l3 = l3
        self.l3_status = l3_status
        self.lnns = lnns
        self.manual = manual
        self.name = name
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if tier is not None:
            self.tier = tier
        self.usage = usage

    @property
    def can_enable_l3(self):
        """Gets the can_enable_l3 of this StoragepoolNodepoolExtended.  # noqa: E501

        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.  # noqa: E501

        :return: The can_enable_l3 of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: bool
        """
        return self._can_enable_l3

    @can_enable_l3.setter
    def can_enable_l3(self, can_enable_l3):
        """Sets the can_enable_l3 of this StoragepoolNodepoolExtended.

        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.  # noqa: E501

        :param can_enable_l3: The can_enable_l3 of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: bool
        """
        if can_enable_l3 is None:
            raise ValueError("Invalid value for `can_enable_l3`, must not be `None`")  # noqa: E501

        self._can_enable_l3 = can_enable_l3

    @property
    def health_flags(self):
        """Gets the health_flags of this StoragepoolNodepoolExtended.  # noqa: E501

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  # noqa: E501

        :return: The health_flags of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._health_flags

    @health_flags.setter
    def health_flags(self, health_flags):
        """Sets the health_flags of this StoragepoolNodepoolExtended.

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  # noqa: E501

        :param health_flags: The health_flags of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["underprovisioned", "missing_drives", "devices_down", "devices_smartfailed", "waiting_repair"]  # noqa: E501
        if not set(health_flags).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `health_flags` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(health_flags) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._health_flags = health_flags

    @property
    def id(self):
        """Gets the id of this StoragepoolNodepoolExtended.  # noqa: E501

        The system ID given to the node pool.  # noqa: E501

        :return: The id of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoragepoolNodepoolExtended.

        The system ID given to the node pool.  # noqa: E501

        :param id: The id of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def l3(self):
        """Gets the l3 of this StoragepoolNodepoolExtended.  # noqa: E501

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :return: The l3 of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this StoragepoolNodepoolExtended.

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :param l3: The l3 of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: bool
        """
        if l3 is None:
            raise ValueError("Invalid value for `l3`, must not be `None`")  # noqa: E501

        self._l3 = l3

    @property
    def l3_status(self):
        """Gets the l3_status of this StoragepoolNodepoolExtended.  # noqa: E501

        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.  # noqa: E501

        :return: The l3_status of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._l3_status

    @l3_status.setter
    def l3_status(self, l3_status):
        """Sets the l3_status of this StoragepoolNodepoolExtended.

        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.  # noqa: E501

        :param l3_status: The l3_status of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: str
        """
        if l3_status is None:
            raise ValueError("Invalid value for `l3_status`, must not be `None`")  # noqa: E501
        allowed_values = ["l3", "storage", "migrating"]  # noqa: E501
        if l3_status not in allowed_values:
            raise ValueError(
                "Invalid value for `l3_status` ({0}), must be one of {1}"  # noqa: E501
                .format(l3_status, allowed_values)
            )

        self._l3_status = l3_status

    @property
    def lnns(self):
        """Gets the lnns of this StoragepoolNodepoolExtended.  # noqa: E501

        The nodes that are part of this node pool.  # noqa: E501

        :return: The lnns of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """Sets the lnns of this StoragepoolNodepoolExtended.

        The nodes that are part of this node pool.  # noqa: E501

        :param lnns: The lnns of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: list[int]
        """
        if lnns is None:
            raise ValueError("Invalid value for `lnns`, must not be `None`")  # noqa: E501

        self._lnns = lnns

    @property
    def manual(self):
        """Gets the manual of this StoragepoolNodepoolExtended.  # noqa: E501

        Whether or not the node pool is manually managed.  # noqa: E501

        :return: The manual of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this StoragepoolNodepoolExtended.

        Whether or not the node pool is manually managed.  # noqa: E501

        :param manual: The manual of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: bool
        """
        if manual is None:
            raise ValueError("Invalid value for `manual`, must not be `None`")  # noqa: E501

        self._manual = manual

    @property
    def name(self):
        """Gets the name of this StoragepoolNodepoolExtended.  # noqa: E501

        The node pool name.  # noqa: E501

        :return: The name of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoragepoolNodepoolExtended.

        The node pool name.  # noqa: E501

        :param name: The name of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protection_policy(self):
        """Gets the protection_policy of this StoragepoolNodepoolExtended.  # noqa: E501

        The underlying protection policy.  # noqa: E501

        :return: The protection_policy of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this StoragepoolNodepoolExtended.

        The underlying protection policy.  # noqa: E501

        :param protection_policy: The protection_policy of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: str
        """

        self._protection_policy = protection_policy

    @property
    def tier(self):
        """Gets the tier of this StoragepoolNodepoolExtended.  # noqa: E501

        The name (if named) or system ID of the node pool's tier, if it is in a tier. Otherwise null.  # noqa: E501

        :return: The tier of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this StoragepoolNodepoolExtended.

        The name (if named) or system ID of the node pool's tier, if it is in a tier. Otherwise null.  # noqa: E501

        :param tier: The tier of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def usage(self):
        """Gets the usage of this StoragepoolNodepoolExtended.  # noqa: E501

        Total pool usage.  # noqa: E501

        :return: The usage of this StoragepoolNodepoolExtended.  # noqa: E501
        :rtype: StoragepoolTierUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this StoragepoolNodepoolExtended.

        Total pool usage.  # noqa: E501

        :param usage: The usage of this StoragepoolNodepoolExtended.  # noqa: E501
        :type: StoragepoolTierUsage
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

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
        if not isinstance(other, StoragepoolNodepoolExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
