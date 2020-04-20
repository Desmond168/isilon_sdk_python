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


class PoolsPoolRulesRule(object):
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
        'groupnet': 'str',
        'id': 'str',
        'iface': 'str',
        'name': 'str',
        'node_type': 'str',
        'pool': 'str',
        'subnet': 'str'
    }

    attribute_map = {
        'description': 'description',
        'groupnet': 'groupnet',
        'id': 'id',
        'iface': 'iface',
        'name': 'name',
        'node_type': 'node_type',
        'pool': 'pool',
        'subnet': 'subnet'
    }

    def __init__(self, description=None, groupnet=None, id=None, iface=None, name=None, node_type=None, pool=None, subnet=None):  # noqa: E501
        """PoolsPoolRulesRule - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._groupnet = None
        self._id = None
        self._iface = None
        self._name = None
        self._node_type = None
        self._pool = None
        self._subnet = None
        self.discriminator = None

        self.description = description
        self.groupnet = groupnet
        self.id = id
        self.iface = iface
        self.name = name
        self.node_type = node_type
        self.pool = pool
        self.subnet = subnet

    @property
    def description(self):
        """Gets the description of this PoolsPoolRulesRule.  # noqa: E501

        Description for the provisioning rule.  # noqa: E501

        :return: The description of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PoolsPoolRulesRule.

        Description for the provisioning rule.  # noqa: E501

        :param description: The description of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def groupnet(self):
        """Gets the groupnet of this PoolsPoolRulesRule.  # noqa: E501

        Name of the groupnet this rule belongs to  # noqa: E501

        :return: The groupnet of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this PoolsPoolRulesRule.

        Name of the groupnet this rule belongs to  # noqa: E501

        :param groupnet: The groupnet of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if groupnet is None:
            raise ValueError("Invalid value for `groupnet`, must not be `None`")  # noqa: E501
        if groupnet is not None and len(groupnet) > 32:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `32`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 1:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def id(self):
        """Gets the id of this PoolsPoolRulesRule.  # noqa: E501

        Unique rule ID.  # noqa: E501

        :return: The id of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PoolsPoolRulesRule.

        Unique rule ID.  # noqa: E501

        :param id: The id of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 132:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `132`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def iface(self):
        """Gets the iface of this PoolsPoolRulesRule.  # noqa: E501

        Interface name the provisioning rule applies to.  # noqa: E501

        :return: The iface of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._iface

    @iface.setter
    def iface(self, iface):
        """Sets the iface of this PoolsPoolRulesRule.

        Interface name the provisioning rule applies to.  # noqa: E501

        :param iface: The iface of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if iface is None:
            raise ValueError("Invalid value for `iface`, must not be `None`")  # noqa: E501
        if iface is not None and len(iface) > 32:
            raise ValueError("Invalid value for `iface`, length must be less than or equal to `32`")  # noqa: E501
        if iface is not None and len(iface) < 1:
            raise ValueError("Invalid value for `iface`, length must be greater than or equal to `1`")  # noqa: E501

        self._iface = iface

    @property
    def name(self):
        """Gets the name of this PoolsPoolRulesRule.  # noqa: E501

        Name of the provisioning rule.  # noqa: E501

        :return: The name of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoolsPoolRulesRule.

        Name of the provisioning rule.  # noqa: E501

        :param name: The name of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[0-9a-zA-Z_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this PoolsPoolRulesRule.  # noqa: E501

        Node type the provisioning rule applies to.  # noqa: E501

        :return: The node_type of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this PoolsPoolRulesRule.

        Node type the provisioning rule applies to.  # noqa: E501

        :param node_type: The node_type of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if node_type is None:
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501
        allowed_values = ["any", "storage", "accelerator", "storage-i", "accelerator-i", "backup-accelerator"]  # noqa: E501
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def pool(self):
        """Gets the pool of this PoolsPoolRulesRule.  # noqa: E501

        Name of the pool this rule belongs to.  # noqa: E501

        :return: The pool of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this PoolsPoolRulesRule.

        Name of the pool this rule belongs to.  # noqa: E501

        :param pool: The pool of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if pool is None:
            raise ValueError("Invalid value for `pool`, must not be `None`")  # noqa: E501
        if pool is not None and len(pool) > 32:
            raise ValueError("Invalid value for `pool`, length must be less than or equal to `32`")  # noqa: E501
        if pool is not None and len(pool) < 1:
            raise ValueError("Invalid value for `pool`, length must be greater than or equal to `1`")  # noqa: E501

        self._pool = pool

    @property
    def subnet(self):
        """Gets the subnet of this PoolsPoolRulesRule.  # noqa: E501

        Name of the subnet this rule belongs to.  # noqa: E501

        :return: The subnet of this PoolsPoolRulesRule.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this PoolsPoolRulesRule.

        Name of the subnet this rule belongs to.  # noqa: E501

        :param subnet: The subnet of this PoolsPoolRulesRule.  # noqa: E501
        :type: str
        """
        if subnet is None:
            raise ValueError("Invalid value for `subnet`, must not be `None`")  # noqa: E501
        if subnet is not None and len(subnet) > 32:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `32`")  # noqa: E501
        if subnet is not None and len(subnet) < 1:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._subnet = subnet

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
        if not isinstance(other, PoolsPoolRulesRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
