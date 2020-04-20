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


class AuthPrivilege(object):
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
        'category': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'read_write': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'read_write': 'read_write'
    }

    def __init__(self, category=None, description=None, id=None, name=None, read_write=None):  # noqa: E501
        """AuthPrivilege - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._description = None
        self._id = None
        self._name = None
        self._read_write = None
        self.discriminator = None

        self.category = category
        self.description = description
        self.id = id
        if name is not None:
            self.name = name
        if read_write is not None:
            self.read_write = read_write

    @property
    def category(self):
        """Gets the category of this AuthPrivilege.  # noqa: E501

        Specifies the general categorization of the privilege.  # noqa: E501

        :return: The category of this AuthPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AuthPrivilege.

        Specifies the general categorization of the privilege.  # noqa: E501

        :param category: The category of this AuthPrivilege.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def description(self):
        """Gets the description of this AuthPrivilege.  # noqa: E501

        Specifies a short description of the privilege.  # noqa: E501

        :return: The description of this AuthPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthPrivilege.

        Specifies a short description of the privilege.  # noqa: E501

        :param description: The description of this AuthPrivilege.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this AuthPrivilege.  # noqa: E501

        Specifies the ID of the privilege.  # noqa: E501

        :return: The id of this AuthPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthPrivilege.

        Specifies the ID of the privilege.  # noqa: E501

        :param id: The id of this AuthPrivilege.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthPrivilege.  # noqa: E501

        Specifies the name of the privilege.  # noqa: E501

        :return: The name of this AuthPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthPrivilege.

        Specifies the name of the privilege.  # noqa: E501

        :param name: The name of this AuthPrivilege.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def read_write(self):
        """Gets the read_write of this AuthPrivilege.  # noqa: E501

        True, if the privilege is read-write.  # noqa: E501

        :return: The read_write of this AuthPrivilege.  # noqa: E501
        :rtype: bool
        """
        return self._read_write

    @read_write.setter
    def read_write(self, read_write):
        """Sets the read_write of this AuthPrivilege.

        True, if the privilege is read-write.  # noqa: E501

        :param read_write: The read_write of this AuthPrivilege.  # noqa: E501
        :type: bool
        """

        self._read_write = read_write

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
        if not isinstance(other, AuthPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
