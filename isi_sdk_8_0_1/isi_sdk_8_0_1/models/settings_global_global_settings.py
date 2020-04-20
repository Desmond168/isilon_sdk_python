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


class SettingsGlobalGlobalSettings(object):
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
        'alloc_retries': 'int',
        'gid_range_enabled': 'bool',
        'gid_range_max': 'int',
        'gid_range_min': 'int',
        'gid_range_next': 'int',
        'group_uid': 'int',
        'load_providers': 'list[str]',
        'min_mapped_rid': 'int',
        'null_gid': 'int',
        'null_uid': 'int',
        'on_disk_identity': 'str',
        'rpc_block_time': 'int',
        'rpc_max_requests': 'int',
        'rpc_timeout': 'int',
        'send_ntlmv2': 'bool',
        'space_replacement': 'str',
        'system_gid_threshold': 'int',
        'system_uid_threshold': 'int',
        'uid_range_enabled': 'bool',
        'uid_range_max': 'int',
        'uid_range_min': 'int',
        'uid_range_next': 'int',
        'unknown_gid': 'int',
        'unknown_uid': 'int',
        'user_object_cache_size': 'int',
        'workgroup': 'str'
    }

    attribute_map = {
        'alloc_retries': 'alloc_retries',
        'gid_range_enabled': 'gid_range_enabled',
        'gid_range_max': 'gid_range_max',
        'gid_range_min': 'gid_range_min',
        'gid_range_next': 'gid_range_next',
        'group_uid': 'group_uid',
        'load_providers': 'load_providers',
        'min_mapped_rid': 'min_mapped_rid',
        'null_gid': 'null_gid',
        'null_uid': 'null_uid',
        'on_disk_identity': 'on_disk_identity',
        'rpc_block_time': 'rpc_block_time',
        'rpc_max_requests': 'rpc_max_requests',
        'rpc_timeout': 'rpc_timeout',
        'send_ntlmv2': 'send_ntlmv2',
        'space_replacement': 'space_replacement',
        'system_gid_threshold': 'system_gid_threshold',
        'system_uid_threshold': 'system_uid_threshold',
        'uid_range_enabled': 'uid_range_enabled',
        'uid_range_max': 'uid_range_max',
        'uid_range_min': 'uid_range_min',
        'uid_range_next': 'uid_range_next',
        'unknown_gid': 'unknown_gid',
        'unknown_uid': 'unknown_uid',
        'user_object_cache_size': 'user_object_cache_size',
        'workgroup': 'workgroup'
    }

    def __init__(self, alloc_retries=None, gid_range_enabled=None, gid_range_max=None, gid_range_min=None, gid_range_next=None, group_uid=None, load_providers=None, min_mapped_rid=None, null_gid=None, null_uid=None, on_disk_identity=None, rpc_block_time=None, rpc_max_requests=None, rpc_timeout=None, send_ntlmv2=None, space_replacement=None, system_gid_threshold=None, system_uid_threshold=None, uid_range_enabled=None, uid_range_max=None, uid_range_min=None, uid_range_next=None, unknown_gid=None, unknown_uid=None, user_object_cache_size=None, workgroup=None):  # noqa: E501
        """SettingsGlobalGlobalSettings - a model defined in Swagger"""  # noqa: E501

        self._alloc_retries = None
        self._gid_range_enabled = None
        self._gid_range_max = None
        self._gid_range_min = None
        self._gid_range_next = None
        self._group_uid = None
        self._load_providers = None
        self._min_mapped_rid = None
        self._null_gid = None
        self._null_uid = None
        self._on_disk_identity = None
        self._rpc_block_time = None
        self._rpc_max_requests = None
        self._rpc_timeout = None
        self._send_ntlmv2 = None
        self._space_replacement = None
        self._system_gid_threshold = None
        self._system_uid_threshold = None
        self._uid_range_enabled = None
        self._uid_range_max = None
        self._uid_range_min = None
        self._uid_range_next = None
        self._unknown_gid = None
        self._unknown_uid = None
        self._user_object_cache_size = None
        self._workgroup = None
        self.discriminator = None

        if alloc_retries is not None:
            self.alloc_retries = alloc_retries
        if gid_range_enabled is not None:
            self.gid_range_enabled = gid_range_enabled
        if gid_range_max is not None:
            self.gid_range_max = gid_range_max
        if gid_range_min is not None:
            self.gid_range_min = gid_range_min
        if gid_range_next is not None:
            self.gid_range_next = gid_range_next
        if group_uid is not None:
            self.group_uid = group_uid
        if load_providers is not None:
            self.load_providers = load_providers
        if min_mapped_rid is not None:
            self.min_mapped_rid = min_mapped_rid
        if null_gid is not None:
            self.null_gid = null_gid
        if null_uid is not None:
            self.null_uid = null_uid
        if on_disk_identity is not None:
            self.on_disk_identity = on_disk_identity
        if rpc_block_time is not None:
            self.rpc_block_time = rpc_block_time
        if rpc_max_requests is not None:
            self.rpc_max_requests = rpc_max_requests
        if rpc_timeout is not None:
            self.rpc_timeout = rpc_timeout
        if send_ntlmv2 is not None:
            self.send_ntlmv2 = send_ntlmv2
        if space_replacement is not None:
            self.space_replacement = space_replacement
        if system_gid_threshold is not None:
            self.system_gid_threshold = system_gid_threshold
        if system_uid_threshold is not None:
            self.system_uid_threshold = system_uid_threshold
        if uid_range_enabled is not None:
            self.uid_range_enabled = uid_range_enabled
        if uid_range_max is not None:
            self.uid_range_max = uid_range_max
        if uid_range_min is not None:
            self.uid_range_min = uid_range_min
        if uid_range_next is not None:
            self.uid_range_next = uid_range_next
        if unknown_gid is not None:
            self.unknown_gid = unknown_gid
        if unknown_uid is not None:
            self.unknown_uid = unknown_uid
        if user_object_cache_size is not None:
            self.user_object_cache_size = user_object_cache_size
        if workgroup is not None:
            self.workgroup = workgroup

    @property
    def alloc_retries(self):
        """Gets the alloc_retries of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the number of times to retry an ID allocation before failing.  # noqa: E501

        :return: The alloc_retries of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._alloc_retries

    @alloc_retries.setter
    def alloc_retries(self, alloc_retries):
        """Sets the alloc_retries of this SettingsGlobalGlobalSettings.

        Specifies the number of times to retry an ID allocation before failing.  # noqa: E501

        :param alloc_retries: The alloc_retries of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._alloc_retries = alloc_retries

    @property
    def gid_range_enabled(self):
        """Gets the gid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501

        If true, allocates GIDs from a fixed range.  # noqa: E501

        :return: The gid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._gid_range_enabled

    @gid_range_enabled.setter
    def gid_range_enabled(self, gid_range_enabled):
        """Sets the gid_range_enabled of this SettingsGlobalGlobalSettings.

        If true, allocates GIDs from a fixed range.  # noqa: E501

        :param gid_range_enabled: The gid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._gid_range_enabled = gid_range_enabled

    @property
    def gid_range_max(self):
        """Gets the gid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the ending number for a fixed range from which GIDs are allocated.  # noqa: E501

        :return: The gid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_max

    @gid_range_max.setter
    def gid_range_max(self, gid_range_max):
        """Sets the gid_range_max of this SettingsGlobalGlobalSettings.

        Specifies the ending number for a fixed range from which GIDs are allocated.  # noqa: E501

        :param gid_range_max: The gid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._gid_range_max = gid_range_max

    @property
    def gid_range_min(self):
        """Gets the gid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the starting number for a fixed range from which GIDs are allocated.  # noqa: E501

        :return: The gid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_min

    @gid_range_min.setter
    def gid_range_min(self, gid_range_min):
        """Sets the gid_range_min of this SettingsGlobalGlobalSettings.

        Specifies the starting number for a fixed range from which GIDs are allocated.  # noqa: E501

        :param gid_range_min: The gid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._gid_range_min = gid_range_min

    @property
    def gid_range_next(self):
        """Gets the gid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the next GID to allocate.  # noqa: E501

        :return: The gid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._gid_range_next

    @gid_range_next.setter
    def gid_range_next(self, gid_range_next):
        """Sets the gid_range_next of this SettingsGlobalGlobalSettings.

        Specifies the next GID to allocate.  # noqa: E501

        :param gid_range_next: The gid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._gid_range_next = gid_range_next

    @property
    def group_uid(self):
        """Gets the group_uid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the user iD for a group when requested by the kernel.  # noqa: E501

        :return: The group_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._group_uid

    @group_uid.setter
    def group_uid(self, group_uid):
        """Sets the group_uid of this SettingsGlobalGlobalSettings.

        Specifies the user iD for a group when requested by the kernel.  # noqa: E501

        :param group_uid: The group_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._group_uid = group_uid

    @property
    def load_providers(self):
        """Gets the load_providers of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies which providers are loaded by the authentication daemon (lsassd).  # noqa: E501

        :return: The load_providers of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_providers

    @load_providers.setter
    def load_providers(self, load_providers):
        """Sets the load_providers of this SettingsGlobalGlobalSettings.

        Specifies which providers are loaded by the authentication daemon (lsassd).  # noqa: E501

        :param load_providers: The load_providers of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ActiveDirectory", "Local", "Nss", "File", "Nis", "Ldap", "Krb5"]  # noqa: E501
        if not set(load_providers).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `load_providers` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(load_providers) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._load_providers = load_providers

    @property
    def min_mapped_rid(self):
        """Gets the min_mapped_rid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Starts the RID in the local domain to map a UID and a GID.  # noqa: E501

        :return: The min_mapped_rid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._min_mapped_rid

    @min_mapped_rid.setter
    def min_mapped_rid(self, min_mapped_rid):
        """Sets the min_mapped_rid of this SettingsGlobalGlobalSettings.

        Starts the RID in the local domain to map a UID and a GID.  # noqa: E501

        :param min_mapped_rid: The min_mapped_rid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._min_mapped_rid = min_mapped_rid

    @property
    def null_gid(self):
        """Gets the null_gid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies an alternative GID when the kernel is unable to retrieve a GID for a persona.  # noqa: E501

        :return: The null_gid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._null_gid

    @null_gid.setter
    def null_gid(self, null_gid):
        """Sets the null_gid of this SettingsGlobalGlobalSettings.

        Specifies an alternative GID when the kernel is unable to retrieve a GID for a persona.  # noqa: E501

        :param null_gid: The null_gid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._null_gid = null_gid

    @property
    def null_uid(self):
        """Gets the null_uid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies an alternative UID when the kernel is unable to retrieve a UID for a persona.  # noqa: E501

        :return: The null_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._null_uid

    @null_uid.setter
    def null_uid(self, null_uid):
        """Sets the null_uid of this SettingsGlobalGlobalSettings.

        Specifies an alternative UID when the kernel is unable to retrieve a UID for a persona.  # noqa: E501

        :param null_uid: The null_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._null_uid = null_uid

    @property
    def on_disk_identity(self):
        """Gets the on_disk_identity of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the type of identity that is stored on disk.  # noqa: E501

        :return: The on_disk_identity of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: str
        """
        return self._on_disk_identity

    @on_disk_identity.setter
    def on_disk_identity(self, on_disk_identity):
        """Sets the on_disk_identity of this SettingsGlobalGlobalSettings.

        Specifies the type of identity that is stored on disk.  # noqa: E501

        :param on_disk_identity: The on_disk_identity of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: str
        """

        self._on_disk_identity = on_disk_identity

    @property
    def rpc_block_time(self):
        """Gets the rpc_block_time of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the minimum amount of time in milliseconds to wait before performing an oprestart.  # noqa: E501

        :return: The rpc_block_time of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._rpc_block_time

    @rpc_block_time.setter
    def rpc_block_time(self, rpc_block_time):
        """Sets the rpc_block_time of this SettingsGlobalGlobalSettings.

        Specifies the minimum amount of time in milliseconds to wait before performing an oprestart.  # noqa: E501

        :param rpc_block_time: The rpc_block_time of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._rpc_block_time = rpc_block_time

    @property
    def rpc_max_requests(self):
        """Gets the rpc_max_requests of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the maximum number of outstanding RPC requests.  # noqa: E501

        :return: The rpc_max_requests of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._rpc_max_requests

    @rpc_max_requests.setter
    def rpc_max_requests(self, rpc_max_requests):
        """Sets the rpc_max_requests of this SettingsGlobalGlobalSettings.

        Specifies the maximum number of outstanding RPC requests.  # noqa: E501

        :param rpc_max_requests: The rpc_max_requests of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._rpc_max_requests = rpc_max_requests

    @property
    def rpc_timeout(self):
        """Gets the rpc_timeout of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the maximum amount of time in seconds to wait for an idmap response.  # noqa: E501

        :return: The rpc_timeout of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._rpc_timeout

    @rpc_timeout.setter
    def rpc_timeout(self, rpc_timeout):
        """Sets the rpc_timeout of this SettingsGlobalGlobalSettings.

        Specifies the maximum amount of time in seconds to wait for an idmap response.  # noqa: E501

        :param rpc_timeout: The rpc_timeout of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._rpc_timeout = rpc_timeout

    @property
    def send_ntlmv2(self):
        """Gets the send_ntlmv2 of this SettingsGlobalGlobalSettings.  # noqa: E501

        If true, sends NTLMv2 responses.  # noqa: E501

        :return: The send_ntlmv2 of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._send_ntlmv2

    @send_ntlmv2.setter
    def send_ntlmv2(self, send_ntlmv2):
        """Sets the send_ntlmv2 of this SettingsGlobalGlobalSettings.

        If true, sends NTLMv2 responses.  # noqa: E501

        :param send_ntlmv2: The send_ntlmv2 of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._send_ntlmv2 = send_ntlmv2

    @property
    def space_replacement(self):
        """Gets the space_replacement of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the space replacement character.  # noqa: E501

        :return: The space_replacement of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: str
        """
        return self._space_replacement

    @space_replacement.setter
    def space_replacement(self, space_replacement):
        """Sets the space_replacement of this SettingsGlobalGlobalSettings.

        Specifies the space replacement character.  # noqa: E501

        :param space_replacement: The space_replacement of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: str
        """

        self._space_replacement = space_replacement

    @property
    def system_gid_threshold(self):
        """Gets the system_gid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the minimum GID to attempt to look up in the idmap database.  # noqa: E501

        :return: The system_gid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._system_gid_threshold

    @system_gid_threshold.setter
    def system_gid_threshold(self, system_gid_threshold):
        """Sets the system_gid_threshold of this SettingsGlobalGlobalSettings.

        Specifies the minimum GID to attempt to look up in the idmap database.  # noqa: E501

        :param system_gid_threshold: The system_gid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._system_gid_threshold = system_gid_threshold

    @property
    def system_uid_threshold(self):
        """Gets the system_uid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the minimum UID to attempt to look up in the idmap database.  # noqa: E501

        :return: The system_uid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._system_uid_threshold

    @system_uid_threshold.setter
    def system_uid_threshold(self, system_uid_threshold):
        """Sets the system_uid_threshold of this SettingsGlobalGlobalSettings.

        Specifies the minimum UID to attempt to look up in the idmap database.  # noqa: E501

        :param system_uid_threshold: The system_uid_threshold of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._system_uid_threshold = system_uid_threshold

    @property
    def uid_range_enabled(self):
        """Gets the uid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501

        If true, allocates UIDs from a fixed range.  # noqa: E501

        :return: The uid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._uid_range_enabled

    @uid_range_enabled.setter
    def uid_range_enabled(self, uid_range_enabled):
        """Sets the uid_range_enabled of this SettingsGlobalGlobalSettings.

        If true, allocates UIDs from a fixed range.  # noqa: E501

        :param uid_range_enabled: The uid_range_enabled of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._uid_range_enabled = uid_range_enabled

    @property
    def uid_range_max(self):
        """Gets the uid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the ending number for a fixed range from which UIDs are allocated.  # noqa: E501

        :return: The uid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_max

    @uid_range_max.setter
    def uid_range_max(self, uid_range_max):
        """Sets the uid_range_max of this SettingsGlobalGlobalSettings.

        Specifies the ending number for a fixed range from which UIDs are allocated.  # noqa: E501

        :param uid_range_max: The uid_range_max of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._uid_range_max = uid_range_max

    @property
    def uid_range_min(self):
        """Gets the uid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the starting number for a fixed range from which UIDs are allocated.  # noqa: E501

        :return: The uid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_min

    @uid_range_min.setter
    def uid_range_min(self, uid_range_min):
        """Sets the uid_range_min of this SettingsGlobalGlobalSettings.

        Specifies the starting number for a fixed range from which UIDs are allocated.  # noqa: E501

        :param uid_range_min: The uid_range_min of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._uid_range_min = uid_range_min

    @property
    def uid_range_next(self):
        """Gets the uid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the next UID to allocate.  # noqa: E501

        :return: The uid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._uid_range_next

    @uid_range_next.setter
    def uid_range_next(self, uid_range_next):
        """Sets the uid_range_next of this SettingsGlobalGlobalSettings.

        Specifies the next UID to allocate.  # noqa: E501

        :param uid_range_next: The uid_range_next of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._uid_range_next = uid_range_next

    @property
    def unknown_gid(self):
        """Gets the unknown_gid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the GID for the unknown (anonymous) group.  # noqa: E501

        :return: The unknown_gid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._unknown_gid

    @unknown_gid.setter
    def unknown_gid(self, unknown_gid):
        """Sets the unknown_gid of this SettingsGlobalGlobalSettings.

        Specifies the GID for the unknown (anonymous) group.  # noqa: E501

        :param unknown_gid: The unknown_gid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._unknown_gid = unknown_gid

    @property
    def unknown_uid(self):
        """Gets the unknown_uid of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the UID for the unknown (anonymous) user.  # noqa: E501

        :return: The unknown_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._unknown_uid

    @unknown_uid.setter
    def unknown_uid(self, unknown_uid):
        """Sets the unknown_uid of this SettingsGlobalGlobalSettings.

        Specifies the UID for the unknown (anonymous) user.  # noqa: E501

        :param unknown_uid: The unknown_uid of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._unknown_uid = unknown_uid

    @property
    def user_object_cache_size(self):
        """Gets the user_object_cache_size of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the maximum size (in bytes) of the security object cache in the authentication daemon.  # noqa: E501

        :return: The user_object_cache_size of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._user_object_cache_size

    @user_object_cache_size.setter
    def user_object_cache_size(self, user_object_cache_size):
        """Sets the user_object_cache_size of this SettingsGlobalGlobalSettings.

        Specifies the maximum size (in bytes) of the security object cache in the authentication daemon.  # noqa: E501

        :param user_object_cache_size: The user_object_cache_size of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: int
        """

        self._user_object_cache_size = user_object_cache_size

    @property
    def workgroup(self):
        """Gets the workgroup of this SettingsGlobalGlobalSettings.  # noqa: E501

        Specifies the NetBIOS workgroup or domain.  # noqa: E501

        :return: The workgroup of this SettingsGlobalGlobalSettings.  # noqa: E501
        :rtype: str
        """
        return self._workgroup

    @workgroup.setter
    def workgroup(self, workgroup):
        """Sets the workgroup of this SettingsGlobalGlobalSettings.

        Specifies the NetBIOS workgroup or domain.  # noqa: E501

        :param workgroup: The workgroup of this SettingsGlobalGlobalSettings.  # noqa: E501
        :type: str
        """

        self._workgroup = workgroup

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
        if not isinstance(other, SettingsGlobalGlobalSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
