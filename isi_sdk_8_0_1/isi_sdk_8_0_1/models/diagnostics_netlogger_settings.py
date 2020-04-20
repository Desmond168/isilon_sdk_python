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


class DiagnosticsNetloggerSettings(object):
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
        'clients': 'str',
        'count': 'int',
        'duration': 'int',
        'interfaces': 'str',
        'nodelist': 'str',
        'ports': 'str',
        'protocols': 'str',
        'snaplength': 'int'
    }

    attribute_map = {
        'clients': 'clients',
        'count': 'count',
        'duration': 'duration',
        'interfaces': 'interfaces',
        'nodelist': 'nodelist',
        'ports': 'ports',
        'protocols': 'protocols',
        'snaplength': 'snaplength'
    }

    def __init__(self, clients=None, count=None, duration=None, interfaces=None, nodelist=None, ports=None, protocols=None, snaplength=None):  # noqa: E501
        """DiagnosticsNetloggerSettings - a model defined in Swagger"""  # noqa: E501

        self._clients = None
        self._count = None
        self._duration = None
        self._interfaces = None
        self._nodelist = None
        self._ports = None
        self._protocols = None
        self._snaplength = None
        self.discriminator = None

        if clients is not None:
            self.clients = clients
        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration
        if interfaces is not None:
            self.interfaces = interfaces
        if nodelist is not None:
            self.nodelist = nodelist
        if ports is not None:
            self.ports = ports
        if protocols is not None:
            self.protocols = protocols
        if snaplength is not None:
            self.snaplength = snaplength

    @property
    def clients(self):
        """Gets the clients of this DiagnosticsNetloggerSettings.  # noqa: E501

        IP Addresses or host names of clients  # noqa: E501

        :return: The clients of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: str
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this DiagnosticsNetloggerSettings.

        IP Addresses or host names of clients  # noqa: E501

        :param clients: The clients of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: str
        """

        self._clients = clients

    @property
    def count(self):
        """Gets the count of this DiagnosticsNetloggerSettings.  # noqa: E501

        Count of capture files to keep, 0 is infinite.  # noqa: E501

        :return: The count of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DiagnosticsNetloggerSettings.

        Count of capture files to keep, 0 is infinite.  # noqa: E501

        :param count: The count of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: int
        """
        if count is not None and count > 1024:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `1024`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def duration(self):
        """Gets the duration of this DiagnosticsNetloggerSettings.  # noqa: E501

        Duration in minutes of each capture file  # noqa: E501

        :return: The duration of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DiagnosticsNetloggerSettings.

        Duration in minutes of each capture file  # noqa: E501

        :param duration: The duration of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: int
        """
        if duration is not None and duration > 255:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `255`")  # noqa: E501
        if duration is not None and duration < 1:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `1`")  # noqa: E501

        self._duration = duration

    @property
    def interfaces(self):
        """Gets the interfaces of this DiagnosticsNetloggerSettings.  # noqa: E501

        Network interfaces to capture on.  # noqa: E501

        :return: The interfaces of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: str
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this DiagnosticsNetloggerSettings.

        Network interfaces to capture on.  # noqa: E501

        :param interfaces: The interfaces of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: str
        """

        self._interfaces = interfaces

    @property
    def nodelist(self):
        """Gets the nodelist of this DiagnosticsNetloggerSettings.  # noqa: E501

        List of nodes, or empty for all  # noqa: E501

        :return: The nodelist of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: str
        """
        return self._nodelist

    @nodelist.setter
    def nodelist(self, nodelist):
        """Sets the nodelist of this DiagnosticsNetloggerSettings.

        List of nodes, or empty for all  # noqa: E501

        :param nodelist: The nodelist of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: str
        """

        self._nodelist = nodelist

    @property
    def ports(self):
        """Gets the ports of this DiagnosticsNetloggerSettings.  # noqa: E501

        List of Integers of TCP or UDP ports  # noqa: E501

        :return: The ports of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this DiagnosticsNetloggerSettings.

        List of Integers of TCP or UDP ports  # noqa: E501

        :param ports: The ports of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: str
        """

        self._ports = ports

    @property
    def protocols(self):
        """Gets the protocols of this DiagnosticsNetloggerSettings.  # noqa: E501

        which protocol(s) to gather on  # noqa: E501

        :return: The protocols of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: str
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this DiagnosticsNetloggerSettings.

        which protocol(s) to gather on  # noqa: E501

        :param protocols: The protocols of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: str
        """

        self._protocols = protocols

    @property
    def snaplength(self):
        """Gets the snaplength of this DiagnosticsNetloggerSettings.  # noqa: E501

        Amount of bytes per packet to capture  # noqa: E501

        :return: The snaplength of this DiagnosticsNetloggerSettings.  # noqa: E501
        :rtype: int
        """
        return self._snaplength

    @snaplength.setter
    def snaplength(self, snaplength):
        """Sets the snaplength of this DiagnosticsNetloggerSettings.

        Amount of bytes per packet to capture  # noqa: E501

        :param snaplength: The snaplength of this DiagnosticsNetloggerSettings.  # noqa: E501
        :type: int
        """
        if snaplength is not None and snaplength > 9100:  # noqa: E501
            raise ValueError("Invalid value for `snaplength`, must be a value less than or equal to `9100`")  # noqa: E501
        if snaplength is not None and snaplength < 64:  # noqa: E501
            raise ValueError("Invalid value for `snaplength`, must be a value greater than or equal to `64`")  # noqa: E501

        self._snaplength = snaplength

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
        if not isinstance(other, DiagnosticsNetloggerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
