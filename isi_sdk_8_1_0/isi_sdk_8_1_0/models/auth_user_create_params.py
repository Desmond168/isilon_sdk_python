# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 5
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isi_sdk_8_1_0.models.auth_user import AuthUser  # noqa: F401,E501


class AuthUserCreateParams(object):
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
        'email': 'str',
        'enabled': 'bool',
        'expiry': 'int',
        'gecos': 'str',
        'home_directory': 'str',
        'password': 'str',
        'password_expires': 'bool',
        'primary_group': 'AuthAccessAccessItemFileGroup',
        'prompt_password_change': 'bool',
        'shell': 'str',
        'sid': 'str',
        'uid': 'int',
        'unlock': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'email': 'email',
        'enabled': 'enabled',
        'expiry': 'expiry',
        'gecos': 'gecos',
        'home_directory': 'home_directory',
        'password': 'password',
        'password_expires': 'password_expires',
        'primary_group': 'primary_group',
        'prompt_password_change': 'prompt_password_change',
        'shell': 'shell',
        'sid': 'sid',
        'uid': 'uid',
        'unlock': 'unlock',
        'name': 'name'
    }

    def __init__(self, email=None, enabled=None, expiry=None, gecos=None, home_directory=None, password=None, password_expires=None, primary_group=None, prompt_password_change=None, shell=None, sid=None, uid=None, unlock=None, name=None):  # noqa: E501
        """AuthUserCreateParams - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._enabled = None
        self._expiry = None
        self._gecos = None
        self._home_directory = None
        self._password = None
        self._password_expires = None
        self._primary_group = None
        self._prompt_password_change = None
        self._shell = None
        self._sid = None
        self._uid = None
        self._unlock = None
        self._name = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if enabled is not None:
            self.enabled = enabled
        if expiry is not None:
            self.expiry = expiry
        if gecos is not None:
            self.gecos = gecos
        if home_directory is not None:
            self.home_directory = home_directory
        if password is not None:
            self.password = password
        if password_expires is not None:
            self.password_expires = password_expires
        if primary_group is not None:
            self.primary_group = primary_group
        if prompt_password_change is not None:
            self.prompt_password_change = prompt_password_change
        if shell is not None:
            self.shell = shell
        if sid is not None:
            self.sid = sid
        if uid is not None:
            self.uid = uid
        if unlock is not None:
            self.unlock = unlock
        self.name = name

    @property
    def email(self):
        """Gets the email of this AuthUserCreateParams.  # noqa: E501

        Specifies an email address for the user.  # noqa: E501

        :return: The email of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthUserCreateParams.

        Specifies an email address for the user.  # noqa: E501

        :param email: The email of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and len(email) < 0:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `0`")  # noqa: E501

        self._email = email

    @property
    def enabled(self):
        """Gets the enabled of this AuthUserCreateParams.  # noqa: E501

        If true, the authenticated user is enabled.  # noqa: E501

        :return: The enabled of this AuthUserCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AuthUserCreateParams.

        If true, the authenticated user is enabled.  # noqa: E501

        :param enabled: The enabled of this AuthUserCreateParams.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def expiry(self):
        """Gets the expiry of this AuthUserCreateParams.  # noqa: E501

        Specifies the Unix Epoch time when the auth user will expire.  # noqa: E501

        :return: The expiry of this AuthUserCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this AuthUserCreateParams.

        Specifies the Unix Epoch time when the auth user will expire.  # noqa: E501

        :param expiry: The expiry of this AuthUserCreateParams.  # noqa: E501
        :type: int
        """
        if expiry is not None and expiry > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if expiry is not None and expiry < 0:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._expiry = expiry

    @property
    def gecos(self):
        """Gets the gecos of this AuthUserCreateParams.  # noqa: E501

        Specifies the GECOS value, which is usually the full name.  # noqa: E501

        :return: The gecos of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._gecos

    @gecos.setter
    def gecos(self, gecos):
        """Sets the gecos of this AuthUserCreateParams.

        Specifies the GECOS value, which is usually the full name.  # noqa: E501

        :param gecos: The gecos of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if gecos is not None and len(gecos) > 255:
            raise ValueError("Invalid value for `gecos`, length must be less than or equal to `255`")  # noqa: E501
        if gecos is not None and len(gecos) < 0:
            raise ValueError("Invalid value for `gecos`, length must be greater than or equal to `0`")  # noqa: E501

        self._gecos = gecos

    @property
    def home_directory(self):
        """Gets the home_directory of this AuthUserCreateParams.  # noqa: E501

        Specifies a home directory for the user.  # noqa: E501

        :return: The home_directory of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """Sets the home_directory of this AuthUserCreateParams.

        Specifies a home directory for the user.  # noqa: E501

        :param home_directory: The home_directory of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if home_directory is not None and len(home_directory) > 4096:
            raise ValueError("Invalid value for `home_directory`, length must be less than or equal to `4096`")  # noqa: E501
        if home_directory is not None and len(home_directory) < 0:
            raise ValueError("Invalid value for `home_directory`, length must be greater than or equal to `0`")  # noqa: E501

        self._home_directory = home_directory

    @property
    def password(self):
        """Gets the password of this AuthUserCreateParams.  # noqa: E501

        Changes the password for the user.  # noqa: E501

        :return: The password of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AuthUserCreateParams.

        Changes the password for the user.  # noqa: E501

        :param password: The password of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if password is not None and len(password) > 255:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `255`")  # noqa: E501
        if password is not None and len(password) < 0:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

    @property
    def password_expires(self):
        """Gets the password_expires of this AuthUserCreateParams.  # noqa: E501

        If true, the password should expire.  # noqa: E501

        :return: The password_expires of this AuthUserCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._password_expires

    @password_expires.setter
    def password_expires(self, password_expires):
        """Sets the password_expires of this AuthUserCreateParams.

        If true, the password should expire.  # noqa: E501

        :param password_expires: The password_expires of this AuthUserCreateParams.  # noqa: E501
        :type: bool
        """

        self._password_expires = password_expires

    @property
    def primary_group(self):
        """Gets the primary_group of this AuthUserCreateParams.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The primary_group of this AuthUserCreateParams.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._primary_group

    @primary_group.setter
    def primary_group(self, primary_group):
        """Sets the primary_group of this AuthUserCreateParams.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param primary_group: The primary_group of this AuthUserCreateParams.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._primary_group = primary_group

    @property
    def prompt_password_change(self):
        """Gets the prompt_password_change of this AuthUserCreateParams.  # noqa: E501

        If true, prompts the user to change their password at the next login.  # noqa: E501

        :return: The prompt_password_change of this AuthUserCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._prompt_password_change

    @prompt_password_change.setter
    def prompt_password_change(self, prompt_password_change):
        """Sets the prompt_password_change of this AuthUserCreateParams.

        If true, prompts the user to change their password at the next login.  # noqa: E501

        :param prompt_password_change: The prompt_password_change of this AuthUserCreateParams.  # noqa: E501
        :type: bool
        """

        self._prompt_password_change = prompt_password_change

    @property
    def shell(self):
        """Gets the shell of this AuthUserCreateParams.  # noqa: E501

        Specifies the shell for the user.  # noqa: E501

        :return: The shell of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this AuthUserCreateParams.

        Specifies the shell for the user.  # noqa: E501

        :param shell: The shell of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if shell is not None and len(shell) > 4096:
            raise ValueError("Invalid value for `shell`, length must be less than or equal to `4096`")  # noqa: E501
        if shell is not None and len(shell) < 0:
            raise ValueError("Invalid value for `shell`, length must be greater than or equal to `0`")  # noqa: E501

        self._shell = shell

    @property
    def sid(self):
        """Gets the sid of this AuthUserCreateParams.  # noqa: E501

        Specifies a security identifier.  # noqa: E501

        :return: The sid of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthUserCreateParams.

        Specifies a security identifier.  # noqa: E501

        :param sid: The sid of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if sid is not None and len(sid) > 255:
            raise ValueError("Invalid value for `sid`, length must be less than or equal to `255`")  # noqa: E501
        if sid is not None and len(sid) < 0:
            raise ValueError("Invalid value for `sid`, length must be greater than or equal to `0`")  # noqa: E501

        self._sid = sid

    @property
    def uid(self):
        """Gets the uid of this AuthUserCreateParams.  # noqa: E501

        Specifies a numeric user identifier.  # noqa: E501

        :return: The uid of this AuthUserCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AuthUserCreateParams.

        Specifies a numeric user identifier.  # noqa: E501

        :param uid: The uid of this AuthUserCreateParams.  # noqa: E501
        :type: int
        """
        if uid is not None and uid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if uid is not None and uid < 0:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid = uid

    @property
    def unlock(self):
        """Gets the unlock of this AuthUserCreateParams.  # noqa: E501

        If true, the user account should be unlocked.  # noqa: E501

        :return: The unlock of this AuthUserCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._unlock

    @unlock.setter
    def unlock(self, unlock):
        """Sets the unlock of this AuthUserCreateParams.

        If true, the user account should be unlocked.  # noqa: E501

        :param unlock: The unlock of this AuthUserCreateParams.  # noqa: E501
        :type: bool
        """

        self._unlock = unlock

    @property
    def name(self):
        """Gets the name of this AuthUserCreateParams.  # noqa: E501

        Specifies a user name.  # noqa: E501

        :return: The name of this AuthUserCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthUserCreateParams.

        Specifies a user name.  # noqa: E501

        :param name: The name of this AuthUserCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, AuthUserCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
