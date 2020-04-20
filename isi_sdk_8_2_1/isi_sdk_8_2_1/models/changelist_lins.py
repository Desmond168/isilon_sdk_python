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

from isi_sdk_8_2_1.models.changelist_lins_ctime import ChangelistLinsCtime  # noqa: F401,E501


class ChangelistLins(object):
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
        'atime': 'ChangelistLinsCtime',
        'ctime': 'ChangelistLinsCtime',
        'id': 'str',
        'mtime': 'ChangelistLinsCtime',
        'path': 'str',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'atime': 'atime',
        'ctime': 'ctime',
        'id': 'id',
        'mtime': 'mtime',
        'path': 'path',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, atime=None, ctime=None, id=None, mtime=None, path=None, size=None, type=None):  # noqa: E501
        """ChangelistLins - a model defined in Swagger"""  # noqa: E501

        self._atime = None
        self._ctime = None
        self._id = None
        self._mtime = None
        self._path = None
        self._size = None
        self._type = None
        self.discriminator = None

        if atime is not None:
            self.atime = atime
        if ctime is not None:
            self.ctime = ctime
        self.id = id
        if mtime is not None:
            self.mtime = mtime
        self.path = path
        self.size = size
        self.type = type

    @property
    def atime(self):
        """Gets the atime of this ChangelistLins.  # noqa: E501

          # noqa: E501

        :return: The atime of this ChangelistLins.  # noqa: E501
        :rtype: ChangelistLinsCtime
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this ChangelistLins.

          # noqa: E501

        :param atime: The atime of this ChangelistLins.  # noqa: E501
        :type: ChangelistLinsCtime
        """

        self._atime = atime

    @property
    def ctime(self):
        """Gets the ctime of this ChangelistLins.  # noqa: E501

          # noqa: E501

        :return: The ctime of this ChangelistLins.  # noqa: E501
        :rtype: ChangelistLinsCtime
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ChangelistLins.

          # noqa: E501

        :param ctime: The ctime of this ChangelistLins.  # noqa: E501
        :type: ChangelistLinsCtime
        """

        self._ctime = ctime

    @property
    def id(self):
        """Gets the id of this ChangelistLins.  # noqa: E501

        The LIN number of the file associated with the entry.  # noqa: E501

        :return: The id of this ChangelistLins.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangelistLins.

        The LIN number of the file associated with the entry.  # noqa: E501

        :param id: The id of this ChangelistLins.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def mtime(self):
        """Gets the mtime of this ChangelistLins.  # noqa: E501

          # noqa: E501

        :return: The mtime of this ChangelistLins.  # noqa: E501
        :rtype: ChangelistLinsCtime
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this ChangelistLins.

          # noqa: E501

        :param mtime: The mtime of this ChangelistLins.  # noqa: E501
        :type: ChangelistLinsCtime
        """

        self._mtime = mtime

    @property
    def path(self):
        """Gets the path of this ChangelistLins.  # noqa: E501

        The path to the file associated with the entry.  # noqa: E501

        :return: The path of this ChangelistLins.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ChangelistLins.

        The path to the file associated with the entry.  # noqa: E501

        :param path: The path of this ChangelistLins.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this ChangelistLins.  # noqa: E501

        The size of the file associated with the entry.  # noqa: E501

        :return: The size of this ChangelistLins.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ChangelistLins.

        The size of the file associated with the entry.  # noqa: E501

        :param size: The size of this ChangelistLins.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def type(self):
        """Gets the type of this ChangelistLins.  # noqa: E501

        Type of file.  # noqa: E501

        :return: The type of this ChangelistLins.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChangelistLins.

        Type of file.  # noqa: E501

        :param type: The type of this ChangelistLins.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, ChangelistLins):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
