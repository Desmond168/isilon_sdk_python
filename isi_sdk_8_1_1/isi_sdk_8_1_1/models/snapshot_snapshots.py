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

from isi_sdk_8_1_1.models.snapshot_snapshot_extended import SnapshotSnapshotExtended  # noqa: F401,E501


class SnapshotSnapshots(object):
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
        'snapshots': 'list[SnapshotSnapshotExtended]'
    }

    attribute_map = {
        'snapshots': 'snapshots'
    }

    def __init__(self, snapshots=None):  # noqa: E501
        """SnapshotSnapshots - a model defined in Swagger"""  # noqa: E501

        self._snapshots = None
        self.discriminator = None

        if snapshots is not None:
            self.snapshots = snapshots

    @property
    def snapshots(self):
        """Gets the snapshots of this SnapshotSnapshots.  # noqa: E501


        :return: The snapshots of this SnapshotSnapshots.  # noqa: E501
        :rtype: list[SnapshotSnapshotExtended]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this SnapshotSnapshots.


        :param snapshots: The snapshots of this SnapshotSnapshots.  # noqa: E501
        :type: list[SnapshotSnapshotExtended]
        """

        self._snapshots = snapshots

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
        if not isinstance(other, SnapshotSnapshots):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
