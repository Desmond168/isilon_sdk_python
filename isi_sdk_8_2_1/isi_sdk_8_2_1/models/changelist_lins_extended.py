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

from isi_sdk_8_2_1.models.changelist_lins import ChangelistLins  # noqa: F401,E501


class ChangelistLinsExtended(object):
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
        'lins': 'list[ChangelistLins]',
        'resume': 'str',
        'total': 'int'
    }

    attribute_map = {
        'lins': 'lins',
        'resume': 'resume',
        'total': 'total'
    }

    def __init__(self, lins=None, resume=None, total=None):  # noqa: E501
        """ChangelistLinsExtended - a model defined in Swagger"""  # noqa: E501

        self._lins = None
        self._resume = None
        self._total = None
        self.discriminator = None

        if lins is not None:
            self.lins = lins
        if resume is not None:
            self.resume = resume
        if total is not None:
            self.total = total

    @property
    def lins(self):
        """Gets the lins of this ChangelistLinsExtended.  # noqa: E501


        :return: The lins of this ChangelistLinsExtended.  # noqa: E501
        :rtype: list[ChangelistLins]
        """
        return self._lins

    @lins.setter
    def lins(self, lins):
        """Sets the lins of this ChangelistLinsExtended.


        :param lins: The lins of this ChangelistLinsExtended.  # noqa: E501
        :type: list[ChangelistLins]
        """

        self._lins = lins

    @property
    def resume(self):
        """Gets the resume of this ChangelistLinsExtended.  # noqa: E501

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :return: The resume of this ChangelistLinsExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this ChangelistLinsExtended.

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :param resume: The resume of this ChangelistLinsExtended.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) > 8192:
            raise ValueError("Invalid value for `resume`, length must be less than or equal to `8192`")  # noqa: E501
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

        self._resume = resume

    @property
    def total(self):
        """Gets the total of this ChangelistLinsExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this ChangelistLinsExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ChangelistLinsExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this ChangelistLinsExtended.  # noqa: E501
        :type: int
        """
        if total is not None and total > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, ChangelistLinsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
