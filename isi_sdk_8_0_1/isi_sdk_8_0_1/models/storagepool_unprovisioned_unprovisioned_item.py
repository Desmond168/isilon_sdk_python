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

from isi_sdk_8_0_1.models.storagepool_status_unprovisioned_item import StoragepoolStatusUnprovisionedItem  # noqa: F401,E501


class StoragepoolUnprovisionedUnprovisionedItem(object):
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
        'drives': 'list[StoragepoolStatusUnprovisionedItem]',
        'lnns': 'list[int]'
    }

    attribute_map = {
        'drives': 'drives',
        'lnns': 'lnns'
    }

    def __init__(self, drives=None, lnns=None):  # noqa: E501
        """StoragepoolUnprovisionedUnprovisionedItem - a model defined in Swagger"""  # noqa: E501

        self._drives = None
        self._lnns = None
        self.discriminator = None

        self.drives = drives
        self.lnns = lnns

    @property
    def drives(self):
        """Gets the drives of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501

        A list of unprovisioned drives that do not belong to an unprovisioned node.  # noqa: E501

        :return: The drives of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501
        :rtype: list[StoragepoolStatusUnprovisionedItem]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this StoragepoolUnprovisionedUnprovisionedItem.

        A list of unprovisioned drives that do not belong to an unprovisioned node.  # noqa: E501

        :param drives: The drives of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501
        :type: list[StoragepoolStatusUnprovisionedItem]
        """
        if drives is None:
            raise ValueError("Invalid value for `drives`, must not be `None`")  # noqa: E501

        self._drives = drives

    @property
    def lnns(self):
        """Gets the lnns of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501

        A list of lnns whose drives are all unprovisioned  # noqa: E501

        :return: The lnns of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """Sets the lnns of this StoragepoolUnprovisionedUnprovisionedItem.

        A list of lnns whose drives are all unprovisioned  # noqa: E501

        :param lnns: The lnns of this StoragepoolUnprovisionedUnprovisionedItem.  # noqa: E501
        :type: list[int]
        """
        if lnns is None:
            raise ValueError("Invalid value for `lnns`, must not be `None`")  # noqa: E501

        self._lnns = lnns

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
        if not isinstance(other, StoragepoolUnprovisionedUnprovisionedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
