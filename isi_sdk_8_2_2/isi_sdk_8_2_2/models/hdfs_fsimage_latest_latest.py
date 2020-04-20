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


class HdfsFsimageLatestLatest(object):
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
        'created': 'int',
        'size': 'int',
        'txid': 'int'
    }

    attribute_map = {
        'created': 'created',
        'size': 'size',
        'txid': 'txid'
    }

    def __init__(self, created=None, size=None, txid=None):  # noqa: E501
        """HdfsFsimageLatestLatest - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._size = None
        self._txid = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if size is not None:
            self.size = size
        if txid is not None:
            self.txid = txid

    @property
    def created(self):
        """Gets the created of this HdfsFsimageLatestLatest.  # noqa: E501

        The date and time FSImage was created as a UNIX epoch.  # noqa: E501

        :return: The created of this HdfsFsimageLatestLatest.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this HdfsFsimageLatestLatest.

        The date and time FSImage was created as a UNIX epoch.  # noqa: E501

        :param created: The created of this HdfsFsimageLatestLatest.  # noqa: E501
        :type: int
        """
        if created is not None and created > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `created`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if created is not None and created < 0:  # noqa: E501
            raise ValueError("Invalid value for `created`, must be a value greater than or equal to `0`")  # noqa: E501

        self._created = created

    @property
    def size(self):
        """Gets the size of this HdfsFsimageLatestLatest.  # noqa: E501

        Size of the FSImage in bytes. If null, FSImage is not present.  # noqa: E501

        :return: The size of this HdfsFsimageLatestLatest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this HdfsFsimageLatestLatest.

        Size of the FSImage in bytes. If null, FSImage is not present.  # noqa: E501

        :param size: The size of this HdfsFsimageLatestLatest.  # noqa: E501
        :type: int
        """
        if size is not None and size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def txid(self):
        """Gets the txid of this HdfsFsimageLatestLatest.  # noqa: E501

        The transaction id of the latest HDFS FSImage. If null, FSImage is not present.  # noqa: E501

        :return: The txid of this HdfsFsimageLatestLatest.  # noqa: E501
        :rtype: int
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this HdfsFsimageLatestLatest.

        The transaction id of the latest HDFS FSImage. If null, FSImage is not present.  # noqa: E501

        :param txid: The txid of this HdfsFsimageLatestLatest.  # noqa: E501
        :type: int
        """
        if txid is not None and txid > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `txid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if txid is not None and txid < 0:  # noqa: E501
            raise ValueError("Invalid value for `txid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._txid = txid

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
        if not isinstance(other, HdfsFsimageLatestLatest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
