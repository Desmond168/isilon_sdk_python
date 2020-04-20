# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SmbSession(object):
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
        'active_time': 'int',
        'client_type': 'str',
        'computer': 'str',
        'encryption': 'bool',
        'guest_login': 'bool',
        'id': 'int',
        'idle_time': 'int',
        'openfiles': 'int',
        'user': 'str'
    }

    attribute_map = {
        'active_time': 'active_time',
        'client_type': 'client_type',
        'computer': 'computer',
        'encryption': 'encryption',
        'guest_login': 'guest_login',
        'id': 'id',
        'idle_time': 'idle_time',
        'openfiles': 'openfiles',
        'user': 'user'
    }

    def __init__(self, active_time=None, client_type=None, computer=None, encryption=None, guest_login=None, id=None, idle_time=None, openfiles=None, user=None):  # noqa: E501
        """SmbSession - a model defined in Swagger"""  # noqa: E501

        self._active_time = None
        self._client_type = None
        self._computer = None
        self._encryption = None
        self._guest_login = None
        self._id = None
        self._idle_time = None
        self._openfiles = None
        self._user = None
        self.discriminator = None

        self.active_time = active_time
        self.client_type = client_type
        self.computer = computer
        self.encryption = encryption
        self.guest_login = guest_login
        self.id = id
        self.idle_time = idle_time
        self.openfiles = openfiles
        self.user = user

    @property
    def active_time(self):
        """Gets the active_time of this SmbSession.  # noqa: E501

        Number of seconds since session start.  # noqa: E501

        :return: The active_time of this SmbSession.  # noqa: E501
        :rtype: int
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this SmbSession.

        Number of seconds since session start.  # noqa: E501

        :param active_time: The active_time of this SmbSession.  # noqa: E501
        :type: int
        """
        if active_time is None:
            raise ValueError("Invalid value for `active_time`, must not be `None`")  # noqa: E501

        self._active_time = active_time

    @property
    def client_type(self):
        """Gets the client_type of this SmbSession.  # noqa: E501

        Client type.  # noqa: E501

        :return: The client_type of this SmbSession.  # noqa: E501
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this SmbSession.

        Client type.  # noqa: E501

        :param client_type: The client_type of this SmbSession.  # noqa: E501
        :type: str
        """
        if client_type is None:
            raise ValueError("Invalid value for `client_type`, must not be `None`")  # noqa: E501

        self._client_type = client_type

    @property
    def computer(self):
        """Gets the computer of this SmbSession.  # noqa: E501

        Client internet address.  # noqa: E501

        :return: The computer of this SmbSession.  # noqa: E501
        :rtype: str
        """
        return self._computer

    @computer.setter
    def computer(self, computer):
        """Sets the computer of this SmbSession.

        Client internet address.  # noqa: E501

        :param computer: The computer of this SmbSession.  # noqa: E501
        :type: str
        """
        if computer is None:
            raise ValueError("Invalid value for `computer`, must not be `None`")  # noqa: E501

        self._computer = computer

    @property
    def encryption(self):
        """Gets the encryption of this SmbSession.  # noqa: E501

        True if session is encrypted.  # noqa: E501

        :return: The encryption of this SmbSession.  # noqa: E501
        :rtype: bool
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this SmbSession.

        True if session is encrypted.  # noqa: E501

        :param encryption: The encryption of this SmbSession.  # noqa: E501
        :type: bool
        """
        if encryption is None:
            raise ValueError("Invalid value for `encryption`, must not be `None`")  # noqa: E501

        self._encryption = encryption

    @property
    def guest_login(self):
        """Gets the guest_login of this SmbSession.  # noqa: E501

        True for guest logins.  # noqa: E501

        :return: The guest_login of this SmbSession.  # noqa: E501
        :rtype: bool
        """
        return self._guest_login

    @guest_login.setter
    def guest_login(self, guest_login):
        """Sets the guest_login of this SmbSession.

        True for guest logins.  # noqa: E501

        :param guest_login: The guest_login of this SmbSession.  # noqa: E501
        :type: bool
        """
        if guest_login is None:
            raise ValueError("Invalid value for `guest_login`, must not be `None`")  # noqa: E501

        self._guest_login = guest_login

    @property
    def id(self):
        """Gets the id of this SmbSession.  # noqa: E501

        The session ID.  # noqa: E501

        :return: The id of this SmbSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbSession.

        The session ID.  # noqa: E501

        :param id: The id of this SmbSession.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def idle_time(self):
        """Gets the idle_time of this SmbSession.  # noqa: E501

        Number of seconds since last client operation.  # noqa: E501

        :return: The idle_time of this SmbSession.  # noqa: E501
        :rtype: int
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        """Sets the idle_time of this SmbSession.

        Number of seconds since last client operation.  # noqa: E501

        :param idle_time: The idle_time of this SmbSession.  # noqa: E501
        :type: int
        """
        if idle_time is None:
            raise ValueError("Invalid value for `idle_time`, must not be `None`")  # noqa: E501

        self._idle_time = idle_time

    @property
    def openfiles(self):
        """Gets the openfiles of this SmbSession.  # noqa: E501

        Number of files open by client.  # noqa: E501

        :return: The openfiles of this SmbSession.  # noqa: E501
        :rtype: int
        """
        return self._openfiles

    @openfiles.setter
    def openfiles(self, openfiles):
        """Sets the openfiles of this SmbSession.

        Number of files open by client.  # noqa: E501

        :param openfiles: The openfiles of this SmbSession.  # noqa: E501
        :type: int
        """
        if openfiles is None:
            raise ValueError("Invalid value for `openfiles`, must not be `None`")  # noqa: E501

        self._openfiles = openfiles

    @property
    def user(self):
        """Gets the user of this SmbSession.  # noqa: E501

        Local user name.  # noqa: E501

        :return: The user of this SmbSession.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SmbSession.

        Local user name.  # noqa: E501

        :param user: The user of this SmbSession.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, SmbSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
