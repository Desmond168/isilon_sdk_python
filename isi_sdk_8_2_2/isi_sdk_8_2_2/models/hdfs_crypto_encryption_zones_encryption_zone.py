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


class HdfsCryptoEncryptionZonesEncryptionZone(object):
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
        'id': 'str',
        'key_name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key_name': 'key_name',
        'path': 'path'
    }

    def __init__(self, id=None, key_name=None, path=None):  # noqa: E501
        """HdfsCryptoEncryptionZonesEncryptionZone - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._key_name = None
        self._path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.key_name = key_name
        if path is not None:
            self.path = path

    @property
    def id(self):
        """Gets the id of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501


        :return: The id of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HdfsCryptoEncryptionZonesEncryptionZone.


        :param id: The id of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 4096:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `4096`")  # noqa: E501
        if id is not None and len(id) < 4:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `4`")  # noqa: E501
        if id is not None and not re.search('^\/ifs|^\/ifs\/.*', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^\/ifs|^\/ifs\/.*/`")  # noqa: E501

        self._id = id

    @property
    def key_name(self):
        """Gets the key_name of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501

        The name of a key stored on the associated key management server.  # noqa: E501

        :return: The key_name of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this HdfsCryptoEncryptionZonesEncryptionZone.

        The name of a key stored on the associated key management server.  # noqa: E501

        :param key_name: The key_name of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :type: str
        """
        if key_name is None:
            raise ValueError("Invalid value for `key_name`, must not be `None`")  # noqa: E501
        if key_name is not None and len(key_name) > 960:
            raise ValueError("Invalid value for `key_name`, length must be less than or equal to `960`")  # noqa: E501
        if key_name is not None and len(key_name) < 1:
            raise ValueError("Invalid value for `key_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._key_name = key_name

    @property
    def path(self):
        """Gets the path of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501


        :return: The path of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HdfsCryptoEncryptionZonesEncryptionZone.


        :param path: The path of this HdfsCryptoEncryptionZonesEncryptionZone.  # noqa: E501
        :type: str
        """
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 4:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")  # noqa: E501
        if path is not None and not re.search('^\/ifs|^\/ifs\/.*', path):  # noqa: E501
            raise ValueError("Invalid value for `path`, must be a follow pattern or equal to `/^\/ifs|^\/ifs\/.*/`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, HdfsCryptoEncryptionZonesEncryptionZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
