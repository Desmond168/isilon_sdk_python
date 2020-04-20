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

from isi_sdk_8_2_2.models.cluster_internal_networks_failover_ip_addresse import ClusterInternalNetworksFailoverIpAddresse  # noqa: F401,E501


class ClusterInternalNetworks(object):
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
        'failover_ip_addresses': 'list[ClusterInternalNetworksFailoverIpAddresse]',
        'failover_status': 'str',
        'int_a_fabric': 'str',
        'int_a_ip_addresses': 'list[ClusterInternalNetworksFailoverIpAddresse]',
        'int_a_mtu': 'int',
        'int_a_prefix_length': 'int',
        'int_a_status': 'str',
        'int_b_fabric': 'str',
        'int_b_ip_addresses': 'list[ClusterInternalNetworksFailoverIpAddresse]',
        'int_b_mtu': 'int',
        'int_b_prefix_length': 'int'
    }

    attribute_map = {
        'failover_ip_addresses': 'failover_ip_addresses',
        'failover_status': 'failover_status',
        'int_a_fabric': 'int_a_fabric',
        'int_a_ip_addresses': 'int_a_ip_addresses',
        'int_a_mtu': 'int_a_mtu',
        'int_a_prefix_length': 'int_a_prefix_length',
        'int_a_status': 'int_a_status',
        'int_b_fabric': 'int_b_fabric',
        'int_b_ip_addresses': 'int_b_ip_addresses',
        'int_b_mtu': 'int_b_mtu',
        'int_b_prefix_length': 'int_b_prefix_length'
    }

    def __init__(self, failover_ip_addresses=None, failover_status=None, int_a_fabric=None, int_a_ip_addresses=None, int_a_mtu=None, int_a_prefix_length=None, int_a_status=None, int_b_fabric=None, int_b_ip_addresses=None, int_b_mtu=None, int_b_prefix_length=None):  # noqa: E501
        """ClusterInternalNetworks - a model defined in Swagger"""  # noqa: E501

        self._failover_ip_addresses = None
        self._failover_status = None
        self._int_a_fabric = None
        self._int_a_ip_addresses = None
        self._int_a_mtu = None
        self._int_a_prefix_length = None
        self._int_a_status = None
        self._int_b_fabric = None
        self._int_b_ip_addresses = None
        self._int_b_mtu = None
        self._int_b_prefix_length = None
        self.discriminator = None

        if failover_ip_addresses is not None:
            self.failover_ip_addresses = failover_ip_addresses
        if failover_status is not None:
            self.failover_status = failover_status
        if int_a_fabric is not None:
            self.int_a_fabric = int_a_fabric
        if int_a_ip_addresses is not None:
            self.int_a_ip_addresses = int_a_ip_addresses
        if int_a_mtu is not None:
            self.int_a_mtu = int_a_mtu
        if int_a_prefix_length is not None:
            self.int_a_prefix_length = int_a_prefix_length
        if int_a_status is not None:
            self.int_a_status = int_a_status
        if int_b_fabric is not None:
            self.int_b_fabric = int_b_fabric
        if int_b_ip_addresses is not None:
            self.int_b_ip_addresses = int_b_ip_addresses
        if int_b_mtu is not None:
            self.int_b_mtu = int_b_mtu
        if int_b_prefix_length is not None:
            self.int_b_prefix_length = int_b_prefix_length

    @property
    def failover_ip_addresses(self):
        """Gets the failover_ip_addresses of this ClusterInternalNetworks.  # noqa: E501

        Array of IP address ranges to be used to configure the internal failover network of the OneFS cluster.  # noqa: E501

        :return: The failover_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :rtype: list[ClusterInternalNetworksFailoverIpAddresse]
        """
        return self._failover_ip_addresses

    @failover_ip_addresses.setter
    def failover_ip_addresses(self, failover_ip_addresses):
        """Sets the failover_ip_addresses of this ClusterInternalNetworks.

        Array of IP address ranges to be used to configure the internal failover network of the OneFS cluster.  # noqa: E501

        :param failover_ip_addresses: The failover_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :type: list[ClusterInternalNetworksFailoverIpAddresse]
        """

        self._failover_ip_addresses = failover_ip_addresses

    @property
    def failover_status(self):
        """Gets the failover_status of this ClusterInternalNetworks.  # noqa: E501

        Status of failover network.  # noqa: E501

        :return: The failover_status of this ClusterInternalNetworks.  # noqa: E501
        :rtype: str
        """
        return self._failover_status

    @failover_status.setter
    def failover_status(self, failover_status):
        """Sets the failover_status of this ClusterInternalNetworks.

        Status of failover network.  # noqa: E501

        :param failover_status: The failover_status of this ClusterInternalNetworks.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if failover_status not in allowed_values:
            raise ValueError(
                "Invalid value for `failover_status` ({0}), must be one of {1}"  # noqa: E501
                .format(failover_status, allowed_values)
            )

        self._failover_status = failover_status

    @property
    def int_a_fabric(self):
        """Gets the int_a_fabric of this ClusterInternalNetworks.  # noqa: E501

        Network fabric used for the primary network int-a.  # noqa: E501

        :return: The int_a_fabric of this ClusterInternalNetworks.  # noqa: E501
        :rtype: str
        """
        return self._int_a_fabric

    @int_a_fabric.setter
    def int_a_fabric(self, int_a_fabric):
        """Sets the int_a_fabric of this ClusterInternalNetworks.

        Network fabric used for the primary network int-a.  # noqa: E501

        :param int_a_fabric: The int_a_fabric of this ClusterInternalNetworks.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ethernet", "InfiniBand"]  # noqa: E501
        if int_a_fabric not in allowed_values:
            raise ValueError(
                "Invalid value for `int_a_fabric` ({0}), must be one of {1}"  # noqa: E501
                .format(int_a_fabric, allowed_values)
            )

        self._int_a_fabric = int_a_fabric

    @property
    def int_a_ip_addresses(self):
        """Gets the int_a_ip_addresses of this ClusterInternalNetworks.  # noqa: E501

        Array of IP address ranges to be used to configure the internal int-a network of the OneFS cluster.  # noqa: E501

        :return: The int_a_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :rtype: list[ClusterInternalNetworksFailoverIpAddresse]
        """
        return self._int_a_ip_addresses

    @int_a_ip_addresses.setter
    def int_a_ip_addresses(self, int_a_ip_addresses):
        """Sets the int_a_ip_addresses of this ClusterInternalNetworks.

        Array of IP address ranges to be used to configure the internal int-a network of the OneFS cluster.  # noqa: E501

        :param int_a_ip_addresses: The int_a_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :type: list[ClusterInternalNetworksFailoverIpAddresse]
        """

        self._int_a_ip_addresses = int_a_ip_addresses

    @property
    def int_a_mtu(self):
        """Gets the int_a_mtu of this ClusterInternalNetworks.  # noqa: E501

        Maximum Transfer Unit (MTU) of the primary network int-a.  # noqa: E501

        :return: The int_a_mtu of this ClusterInternalNetworks.  # noqa: E501
        :rtype: int
        """
        return self._int_a_mtu

    @int_a_mtu.setter
    def int_a_mtu(self, int_a_mtu):
        """Sets the int_a_mtu of this ClusterInternalNetworks.

        Maximum Transfer Unit (MTU) of the primary network int-a.  # noqa: E501

        :param int_a_mtu: The int_a_mtu of this ClusterInternalNetworks.  # noqa: E501
        :type: int
        """

        self._int_a_mtu = int_a_mtu

    @property
    def int_a_prefix_length(self):
        """Gets the int_a_prefix_length of this ClusterInternalNetworks.  # noqa: E501

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :return: The int_a_prefix_length of this ClusterInternalNetworks.  # noqa: E501
        :rtype: int
        """
        return self._int_a_prefix_length

    @int_a_prefix_length.setter
    def int_a_prefix_length(self, int_a_prefix_length):
        """Sets the int_a_prefix_length of this ClusterInternalNetworks.

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :param int_a_prefix_length: The int_a_prefix_length of this ClusterInternalNetworks.  # noqa: E501
        :type: int
        """
        if int_a_prefix_length is not None and int_a_prefix_length > 128:  # noqa: E501
            raise ValueError("Invalid value for `int_a_prefix_length`, must be a value less than or equal to `128`")  # noqa: E501
        if int_a_prefix_length is not None and int_a_prefix_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `int_a_prefix_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._int_a_prefix_length = int_a_prefix_length

    @property
    def int_a_status(self):
        """Gets the int_a_status of this ClusterInternalNetworks.  # noqa: E501

        Status of the primary network int-a.  # noqa: E501

        :return: The int_a_status of this ClusterInternalNetworks.  # noqa: E501
        :rtype: str
        """
        return self._int_a_status

    @int_a_status.setter
    def int_a_status(self, int_a_status):
        """Sets the int_a_status of this ClusterInternalNetworks.

        Status of the primary network int-a.  # noqa: E501

        :param int_a_status: The int_a_status of this ClusterInternalNetworks.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if int_a_status not in allowed_values:
            raise ValueError(
                "Invalid value for `int_a_status` ({0}), must be one of {1}"  # noqa: E501
                .format(int_a_status, allowed_values)
            )

        self._int_a_status = int_a_status

    @property
    def int_b_fabric(self):
        """Gets the int_b_fabric of this ClusterInternalNetworks.  # noqa: E501

        Network fabric used for the failover network.  # noqa: E501

        :return: The int_b_fabric of this ClusterInternalNetworks.  # noqa: E501
        :rtype: str
        """
        return self._int_b_fabric

    @int_b_fabric.setter
    def int_b_fabric(self, int_b_fabric):
        """Sets the int_b_fabric of this ClusterInternalNetworks.

        Network fabric used for the failover network.  # noqa: E501

        :param int_b_fabric: The int_b_fabric of this ClusterInternalNetworks.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ethernet", "InfiniBand"]  # noqa: E501
        if int_b_fabric not in allowed_values:
            raise ValueError(
                "Invalid value for `int_b_fabric` ({0}), must be one of {1}"  # noqa: E501
                .format(int_b_fabric, allowed_values)
            )

        self._int_b_fabric = int_b_fabric

    @property
    def int_b_ip_addresses(self):
        """Gets the int_b_ip_addresses of this ClusterInternalNetworks.  # noqa: E501

        Array of IP address ranges to be used to configure the internal int-b network of the OneFS cluster.  # noqa: E501

        :return: The int_b_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :rtype: list[ClusterInternalNetworksFailoverIpAddresse]
        """
        return self._int_b_ip_addresses

    @int_b_ip_addresses.setter
    def int_b_ip_addresses(self, int_b_ip_addresses):
        """Sets the int_b_ip_addresses of this ClusterInternalNetworks.

        Array of IP address ranges to be used to configure the internal int-b network of the OneFS cluster.  # noqa: E501

        :param int_b_ip_addresses: The int_b_ip_addresses of this ClusterInternalNetworks.  # noqa: E501
        :type: list[ClusterInternalNetworksFailoverIpAddresse]
        """

        self._int_b_ip_addresses = int_b_ip_addresses

    @property
    def int_b_mtu(self):
        """Gets the int_b_mtu of this ClusterInternalNetworks.  # noqa: E501

        Maximum Transfer Unit (MTU) of the failover network int-b.  # noqa: E501

        :return: The int_b_mtu of this ClusterInternalNetworks.  # noqa: E501
        :rtype: int
        """
        return self._int_b_mtu

    @int_b_mtu.setter
    def int_b_mtu(self, int_b_mtu):
        """Sets the int_b_mtu of this ClusterInternalNetworks.

        Maximum Transfer Unit (MTU) of the failover network int-b.  # noqa: E501

        :param int_b_mtu: The int_b_mtu of this ClusterInternalNetworks.  # noqa: E501
        :type: int
        """

        self._int_b_mtu = int_b_mtu

    @property
    def int_b_prefix_length(self):
        """Gets the int_b_prefix_length of this ClusterInternalNetworks.  # noqa: E501

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :return: The int_b_prefix_length of this ClusterInternalNetworks.  # noqa: E501
        :rtype: int
        """
        return self._int_b_prefix_length

    @int_b_prefix_length.setter
    def int_b_prefix_length(self, int_b_prefix_length):
        """Sets the int_b_prefix_length of this ClusterInternalNetworks.

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :param int_b_prefix_length: The int_b_prefix_length of this ClusterInternalNetworks.  # noqa: E501
        :type: int
        """
        if int_b_prefix_length is not None and int_b_prefix_length > 128:  # noqa: E501
            raise ValueError("Invalid value for `int_b_prefix_length`, must be a value less than or equal to `128`")  # noqa: E501
        if int_b_prefix_length is not None and int_b_prefix_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `int_b_prefix_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._int_b_prefix_length = int_b_prefix_length

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
        if not isinstance(other, ClusterInternalNetworks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
