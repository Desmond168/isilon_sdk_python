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


class HardwareFcport(object):
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
        'firmware_revision': 'str',
        'id': 'str',
        'rate': 'str',
        'state': 'str',
        'topology': 'str',
        'vendor': 'str',
        'wwnn': 'str',
        'wwpn': 'str'
    }

    attribute_map = {
        'firmware_revision': 'firmware_revision',
        'id': 'id',
        'rate': 'rate',
        'state': 'state',
        'topology': 'topology',
        'vendor': 'vendor',
        'wwnn': 'wwnn',
        'wwpn': 'wwpn'
    }

    def __init__(self, firmware_revision=None, id=None, rate=None, state=None, topology=None, vendor=None, wwnn=None, wwpn=None):  # noqa: E501
        """HardwareFcport - a model defined in Swagger"""  # noqa: E501

        self._firmware_revision = None
        self._id = None
        self._rate = None
        self._state = None
        self._topology = None
        self._vendor = None
        self._wwnn = None
        self._wwpn = None
        self.discriminator = None

        if firmware_revision is not None:
            self.firmware_revision = firmware_revision
        if id is not None:
            self.id = id
        if rate is not None:
            self.rate = rate
        if state is not None:
            self.state = state
        if topology is not None:
            self.topology = topology
        if vendor is not None:
            self.vendor = vendor
        if wwnn is not None:
            self.wwnn = wwnn
        if wwpn is not None:
            self.wwpn = wwpn

    @property
    def firmware_revision(self):
        """Gets the firmware_revision of this HardwareFcport.  # noqa: E501

        firmware revision of FC device  # noqa: E501

        :return: The firmware_revision of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._firmware_revision

    @firmware_revision.setter
    def firmware_revision(self, firmware_revision):
        """Sets the firmware_revision of this HardwareFcport.

        firmware revision of FC device  # noqa: E501

        :param firmware_revision: The firmware_revision of this HardwareFcport.  # noqa: E501
        :type: str
        """

        self._firmware_revision = firmware_revision

    @property
    def id(self):
        """Gets the id of this HardwareFcport.  # noqa: E501

        The unique display id  # noqa: E501

        :return: The id of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HardwareFcport.

        The unique display id  # noqa: E501

        :param id: The id of this HardwareFcport.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rate(self):
        """Gets the rate of this HardwareFcport.  # noqa: E501

        Data rate in Gbps, Qlogic card does not support rates above 8  # noqa: E501

        :return: The rate of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this HardwareFcport.

        Data rate in Gbps, Qlogic card does not support rates above 8  # noqa: E501

        :param rate: The rate of this HardwareFcport.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "1", "2", "4", "8", "16", "32"]  # noqa: E501
        if rate not in allowed_values:
            raise ValueError(
                "Invalid value for `rate` ({0}), must be one of {1}"  # noqa: E501
                .format(rate, allowed_values)
            )

        self._rate = rate

    @property
    def state(self):
        """Gets the state of this HardwareFcport.  # noqa: E501

        State of the port  # noqa: E501

        :return: The state of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HardwareFcport.

        State of the port  # noqa: E501

        :param state: The state of this HardwareFcport.  # noqa: E501
        :type: str
        """
        allowed_values = ["enable", "disable"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def topology(self):
        """Gets the topology of this HardwareFcport.  # noqa: E501

        Supported topologies, Sheba card & Qlogic card do not support ptp and nport topology respectively  # noqa: E501

        :return: The topology of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this HardwareFcport.

        Supported topologies, Sheba card & Qlogic card do not support ptp and nport topology respectively  # noqa: E501

        :param topology: The topology of this HardwareFcport.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "ptp", "loop", "nport"]  # noqa: E501
        if topology not in allowed_values:
            raise ValueError(
                "Invalid value for `topology` ({0}), must be one of {1}"  # noqa: E501
                .format(topology, allowed_values)
            )

        self._topology = topology

    @property
    def vendor(self):
        """Gets the vendor of this HardwareFcport.  # noqa: E501

        Vendor of fiber channel card  # noqa: E501

        :return: The vendor of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this HardwareFcport.

        Vendor of fiber channel card  # noqa: E501

        :param vendor: The vendor of this HardwareFcport.  # noqa: E501
        :type: str
        """
        allowed_values = ["Broadcom", "Qlogic"]  # noqa: E501
        if vendor not in allowed_values:
            raise ValueError(
                "Invalid value for `vendor` ({0}), must be one of {1}"  # noqa: E501
                .format(vendor, allowed_values)
            )

        self._vendor = vendor

    @property
    def wwnn(self):
        """Gets the wwnn of this HardwareFcport.  # noqa: E501

        World wide node name of the port  # noqa: E501

        :return: The wwnn of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this HardwareFcport.

        World wide node name of the port  # noqa: E501

        :param wwnn: The wwnn of this HardwareFcport.  # noqa: E501
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """Gets the wwpn of this HardwareFcport.  # noqa: E501

        World wide port name of the port  # noqa: E501

        :return: The wwpn of this HardwareFcport.  # noqa: E501
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """Sets the wwpn of this HardwareFcport.

        World wide port name of the port  # noqa: E501

        :param wwpn: The wwpn of this HardwareFcport.  # noqa: E501
        :type: str
        """

        self._wwpn = wwpn

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
        if not isinstance(other, HardwareFcport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
