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

from isi_sdk_8_2_2.models.license_license_tier_entitlements_exceeded_alert import LicenseLicenseTierEntitlementsExceededAlert  # noqa: F401,E501


class LicenseLicenseTier(object):
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
        'entitlements_exceeded_alerts': 'list[LicenseLicenseTierEntitlementsExceededAlert]',
        'licensed_drive_capacity': 'int',
        'licensed_node_count': 'int',
        'licensed_nodes_with_seds_count': 'int',
        'tier': 'str',
        'used_drive_capacity': 'int',
        'used_node_count': 'int',
        'used_nodes_with_seds_count': 'int'
    }

    attribute_map = {
        'entitlements_exceeded_alerts': 'entitlements_exceeded_alerts',
        'licensed_drive_capacity': 'licensed_drive_capacity',
        'licensed_node_count': 'licensed_node_count',
        'licensed_nodes_with_seds_count': 'licensed_nodes_with_seds_count',
        'tier': 'tier',
        'used_drive_capacity': 'used_drive_capacity',
        'used_node_count': 'used_node_count',
        'used_nodes_with_seds_count': 'used_nodes_with_seds_count'
    }

    def __init__(self, entitlements_exceeded_alerts=None, licensed_drive_capacity=None, licensed_node_count=None, licensed_nodes_with_seds_count=None, tier=None, used_drive_capacity=None, used_node_count=None, used_nodes_with_seds_count=None):  # noqa: E501
        """LicenseLicenseTier - a model defined in Swagger"""  # noqa: E501

        self._entitlements_exceeded_alerts = None
        self._licensed_drive_capacity = None
        self._licensed_node_count = None
        self._licensed_nodes_with_seds_count = None
        self._tier = None
        self._used_drive_capacity = None
        self._used_node_count = None
        self._used_nodes_with_seds_count = None
        self.discriminator = None

        if entitlements_exceeded_alerts is not None:
            self.entitlements_exceeded_alerts = entitlements_exceeded_alerts
        if licensed_drive_capacity is not None:
            self.licensed_drive_capacity = licensed_drive_capacity
        if licensed_node_count is not None:
            self.licensed_node_count = licensed_node_count
        if licensed_nodes_with_seds_count is not None:
            self.licensed_nodes_with_seds_count = licensed_nodes_with_seds_count
        if tier is not None:
            self.tier = tier
        if used_drive_capacity is not None:
            self.used_drive_capacity = used_drive_capacity
        if used_node_count is not None:
            self.used_node_count = used_node_count
        if used_nodes_with_seds_count is not None:
            self.used_nodes_with_seds_count = used_nodes_with_seds_count

    @property
    def entitlements_exceeded_alerts(self):
        """Gets the entitlements_exceeded_alerts of this LicenseLicenseTier.  # noqa: E501

        List of alerts about exceeded entitlements: The following alerts appear when usage of a resource such as a node, an encryption node, or storage capacity exceeds the quantity licensed for that resource.  # noqa: E501

        :return: The entitlements_exceeded_alerts of this LicenseLicenseTier.  # noqa: E501
        :rtype: list[LicenseLicenseTierEntitlementsExceededAlert]
        """
        return self._entitlements_exceeded_alerts

    @entitlements_exceeded_alerts.setter
    def entitlements_exceeded_alerts(self, entitlements_exceeded_alerts):
        """Sets the entitlements_exceeded_alerts of this LicenseLicenseTier.

        List of alerts about exceeded entitlements: The following alerts appear when usage of a resource such as a node, an encryption node, or storage capacity exceeds the quantity licensed for that resource.  # noqa: E501

        :param entitlements_exceeded_alerts: The entitlements_exceeded_alerts of this LicenseLicenseTier.  # noqa: E501
        :type: list[LicenseLicenseTierEntitlementsExceededAlert]
        """

        self._entitlements_exceeded_alerts = entitlements_exceeded_alerts

    @property
    def licensed_drive_capacity(self):
        """Gets the licensed_drive_capacity of this LicenseLicenseTier.  # noqa: E501

        Licensed terabyte (TB, 10^12 bytes) drive capacity allocated as storage associated with tier. Included if tier is not NONINF and license is not a base only license.  # noqa: E501

        :return: The licensed_drive_capacity of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._licensed_drive_capacity

    @licensed_drive_capacity.setter
    def licensed_drive_capacity(self, licensed_drive_capacity):
        """Sets the licensed_drive_capacity of this LicenseLicenseTier.

        Licensed terabyte (TB, 10^12 bytes) drive capacity allocated as storage associated with tier. Included if tier is not NONINF and license is not a base only license.  # noqa: E501

        :param licensed_drive_capacity: The licensed_drive_capacity of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if licensed_drive_capacity is not None and licensed_drive_capacity > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `licensed_drive_capacity`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if licensed_drive_capacity is not None and licensed_drive_capacity < 0:  # noqa: E501
            raise ValueError("Invalid value for `licensed_drive_capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._licensed_drive_capacity = licensed_drive_capacity

    @property
    def licensed_node_count(self):
        """Gets the licensed_node_count of this LicenseLicenseTier.  # noqa: E501

        Licensed number of nodes in this tier.  # noqa: E501

        :return: The licensed_node_count of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._licensed_node_count

    @licensed_node_count.setter
    def licensed_node_count(self, licensed_node_count):
        """Sets the licensed_node_count of this LicenseLicenseTier.

        Licensed number of nodes in this tier.  # noqa: E501

        :param licensed_node_count: The licensed_node_count of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if licensed_node_count is not None and licensed_node_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `licensed_node_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if licensed_node_count is not None and licensed_node_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `licensed_node_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._licensed_node_count = licensed_node_count

    @property
    def licensed_nodes_with_seds_count(self):
        """Gets the licensed_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501

        Licensed number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and tier is not NONINF.  # noqa: E501

        :return: The licensed_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._licensed_nodes_with_seds_count

    @licensed_nodes_with_seds_count.setter
    def licensed_nodes_with_seds_count(self, licensed_nodes_with_seds_count):
        """Sets the licensed_nodes_with_seds_count of this LicenseLicenseTier.

        Licensed number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and tier is not NONINF.  # noqa: E501

        :param licensed_nodes_with_seds_count: The licensed_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if licensed_nodes_with_seds_count is not None and licensed_nodes_with_seds_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `licensed_nodes_with_seds_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if licensed_nodes_with_seds_count is not None and licensed_nodes_with_seds_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `licensed_nodes_with_seds_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._licensed_nodes_with_seds_count = licensed_nodes_with_seds_count

    @property
    def tier(self):
        """Gets the tier of this LicenseLicenseTier.  # noqa: E501

        OneFS hardware tier. Tier is a number, NONINF, or NO_TIER. NONINF indicates a non infinity tier. NO_TIER indicates a license that is not tier based.  # noqa: E501

        :return: The tier of this LicenseLicenseTier.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this LicenseLicenseTier.

        OneFS hardware tier. Tier is a number, NONINF, or NO_TIER. NONINF indicates a non infinity tier. NO_TIER indicates a license that is not tier based.  # noqa: E501

        :param tier: The tier of this LicenseLicenseTier.  # noqa: E501
        :type: str
        """
        if tier is not None and len(tier) > 50:
            raise ValueError("Invalid value for `tier`, length must be less than or equal to `50`")  # noqa: E501
        if tier is not None and len(tier) < 1:
            raise ValueError("Invalid value for `tier`, length must be greater than or equal to `1`")  # noqa: E501
        if tier is not None and not re.search('^NONINF$|^NO_TIER$|^\\d+$', tier):  # noqa: E501
            raise ValueError("Invalid value for `tier`, must be a follow pattern or equal to `/^NONINF$|^NO_TIER$|^\\d+$/`")  # noqa: E501

        self._tier = tier

    @property
    def used_drive_capacity(self):
        """Gets the used_drive_capacity of this LicenseLicenseTier.  # noqa: E501

        Actual terabyte (TB, 10^12 bytes) drive capacity allocated as storage space associated with tier. Included if tier is not NONINF and license is not a base only license.  # noqa: E501

        :return: The used_drive_capacity of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._used_drive_capacity

    @used_drive_capacity.setter
    def used_drive_capacity(self, used_drive_capacity):
        """Sets the used_drive_capacity of this LicenseLicenseTier.

        Actual terabyte (TB, 10^12 bytes) drive capacity allocated as storage space associated with tier. Included if tier is not NONINF and license is not a base only license.  # noqa: E501

        :param used_drive_capacity: The used_drive_capacity of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if used_drive_capacity is not None and used_drive_capacity > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `used_drive_capacity`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if used_drive_capacity is not None and used_drive_capacity < 0:  # noqa: E501
            raise ValueError("Invalid value for `used_drive_capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._used_drive_capacity = used_drive_capacity

    @property
    def used_node_count(self):
        """Gets the used_node_count of this LicenseLicenseTier.  # noqa: E501

        Actual number of nodes in this tier.  # noqa: E501

        :return: The used_node_count of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._used_node_count

    @used_node_count.setter
    def used_node_count(self, used_node_count):
        """Sets the used_node_count of this LicenseLicenseTier.

        Actual number of nodes in this tier.  # noqa: E501

        :param used_node_count: The used_node_count of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if used_node_count is not None and used_node_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `used_node_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if used_node_count is not None and used_node_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `used_node_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._used_node_count = used_node_count

    @property
    def used_nodes_with_seds_count(self):
        """Gets the used_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501

        Actual number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and if tier is not NONINF.  # noqa: E501

        :return: The used_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501
        :rtype: int
        """
        return self._used_nodes_with_seds_count

    @used_nodes_with_seds_count.setter
    def used_nodes_with_seds_count(self, used_nodes_with_seds_count):
        """Sets the used_nodes_with_seds_count of this LicenseLicenseTier.

        Actual number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and if tier is not NONINF.  # noqa: E501

        :param used_nodes_with_seds_count: The used_nodes_with_seds_count of this LicenseLicenseTier.  # noqa: E501
        :type: int
        """
        if used_nodes_with_seds_count is not None and used_nodes_with_seds_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `used_nodes_with_seds_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if used_nodes_with_seds_count is not None and used_nodes_with_seds_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `used_nodes_with_seds_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._used_nodes_with_seds_count = used_nodes_with_seds_count

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
        if not isinstance(other, LicenseLicenseTier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
