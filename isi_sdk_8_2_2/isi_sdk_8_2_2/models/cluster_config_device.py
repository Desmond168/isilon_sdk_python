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


class ClusterConfigDevice(object):
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
        'devid': 'int',
        'guid': 'str',
        'is_up': 'bool',
        'lnn': 'int'
    }

    attribute_map = {
        'devid': 'devid',
        'guid': 'guid',
        'is_up': 'is_up',
        'lnn': 'lnn'
    }

    def __init__(self, devid=None, guid=None, is_up=None, lnn=None):  # noqa: E501
        """ClusterConfigDevice - a model defined in Swagger"""  # noqa: E501

        self._devid = None
        self._guid = None
        self._is_up = None
        self._lnn = None
        self.discriminator = None

        self.devid = devid
        self.guid = guid
        self.is_up = is_up
        self.lnn = lnn

    @property
    def devid(self):
        """Gets the devid of this ClusterConfigDevice.  # noqa: E501

        Device ID.  # noqa: E501

        :return: The devid of this ClusterConfigDevice.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this ClusterConfigDevice.

        Device ID.  # noqa: E501

        :param devid: The devid of this ClusterConfigDevice.  # noqa: E501
        :type: int
        """
        if devid is None:
            raise ValueError("Invalid value for `devid`, must not be `None`")  # noqa: E501

        self._devid = devid

    @property
    def guid(self):
        """Gets the guid of this ClusterConfigDevice.  # noqa: E501

        Device GUID.  # noqa: E501

        :return: The guid of this ClusterConfigDevice.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ClusterConfigDevice.

        Device GUID.  # noqa: E501

        :param guid: The guid of this ClusterConfigDevice.  # noqa: E501
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def is_up(self):
        """Gets the is_up of this ClusterConfigDevice.  # noqa: E501

        If true, this node is online and communicating with the local node and every other node with the is_up property normally.  If false, this node is not currently communicating with the local node or other nodes with the is_up property.  It may be shut down, rebooting, disconnected from the backend network, or connected only to other nodes.  # noqa: E501

        :return: The is_up of this ClusterConfigDevice.  # noqa: E501
        :rtype: bool
        """
        return self._is_up

    @is_up.setter
    def is_up(self, is_up):
        """Sets the is_up of this ClusterConfigDevice.

        If true, this node is online and communicating with the local node and every other node with the is_up property normally.  If false, this node is not currently communicating with the local node or other nodes with the is_up property.  It may be shut down, rebooting, disconnected from the backend network, or connected only to other nodes.  # noqa: E501

        :param is_up: The is_up of this ClusterConfigDevice.  # noqa: E501
        :type: bool
        """
        if is_up is None:
            raise ValueError("Invalid value for `is_up`, must not be `None`")  # noqa: E501

        self._is_up = is_up

    @property
    def lnn(self):
        """Gets the lnn of this ClusterConfigDevice.  # noqa: E501

        Device logical node number.  # noqa: E501

        :return: The lnn of this ClusterConfigDevice.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ClusterConfigDevice.

        Device logical node number.  # noqa: E501

        :param lnn: The lnn of this ClusterConfigDevice.  # noqa: E501
        :type: int
        """
        if lnn is None:
            raise ValueError("Invalid value for `lnn`, must not be `None`")  # noqa: E501

        self._lnn = lnn

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
        if not isinstance(other, ClusterConfigDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
