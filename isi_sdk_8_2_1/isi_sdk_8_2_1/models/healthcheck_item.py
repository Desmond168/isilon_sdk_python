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

from isi_sdk_8_2_1.models.healthcheck_item_parameter import HealthcheckItemParameter  # noqa: F401,E501


class HealthcheckItem(object):
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
        'freshness': 'int',
        'id': 'str',
        'node': 'bool',
        'parameters': 'list[HealthcheckItemParameter]',
        'reference': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'description': 'description',
        'freshness': 'freshness',
        'id': 'id',
        'node': 'node',
        'parameters': 'parameters',
        'reference': 'reference',
        'summary': 'summary'
    }

    def __init__(self, description=None, freshness=None, id=None, node=None, parameters=None, reference=None, summary=None):  # noqa: E501
        """HealthcheckItem - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._freshness = None
        self._id = None
        self._node = None
        self._parameters = None
        self._reference = None
        self._summary = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if freshness is not None:
            self.freshness = freshness
        if id is not None:
            self.id = id
        if node is not None:
            self.node = node
        if parameters is not None:
            self.parameters = parameters
        if reference is not None:
            self.reference = reference
        if summary is not None:
            self.summary = summary

    @property
    def description(self):
        """Gets the description of this HealthcheckItem.  # noqa: E501

        Optional extended description of item  # noqa: E501

        :return: The description of this HealthcheckItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HealthcheckItem.

        Optional extended description of item  # noqa: E501

        :param description: The description of this HealthcheckItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def freshness(self):
        """Gets the freshness of this HealthcheckItem.  # noqa: E501

        Maximum age in seconds of acceptable earlier results  # noqa: E501

        :return: The freshness of this HealthcheckItem.  # noqa: E501
        :rtype: int
        """
        return self._freshness

    @freshness.setter
    def freshness(self, freshness):
        """Sets the freshness of this HealthcheckItem.

        Maximum age in seconds of acceptable earlier results  # noqa: E501

        :param freshness: The freshness of this HealthcheckItem.  # noqa: E501
        :type: int
        """
        if freshness is not None and freshness < 0:  # noqa: E501
            raise ValueError("Invalid value for `freshness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._freshness = freshness

    @property
    def id(self):
        """Gets the id of this HealthcheckItem.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this HealthcheckItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckItem.

        Unique identifier  # noqa: E501

        :param id: The id of this HealthcheckItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def node(self):
        """Gets the node of this HealthcheckItem.  # noqa: E501

        True if this item is to be evaluated on each node  # noqa: E501

        :return: The node of this HealthcheckItem.  # noqa: E501
        :rtype: bool
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this HealthcheckItem.

        True if this item is to be evaluated on each node  # noqa: E501

        :param node: The node of this HealthcheckItem.  # noqa: E501
        :type: bool
        """

        self._node = node

    @property
    def parameters(self):
        """Gets the parameters of this HealthcheckItem.  # noqa: E501

        Accepted and required parameters  # noqa: E501

        :return: The parameters of this HealthcheckItem.  # noqa: E501
        :rtype: list[HealthcheckItemParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this HealthcheckItem.

        Accepted and required parameters  # noqa: E501

        :param parameters: The parameters of this HealthcheckItem.  # noqa: E501
        :type: list[HealthcheckItemParameter]
        """

        self._parameters = parameters

    @property
    def reference(self):
        """Gets the reference of this HealthcheckItem.  # noqa: E501

        KB URL or similar reference link  # noqa: E501

        :return: The reference of this HealthcheckItem.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this HealthcheckItem.

        KB URL or similar reference link  # noqa: E501

        :param reference: The reference of this HealthcheckItem.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def summary(self):
        """Gets the summary of this HealthcheckItem.  # noqa: E501

        Brief description of item  # noqa: E501

        :return: The summary of this HealthcheckItem.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this HealthcheckItem.

        Brief description of item  # noqa: E501

        :param summary: The summary of this HealthcheckItem.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if not isinstance(other, HealthcheckItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
