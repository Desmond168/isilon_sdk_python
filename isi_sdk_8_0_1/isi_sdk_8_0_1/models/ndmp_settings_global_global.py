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


class NdmpSettingsGlobalGlobal(object):
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
        'bre_max_num_contexts': 'int',
        'dma': 'str',
        'msb_context_retention_duration': 'int',
        'msr_context_retention_duration': 'int',
        'port': 'int',
        'service': 'bool'
    }

    attribute_map = {
        'bre_max_num_contexts': 'bre_max_num_contexts',
        'dma': 'dma',
        'msb_context_retention_duration': 'msb_context_retention_duration',
        'msr_context_retention_duration': 'msr_context_retention_duration',
        'port': 'port',
        'service': 'service'
    }

    def __init__(self, bre_max_num_contexts=None, dma=None, msb_context_retention_duration=None, msr_context_retention_duration=None, port=None, service=None):  # noqa: E501
        """NdmpSettingsGlobalGlobal - a model defined in Swagger"""  # noqa: E501

        self._bre_max_num_contexts = None
        self._dma = None
        self._msb_context_retention_duration = None
        self._msr_context_retention_duration = None
        self._port = None
        self._service = None
        self.discriminator = None

        if bre_max_num_contexts is not None:
            self.bre_max_num_contexts = bre_max_num_contexts
        if dma is not None:
            self.dma = dma
        if msb_context_retention_duration is not None:
            self.msb_context_retention_duration = msb_context_retention_duration
        if msr_context_retention_duration is not None:
            self.msr_context_retention_duration = msr_context_retention_duration
        if port is not None:
            self.port = port
        if service is not None:
            self.service = service

    @property
    def bre_max_num_contexts(self):
        """Gets the bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Maximum number of BRE contexts.  # noqa: E501

        :return: The bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._bre_max_num_contexts

    @bre_max_num_contexts.setter
    def bre_max_num_contexts(self, bre_max_num_contexts):
        """Sets the bre_max_num_contexts of this NdmpSettingsGlobalGlobal.

        Maximum number of BRE contexts.  # noqa: E501

        :param bre_max_num_contexts: The bre_max_num_contexts of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """

        self._bre_max_num_contexts = bre_max_num_contexts

    @property
    def dma(self):
        """Gets the dma of this NdmpSettingsGlobalGlobal.  # noqa: E501

        A unique identifier for the dma vendor.  # noqa: E501

        :return: The dma of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: str
        """
        return self._dma

    @dma.setter
    def dma(self, dma):
        """Sets the dma of this NdmpSettingsGlobalGlobal.

        A unique identifier for the dma vendor.  # noqa: E501

        :param dma: The dma of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: str
        """
        allowed_values = ["generic", "atempo", "bakbone", "commvault", "emc", "symantec", "tivoli", "symantec-netbackup", "symantec-backupexec"]  # noqa: E501
        if dma not in allowed_values:
            raise ValueError(
                "Invalid value for `dma` ({0}), must be one of {1}"  # noqa: E501
                .format(dma, allowed_values)
            )

        self._dma = dma

    @property
    def msb_context_retention_duration(self):
        """Gets the msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Multi-Stream Backup context retention duration.  # noqa: E501

        :return: The msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._msb_context_retention_duration

    @msb_context_retention_duration.setter
    def msb_context_retention_duration(self, msb_context_retention_duration):
        """Sets the msb_context_retention_duration of this NdmpSettingsGlobalGlobal.

        Multi-Stream Backup context retention duration.  # noqa: E501

        :param msb_context_retention_duration: The msb_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """

        self._msb_context_retention_duration = msb_context_retention_duration

    @property
    def msr_context_retention_duration(self):
        """Gets the msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Multi-Stream Restore context retention duration.  # noqa: E501

        :return: The msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._msr_context_retention_duration

    @msr_context_retention_duration.setter
    def msr_context_retention_duration(self, msr_context_retention_duration):
        """Sets the msr_context_retention_duration of this NdmpSettingsGlobalGlobal.

        Multi-Stream Restore context retention duration.  # noqa: E501

        :param msr_context_retention_duration: The msr_context_retention_duration of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """

        self._msr_context_retention_duration = msr_context_retention_duration

    @property
    def port(self):
        """Gets the port of this NdmpSettingsGlobalGlobal.  # noqa: E501

        The port to listen on.  # noqa: E501

        :return: The port of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NdmpSettingsGlobalGlobal.

        The port to listen on.  # noqa: E501

        :param port: The port of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def service(self):
        """Gets the service of this NdmpSettingsGlobalGlobal.  # noqa: E501

        Property to enable/diable the NDMP service.  # noqa: E501

        :return: The service of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this NdmpSettingsGlobalGlobal.

        Property to enable/diable the NDMP service.  # noqa: E501

        :param service: The service of this NdmpSettingsGlobalGlobal.  # noqa: E501
        :type: bool
        """

        self._service = service

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
        if not isinstance(other, NdmpSettingsGlobalGlobal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
