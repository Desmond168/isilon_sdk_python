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

from isi_sdk_8_2_1.models.node_status_node_batterystatus import NodeStatusNodeBatterystatus  # noqa: F401,E501
from isi_sdk_8_2_1.models.node_status_node_capacity_item import NodeStatusNodeCapacityItem  # noqa: F401,E501
from isi_sdk_8_2_1.models.node_status_node_cpu import NodeStatusNodeCpu  # noqa: F401,E501
from isi_sdk_8_2_1.models.node_status_node_nvram import NodeStatusNodeNvram  # noqa: F401,E501
from isi_sdk_8_2_1.models.node_status_node_powersupplies import NodeStatusNodePowersupplies  # noqa: F401,E501


class NodeStatusNode(object):
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
        'batterystatus': 'NodeStatusNodeBatterystatus',
        'capacity': 'list[NodeStatusNodeCapacityItem]',
        'cpu': 'NodeStatusNodeCpu',
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'nvram': 'NodeStatusNodeNvram',
        'powersupplies': 'NodeStatusNodePowersupplies',
        'release': 'str',
        'status': 'int',
        'uptime': 'int',
        'version': 'str'
    }

    attribute_map = {
        'batterystatus': 'batterystatus',
        'capacity': 'capacity',
        'cpu': 'cpu',
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'nvram': 'nvram',
        'powersupplies': 'powersupplies',
        'release': 'release',
        'status': 'status',
        'uptime': 'uptime',
        'version': 'version'
    }

    def __init__(self, batterystatus=None, capacity=None, cpu=None, error=None, id=None, lnn=None, nvram=None, powersupplies=None, release=None, status=None, uptime=None, version=None):  # noqa: E501
        """NodeStatusNode - a model defined in Swagger"""  # noqa: E501

        self._batterystatus = None
        self._capacity = None
        self._cpu = None
        self._error = None
        self._id = None
        self._lnn = None
        self._nvram = None
        self._powersupplies = None
        self._release = None
        self._status = None
        self._uptime = None
        self._version = None
        self.discriminator = None

        if batterystatus is not None:
            self.batterystatus = batterystatus
        if capacity is not None:
            self.capacity = capacity
        if cpu is not None:
            self.cpu = cpu
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if nvram is not None:
            self.nvram = nvram
        if powersupplies is not None:
            self.powersupplies = powersupplies
        if release is not None:
            self.release = release
        if status is not None:
            self.status = status
        if uptime is not None:
            self.uptime = uptime
        if version is not None:
            self.version = version

    @property
    def batterystatus(self):
        """Gets the batterystatus of this NodeStatusNode.  # noqa: E501

        Battery status information.  # noqa: E501

        :return: The batterystatus of this NodeStatusNode.  # noqa: E501
        :rtype: NodeStatusNodeBatterystatus
        """
        return self._batterystatus

    @batterystatus.setter
    def batterystatus(self, batterystatus):
        """Sets the batterystatus of this NodeStatusNode.

        Battery status information.  # noqa: E501

        :param batterystatus: The batterystatus of this NodeStatusNode.  # noqa: E501
        :type: NodeStatusNodeBatterystatus
        """

        self._batterystatus = batterystatus

    @property
    def capacity(self):
        """Gets the capacity of this NodeStatusNode.  # noqa: E501

        Storage capacity of this node.  # noqa: E501

        :return: The capacity of this NodeStatusNode.  # noqa: E501
        :rtype: list[NodeStatusNodeCapacityItem]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this NodeStatusNode.

        Storage capacity of this node.  # noqa: E501

        :param capacity: The capacity of this NodeStatusNode.  # noqa: E501
        :type: list[NodeStatusNodeCapacityItem]
        """

        self._capacity = capacity

    @property
    def cpu(self):
        """Gets the cpu of this NodeStatusNode.  # noqa: E501

        CPU status information for this node.  # noqa: E501

        :return: The cpu of this NodeStatusNode.  # noqa: E501
        :rtype: NodeStatusNodeCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this NodeStatusNode.

        CPU status information for this node.  # noqa: E501

        :param cpu: The cpu of this NodeStatusNode.  # noqa: E501
        :type: NodeStatusNodeCpu
        """

        self._cpu = cpu

    @property
    def error(self):
        """Gets the error of this NodeStatusNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeStatusNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeStatusNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeStatusNode.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 8192:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if error is not None and len(error) < 0:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeStatusNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeStatusNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeStatusNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeStatusNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeStatusNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStatusNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeStatusNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def nvram(self):
        """Gets the nvram of this NodeStatusNode.  # noqa: E501

        Node NVRAM information.  # noqa: E501

        :return: The nvram of this NodeStatusNode.  # noqa: E501
        :rtype: NodeStatusNodeNvram
        """
        return self._nvram

    @nvram.setter
    def nvram(self, nvram):
        """Sets the nvram of this NodeStatusNode.

        Node NVRAM information.  # noqa: E501

        :param nvram: The nvram of this NodeStatusNode.  # noqa: E501
        :type: NodeStatusNodeNvram
        """

        self._nvram = nvram

    @property
    def powersupplies(self):
        """Gets the powersupplies of this NodeStatusNode.  # noqa: E501

        Information about this node's power supplies.  # noqa: E501

        :return: The powersupplies of this NodeStatusNode.  # noqa: E501
        :rtype: NodeStatusNodePowersupplies
        """
        return self._powersupplies

    @powersupplies.setter
    def powersupplies(self, powersupplies):
        """Sets the powersupplies of this NodeStatusNode.

        Information about this node's power supplies.  # noqa: E501

        :param powersupplies: The powersupplies of this NodeStatusNode.  # noqa: E501
        :type: NodeStatusNodePowersupplies
        """

        self._powersupplies = powersupplies

    @property
    def release(self):
        """Gets the release of this NodeStatusNode.  # noqa: E501

        OneFS release.  # noqa: E501

        :return: The release of this NodeStatusNode.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this NodeStatusNode.

        OneFS release.  # noqa: E501

        :param release: The release of this NodeStatusNode.  # noqa: E501
        :type: str
        """
        if release is not None and len(release) > 255:
            raise ValueError("Invalid value for `release`, length must be less than or equal to `255`")  # noqa: E501
        if release is not None and len(release) < 0:
            raise ValueError("Invalid value for `release`, length must be greater than or equal to `0`")  # noqa: E501

        self._release = release

    @property
    def status(self):
        """Gets the status of this NodeStatusNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this NodeStatusNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStatusNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this NodeStatusNode.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def uptime(self):
        """Gets the uptime of this NodeStatusNode.  # noqa: E501

        Seconds this node has been online.  # noqa: E501

        :return: The uptime of this NodeStatusNode.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this NodeStatusNode.

        Seconds this node has been online.  # noqa: E501

        :param uptime: The uptime of this NodeStatusNode.  # noqa: E501
        :type: int
        """
        if uptime is not None and uptime > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `uptime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if uptime is not None and uptime < 0:  # noqa: E501
            raise ValueError("Invalid value for `uptime`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uptime = uptime

    @property
    def version(self):
        """Gets the version of this NodeStatusNode.  # noqa: E501

        OneFS version.  # noqa: E501

        :return: The version of this NodeStatusNode.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodeStatusNode.

        OneFS version.  # noqa: E501

        :param version: The version of this NodeStatusNode.  # noqa: E501
        :type: str
        """
        if version is not None and len(version) > 511:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `511`")  # noqa: E501
        if version is not None and len(version) < 0:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `0`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, NodeStatusNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
