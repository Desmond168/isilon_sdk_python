# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnapshotRepstates(object):
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
        'snap1': 'int',
        'snap2': 'int'
    }

    attribute_map = {
        'id': 'id',
        'snap1': 'snap1',
        'snap2': 'snap2'
    }

    def __init__(self, id=None, snap1=None, snap2=None):  # noqa: E501
        """SnapshotRepstates - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._snap1 = None
        self._snap2 = None
        self.discriminator = None

        self.id = id
        self.snap1 = snap1
        self.snap2 = snap2

    @property
    def id(self):
        """Gets the id of this SnapshotRepstates.  # noqa: E501

        The system ID given to the repstate.  # noqa: E501

        :return: The id of this SnapshotRepstates.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotRepstates.

        The system ID given to the repstate.  # noqa: E501

        :param id: The id of this SnapshotRepstates.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def snap1(self):
        """Gets the snap1 of this SnapshotRepstates.  # noqa: E501

        The lower snapid used to compute the repstate.  # noqa: E501

        :return: The snap1 of this SnapshotRepstates.  # noqa: E501
        :rtype: int
        """
        return self._snap1

    @snap1.setter
    def snap1(self, snap1):
        """Sets the snap1 of this SnapshotRepstates.

        The lower snapid used to compute the repstate.  # noqa: E501

        :param snap1: The snap1 of this SnapshotRepstates.  # noqa: E501
        :type: int
        """
        if snap1 is None:
            raise ValueError("Invalid value for `snap1`, must not be `None`")  # noqa: E501

        self._snap1 = snap1

    @property
    def snap2(self):
        """Gets the snap2 of this SnapshotRepstates.  # noqa: E501

        The higher snapid used to compute the repstate.  # noqa: E501

        :return: The snap2 of this SnapshotRepstates.  # noqa: E501
        :rtype: int
        """
        return self._snap2

    @snap2.setter
    def snap2(self, snap2):
        """Sets the snap2 of this SnapshotRepstates.

        The higher snapid used to compute the repstate.  # noqa: E501

        :param snap2: The snap2 of this SnapshotRepstates.  # noqa: E501
        :type: int
        """
        if snap2 is None:
            raise ValueError("Invalid value for `snap2`, must not be `None`")  # noqa: E501

        self._snap2 = snap2

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
        if not isinstance(other, SnapshotRepstates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
