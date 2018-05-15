# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_1_1.api_client import ApiClient


class CertificateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_certificate_server_item(self, certificate_server_item, **kwargs):  # noqa: E501
        """create_certificate_server_item  # noqa: E501

        Import a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_certificate_server_item(certificate_server_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param CertificateServerItem certificate_server_item: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_certificate_server_item_with_http_info(certificate_server_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_certificate_server_item_with_http_info(certificate_server_item, **kwargs)  # noqa: E501
            return data

    def create_certificate_server_item_with_http_info(self, certificate_server_item, **kwargs):  # noqa: E501
        """create_certificate_server_item  # noqa: E501

        Import a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_certificate_server_item_with_http_info(certificate_server_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param CertificateServerItem certificate_server_item: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['certificate_server_item']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_certificate_server_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'certificate_server_item' is set
        if ('certificate_server_item' not in params or
                params['certificate_server_item'] is None):
            raise ValueError("Missing the required parameter `certificate_server_item` when calling `create_certificate_server_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'certificate_server_item' in params:
            body_params = params['certificate_server_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/certificate/server', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_certificate_server_by_id(self, certificate_server_id, **kwargs):  # noqa: E501
        """delete_certificate_server_by_id  # noqa: E501

        Delete a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_certificate_server_by_id(certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str certificate_server_id: Delete a TLS server certificate. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_certificate_server_by_id_with_http_info(certificate_server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_certificate_server_by_id_with_http_info(certificate_server_id, **kwargs)  # noqa: E501
            return data

    def delete_certificate_server_by_id_with_http_info(self, certificate_server_id, **kwargs):  # noqa: E501
        """delete_certificate_server_by_id  # noqa: E501

        Delete a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_certificate_server_by_id_with_http_info(certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str certificate_server_id: Delete a TLS server certificate. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['certificate_server_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_certificate_server_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'certificate_server_id' is set
        if ('certificate_server_id' not in params or
                params['certificate_server_id'] is None):
            raise ValueError("Missing the required parameter `certificate_server_id` when calling `delete_certificate_server_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'certificate_server_id' in params:
            path_params['CertificateServerId'] = params['certificate_server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/certificate/server/{CertificateServerId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_certificate_server_by_id(self, certificate_server_id, **kwargs):  # noqa: E501
        """get_certificate_server_by_id  # noqa: E501

        Retrieve a single TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_certificate_server_by_id(certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str certificate_server_id: Retrieve a single TLS server certificate. (required)
        :return: CertificateServer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_certificate_server_by_id_with_http_info(certificate_server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_certificate_server_by_id_with_http_info(certificate_server_id, **kwargs)  # noqa: E501
            return data

    def get_certificate_server_by_id_with_http_info(self, certificate_server_id, **kwargs):  # noqa: E501
        """get_certificate_server_by_id  # noqa: E501

        Retrieve a single TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_certificate_server_by_id_with_http_info(certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str certificate_server_id: Retrieve a single TLS server certificate. (required)
        :return: CertificateServer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['certificate_server_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_certificate_server_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'certificate_server_id' is set
        if ('certificate_server_id' not in params or
                params['certificate_server_id'] is None):
            raise ValueError("Missing the required parameter `certificate_server_id` when calling `get_certificate_server_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'certificate_server_id' in params:
            path_params['CertificateServerId'] = params['certificate_server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/certificate/server/{CertificateServerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CertificateServer',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_certificate_server(self, **kwargs):  # noqa: E501
        """list_certificate_server  # noqa: E501

        Retrieve a list of all configured TLS server certificates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_certificate_server(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sort: The field that will be used for sorting.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: CertificateServerExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_certificate_server_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_certificate_server_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_certificate_server_with_http_info(self, **kwargs):  # noqa: E501
        """list_certificate_server  # noqa: E501

        Retrieve a list of all configured TLS server certificates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_certificate_server_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sort: The field that will be used for sorting.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: CertificateServerExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'limit', 'dir', 'resume']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_certificate_server" % key
                )
            params[key] = val
        del params['kwargs']

        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `list_certificate_server`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `list_certificate_server`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_certificate_server`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_certificate_server`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `list_certificate_server`, length must be greater than or equal to `0`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_certificate_server`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_certificate_server`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/certificate/server', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CertificateServerExtended',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_certificate_server_by_id(self, certificate_server_id_params, certificate_server_id, **kwargs):  # noqa: E501
        """update_certificate_server_by_id  # noqa: E501

        Modify a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_certificate_server_by_id(certificate_server_id_params, certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param CertificateServerIdParams certificate_server_id_params: (required)
        :param str certificate_server_id: Modify a TLS server certificate. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_certificate_server_by_id_with_http_info(certificate_server_id_params, certificate_server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_certificate_server_by_id_with_http_info(certificate_server_id_params, certificate_server_id, **kwargs)  # noqa: E501
            return data

    def update_certificate_server_by_id_with_http_info(self, certificate_server_id_params, certificate_server_id, **kwargs):  # noqa: E501
        """update_certificate_server_by_id  # noqa: E501

        Modify a TLS server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_certificate_server_by_id_with_http_info(certificate_server_id_params, certificate_server_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param CertificateServerIdParams certificate_server_id_params: (required)
        :param str certificate_server_id: Modify a TLS server certificate. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['certificate_server_id_params', 'certificate_server_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_certificate_server_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'certificate_server_id_params' is set
        if ('certificate_server_id_params' not in params or
                params['certificate_server_id_params'] is None):
            raise ValueError("Missing the required parameter `certificate_server_id_params` when calling `update_certificate_server_by_id`")  # noqa: E501
        # verify the required parameter 'certificate_server_id' is set
        if ('certificate_server_id' not in params or
                params['certificate_server_id'] is None):
            raise ValueError("Missing the required parameter `certificate_server_id` when calling `update_certificate_server_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'certificate_server_id' in params:
            path_params['CertificateServerId'] = params['certificate_server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'certificate_server_id_params' in params:
            body_params = params['certificate_server_id_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/certificate/server/{CertificateServerId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
