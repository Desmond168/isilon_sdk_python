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
from isi_sdk_8_1_1.models.mapping_identities_target import MappingIdentitiesTarget  # noqa: F401,E501


class MappingIdentitiesCreateParams(object):
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
        'source': 'AuthAccessAccessItemFileGroup',
        'targets': 'list[MappingIdentitiesTarget]'
    }

    attribute_map = {
        'source': 'source',
        'targets': 'targets'
    }

    def __init__(self, source=None, targets=None):  # noqa: E501
        """MappingIdentitiesCreateParams - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._targets = None
        self.discriminator = None

        self.source = source
        self.targets = targets

    @property
    def source(self):
        """Gets the source of this MappingIdentitiesCreateParams.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The source of this MappingIdentitiesCreateParams.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MappingIdentitiesCreateParams.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param source: The source of this MappingIdentitiesCreateParams.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def targets(self):
        """Gets the targets of this MappingIdentitiesCreateParams.  # noqa: E501


        :return: The targets of this MappingIdentitiesCreateParams.  # noqa: E501
        :rtype: list[MappingIdentitiesTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this MappingIdentitiesCreateParams.


        :param targets: The targets of this MappingIdentitiesCreateParams.  # noqa: E501
        :type: list[MappingIdentitiesTarget]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

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
        if not isinstance(other, MappingIdentitiesCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
