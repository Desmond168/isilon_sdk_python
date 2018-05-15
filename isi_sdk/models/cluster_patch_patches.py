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

from isi_sdk_8_1_1.models.cluster_patch_patches_patch import ClusterPatchPatchesPatch  # noqa: F401,E501


class ClusterPatchPatches(object):
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
        'patches': 'list[ClusterPatchPatchesPatch]'
    }

    attribute_map = {
        'patches': 'patches'
    }

    def __init__(self, patches=None):  # noqa: E501
        """ClusterPatchPatches - a model defined in Swagger"""  # noqa: E501

        self._patches = None
        self.discriminator = None

        if patches is not None:
            self.patches = patches

    @property
    def patches(self):
        """Gets the patches of this ClusterPatchPatches.  # noqa: E501


        :return: The patches of this ClusterPatchPatches.  # noqa: E501
        :rtype: list[ClusterPatchPatchesPatch]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this ClusterPatchPatches.


        :param patches: The patches of this ClusterPatchPatches.  # noqa: E501
        :type: list[ClusterPatchPatchesPatch]
        """

        self._patches = patches

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
        if not isinstance(other, ClusterPatchPatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
