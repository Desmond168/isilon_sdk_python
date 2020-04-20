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


class ProvidersKrb5IdParamsKeytabEntry(object):
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
        'encryption': 'list[str]',
        'kvno': 'int',
        'spn': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'encryption': 'encryption',
        'kvno': 'kvno',
        'spn': 'spn',
        'timestamp': 'timestamp'
    }

    def __init__(self, encryption=None, kvno=None, spn=None, timestamp=None):  # noqa: E501
        """ProvidersKrb5IdParamsKeytabEntry - a model defined in Swagger"""  # noqa: E501

        self._encryption = None
        self._kvno = None
        self._spn = None
        self._timestamp = None
        self.discriminator = None

        if encryption is not None:
            self.encryption = encryption
        if kvno is not None:
            self.kvno = kvno
        if spn is not None:
            self.spn = spn
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def encryption(self):
        """Gets the encryption of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501

        Specifies the encryption types.  # noqa: E501

        :return: The encryption of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :rtype: list[str]
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this ProvidersKrb5IdParamsKeytabEntry.

        Specifies the encryption types.  # noqa: E501

        :param encryption: The encryption of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :type: list[str]
        """

        self._encryption = encryption

    @property
    def kvno(self):
        """Gets the kvno of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501

        Specifies the version number of the SPN key.  # noqa: E501

        :return: The kvno of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :rtype: int
        """
        return self._kvno

    @kvno.setter
    def kvno(self, kvno):
        """Sets the kvno of this ProvidersKrb5IdParamsKeytabEntry.

        Specifies the version number of the SPN key.  # noqa: E501

        :param kvno: The kvno of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :type: int
        """
        if kvno is not None and kvno > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `kvno`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if kvno is not None and kvno < 0:  # noqa: E501
            raise ValueError("Invalid value for `kvno`, must be a value greater than or equal to `0`")  # noqa: E501

        self._kvno = kvno

    @property
    def spn(self):
        """Gets the spn of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501

        Specifies the Service Principal Name (SPN).  # noqa: E501

        :return: The spn of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :rtype: str
        """
        return self._spn

    @spn.setter
    def spn(self, spn):
        """Sets the spn of this ProvidersKrb5IdParamsKeytabEntry.

        Specifies the Service Principal Name (SPN).  # noqa: E501

        :param spn: The spn of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :type: str
        """
        if spn is not None and len(spn) > 2048:
            raise ValueError("Invalid value for `spn`, length must be less than or equal to `2048`")  # noqa: E501
        if spn is not None and len(spn) < 0:
            raise ValueError("Invalid value for `spn`, length must be greater than or equal to `0`")  # noqa: E501

        self._spn = spn

    @property
    def timestamp(self):
        """Gets the timestamp of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501

        Specifies the time the SPN key was created.  # noqa: E501

        :return: The timestamp of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ProvidersKrb5IdParamsKeytabEntry.

        Specifies the time the SPN key was created.  # noqa: E501

        :param timestamp: The timestamp of this ProvidersKrb5IdParamsKeytabEntry.  # noqa: E501
        :type: int
        """
        if timestamp is not None and timestamp > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if timestamp is not None and timestamp < 0:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `0`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, ProvidersKrb5IdParamsKeytabEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
