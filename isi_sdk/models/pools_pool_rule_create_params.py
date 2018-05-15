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


class PoolsPoolRuleCreateParams(object):
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
        'description': 'str',
        'iface': 'str',
        'name': 'str',
        'node_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'iface': 'iface',
        'name': 'name',
        'node_type': 'node_type'
    }

    def __init__(self, description=None, iface=None, name=None, node_type=None):  # noqa: E501
        """PoolsPoolRuleCreateParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._iface = None
        self._name = None
        self._node_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.iface = iface
        self.name = name
        if node_type is not None:
            self.node_type = node_type

    @property
    def description(self):
        """Gets the description of this PoolsPoolRuleCreateParams.  # noqa: E501

        Description for the provisioning rule.  # noqa: E501

        :return: The description of this PoolsPoolRuleCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PoolsPoolRuleCreateParams.

        Description for the provisioning rule.  # noqa: E501

        :param description: The description of this PoolsPoolRuleCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501

        self._description = description

    @property
    def iface(self):
        """Gets the iface of this PoolsPoolRuleCreateParams.  # noqa: E501

        Interface name the provisioning rule applies to.  # noqa: E501

        :return: The iface of this PoolsPoolRuleCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._iface

    @iface.setter
    def iface(self, iface):
        """Sets the iface of this PoolsPoolRuleCreateParams.

        Interface name the provisioning rule applies to.  # noqa: E501

        :param iface: The iface of this PoolsPoolRuleCreateParams.  # noqa: E501
        :type: str
        """
        if iface is None:
            raise ValueError("Invalid value for `iface`, must not be `None`")  # noqa: E501

        self._iface = iface

    @property
    def name(self):
        """Gets the name of this PoolsPoolRuleCreateParams.  # noqa: E501

        Name of the provisioning rule.  # noqa: E501

        :return: The name of this PoolsPoolRuleCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoolsPoolRuleCreateParams.

        Name of the provisioning rule.  # noqa: E501

        :param name: The name of this PoolsPoolRuleCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501

        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this PoolsPoolRuleCreateParams.  # noqa: E501

        Node type the provisioning rule applies to.  # noqa: E501

        :return: The node_type of this PoolsPoolRuleCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this PoolsPoolRuleCreateParams.

        Node type the provisioning rule applies to.  # noqa: E501

        :param node_type: The node_type of this PoolsPoolRuleCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["any", "storage", "accelerator", "storage-i", "accelerator-i", "backup-accelerator"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

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
        if not isinstance(other, PoolsPoolRuleCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
