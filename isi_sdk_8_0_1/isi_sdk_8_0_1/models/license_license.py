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


class LicenseLicense(object):
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
        'duration': 'int',
        'expiration': 'int',
        'id': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'expiration': 'expiration',
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, duration=None, expiration=None, id=None, name=None, status=None):  # noqa: E501
        """LicenseLicense - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._expiration = None
        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if expiration is not None:
            self.expiration = expiration
        self.id = id
        self.name = name
        self.status = status

    @property
    def duration(self):
        """Gets the duration of this LicenseLicense.  # noqa: E501

        Total duration in seconds for temporary licenses.  # noqa: E501

        :return: The duration of this LicenseLicense.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this LicenseLicense.

        Total duration in seconds for temporary licenses.  # noqa: E501

        :param duration: The duration of this LicenseLicense.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def expiration(self):
        """Gets the expiration of this LicenseLicense.  # noqa: E501

        Unix epoch time the license will expire.  # noqa: E501

        :return: The expiration of this LicenseLicense.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this LicenseLicense.

        Unix epoch time the license will expire.  # noqa: E501

        :param expiration: The expiration of this LicenseLicense.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

    @property
    def id(self):
        """Gets the id of this LicenseLicense.  # noqa: E501

        Unique identifier for the license.  # noqa: E501

        :return: The id of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicenseLicense.

        Unique identifier for the license.  # noqa: E501

        :param id: The id of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this LicenseLicense.  # noqa: E501

        Name of the licensed feature.  # noqa: E501

        :return: The name of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenseLicense.

        Name of the licensed feature.  # noqa: E501

        :param name: The name of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this LicenseLicense.  # noqa: E501

        Current status of the license.  # noqa: E501

        :return: The status of this LicenseLicense.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LicenseLicense.

        Current status of the license.  # noqa: E501

        :param status: The status of this LicenseLicense.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Activated", "Evaluation", "Expired", "Inactive", "Unknown"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, LicenseLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
