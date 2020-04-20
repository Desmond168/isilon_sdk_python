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

from isi_sdk_8_2_2.models.certificate_server_certificate_fingerprint import CertificateServerCertificateFingerprint  # noqa: F401,E501


class CertificateServerCertificate(object):
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
        'description': 'str',
        'dnsnames': 'list[str]',
        'fingerprints': 'list[CertificateServerCertificateFingerprint]',
        'id': 'str',
        'issuer': 'str',
        'name': 'str',
        'not_after': 'int',
        'not_before': 'int',
        'status': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'description': 'description',
        'dnsnames': 'dnsnames',
        'fingerprints': 'fingerprints',
        'id': 'id',
        'issuer': 'issuer',
        'name': 'name',
        'not_after': 'not_after',
        'not_before': 'not_before',
        'status': 'status',
        'subject': 'subject'
    }

    def __init__(self, description=None, dnsnames=None, fingerprints=None, id=None, issuer=None, name=None, not_after=None, not_before=None, status=None, subject=None):  # noqa: E501
        """CertificateServerCertificate - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._dnsnames = None
        self._fingerprints = None
        self._id = None
        self._issuer = None
        self._name = None
        self._not_after = None
        self._not_before = None
        self._status = None
        self._subject = None
        self.discriminator = None

        self.description = description
        self.dnsnames = dnsnames
        self.fingerprints = fingerprints
        self.id = id
        self.issuer = issuer
        self.name = name
        self.not_after = not_after
        self.not_before = not_before
        self.status = status
        self.subject = subject

    @property
    def description(self):
        """Gets the description of this CertificateServerCertificate.  # noqa: E501

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :return: The description of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateServerCertificate.

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :param description: The description of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 2048:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2048`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def dnsnames(self):
        """Gets the dnsnames of this CertificateServerCertificate.  # noqa: E501

        A list of DNS names/patterns for which this certificate is valid. This list is extracted from the certificates CN (Common Name) and subjectAtlName extension fields.  # noqa: E501

        :return: The dnsnames of this CertificateServerCertificate.  # noqa: E501
        :rtype: list[str]
        """
        return self._dnsnames

    @dnsnames.setter
    def dnsnames(self, dnsnames):
        """Sets the dnsnames of this CertificateServerCertificate.

        A list of DNS names/patterns for which this certificate is valid. This list is extracted from the certificates CN (Common Name) and subjectAtlName extension fields.  # noqa: E501

        :param dnsnames: The dnsnames of this CertificateServerCertificate.  # noqa: E501
        :type: list[str]
        """
        if dnsnames is None:
            raise ValueError("Invalid value for `dnsnames`, must not be `None`")  # noqa: E501

        self._dnsnames = dnsnames

    @property
    def fingerprints(self):
        """Gets the fingerprints of this CertificateServerCertificate.  # noqa: E501

        A list of zero or more certificate fingerprints which can be used for certificate identification.  # noqa: E501

        :return: The fingerprints of this CertificateServerCertificate.  # noqa: E501
        :rtype: list[CertificateServerCertificateFingerprint]
        """
        return self._fingerprints

    @fingerprints.setter
    def fingerprints(self, fingerprints):
        """Sets the fingerprints of this CertificateServerCertificate.

        A list of zero or more certificate fingerprints which can be used for certificate identification.  # noqa: E501

        :param fingerprints: The fingerprints of this CertificateServerCertificate.  # noqa: E501
        :type: list[CertificateServerCertificateFingerprint]
        """
        if fingerprints is None:
            raise ValueError("Invalid value for `fingerprints`, must not be `None`")  # noqa: E501

        self._fingerprints = fingerprints

    @property
    def id(self):
        """Gets the id of this CertificateServerCertificate.  # noqa: E501

        Unique server certificate identifier.  # noqa: E501

        :return: The id of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateServerCertificate.

        Unique server certificate identifier.  # noqa: E501

        :param id: The id of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 512:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `512`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def issuer(self):
        """Gets the issuer of this CertificateServerCertificate.  # noqa: E501

        Certificate issuer field extracted from the certificate.  # noqa: E501

        :return: The issuer of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CertificateServerCertificate.

        Certificate issuer field extracted from the certificate.  # noqa: E501

        :param issuer: The issuer of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501
        if issuer is not None and len(issuer) > 2048:
            raise ValueError("Invalid value for `issuer`, length must be less than or equal to `2048`")  # noqa: E501
        if issuer is not None and len(issuer) < 1:
            raise ValueError("Invalid value for `issuer`, length must be greater than or equal to `1`")  # noqa: E501

        self._issuer = issuer

    @property
    def name(self):
        """Gets the name of this CertificateServerCertificate.  # noqa: E501

        Administrator specified name identifier.  # noqa: E501

        :return: The name of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateServerCertificate.

        Administrator specified name identifier.  # noqa: E501

        :param name: The name of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501
        if name is not None and not re.search('^[a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def not_after(self):
        """Gets the not_after of this CertificateServerCertificate.  # noqa: E501

        Certificate notAfter field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid after this timestamp.  # noqa: E501

        :return: The not_after of this CertificateServerCertificate.  # noqa: E501
        :rtype: int
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertificateServerCertificate.

        Certificate notAfter field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid after this timestamp.  # noqa: E501

        :param not_after: The not_after of this CertificateServerCertificate.  # noqa: E501
        :type: int
        """
        if not_after is None:
            raise ValueError("Invalid value for `not_after`, must not be `None`")  # noqa: E501
        if not_after is not None and not_after > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `not_after`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if not_after is not None and not_after < 0:  # noqa: E501
            raise ValueError("Invalid value for `not_after`, must be a value greater than or equal to `0`")  # noqa: E501

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this CertificateServerCertificate.  # noqa: E501

        Certificate notBefore field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid before this timestamp.  # noqa: E501

        :return: The not_before of this CertificateServerCertificate.  # noqa: E501
        :rtype: int
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this CertificateServerCertificate.

        Certificate notBefore field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid before this timestamp.  # noqa: E501

        :param not_before: The not_before of this CertificateServerCertificate.  # noqa: E501
        :type: int
        """
        if not_before is None:
            raise ValueError("Invalid value for `not_before`, must not be `None`")  # noqa: E501
        if not_before is not None and not_before > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `not_before`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if not_before is not None and not_before < 0:  # noqa: E501
            raise ValueError("Invalid value for `not_before`, must be a value greater than or equal to `0`")  # noqa: E501

        self._not_before = not_before

    @property
    def status(self):
        """Gets the status of this CertificateServerCertificate.  # noqa: E501

        Certificate validity status  # noqa: E501

        :return: The status of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CertificateServerCertificate.

        Certificate validity status  # noqa: E501

        :param status: The status of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["valid", "invalid", "expired", "expiring"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subject(self):
        """Gets the subject of this CertificateServerCertificate.  # noqa: E501

        Certificate subject field extracted from the certificate.  # noqa: E501

        :return: The subject of this CertificateServerCertificate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CertificateServerCertificate.

        Certificate subject field extracted from the certificate.  # noqa: E501

        :param subject: The subject of this CertificateServerCertificate.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if subject is not None and len(subject) > 2048:
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `2048`")  # noqa: E501
        if subject is not None and len(subject) < 1:
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501

        self._subject = subject

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
        if not isinstance(other, CertificateServerCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
