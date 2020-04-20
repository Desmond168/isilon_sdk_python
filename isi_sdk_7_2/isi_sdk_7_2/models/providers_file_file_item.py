# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProvidersFileFileItem(object):
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
        'authentication': 'bool',
        'cache_entry_expiry': 'int',
        'create_home_directory': 'bool',
        'enabled': 'bool',
        'enumerate_groups': 'bool',
        'enumerate_users': 'bool',
        'findable_groups': 'list[str]',
        'findable_users': 'list[str]',
        'group_domain': 'str',
        'group_file': 'str',
        'home_directory_template': 'str',
        'id': 'str',
        'listable_groups': 'list[str]',
        'listable_users': 'list[str]',
        'login_shell': 'str',
        'modifiable_groups': 'list[str]',
        'modifiable_users': 'list[str]',
        'name': 'str',
        'netgroup_file': 'str',
        'normalize_groups': 'bool',
        'normalize_users': 'bool',
        'ntlm_support': 'str',
        'password_file': 'str',
        'provider_domain': 'str',
        'restrict_findable': 'bool',
        'restrict_listable': 'bool',
        'restrict_modifiable': 'bool',
        'status': 'str',
        'system': 'bool',
        'unfindable_groups': 'list[str]',
        'unfindable_users': 'list[str]',
        'unlistable_groups': 'list[str]',
        'unlistable_users': 'list[str]',
        'unmodifiable_groups': 'list[str]',
        'unmodifiable_users': 'list[str]',
        'user_domain': 'str'
    }

    attribute_map = {
        'authentication': 'authentication',
        'cache_entry_expiry': 'cache_entry_expiry',
        'create_home_directory': 'create_home_directory',
        'enabled': 'enabled',
        'enumerate_groups': 'enumerate_groups',
        'enumerate_users': 'enumerate_users',
        'findable_groups': 'findable_groups',
        'findable_users': 'findable_users',
        'group_domain': 'group_domain',
        'group_file': 'group_file',
        'home_directory_template': 'home_directory_template',
        'id': 'id',
        'listable_groups': 'listable_groups',
        'listable_users': 'listable_users',
        'login_shell': 'login_shell',
        'modifiable_groups': 'modifiable_groups',
        'modifiable_users': 'modifiable_users',
        'name': 'name',
        'netgroup_file': 'netgroup_file',
        'normalize_groups': 'normalize_groups',
        'normalize_users': 'normalize_users',
        'ntlm_support': 'ntlm_support',
        'password_file': 'password_file',
        'provider_domain': 'provider_domain',
        'restrict_findable': 'restrict_findable',
        'restrict_listable': 'restrict_listable',
        'restrict_modifiable': 'restrict_modifiable',
        'status': 'status',
        'system': 'system',
        'unfindable_groups': 'unfindable_groups',
        'unfindable_users': 'unfindable_users',
        'unlistable_groups': 'unlistable_groups',
        'unlistable_users': 'unlistable_users',
        'unmodifiable_groups': 'unmodifiable_groups',
        'unmodifiable_users': 'unmodifiable_users',
        'user_domain': 'user_domain'
    }

    def __init__(self, authentication=None, cache_entry_expiry=None, create_home_directory=None, enabled=None, enumerate_groups=None, enumerate_users=None, findable_groups=None, findable_users=None, group_domain=None, group_file=None, home_directory_template=None, id=None, listable_groups=None, listable_users=None, login_shell=None, modifiable_groups=None, modifiable_users=None, name=None, netgroup_file=None, normalize_groups=None, normalize_users=None, ntlm_support=None, password_file=None, provider_domain=None, restrict_findable=None, restrict_listable=None, restrict_modifiable=None, status=None, system=None, unfindable_groups=None, unfindable_users=None, unlistable_groups=None, unlistable_users=None, unmodifiable_groups=None, unmodifiable_users=None, user_domain=None):  # noqa: E501
        """ProvidersFileFileItem - a model defined in Swagger"""  # noqa: E501

        self._authentication = None
        self._cache_entry_expiry = None
        self._create_home_directory = None
        self._enabled = None
        self._enumerate_groups = None
        self._enumerate_users = None
        self._findable_groups = None
        self._findable_users = None
        self._group_domain = None
        self._group_file = None
        self._home_directory_template = None
        self._id = None
        self._listable_groups = None
        self._listable_users = None
        self._login_shell = None
        self._modifiable_groups = None
        self._modifiable_users = None
        self._name = None
        self._netgroup_file = None
        self._normalize_groups = None
        self._normalize_users = None
        self._ntlm_support = None
        self._password_file = None
        self._provider_domain = None
        self._restrict_findable = None
        self._restrict_listable = None
        self._restrict_modifiable = None
        self._status = None
        self._system = None
        self._unfindable_groups = None
        self._unfindable_users = None
        self._unlistable_groups = None
        self._unlistable_users = None
        self._unmodifiable_groups = None
        self._unmodifiable_users = None
        self._user_domain = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if cache_entry_expiry is not None:
            self.cache_entry_expiry = cache_entry_expiry
        if create_home_directory is not None:
            self.create_home_directory = create_home_directory
        if enabled is not None:
            self.enabled = enabled
        if enumerate_groups is not None:
            self.enumerate_groups = enumerate_groups
        if enumerate_users is not None:
            self.enumerate_users = enumerate_users
        if findable_groups is not None:
            self.findable_groups = findable_groups
        if findable_users is not None:
            self.findable_users = findable_users
        if group_domain is not None:
            self.group_domain = group_domain
        if group_file is not None:
            self.group_file = group_file
        if home_directory_template is not None:
            self.home_directory_template = home_directory_template
        if id is not None:
            self.id = id
        if listable_groups is not None:
            self.listable_groups = listable_groups
        if listable_users is not None:
            self.listable_users = listable_users
        if login_shell is not None:
            self.login_shell = login_shell
        if modifiable_groups is not None:
            self.modifiable_groups = modifiable_groups
        if modifiable_users is not None:
            self.modifiable_users = modifiable_users
        if name is not None:
            self.name = name
        if netgroup_file is not None:
            self.netgroup_file = netgroup_file
        if normalize_groups is not None:
            self.normalize_groups = normalize_groups
        if normalize_users is not None:
            self.normalize_users = normalize_users
        if ntlm_support is not None:
            self.ntlm_support = ntlm_support
        if password_file is not None:
            self.password_file = password_file
        if provider_domain is not None:
            self.provider_domain = provider_domain
        if restrict_findable is not None:
            self.restrict_findable = restrict_findable
        if restrict_listable is not None:
            self.restrict_listable = restrict_listable
        if restrict_modifiable is not None:
            self.restrict_modifiable = restrict_modifiable
        if status is not None:
            self.status = status
        if system is not None:
            self.system = system
        if unfindable_groups is not None:
            self.unfindable_groups = unfindable_groups
        if unfindable_users is not None:
            self.unfindable_users = unfindable_users
        if unlistable_groups is not None:
            self.unlistable_groups = unlistable_groups
        if unlistable_users is not None:
            self.unlistable_users = unlistable_users
        if unmodifiable_groups is not None:
            self.unmodifiable_groups = unmodifiable_groups
        if unmodifiable_users is not None:
            self.unmodifiable_users = unmodifiable_users
        if user_domain is not None:
            self.user_domain = user_domain

    @property
    def authentication(self):
        """Gets the authentication of this ProvidersFileFileItem.  # noqa: E501

        Enables use of provider for authentication as well as identity.  # noqa: E501

        :return: The authentication of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ProvidersFileFileItem.

        Enables use of provider for authentication as well as identity.  # noqa: E501

        :param authentication: The authentication of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._authentication = authentication

    @property
    def cache_entry_expiry(self):
        """Gets the cache_entry_expiry of this ProvidersFileFileItem.  # noqa: E501

        Specifies amount of time in seconds to cache a user/group.  # noqa: E501

        :return: The cache_entry_expiry of this ProvidersFileFileItem.  # noqa: E501
        :rtype: int
        """
        return self._cache_entry_expiry

    @cache_entry_expiry.setter
    def cache_entry_expiry(self, cache_entry_expiry):
        """Sets the cache_entry_expiry of this ProvidersFileFileItem.

        Specifies amount of time in seconds to cache a user/group.  # noqa: E501

        :param cache_entry_expiry: The cache_entry_expiry of this ProvidersFileFileItem.  # noqa: E501
        :type: int
        """

        self._cache_entry_expiry = cache_entry_expiry

    @property
    def create_home_directory(self):
        """Gets the create_home_directory of this ProvidersFileFileItem.  # noqa: E501

        Automatically create home directory on first login.  # noqa: E501

        :return: The create_home_directory of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """Sets the create_home_directory of this ProvidersFileFileItem.

        Automatically create home directory on first login.  # noqa: E501

        :param create_home_directory: The create_home_directory of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._create_home_directory = create_home_directory

    @property
    def enabled(self):
        """Gets the enabled of this ProvidersFileFileItem.  # noqa: E501

        Enables the file provider.  # noqa: E501

        :return: The enabled of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProvidersFileFileItem.

        Enables the file provider.  # noqa: E501

        :param enabled: The enabled of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def enumerate_groups(self):
        """Gets the enumerate_groups of this ProvidersFileFileItem.  # noqa: E501

        Enables provider to enumerate groups.  # noqa: E501

        :return: The enumerate_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._enumerate_groups

    @enumerate_groups.setter
    def enumerate_groups(self, enumerate_groups):
        """Sets the enumerate_groups of this ProvidersFileFileItem.

        Enables provider to enumerate groups.  # noqa: E501

        :param enumerate_groups: The enumerate_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._enumerate_groups = enumerate_groups

    @property
    def enumerate_users(self):
        """Gets the enumerate_users of this ProvidersFileFileItem.  # noqa: E501

        Enables provider to enumerate users.  # noqa: E501

        :return: The enumerate_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._enumerate_users

    @enumerate_users.setter
    def enumerate_users(self, enumerate_users):
        """Sets the enumerate_users of this ProvidersFileFileItem.

        Enables provider to enumerate users.  # noqa: E501

        :param enumerate_users: The enumerate_users of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._enumerate_users = enumerate_users

    @property
    def findable_groups(self):
        """Gets the findable_groups of this ProvidersFileFileItem.  # noqa: E501

        Sets list of groups that can be resolved.  # noqa: E501

        :return: The findable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._findable_groups

    @findable_groups.setter
    def findable_groups(self, findable_groups):
        """Sets the findable_groups of this ProvidersFileFileItem.

        Sets list of groups that can be resolved.  # noqa: E501

        :param findable_groups: The findable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._findable_groups = findable_groups

    @property
    def findable_users(self):
        """Gets the findable_users of this ProvidersFileFileItem.  # noqa: E501

        Sets list of users that can be resolved.  # noqa: E501

        :return: The findable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._findable_users

    @findable_users.setter
    def findable_users(self, findable_users):
        """Sets the findable_users of this ProvidersFileFileItem.

        Sets list of users that can be resolved.  # noqa: E501

        :param findable_users: The findable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._findable_users = findable_users

    @property
    def group_domain(self):
        """Gets the group_domain of this ProvidersFileFileItem.  # noqa: E501

        Domain used to qualify groups for this provider.  # noqa: E501

        :return: The group_domain of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._group_domain

    @group_domain.setter
    def group_domain(self, group_domain):
        """Sets the group_domain of this ProvidersFileFileItem.

        Domain used to qualify groups for this provider.  # noqa: E501

        :param group_domain: The group_domain of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._group_domain = group_domain

    @property
    def group_file(self):
        """Gets the group_file of this ProvidersFileFileItem.  # noqa: E501

        Location of the file containing group information.  # noqa: E501

        :return: The group_file of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._group_file

    @group_file.setter
    def group_file(self, group_file):
        """Sets the group_file of this ProvidersFileFileItem.

        Location of the file containing group information.  # noqa: E501

        :param group_file: The group_file of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._group_file = group_file

    @property
    def home_directory_template(self):
        """Gets the home_directory_template of this ProvidersFileFileItem.  # noqa: E501

        Specifies home directory template path.  # noqa: E501

        :return: The home_directory_template of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """Sets the home_directory_template of this ProvidersFileFileItem.

        Specifies home directory template path.  # noqa: E501

        :param home_directory_template: The home_directory_template of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._home_directory_template = home_directory_template

    @property
    def id(self):
        """Gets the id of this ProvidersFileFileItem.  # noqa: E501

        Specifies file provider ID.  # noqa: E501

        :return: The id of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvidersFileFileItem.

        Specifies file provider ID.  # noqa: E501

        :param id: The id of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def listable_groups(self):
        """Gets the listable_groups of this ProvidersFileFileItem.  # noqa: E501

        Specifies groups that can be viewed in the provider.  # noqa: E501

        :return: The listable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._listable_groups

    @listable_groups.setter
    def listable_groups(self, listable_groups):
        """Sets the listable_groups of this ProvidersFileFileItem.

        Specifies groups that can be viewed in the provider.  # noqa: E501

        :param listable_groups: The listable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._listable_groups = listable_groups

    @property
    def listable_users(self):
        """Gets the listable_users of this ProvidersFileFileItem.  # noqa: E501

        Specifies users that can be viewed in the provider.  # noqa: E501

        :return: The listable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._listable_users

    @listable_users.setter
    def listable_users(self, listable_users):
        """Sets the listable_users of this ProvidersFileFileItem.

        Specifies users that can be viewed in the provider.  # noqa: E501

        :param listable_users: The listable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._listable_users = listable_users

    @property
    def login_shell(self):
        """Gets the login_shell of this ProvidersFileFileItem.  # noqa: E501

        Sets login shell path.  # noqa: E501

        :return: The login_shell of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """Sets the login_shell of this ProvidersFileFileItem.

        Sets login shell path.  # noqa: E501

        :param login_shell: The login_shell of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._login_shell = login_shell

    @property
    def modifiable_groups(self):
        """Gets the modifiable_groups of this ProvidersFileFileItem.  # noqa: E501

        Specifies groups that can be modified in the provider.  # noqa: E501

        :return: The modifiable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._modifiable_groups

    @modifiable_groups.setter
    def modifiable_groups(self, modifiable_groups):
        """Sets the modifiable_groups of this ProvidersFileFileItem.

        Specifies groups that can be modified in the provider.  # noqa: E501

        :param modifiable_groups: The modifiable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._modifiable_groups = modifiable_groups

    @property
    def modifiable_users(self):
        """Gets the modifiable_users of this ProvidersFileFileItem.  # noqa: E501

        Specifies users that can be modified in the provider.  # noqa: E501

        :return: The modifiable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._modifiable_users

    @modifiable_users.setter
    def modifiable_users(self, modifiable_users):
        """Sets the modifiable_users of this ProvidersFileFileItem.

        Specifies users that can be modified in the provider.  # noqa: E501

        :param modifiable_users: The modifiable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._modifiable_users = modifiable_users

    @property
    def name(self):
        """Gets the name of this ProvidersFileFileItem.  # noqa: E501

        Specifies file provider name.  # noqa: E501

        :return: The name of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersFileFileItem.

        Specifies file provider name.  # noqa: E501

        :param name: The name of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def netgroup_file(self):
        """Gets the netgroup_file of this ProvidersFileFileItem.  # noqa: E501

        Path to a netgroups replacement file.  # noqa: E501

        :return: The netgroup_file of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._netgroup_file

    @netgroup_file.setter
    def netgroup_file(self, netgroup_file):
        """Sets the netgroup_file of this ProvidersFileFileItem.

        Path to a netgroups replacement file.  # noqa: E501

        :param netgroup_file: The netgroup_file of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._netgroup_file = netgroup_file

    @property
    def normalize_groups(self):
        """Gets the normalize_groups of this ProvidersFileFileItem.  # noqa: E501

        Normalizes group name to lowercase before lookup.  # noqa: E501

        :return: The normalize_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_groups

    @normalize_groups.setter
    def normalize_groups(self, normalize_groups):
        """Sets the normalize_groups of this ProvidersFileFileItem.

        Normalizes group name to lowercase before lookup.  # noqa: E501

        :param normalize_groups: The normalize_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._normalize_groups = normalize_groups

    @property
    def normalize_users(self):
        """Gets the normalize_users of this ProvidersFileFileItem.  # noqa: E501

        Normalizes user name to lowercase before lookup.  # noqa: E501

        :return: The normalize_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_users

    @normalize_users.setter
    def normalize_users(self, normalize_users):
        """Sets the normalize_users of this ProvidersFileFileItem.

        Normalizes user name to lowercase before lookup.  # noqa: E501

        :param normalize_users: The normalize_users of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._normalize_users = normalize_users

    @property
    def ntlm_support(self):
        """Gets the ntlm_support of this ProvidersFileFileItem.  # noqa: E501

        For users with NTLM-compatible credentials, specify what NTLM versions to support.  # noqa: E501

        :return: The ntlm_support of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._ntlm_support

    @ntlm_support.setter
    def ntlm_support(self, ntlm_support):
        """Sets the ntlm_support of this ProvidersFileFileItem.

        For users with NTLM-compatible credentials, specify what NTLM versions to support.  # noqa: E501

        :param ntlm_support: The ntlm_support of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "v2only", "none"]  # noqa: E501
        if ntlm_support not in allowed_values:
            raise ValueError(
                "Invalid value for `ntlm_support` ({0}), must be one of {1}"  # noqa: E501
                .format(ntlm_support, allowed_values)
            )

        self._ntlm_support = ntlm_support

    @property
    def password_file(self):
        """Gets the password_file of this ProvidersFileFileItem.  # noqa: E501

        Location of the file containing user information.  # noqa: E501

        :return: The password_file of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._password_file

    @password_file.setter
    def password_file(self, password_file):
        """Sets the password_file of this ProvidersFileFileItem.

        Location of the file containing user information.  # noqa: E501

        :param password_file: The password_file of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._password_file = password_file

    @property
    def provider_domain(self):
        """Gets the provider_domain of this ProvidersFileFileItem.  # noqa: E501

        Specifies the provider domain.  # noqa: E501

        :return: The provider_domain of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._provider_domain

    @provider_domain.setter
    def provider_domain(self, provider_domain):
        """Sets the provider_domain of this ProvidersFileFileItem.

        Specifies the provider domain.  # noqa: E501

        :param provider_domain: The provider_domain of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._provider_domain = provider_domain

    @property
    def restrict_findable(self):
        """Gets the restrict_findable of this ProvidersFileFileItem.  # noqa: E501

        Check the provider for filtered lists of findable and unfindable users and groups.  # noqa: E501

        :return: The restrict_findable of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_findable

    @restrict_findable.setter
    def restrict_findable(self, restrict_findable):
        """Sets the restrict_findable of this ProvidersFileFileItem.

        Check the provider for filtered lists of findable and unfindable users and groups.  # noqa: E501

        :param restrict_findable: The restrict_findable of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._restrict_findable = restrict_findable

    @property
    def restrict_listable(self):
        """Gets the restrict_listable of this ProvidersFileFileItem.  # noqa: E501

        Check the provider for filtered lists of listable and unlistable users and groups.  # noqa: E501

        :return: The restrict_listable of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_listable

    @restrict_listable.setter
    def restrict_listable(self, restrict_listable):
        """Sets the restrict_listable of this ProvidersFileFileItem.

        Check the provider for filtered lists of listable and unlistable users and groups.  # noqa: E501

        :param restrict_listable: The restrict_listable of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._restrict_listable = restrict_listable

    @property
    def restrict_modifiable(self):
        """Gets the restrict_modifiable of this ProvidersFileFileItem.  # noqa: E501

        Check the provider for filtered lists of modifiable and unmodifiable users and groups.  # noqa: E501

        :return: The restrict_modifiable of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_modifiable

    @restrict_modifiable.setter
    def restrict_modifiable(self, restrict_modifiable):
        """Sets the restrict_modifiable of this ProvidersFileFileItem.

        Check the provider for filtered lists of modifiable and unmodifiable users and groups.  # noqa: E501

        :param restrict_modifiable: The restrict_modifiable of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._restrict_modifiable = restrict_modifiable

    @property
    def status(self):
        """Gets the status of this ProvidersFileFileItem.  # noqa: E501

        The status of the provider.  # noqa: E501

        :return: The status of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProvidersFileFileItem.

        The status of the provider.  # noqa: E501

        :param status: The status of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def system(self):
        """Gets the system of this ProvidersFileFileItem.  # noqa: E501

        If true, this provider instance was created by OneFS and cannot be removed.  # noqa: E501

        :return: The system of this ProvidersFileFileItem.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this ProvidersFileFileItem.

        If true, this provider instance was created by OneFS and cannot be removed.  # noqa: E501

        :param system: The system of this ProvidersFileFileItem.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def unfindable_groups(self):
        """Gets the unfindable_groups of this ProvidersFileFileItem.  # noqa: E501

        Specifies a group that cannot be resolved by the provider.  # noqa: E501

        :return: The unfindable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unfindable_groups

    @unfindable_groups.setter
    def unfindable_groups(self, unfindable_groups):
        """Sets the unfindable_groups of this ProvidersFileFileItem.

        Specifies a group that cannot be resolved by the provider.  # noqa: E501

        :param unfindable_groups: The unfindable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unfindable_groups = unfindable_groups

    @property
    def unfindable_users(self):
        """Gets the unfindable_users of this ProvidersFileFileItem.  # noqa: E501

        Specifies a group that cannot be resolved by the provider.  # noqa: E501

        :return: The unfindable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unfindable_users

    @unfindable_users.setter
    def unfindable_users(self, unfindable_users):
        """Sets the unfindable_users of this ProvidersFileFileItem.

        Specifies a group that cannot be resolved by the provider.  # noqa: E501

        :param unfindable_users: The unfindable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unfindable_users = unfindable_users

    @property
    def unlistable_groups(self):
        """Gets the unlistable_groups of this ProvidersFileFileItem.  # noqa: E501

        Specifies a group that cannot be listed by the provider.  # noqa: E501

        :return: The unlistable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unlistable_groups

    @unlistable_groups.setter
    def unlistable_groups(self, unlistable_groups):
        """Sets the unlistable_groups of this ProvidersFileFileItem.

        Specifies a group that cannot be listed by the provider.  # noqa: E501

        :param unlistable_groups: The unlistable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unlistable_groups = unlistable_groups

    @property
    def unlistable_users(self):
        """Gets the unlistable_users of this ProvidersFileFileItem.  # noqa: E501

        Specifies a user that cannot be listed by the provider.  # noqa: E501

        :return: The unlistable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unlistable_users

    @unlistable_users.setter
    def unlistable_users(self, unlistable_users):
        """Sets the unlistable_users of this ProvidersFileFileItem.

        Specifies a user that cannot be listed by the provider.  # noqa: E501

        :param unlistable_users: The unlistable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unlistable_users = unlistable_users

    @property
    def unmodifiable_groups(self):
        """Gets the unmodifiable_groups of this ProvidersFileFileItem.  # noqa: E501

        Specifies a group that cannot be modified by the provider.  # noqa: E501

        :return: The unmodifiable_groups of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unmodifiable_groups

    @unmodifiable_groups.setter
    def unmodifiable_groups(self, unmodifiable_groups):
        """Sets the unmodifiable_groups of this ProvidersFileFileItem.

        Specifies a group that cannot be modified by the provider.  # noqa: E501

        :param unmodifiable_groups: The unmodifiable_groups of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unmodifiable_groups = unmodifiable_groups

    @property
    def unmodifiable_users(self):
        """Gets the unmodifiable_users of this ProvidersFileFileItem.  # noqa: E501

        Specifies a user that cannot be modified by the provider.  # noqa: E501

        :return: The unmodifiable_users of this ProvidersFileFileItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unmodifiable_users

    @unmodifiable_users.setter
    def unmodifiable_users(self, unmodifiable_users):
        """Sets the unmodifiable_users of this ProvidersFileFileItem.

        Specifies a user that cannot be modified by the provider.  # noqa: E501

        :param unmodifiable_users: The unmodifiable_users of this ProvidersFileFileItem.  # noqa: E501
        :type: list[str]
        """

        self._unmodifiable_users = unmodifiable_users

    @property
    def user_domain(self):
        """Gets the user_domain of this ProvidersFileFileItem.  # noqa: E501

        Domain used to qualify users for this provider.  # noqa: E501

        :return: The user_domain of this ProvidersFileFileItem.  # noqa: E501
        :rtype: str
        """
        return self._user_domain

    @user_domain.setter
    def user_domain(self, user_domain):
        """Sets the user_domain of this ProvidersFileFileItem.

        Domain used to qualify users for this provider.  # noqa: E501

        :param user_domain: The user_domain of this ProvidersFileFileItem.  # noqa: E501
        :type: str
        """

        self._user_domain = user_domain

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
        if not isinstance(other, ProvidersFileFileItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
