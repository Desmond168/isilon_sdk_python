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


class NetworkGroupnet(object):
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
        'description': 'str',
        'dns_cache_enabled': 'bool',
        'dns_options': 'list[str]',
        'dns_search': 'list[str]',
        'dns_servers': 'list[str]',
        'name': 'str',
        'server_side_dns_search': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'dns_cache_enabled': 'dns_cache_enabled',
        'dns_options': 'dns_options',
        'dns_search': 'dns_search',
        'dns_servers': 'dns_servers',
        'name': 'name',
        'server_side_dns_search': 'server_side_dns_search'
    }

    def __init__(self, description=None, dns_cache_enabled=None, dns_options=None, dns_search=None, dns_servers=None, name=None, server_side_dns_search=None):  # noqa: E501
        """NetworkGroupnet - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._dns_cache_enabled = None
        self._dns_options = None
        self._dns_search = None
        self._dns_servers = None
        self._name = None
        self._server_side_dns_search = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if dns_cache_enabled is not None:
            self.dns_cache_enabled = dns_cache_enabled
        if dns_options is not None:
            self.dns_options = dns_options
        if dns_search is not None:
            self.dns_search = dns_search
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if name is not None:
            self.name = name
        if server_side_dns_search is not None:
            self.server_side_dns_search = server_side_dns_search

    @property
    def description(self):
        """Gets the description of this NetworkGroupnet.  # noqa: E501

        A description of the groupnet.  # noqa: E501

        :return: The description of this NetworkGroupnet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkGroupnet.

        A description of the groupnet.  # noqa: E501

        :param description: The description of this NetworkGroupnet.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def dns_cache_enabled(self):
        """Gets the dns_cache_enabled of this NetworkGroupnet.  # noqa: E501

        DNS caching is enabled or disabled.  # noqa: E501

        :return: The dns_cache_enabled of this NetworkGroupnet.  # noqa: E501
        :rtype: bool
        """
        return self._dns_cache_enabled

    @dns_cache_enabled.setter
    def dns_cache_enabled(self, dns_cache_enabled):
        """Sets the dns_cache_enabled of this NetworkGroupnet.

        DNS caching is enabled or disabled.  # noqa: E501

        :param dns_cache_enabled: The dns_cache_enabled of this NetworkGroupnet.  # noqa: E501
        :type: bool
        """

        self._dns_cache_enabled = dns_cache_enabled

    @property
    def dns_options(self):
        """Gets the dns_options of this NetworkGroupnet.  # noqa: E501

        List of DNS resolver options.  # noqa: E501

        :return: The dns_options of this NetworkGroupnet.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_options

    @dns_options.setter
    def dns_options(self, dns_options):
        """Sets the dns_options of this NetworkGroupnet.

        List of DNS resolver options.  # noqa: E501

        :param dns_options: The dns_options of this NetworkGroupnet.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["rotate"]  # noqa: E501
        if not set(dns_options).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `dns_options` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(dns_options) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._dns_options = dns_options

    @property
    def dns_search(self):
        """Gets the dns_search of this NetworkGroupnet.  # noqa: E501

        List of DNS search suffixes.  # noqa: E501

        :return: The dns_search of this NetworkGroupnet.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_search

    @dns_search.setter
    def dns_search(self, dns_search):
        """Sets the dns_search of this NetworkGroupnet.

        List of DNS search suffixes.  # noqa: E501

        :param dns_search: The dns_search of this NetworkGroupnet.  # noqa: E501
        :type: list[str]
        """

        self._dns_search = dns_search

    @property
    def dns_servers(self):
        """Gets the dns_servers of this NetworkGroupnet.  # noqa: E501

        List of Domain Name Server IP addresses.  # noqa: E501

        :return: The dns_servers of this NetworkGroupnet.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this NetworkGroupnet.

        List of Domain Name Server IP addresses.  # noqa: E501

        :param dns_servers: The dns_servers of this NetworkGroupnet.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def name(self):
        """Gets the name of this NetworkGroupnet.  # noqa: E501

        The name of the groupnet.  # noqa: E501

        :return: The name of this NetworkGroupnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkGroupnet.

        The name of the groupnet.  # noqa: E501

        :param name: The name of this NetworkGroupnet.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[0-9a-zA-Z_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def server_side_dns_search(self):
        """Gets the server_side_dns_search of this NetworkGroupnet.  # noqa: E501

        Enable or disable appending nodes DNS search  list to client DNS inquiries directed at SmartConnect service IP.  # noqa: E501

        :return: The server_side_dns_search of this NetworkGroupnet.  # noqa: E501
        :rtype: bool
        """
        return self._server_side_dns_search

    @server_side_dns_search.setter
    def server_side_dns_search(self, server_side_dns_search):
        """Sets the server_side_dns_search of this NetworkGroupnet.

        Enable or disable appending nodes DNS search  list to client DNS inquiries directed at SmartConnect service IP.  # noqa: E501

        :param server_side_dns_search: The server_side_dns_search of this NetworkGroupnet.  # noqa: E501
        :type: bool
        """

        self._server_side_dns_search = server_side_dns_search

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
        if not isinstance(other, NetworkGroupnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
