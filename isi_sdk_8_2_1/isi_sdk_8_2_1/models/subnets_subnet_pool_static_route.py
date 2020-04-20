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


class SubnetsSubnetPoolStaticRoute(object):
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
        'gateway': 'str',
        'prefixlen': 'int',
        'subnet': 'str'
    }

    attribute_map = {
        'gateway': 'gateway',
        'prefixlen': 'prefixlen',
        'subnet': 'subnet'
    }

    def __init__(self, gateway=None, prefixlen=None, subnet=None):  # noqa: E501
        """SubnetsSubnetPoolStaticRoute - a model defined in Swagger"""  # noqa: E501

        self._gateway = None
        self._prefixlen = None
        self._subnet = None
        self.discriminator = None

        self.gateway = gateway
        self.prefixlen = prefixlen
        self.subnet = subnet

    @property
    def gateway(self):
        """Gets the gateway of this SubnetsSubnetPoolStaticRoute.  # noqa: E501

        Address of the gateway in the format: yyy.yyy.yyy.yyy  # noqa: E501

        :return: The gateway of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this SubnetsSubnetPoolStaticRoute.

        Address of the gateway in the format: yyy.yyy.yyy.yyy  # noqa: E501

        :param gateway: The gateway of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501
        if gateway is not None and len(gateway) > 40:
            raise ValueError("Invalid value for `gateway`, length must be less than or equal to `40`")  # noqa: E501
        if gateway is not None and len(gateway) < 1:
            raise ValueError("Invalid value for `gateway`, length must be greater than or equal to `1`")  # noqa: E501
        if gateway is not None and not re.search('(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', gateway):  # noqa: E501
            raise ValueError("Invalid value for `gateway`, must be a follow pattern or equal to `/(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._gateway = gateway

    @property
    def prefixlen(self):
        """Gets the prefixlen of this SubnetsSubnetPoolStaticRoute.  # noqa: E501

        Prefix length in the format: nn.  # noqa: E501

        :return: The prefixlen of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """Sets the prefixlen of this SubnetsSubnetPoolStaticRoute.

        Prefix length in the format: nn.  # noqa: E501

        :param prefixlen: The prefixlen of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :type: int
        """
        if prefixlen is None:
            raise ValueError("Invalid value for `prefixlen`, must not be `None`")  # noqa: E501
        if prefixlen is not None and prefixlen > 128:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value less than or equal to `128`")  # noqa: E501
        if prefixlen is not None and prefixlen < 0:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prefixlen = prefixlen

    @property
    def subnet(self):
        """Gets the subnet of this SubnetsSubnetPoolStaticRoute.  # noqa: E501

        Network address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :return: The subnet of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this SubnetsSubnetPoolStaticRoute.

        Network address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :param subnet: The subnet of this SubnetsSubnetPoolStaticRoute.  # noqa: E501
        :type: str
        """
        if subnet is None:
            raise ValueError("Invalid value for `subnet`, must not be `None`")  # noqa: E501
        if subnet is not None and len(subnet) > 40:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `40`")  # noqa: E501
        if subnet is not None and len(subnet) < 1:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `1`")  # noqa: E501
        if subnet is not None and not re.search('(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', subnet):  # noqa: E501
            raise ValueError("Invalid value for `subnet`, must be a follow pattern or equal to `/(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._subnet = subnet

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
        if not isinstance(other, SubnetsSubnetPoolStaticRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
