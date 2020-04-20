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


class FtpSettingsExtended(object):
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
        'accept_timeout': 'int',
        'allow_anon_access': 'bool',
        'allow_anon_upload': 'bool',
        'allow_dirlists': 'bool',
        'allow_downloads': 'bool',
        'allow_local_access': 'bool',
        'allow_writes': 'bool',
        'always_chdir_homedir': 'bool',
        'anon_chown_username': 'str',
        'anon_password_list': 'list[str]',
        'anon_root_path': 'str',
        'anon_umask': 'int',
        'ascii_mode': 'str',
        'chroot_exception_list': 'list[str]',
        'chroot_local_mode': 'str',
        'connect_timeout': 'int',
        'data_timeout': 'int',
        'denied_user_list': 'list[str]',
        'dirlist_localtime': 'bool',
        'dirlist_names': 'str',
        'file_create_perm': 'int',
        'limit_anon_passwords': 'bool',
        'local_root_path': 'str',
        'local_umask': 'int',
        'server_to_server': 'bool',
        'service': 'bool',
        'session_support': 'bool',
        'session_timeout': 'int',
        'user_config_dir': 'str'
    }

    attribute_map = {
        'accept_timeout': 'accept_timeout',
        'allow_anon_access': 'allow_anon_access',
        'allow_anon_upload': 'allow_anon_upload',
        'allow_dirlists': 'allow_dirlists',
        'allow_downloads': 'allow_downloads',
        'allow_local_access': 'allow_local_access',
        'allow_writes': 'allow_writes',
        'always_chdir_homedir': 'always_chdir_homedir',
        'anon_chown_username': 'anon_chown_username',
        'anon_password_list': 'anon_password_list',
        'anon_root_path': 'anon_root_path',
        'anon_umask': 'anon_umask',
        'ascii_mode': 'ascii_mode',
        'chroot_exception_list': 'chroot_exception_list',
        'chroot_local_mode': 'chroot_local_mode',
        'connect_timeout': 'connect_timeout',
        'data_timeout': 'data_timeout',
        'denied_user_list': 'denied_user_list',
        'dirlist_localtime': 'dirlist_localtime',
        'dirlist_names': 'dirlist_names',
        'file_create_perm': 'file_create_perm',
        'limit_anon_passwords': 'limit_anon_passwords',
        'local_root_path': 'local_root_path',
        'local_umask': 'local_umask',
        'server_to_server': 'server_to_server',
        'service': 'service',
        'session_support': 'session_support',
        'session_timeout': 'session_timeout',
        'user_config_dir': 'user_config_dir'
    }

    def __init__(self, accept_timeout=None, allow_anon_access=None, allow_anon_upload=None, allow_dirlists=None, allow_downloads=None, allow_local_access=None, allow_writes=None, always_chdir_homedir=None, anon_chown_username=None, anon_password_list=None, anon_root_path=None, anon_umask=None, ascii_mode=None, chroot_exception_list=None, chroot_local_mode=None, connect_timeout=None, data_timeout=None, denied_user_list=None, dirlist_localtime=None, dirlist_names=None, file_create_perm=None, limit_anon_passwords=None, local_root_path=None, local_umask=None, server_to_server=None, service=None, session_support=None, session_timeout=None, user_config_dir=None):  # noqa: E501
        """FtpSettingsExtended - a model defined in Swagger"""  # noqa: E501

        self._accept_timeout = None
        self._allow_anon_access = None
        self._allow_anon_upload = None
        self._allow_dirlists = None
        self._allow_downloads = None
        self._allow_local_access = None
        self._allow_writes = None
        self._always_chdir_homedir = None
        self._anon_chown_username = None
        self._anon_password_list = None
        self._anon_root_path = None
        self._anon_umask = None
        self._ascii_mode = None
        self._chroot_exception_list = None
        self._chroot_local_mode = None
        self._connect_timeout = None
        self._data_timeout = None
        self._denied_user_list = None
        self._dirlist_localtime = None
        self._dirlist_names = None
        self._file_create_perm = None
        self._limit_anon_passwords = None
        self._local_root_path = None
        self._local_umask = None
        self._server_to_server = None
        self._service = None
        self._session_support = None
        self._session_timeout = None
        self._user_config_dir = None
        self.discriminator = None

        if accept_timeout is not None:
            self.accept_timeout = accept_timeout
        if allow_anon_access is not None:
            self.allow_anon_access = allow_anon_access
        if allow_anon_upload is not None:
            self.allow_anon_upload = allow_anon_upload
        if allow_dirlists is not None:
            self.allow_dirlists = allow_dirlists
        if allow_downloads is not None:
            self.allow_downloads = allow_downloads
        if allow_local_access is not None:
            self.allow_local_access = allow_local_access
        if allow_writes is not None:
            self.allow_writes = allow_writes
        if always_chdir_homedir is not None:
            self.always_chdir_homedir = always_chdir_homedir
        if anon_chown_username is not None:
            self.anon_chown_username = anon_chown_username
        if anon_password_list is not None:
            self.anon_password_list = anon_password_list
        if anon_root_path is not None:
            self.anon_root_path = anon_root_path
        if anon_umask is not None:
            self.anon_umask = anon_umask
        if ascii_mode is not None:
            self.ascii_mode = ascii_mode
        if chroot_exception_list is not None:
            self.chroot_exception_list = chroot_exception_list
        if chroot_local_mode is not None:
            self.chroot_local_mode = chroot_local_mode
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if data_timeout is not None:
            self.data_timeout = data_timeout
        if denied_user_list is not None:
            self.denied_user_list = denied_user_list
        if dirlist_localtime is not None:
            self.dirlist_localtime = dirlist_localtime
        if dirlist_names is not None:
            self.dirlist_names = dirlist_names
        if file_create_perm is not None:
            self.file_create_perm = file_create_perm
        if limit_anon_passwords is not None:
            self.limit_anon_passwords = limit_anon_passwords
        if local_root_path is not None:
            self.local_root_path = local_root_path
        if local_umask is not None:
            self.local_umask = local_umask
        if server_to_server is not None:
            self.server_to_server = server_to_server
        if service is not None:
            self.service = service
        if session_support is not None:
            self.session_support = session_support
        if session_timeout is not None:
            self.session_timeout = session_timeout
        if user_config_dir is not None:
            self.user_config_dir = user_config_dir

    @property
    def accept_timeout(self):
        """Gets the accept_timeout of this FtpSettingsExtended.  # noqa: E501

        The timeout, in seconds, for a remote client to establish a PASV style data connection.  # noqa: E501

        :return: The accept_timeout of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._accept_timeout

    @accept_timeout.setter
    def accept_timeout(self, accept_timeout):
        """Sets the accept_timeout of this FtpSettingsExtended.

        The timeout, in seconds, for a remote client to establish a PASV style data connection.  # noqa: E501

        :param accept_timeout: The accept_timeout of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if accept_timeout is not None and accept_timeout > 600:  # noqa: E501
            raise ValueError("Invalid value for `accept_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if accept_timeout is not None and accept_timeout < 30:  # noqa: E501
            raise ValueError("Invalid value for `accept_timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._accept_timeout = accept_timeout

    @property
    def allow_anon_access(self):
        """Gets the allow_anon_access of this FtpSettingsExtended.  # noqa: E501

        Controls whether anonymous logins are permitted or not.  # noqa: E501

        :return: The allow_anon_access of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_anon_access

    @allow_anon_access.setter
    def allow_anon_access(self, allow_anon_access):
        """Sets the allow_anon_access of this FtpSettingsExtended.

        Controls whether anonymous logins are permitted or not.  # noqa: E501

        :param allow_anon_access: The allow_anon_access of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_anon_access = allow_anon_access

    @property
    def allow_anon_upload(self):
        """Gets the allow_anon_upload of this FtpSettingsExtended.  # noqa: E501

        Controls whether anonymous users will be permitted to upload files.  # noqa: E501

        :return: The allow_anon_upload of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_anon_upload

    @allow_anon_upload.setter
    def allow_anon_upload(self, allow_anon_upload):
        """Sets the allow_anon_upload of this FtpSettingsExtended.

        Controls whether anonymous users will be permitted to upload files.  # noqa: E501

        :param allow_anon_upload: The allow_anon_upload of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_anon_upload = allow_anon_upload

    @property
    def allow_dirlists(self):
        """Gets the allow_dirlists of this FtpSettingsExtended.  # noqa: E501

        If set to false, all directory list commands will return a permission denied error.  # noqa: E501

        :return: The allow_dirlists of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dirlists

    @allow_dirlists.setter
    def allow_dirlists(self, allow_dirlists):
        """Sets the allow_dirlists of this FtpSettingsExtended.

        If set to false, all directory list commands will return a permission denied error.  # noqa: E501

        :param allow_dirlists: The allow_dirlists of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_dirlists = allow_dirlists

    @property
    def allow_downloads(self):
        """Gets the allow_downloads of this FtpSettingsExtended.  # noqa: E501

        If set to false, all downloads requests will return a permission denied error.  # noqa: E501

        :return: The allow_downloads of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_downloads

    @allow_downloads.setter
    def allow_downloads(self, allow_downloads):
        """Sets the allow_downloads of this FtpSettingsExtended.

        If set to false, all downloads requests will return a permission denied error.  # noqa: E501

        :param allow_downloads: The allow_downloads of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_downloads = allow_downloads

    @property
    def allow_local_access(self):
        """Gets the allow_local_access of this FtpSettingsExtended.  # noqa: E501

        Controls whether local logins are permitted or not.  # noqa: E501

        :return: The allow_local_access of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_local_access

    @allow_local_access.setter
    def allow_local_access(self, allow_local_access):
        """Sets the allow_local_access of this FtpSettingsExtended.

        Controls whether local logins are permitted or not.  # noqa: E501

        :param allow_local_access: The allow_local_access of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_local_access = allow_local_access

    @property
    def allow_writes(self):
        """Gets the allow_writes of this FtpSettingsExtended.  # noqa: E501

        This controls whether any FTP commands which change the filesystem are allowed or not.  # noqa: E501

        :return: The allow_writes of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_writes

    @allow_writes.setter
    def allow_writes(self, allow_writes):
        """Sets the allow_writes of this FtpSettingsExtended.

        This controls whether any FTP commands which change the filesystem are allowed or not.  # noqa: E501

        :param allow_writes: The allow_writes of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._allow_writes = allow_writes

    @property
    def always_chdir_homedir(self):
        """Gets the always_chdir_homedir of this FtpSettingsExtended.  # noqa: E501

        This controls whether FTP will always initially change directories to the home directory of the user, regardless of whether it is chroot-ing.  # noqa: E501

        :return: The always_chdir_homedir of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._always_chdir_homedir

    @always_chdir_homedir.setter
    def always_chdir_homedir(self, always_chdir_homedir):
        """Sets the always_chdir_homedir of this FtpSettingsExtended.

        This controls whether FTP will always initially change directories to the home directory of the user, regardless of whether it is chroot-ing.  # noqa: E501

        :param always_chdir_homedir: The always_chdir_homedir of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._always_chdir_homedir = always_chdir_homedir

    @property
    def anon_chown_username(self):
        """Gets the anon_chown_username of this FtpSettingsExtended.  # noqa: E501

        This is the name of the user who is given ownership of anonymously uploaded files.  # noqa: E501

        :return: The anon_chown_username of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._anon_chown_username

    @anon_chown_username.setter
    def anon_chown_username(self, anon_chown_username):
        """Sets the anon_chown_username of this FtpSettingsExtended.

        This is the name of the user who is given ownership of anonymously uploaded files.  # noqa: E501

        :param anon_chown_username: The anon_chown_username of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._anon_chown_username = anon_chown_username

    @property
    def anon_password_list(self):
        """Gets the anon_password_list of this FtpSettingsExtended.  # noqa: E501

        A list of passwords for anonymous users.  # noqa: E501

        :return: The anon_password_list of this FtpSettingsExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._anon_password_list

    @anon_password_list.setter
    def anon_password_list(self, anon_password_list):
        """Sets the anon_password_list of this FtpSettingsExtended.

        A list of passwords for anonymous users.  # noqa: E501

        :param anon_password_list: The anon_password_list of this FtpSettingsExtended.  # noqa: E501
        :type: list[str]
        """

        self._anon_password_list = anon_password_list

    @property
    def anon_root_path(self):
        """Gets the anon_root_path of this FtpSettingsExtended.  # noqa: E501

        This option represents a directory in /ifs which vsftpd will try to change into after an anonymous login.  # noqa: E501

        :return: The anon_root_path of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._anon_root_path

    @anon_root_path.setter
    def anon_root_path(self, anon_root_path):
        """Sets the anon_root_path of this FtpSettingsExtended.

        This option represents a directory in /ifs which vsftpd will try to change into after an anonymous login.  # noqa: E501

        :param anon_root_path: The anon_root_path of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._anon_root_path = anon_root_path

    @property
    def anon_umask(self):
        """Gets the anon_umask of this FtpSettingsExtended.  # noqa: E501

        The value that the umask for file creation is set to for anonymous users.  # noqa: E501

        :return: The anon_umask of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._anon_umask

    @anon_umask.setter
    def anon_umask(self, anon_umask):
        """Sets the anon_umask of this FtpSettingsExtended.

        The value that the umask for file creation is set to for anonymous users.  # noqa: E501

        :param anon_umask: The anon_umask of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if anon_umask is not None and anon_umask > 511:  # noqa: E501
            raise ValueError("Invalid value for `anon_umask`, must be a value less than or equal to `511`")  # noqa: E501
        if anon_umask is not None and anon_umask < 0:  # noqa: E501
            raise ValueError("Invalid value for `anon_umask`, must be a value greater than or equal to `0`")  # noqa: E501

        self._anon_umask = anon_umask

    @property
    def ascii_mode(self):
        """Gets the ascii_mode of this FtpSettingsExtended.  # noqa: E501

        Controls whether ascii mode data transfers are honored for various types of requests.  # noqa: E501

        :return: The ascii_mode of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._ascii_mode

    @ascii_mode.setter
    def ascii_mode(self, ascii_mode):
        """Sets the ascii_mode of this FtpSettingsExtended.

        Controls whether ascii mode data transfers are honored for various types of requests.  # noqa: E501

        :param ascii_mode: The ascii_mode of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._ascii_mode = ascii_mode

    @property
    def chroot_exception_list(self):
        """Gets the chroot_exception_list of this FtpSettingsExtended.  # noqa: E501

        A list of users that are not chrooted when logging in.  # noqa: E501

        :return: The chroot_exception_list of this FtpSettingsExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._chroot_exception_list

    @chroot_exception_list.setter
    def chroot_exception_list(self, chroot_exception_list):
        """Sets the chroot_exception_list of this FtpSettingsExtended.

        A list of users that are not chrooted when logging in.  # noqa: E501

        :param chroot_exception_list: The chroot_exception_list of this FtpSettingsExtended.  # noqa: E501
        :type: list[str]
        """

        self._chroot_exception_list = chroot_exception_list

    @property
    def chroot_local_mode(self):
        """Gets the chroot_local_mode of this FtpSettingsExtended.  # noqa: E501

        If set to 'all', all local users will be (by default) placed in a chroot() jail in their home directory after login. If set to 'all-with-exceptions', all local users except those listed in the chroot exception list (isi ftp chroot-exception-list) will be placed in a chroot() jail in their home directory after login. If set to 'none', no local users will be chrooted by default. If set to 'none-with-exceptions', only the local users listed in the chroot exception list (isi ftp chroot-exception-list) will be place in a chroot() jail in their home directory after login.  # noqa: E501

        :return: The chroot_local_mode of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._chroot_local_mode

    @chroot_local_mode.setter
    def chroot_local_mode(self, chroot_local_mode):
        """Sets the chroot_local_mode of this FtpSettingsExtended.

        If set to 'all', all local users will be (by default) placed in a chroot() jail in their home directory after login. If set to 'all-with-exceptions', all local users except those listed in the chroot exception list (isi ftp chroot-exception-list) will be placed in a chroot() jail in their home directory after login. If set to 'none', no local users will be chrooted by default. If set to 'none-with-exceptions', only the local users listed in the chroot exception list (isi ftp chroot-exception-list) will be place in a chroot() jail in their home directory after login.  # noqa: E501

        :param chroot_local_mode: The chroot_local_mode of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._chroot_local_mode = chroot_local_mode

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this FtpSettingsExtended.  # noqa: E501

        The timeout, in seconds, for a remote client to respond to our PORT style data connection.  # noqa: E501

        :return: The connect_timeout of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this FtpSettingsExtended.

        The timeout, in seconds, for a remote client to respond to our PORT style data connection.  # noqa: E501

        :param connect_timeout: The connect_timeout of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if connect_timeout is not None and connect_timeout > 600:  # noqa: E501
            raise ValueError("Invalid value for `connect_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if connect_timeout is not None and connect_timeout < 30:  # noqa: E501
            raise ValueError("Invalid value for `connect_timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._connect_timeout = connect_timeout

    @property
    def data_timeout(self):
        """Gets the data_timeout of this FtpSettingsExtended.  # noqa: E501

        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.  # noqa: E501

        :return: The data_timeout of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._data_timeout

    @data_timeout.setter
    def data_timeout(self, data_timeout):
        """Sets the data_timeout of this FtpSettingsExtended.

        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.  # noqa: E501

        :param data_timeout: The data_timeout of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if data_timeout is not None and data_timeout > 600:  # noqa: E501
            raise ValueError("Invalid value for `data_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if data_timeout is not None and data_timeout < 30:  # noqa: E501
            raise ValueError("Invalid value for `data_timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._data_timeout = data_timeout

    @property
    def denied_user_list(self):
        """Gets the denied_user_list of this FtpSettingsExtended.  # noqa: E501

        A list of uses that will be denied access.  # noqa: E501

        :return: The denied_user_list of this FtpSettingsExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._denied_user_list

    @denied_user_list.setter
    def denied_user_list(self, denied_user_list):
        """Sets the denied_user_list of this FtpSettingsExtended.

        A list of uses that will be denied access.  # noqa: E501

        :param denied_user_list: The denied_user_list of this FtpSettingsExtended.  # noqa: E501
        :type: list[str]
        """

        self._denied_user_list = denied_user_list

    @property
    def dirlist_localtime(self):
        """Gets the dirlist_localtime of this FtpSettingsExtended.  # noqa: E501

        If enabled, display directory listings with the time in your local time zone. The default is to display GMT. The times returned by the MDTM FTP command are also affected by this option.  # noqa: E501

        :return: The dirlist_localtime of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dirlist_localtime

    @dirlist_localtime.setter
    def dirlist_localtime(self, dirlist_localtime):
        """Sets the dirlist_localtime of this FtpSettingsExtended.

        If enabled, display directory listings with the time in your local time zone. The default is to display GMT. The times returned by the MDTM FTP command are also affected by this option.  # noqa: E501

        :param dirlist_localtime: The dirlist_localtime of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._dirlist_localtime = dirlist_localtime

    @property
    def dirlist_names(self):
        """Gets the dirlist_names of this FtpSettingsExtended.  # noqa: E501

        When set to 'hide',  all user and group information in directory listings will be displayed as 'ftp'. When set to 'textual', textual names are shown in the user and group fields of directory listings. When set to 'numeric', numeric IDs are show in the user and group fields of directory listings.  # noqa: E501

        :return: The dirlist_names of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._dirlist_names

    @dirlist_names.setter
    def dirlist_names(self, dirlist_names):
        """Sets the dirlist_names of this FtpSettingsExtended.

        When set to 'hide',  all user and group information in directory listings will be displayed as 'ftp'. When set to 'textual', textual names are shown in the user and group fields of directory listings. When set to 'numeric', numeric IDs are show in the user and group fields of directory listings.  # noqa: E501

        :param dirlist_names: The dirlist_names of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._dirlist_names = dirlist_names

    @property
    def file_create_perm(self):
        """Gets the file_create_perm of this FtpSettingsExtended.  # noqa: E501

        The permissions with which uploaded files are created. Umasks are applied on top of this value.  # noqa: E501

        :return: The file_create_perm of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._file_create_perm

    @file_create_perm.setter
    def file_create_perm(self, file_create_perm):
        """Sets the file_create_perm of this FtpSettingsExtended.

        The permissions with which uploaded files are created. Umasks are applied on top of this value.  # noqa: E501

        :param file_create_perm: The file_create_perm of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if file_create_perm is not None and file_create_perm > 511:  # noqa: E501
            raise ValueError("Invalid value for `file_create_perm`, must be a value less than or equal to `511`")  # noqa: E501
        if file_create_perm is not None and file_create_perm < 0:  # noqa: E501
            raise ValueError("Invalid value for `file_create_perm`, must be a value greater than or equal to `0`")  # noqa: E501

        self._file_create_perm = file_create_perm

    @property
    def limit_anon_passwords(self):
        """Gets the limit_anon_passwords of this FtpSettingsExtended.  # noqa: E501

        This field determines whether the anon_password_list is used.  # noqa: E501

        :return: The limit_anon_passwords of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._limit_anon_passwords

    @limit_anon_passwords.setter
    def limit_anon_passwords(self, limit_anon_passwords):
        """Sets the limit_anon_passwords of this FtpSettingsExtended.

        This field determines whether the anon_password_list is used.  # noqa: E501

        :param limit_anon_passwords: The limit_anon_passwords of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._limit_anon_passwords = limit_anon_passwords

    @property
    def local_root_path(self):
        """Gets the local_root_path of this FtpSettingsExtended.  # noqa: E501

        This option represents a directory in /ifs which vsftpd will try to change into after a local login.  # noqa: E501

        :return: The local_root_path of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._local_root_path

    @local_root_path.setter
    def local_root_path(self, local_root_path):
        """Sets the local_root_path of this FtpSettingsExtended.

        This option represents a directory in /ifs which vsftpd will try to change into after a local login.  # noqa: E501

        :param local_root_path: The local_root_path of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._local_root_path = local_root_path

    @property
    def local_umask(self):
        """Gets the local_umask of this FtpSettingsExtended.  # noqa: E501

        The value that the umask for file creation is set to for local users.  # noqa: E501

        :return: The local_umask of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._local_umask

    @local_umask.setter
    def local_umask(self, local_umask):
        """Sets the local_umask of this FtpSettingsExtended.

        The value that the umask for file creation is set to for local users.  # noqa: E501

        :param local_umask: The local_umask of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if local_umask is not None and local_umask > 511:  # noqa: E501
            raise ValueError("Invalid value for `local_umask`, must be a value less than or equal to `511`")  # noqa: E501
        if local_umask is not None and local_umask < 0:  # noqa: E501
            raise ValueError("Invalid value for `local_umask`, must be a value greater than or equal to `0`")  # noqa: E501

        self._local_umask = local_umask

    @property
    def server_to_server(self):
        """Gets the server_to_server of this FtpSettingsExtended.  # noqa: E501

        If enabled, allow server-to-server (FXP) transfers.  # noqa: E501

        :return: The server_to_server of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._server_to_server

    @server_to_server.setter
    def server_to_server(self, server_to_server):
        """Sets the server_to_server of this FtpSettingsExtended.

        If enabled, allow server-to-server (FXP) transfers.  # noqa: E501

        :param server_to_server: The server_to_server of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._server_to_server = server_to_server

    @property
    def service(self):
        """Gets the service of this FtpSettingsExtended.  # noqa: E501

        This field controls whether the FTP daemon is running.  # noqa: E501

        :return: The service of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this FtpSettingsExtended.

        This field controls whether the FTP daemon is running.  # noqa: E501

        :param service: The service of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._service = service

    @property
    def session_support(self):
        """Gets the session_support of this FtpSettingsExtended.  # noqa: E501

        If enabled, maintain login sessions for each user through Pluggable Authentication Modules (PAM). Disabling this option prevents the ability to do automatic home directory creation if that functionality were otherwise available.  # noqa: E501

        :return: The session_support of this FtpSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._session_support

    @session_support.setter
    def session_support(self, session_support):
        """Sets the session_support of this FtpSettingsExtended.

        If enabled, maintain login sessions for each user through Pluggable Authentication Modules (PAM). Disabling this option prevents the ability to do automatic home directory creation if that functionality were otherwise available.  # noqa: E501

        :param session_support: The session_support of this FtpSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._session_support = session_support

    @property
    def session_timeout(self):
        """Gets the session_timeout of this FtpSettingsExtended.  # noqa: E501

        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.  # noqa: E501

        :return: The session_timeout of this FtpSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """Sets the session_timeout of this FtpSettingsExtended.

        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.  # noqa: E501

        :param session_timeout: The session_timeout of this FtpSettingsExtended.  # noqa: E501
        :type: int
        """
        if session_timeout is not None and session_timeout > 600:  # noqa: E501
            raise ValueError("Invalid value for `session_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if session_timeout is not None and session_timeout < 30:  # noqa: E501
            raise ValueError("Invalid value for `session_timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._session_timeout = session_timeout

    @property
    def user_config_dir(self):
        """Gets the user_config_dir of this FtpSettingsExtended.  # noqa: E501

        Specifies the directory where per-user config overrides can be found.  # noqa: E501

        :return: The user_config_dir of this FtpSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._user_config_dir

    @user_config_dir.setter
    def user_config_dir(self, user_config_dir):
        """Sets the user_config_dir of this FtpSettingsExtended.

        Specifies the directory where per-user config overrides can be found.  # noqa: E501

        :param user_config_dir: The user_config_dir of this FtpSettingsExtended.  # noqa: E501
        :type: str
        """

        self._user_config_dir = user_config_dir

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
        if not isinstance(other, FtpSettingsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
