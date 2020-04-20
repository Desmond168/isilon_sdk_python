# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 3
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SettingsAclsExtended(object):
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
        'access': 'str',
        'calcmode': 'str',
        'calcmode_group': 'str',
        'calcmode_owner': 'str',
        'chmod': 'str',
        'chmod_007': 'str',
        'chmod_inheritable': 'str',
        'chown': 'str',
        'create_over_smb': 'str',
        'dos_attr': 'str',
        'group_owner_inheritance': 'str',
        'rwx': 'str',
        'synthetic_denies': 'str',
        'utimes': 'str'
    }

    attribute_map = {
        'access': 'access',
        'calcmode': 'calcmode',
        'calcmode_group': 'calcmode_group',
        'calcmode_owner': 'calcmode_owner',
        'chmod': 'chmod',
        'chmod_007': 'chmod_007',
        'chmod_inheritable': 'chmod_inheritable',
        'chown': 'chown',
        'create_over_smb': 'create_over_smb',
        'dos_attr': 'dos_attr',
        'group_owner_inheritance': 'group_owner_inheritance',
        'rwx': 'rwx',
        'synthetic_denies': 'synthetic_denies',
        'utimes': 'utimes'
    }

    def __init__(self, access=None, calcmode=None, calcmode_group=None, calcmode_owner=None, chmod=None, chmod_007=None, chmod_inheritable=None, chown=None, create_over_smb=None, dos_attr=None, group_owner_inheritance=None, rwx=None, synthetic_denies=None, utimes=None):  # noqa: E501
        """SettingsAclsExtended - a model defined in Swagger"""  # noqa: E501

        self._access = None
        self._calcmode = None
        self._calcmode_group = None
        self._calcmode_owner = None
        self._chmod = None
        self._chmod_007 = None
        self._chmod_inheritable = None
        self._chown = None
        self._create_over_smb = None
        self._dos_attr = None
        self._group_owner_inheritance = None
        self._rwx = None
        self._synthetic_denies = None
        self._utimes = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if calcmode is not None:
            self.calcmode = calcmode
        if calcmode_group is not None:
            self.calcmode_group = calcmode_group
        if calcmode_owner is not None:
            self.calcmode_owner = calcmode_owner
        if chmod is not None:
            self.chmod = chmod
        if chmod_007 is not None:
            self.chmod_007 = chmod_007
        if chmod_inheritable is not None:
            self.chmod_inheritable = chmod_inheritable
        if chown is not None:
            self.chown = chown
        if create_over_smb is not None:
            self.create_over_smb = create_over_smb
        if dos_attr is not None:
            self.dos_attr = dos_attr
        if group_owner_inheritance is not None:
            self.group_owner_inheritance = group_owner_inheritance
        if rwx is not None:
            self.rwx = rwx
        if synthetic_denies is not None:
            self.synthetic_denies = synthetic_denies
        if utimes is not None:
            self.utimes = utimes

    @property
    def access(self):
        """Gets the access of this SettingsAclsExtended.  # noqa: E501

        Access checks (chmod, chown).  # noqa: E501

        :return: The access of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this SettingsAclsExtended.

        Access checks (chmod, chown).  # noqa: E501

        :param access: The access of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["unix", "windows"]  # noqa: E501
        if access not in allowed_values:
            raise ValueError(
                "Invalid value for `access` ({0}), must be one of {1}"  # noqa: E501
                .format(access, allowed_values)
            )

        self._access = access

    @property
    def calcmode(self):
        """Gets the calcmode of this SettingsAclsExtended.  # noqa: E501

        Displayed mode bits.  # noqa: E501

        :return: The calcmode of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._calcmode

    @calcmode.setter
    def calcmode(self, calcmode):
        """Sets the calcmode of this SettingsAclsExtended.

        Displayed mode bits.  # noqa: E501

        :param calcmode: The calcmode of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["approx", "777"]  # noqa: E501
        if calcmode not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode` ({0}), must be one of {1}"  # noqa: E501
                .format(calcmode, allowed_values)
            )

        self._calcmode = calcmode

    @property
    def calcmode_group(self):
        """Gets the calcmode_group of this SettingsAclsExtended.  # noqa: E501

        Approximate group mode bits when ACL exists.  # noqa: E501

        :return: The calcmode_group of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._calcmode_group

    @calcmode_group.setter
    def calcmode_group(self, calcmode_group):
        """Sets the calcmode_group of this SettingsAclsExtended.

        Approximate group mode bits when ACL exists.  # noqa: E501

        :param calcmode_group: The calcmode_group of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["group_aces", "group_only"]  # noqa: E501
        if calcmode_group not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode_group` ({0}), must be one of {1}"  # noqa: E501
                .format(calcmode_group, allowed_values)
            )

        self._calcmode_group = calcmode_group

    @property
    def calcmode_owner(self):
        """Gets the calcmode_owner of this SettingsAclsExtended.  # noqa: E501

        Approximate owner mode bits when ACL exists.  # noqa: E501

        :return: The calcmode_owner of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._calcmode_owner

    @calcmode_owner.setter
    def calcmode_owner(self, calcmode_owner):
        """Sets the calcmode_owner of this SettingsAclsExtended.

        Approximate owner mode bits when ACL exists.  # noqa: E501

        :param calcmode_owner: The calcmode_owner of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["owner_aces", "owner_only"]  # noqa: E501
        if calcmode_owner not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode_owner` ({0}), must be one of {1}"  # noqa: E501
                .format(calcmode_owner, allowed_values)
            )

        self._calcmode_owner = calcmode_owner

    @property
    def chmod(self):
        """Gets the chmod of this SettingsAclsExtended.  # noqa: E501

        chmod on files with existing ACLs.  # noqa: E501

        :return: The chmod of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._chmod

    @chmod.setter
    def chmod(self, chmod):
        """Sets the chmod of this SettingsAclsExtended.

        chmod on files with existing ACLs.  # noqa: E501

        :param chmod: The chmod of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["remove", "replace", "replace_users_and_groups", "merge", "deny", "ignore"]  # noqa: E501
        if chmod not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod` ({0}), must be one of {1}"  # noqa: E501
                .format(chmod, allowed_values)
            )

        self._chmod = chmod

    @property
    def chmod_007(self):
        """Gets the chmod_007 of this SettingsAclsExtended.  # noqa: E501

        chmod (007) on files with existing ACLs.  # noqa: E501

        :return: The chmod_007 of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._chmod_007

    @chmod_007.setter
    def chmod_007(self, chmod_007):
        """Sets the chmod_007 of this SettingsAclsExtended.

        chmod (007) on files with existing ACLs.  # noqa: E501

        :param chmod_007: The chmod_007 of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "remove"]  # noqa: E501
        if chmod_007 not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod_007` ({0}), must be one of {1}"  # noqa: E501
                .format(chmod_007, allowed_values)
            )

        self._chmod_007 = chmod_007

    @property
    def chmod_inheritable(self):
        """Gets the chmod_inheritable of this SettingsAclsExtended.  # noqa: E501

        ACLs created on directories by UNIX chmod.  # noqa: E501

        :return: The chmod_inheritable of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._chmod_inheritable

    @chmod_inheritable.setter
    def chmod_inheritable(self, chmod_inheritable):
        """Sets the chmod_inheritable of this SettingsAclsExtended.

        ACLs created on directories by UNIX chmod.  # noqa: E501

        :param chmod_inheritable: The chmod_inheritable of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["yes", "no"]  # noqa: E501
        if chmod_inheritable not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod_inheritable` ({0}), must be one of {1}"  # noqa: E501
                .format(chmod_inheritable, allowed_values)
            )

        self._chmod_inheritable = chmod_inheritable

    @property
    def chown(self):
        """Gets the chown of this SettingsAclsExtended.  # noqa: E501

        chown/chgrp on files with existing ACLs.  # noqa: E501

        :return: The chown of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._chown

    @chown.setter
    def chown(self, chown):
        """Sets the chown of this SettingsAclsExtended.

        chown/chgrp on files with existing ACLs.  # noqa: E501

        :param chown: The chown of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["owner_group_and_acl", "owner_group_only", "ignore"]  # noqa: E501
        if chown not in allowed_values:
            raise ValueError(
                "Invalid value for `chown` ({0}), must be one of {1}"  # noqa: E501
                .format(chown, allowed_values)
            )

        self._chown = chown

    @property
    def create_over_smb(self):
        """Gets the create_over_smb of this SettingsAclsExtended.  # noqa: E501

        ACL creation over SMB.  # noqa: E501

        :return: The create_over_smb of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._create_over_smb

    @create_over_smb.setter
    def create_over_smb(self, create_over_smb):
        """Sets the create_over_smb of this SettingsAclsExtended.

        ACL creation over SMB.  # noqa: E501

        :param create_over_smb: The create_over_smb of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "disallow"]  # noqa: E501
        if create_over_smb not in allowed_values:
            raise ValueError(
                "Invalid value for `create_over_smb` ({0}), must be one of {1}"  # noqa: E501
                .format(create_over_smb, allowed_values)
            )

        self._create_over_smb = create_over_smb

    @property
    def dos_attr(self):
        """Gets the dos_attr of this SettingsAclsExtended.  # noqa: E501

         Read only DOS attribute.  # noqa: E501

        :return: The dos_attr of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._dos_attr

    @dos_attr.setter
    def dos_attr(self, dos_attr):
        """Sets the dos_attr of this SettingsAclsExtended.

         Read only DOS attribute.  # noqa: E501

        :param dos_attr: The dos_attr of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["deny_smb", "deny_smb_and_nfs"]  # noqa: E501
        if dos_attr not in allowed_values:
            raise ValueError(
                "Invalid value for `dos_attr` ({0}), must be one of {1}"  # noqa: E501
                .format(dos_attr, allowed_values)
            )

        self._dos_attr = dos_attr

    @property
    def group_owner_inheritance(self):
        """Gets the group_owner_inheritance of this SettingsAclsExtended.  # noqa: E501

        Group owner inheritance.  # noqa: E501

        :return: The group_owner_inheritance of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._group_owner_inheritance

    @group_owner_inheritance.setter
    def group_owner_inheritance(self, group_owner_inheritance):
        """Sets the group_owner_inheritance of this SettingsAclsExtended.

        Group owner inheritance.  # noqa: E501

        :param group_owner_inheritance: The group_owner_inheritance of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["native", "parent", "creator"]  # noqa: E501
        if group_owner_inheritance not in allowed_values:
            raise ValueError(
                "Invalid value for `group_owner_inheritance` ({0}), must be one of {1}"  # noqa: E501
                .format(group_owner_inheritance, allowed_values)
            )

        self._group_owner_inheritance = group_owner_inheritance

    @property
    def rwx(self):
        """Gets the rwx of this SettingsAclsExtended.  # noqa: E501

        Treatment of 'rwx' permissions.  # noqa: E501

        :return: The rwx of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._rwx

    @rwx.setter
    def rwx(self, rwx):
        """Sets the rwx of this SettingsAclsExtended.

        Treatment of 'rwx' permissions.  # noqa: E501

        :param rwx: The rwx of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["retain", "full_control"]  # noqa: E501
        if rwx not in allowed_values:
            raise ValueError(
                "Invalid value for `rwx` ({0}), must be one of {1}"  # noqa: E501
                .format(rwx, allowed_values)
            )

        self._rwx = rwx

    @property
    def synthetic_denies(self):
        """Gets the synthetic_denies of this SettingsAclsExtended.  # noqa: E501

        Synthetic 'deny' ACEs.  # noqa: E501

        :return: The synthetic_denies of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._synthetic_denies

    @synthetic_denies.setter
    def synthetic_denies(self, synthetic_denies):
        """Sets the synthetic_denies of this SettingsAclsExtended.

        Synthetic 'deny' ACEs.  # noqa: E501

        :param synthetic_denies: The synthetic_denies of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "remove"]  # noqa: E501
        if synthetic_denies not in allowed_values:
            raise ValueError(
                "Invalid value for `synthetic_denies` ({0}), must be one of {1}"  # noqa: E501
                .format(synthetic_denies, allowed_values)
            )

        self._synthetic_denies = synthetic_denies

    @property
    def utimes(self):
        """Gets the utimes of this SettingsAclsExtended.  # noqa: E501

        Access check (utimes)  # noqa: E501

        :return: The utimes of this SettingsAclsExtended.  # noqa: E501
        :rtype: str
        """
        return self._utimes

    @utimes.setter
    def utimes(self, utimes):
        """Sets the utimes of this SettingsAclsExtended.

        Access check (utimes)  # noqa: E501

        :param utimes: The utimes of this SettingsAclsExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["only_owner", "owner_and_write"]  # noqa: E501
        if utimes not in allowed_values:
            raise ValueError(
                "Invalid value for `utimes` ({0}), must be one of {1}"  # noqa: E501
                .format(utimes, allowed_values)
            )

        self._utimes = utimes

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
        if not isinstance(other, SettingsAclsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
