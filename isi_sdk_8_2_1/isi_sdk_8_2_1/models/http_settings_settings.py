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


class HttpSettingsSettings(object):
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
        'access_control': 'bool',
        'basic_authentication': 'bool',
        'dav': 'bool',
        'enable_access_log': 'bool',
        'https': 'bool',
        'integrated_authentication': 'bool',
        'server_root': 'str',
        'service': 'str'
    }

    attribute_map = {
        'access_control': 'access_control',
        'basic_authentication': 'basic_authentication',
        'dav': 'dav',
        'enable_access_log': 'enable_access_log',
        'https': 'https',
        'integrated_authentication': 'integrated_authentication',
        'server_root': 'server_root',
        'service': 'service'
    }

    def __init__(self, access_control=None, basic_authentication=None, dav=None, enable_access_log=None, https=None, integrated_authentication=None, server_root=None, service=None):  # noqa: E501
        """HttpSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._access_control = None
        self._basic_authentication = None
        self._dav = None
        self._enable_access_log = None
        self._https = None
        self._integrated_authentication = None
        self._server_root = None
        self._service = None
        self.discriminator = None

        if access_control is not None:
            self.access_control = access_control
        if basic_authentication is not None:
            self.basic_authentication = basic_authentication
        if dav is not None:
            self.dav = dav
        if enable_access_log is not None:
            self.enable_access_log = enable_access_log
        if https is not None:
            self.https = https
        if integrated_authentication is not None:
            self.integrated_authentication = integrated_authentication
        if server_root is not None:
            self.server_root = server_root
        if service is not None:
            self.service = service

    @property
    def access_control(self):
        """Gets the access_control of this HttpSettingsSettings.  # noqa: E501

        Enable Access Control Authentication  # noqa: E501

        :return: The access_control of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        """Sets the access_control of this HttpSettingsSettings.

        Enable Access Control Authentication  # noqa: E501

        :param access_control: The access_control of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._access_control = access_control

    @property
    def basic_authentication(self):
        """Gets the basic_authentication of this HttpSettingsSettings.  # noqa: E501

        Enable Basic Authentication  # noqa: E501

        :return: The basic_authentication of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._basic_authentication

    @basic_authentication.setter
    def basic_authentication(self, basic_authentication):
        """Sets the basic_authentication of this HttpSettingsSettings.

        Enable Basic Authentication  # noqa: E501

        :param basic_authentication: The basic_authentication of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._basic_authentication = basic_authentication

    @property
    def dav(self):
        """Gets the dav of this HttpSettingsSettings.  # noqa: E501

        Enable DAV specification  # noqa: E501

        :return: The dav of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._dav

    @dav.setter
    def dav(self, dav):
        """Sets the dav of this HttpSettingsSettings.

        Enable DAV specification  # noqa: E501

        :param dav: The dav of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._dav = dav

    @property
    def enable_access_log(self):
        """Gets the enable_access_log of this HttpSettingsSettings.  # noqa: E501

        Enable HTTP access logging  # noqa: E501

        :return: The enable_access_log of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_access_log

    @enable_access_log.setter
    def enable_access_log(self, enable_access_log):
        """Sets the enable_access_log of this HttpSettingsSettings.

        Enable HTTP access logging  # noqa: E501

        :param enable_access_log: The enable_access_log of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._enable_access_log = enable_access_log

    @property
    def https(self):
        """Gets the https of this HttpSettingsSettings.  # noqa: E501

        Use HTTPS transport  # noqa: E501

        :return: The https of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this HttpSettingsSettings.

        Use HTTPS transport  # noqa: E501

        :param https: The https of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._https = https

    @property
    def integrated_authentication(self):
        """Gets the integrated_authentication of this HttpSettingsSettings.  # noqa: E501

        Enable Integrated Authentication  # noqa: E501

        :return: The integrated_authentication of this HttpSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._integrated_authentication

    @integrated_authentication.setter
    def integrated_authentication(self, integrated_authentication):
        """Sets the integrated_authentication of this HttpSettingsSettings.

        Enable Integrated Authentication  # noqa: E501

        :param integrated_authentication: The integrated_authentication of this HttpSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._integrated_authentication = integrated_authentication

    @property
    def server_root(self):
        """Gets the server_root of this HttpSettingsSettings.  # noqa: E501

        Document root directory. Must be within /ifs.  # noqa: E501

        :return: The server_root of this HttpSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._server_root

    @server_root.setter
    def server_root(self, server_root):
        """Sets the server_root of this HttpSettingsSettings.

        Document root directory. Must be within /ifs.  # noqa: E501

        :param server_root: The server_root of this HttpSettingsSettings.  # noqa: E501
        :type: str
        """

        self._server_root = server_root

    @property
    def service(self):
        """Gets the service of this HttpSettingsSettings.  # noqa: E501

        Enable/disable the HTTP service or redirect to WebUI.  # noqa: E501

        :return: The service of this HttpSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this HttpSettingsSettings.

        Enable/disable the HTTP service or redirect to WebUI.  # noqa: E501

        :param service: The service of this HttpSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled", "redirect"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

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
        if not isinstance(other, HttpSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
