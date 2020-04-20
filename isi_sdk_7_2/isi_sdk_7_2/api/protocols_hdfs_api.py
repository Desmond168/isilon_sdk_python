# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_7_2.api_client import ApiClient


class ProtocolsHdfsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_proxyusers_name_member(self, proxyusers_name_member, name, **kwargs):  # noqa: E501
        """create_proxyusers_name_member  # noqa: E501

        Add a member to the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_proxyusers_name_member(proxyusers_name_member, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param GroupMember proxyusers_name_member: (required)
        :param str name: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_proxyusers_name_member_with_http_info(proxyusers_name_member, name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_proxyusers_name_member_with_http_info(proxyusers_name_member, name, **kwargs)  # noqa: E501
            return data

    def create_proxyusers_name_member_with_http_info(self, proxyusers_name_member, name, **kwargs):  # noqa: E501
        """create_proxyusers_name_member  # noqa: E501

        Add a member to the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_proxyusers_name_member_with_http_info(proxyusers_name_member, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param GroupMember proxyusers_name_member: (required)
        :param str name: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['proxyusers_name_member', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_proxyusers_name_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'proxyusers_name_member' is set
        if ('proxyusers_name_member' not in params or
                params['proxyusers_name_member'] is None):
            raise ValueError("Missing the required parameter `proxyusers_name_member` when calling `create_proxyusers_name_member`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_proxyusers_name_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'proxyusers_name_member' in params:
            body_params = params['proxyusers_name_member']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/protocols/hdfs/proxyusers/{Name}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_proxyusers_name_member(self, proxyusers_name_member_id, name, **kwargs):  # noqa: E501
        """delete_proxyusers_name_member  # noqa: E501

        Remove a member from the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_proxyusers_name_member(proxyusers_name_member_id, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str proxyusers_name_member_id: Remove a member from the HDFS proxyuser. (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_proxyusers_name_member_with_http_info(proxyusers_name_member_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_proxyusers_name_member_with_http_info(proxyusers_name_member_id, name, **kwargs)  # noqa: E501
            return data

    def delete_proxyusers_name_member_with_http_info(self, proxyusers_name_member_id, name, **kwargs):  # noqa: E501
        """delete_proxyusers_name_member  # noqa: E501

        Remove a member from the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_proxyusers_name_member_with_http_info(proxyusers_name_member_id, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str proxyusers_name_member_id: Remove a member from the HDFS proxyuser. (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['proxyusers_name_member_id', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_proxyusers_name_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'proxyusers_name_member_id' is set
        if ('proxyusers_name_member_id' not in params or
                params['proxyusers_name_member_id'] is None):
            raise ValueError("Missing the required parameter `proxyusers_name_member_id` when calling `delete_proxyusers_name_member`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_proxyusers_name_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proxyusers_name_member_id' in params:
            path_params['ProxyusersNameMemberId'] = params['proxyusers_name_member_id']  # noqa: E501
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

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
            '/platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId}', 'DELETE',
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

    def list_proxyusers_name_members(self, name, **kwargs):  # noqa: E501
        """list_proxyusers_name_members  # noqa: E501

        List all the members of the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_proxyusers_name_members(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_proxyusers_name_members_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_proxyusers_name_members_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def list_proxyusers_name_members_with_http_info(self, name, **kwargs):  # noqa: E501
        """list_proxyusers_name_members  # noqa: E501

        List all the members of the HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_proxyusers_name_members_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_proxyusers_name_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_proxyusers_name_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

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
            '/platform/1/protocols/hdfs/proxyusers/{Name}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupMembers',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_proxyusers_name_member(self, proxyusers_name_member, proxyusers_name_member_id, name, **kwargs):  # noqa: E501
        """update_proxyusers_name_member  # noqa: E501

        Create a new HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_proxyusers_name_member(proxyusers_name_member, proxyusers_name_member_id, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty proxyusers_name_member: (required)
        :param str proxyusers_name_member_id: Create a new HDFS proxyuser. (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_proxyusers_name_member_with_http_info(proxyusers_name_member, proxyusers_name_member_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_proxyusers_name_member_with_http_info(proxyusers_name_member, proxyusers_name_member_id, name, **kwargs)  # noqa: E501
            return data

    def update_proxyusers_name_member_with_http_info(self, proxyusers_name_member, proxyusers_name_member_id, name, **kwargs):  # noqa: E501
        """update_proxyusers_name_member  # noqa: E501

        Create a new HDFS proxyuser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_proxyusers_name_member_with_http_info(proxyusers_name_member, proxyusers_name_member_id, name, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empty proxyusers_name_member: (required)
        :param str proxyusers_name_member_id: Create a new HDFS proxyuser. (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['proxyusers_name_member', 'proxyusers_name_member_id', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_proxyusers_name_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'proxyusers_name_member' is set
        if ('proxyusers_name_member' not in params or
                params['proxyusers_name_member'] is None):
            raise ValueError("Missing the required parameter `proxyusers_name_member` when calling `update_proxyusers_name_member`")  # noqa: E501
        # verify the required parameter 'proxyusers_name_member_id' is set
        if ('proxyusers_name_member_id' not in params or
                params['proxyusers_name_member_id'] is None):
            raise ValueError("Missing the required parameter `proxyusers_name_member_id` when calling `update_proxyusers_name_member`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_proxyusers_name_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proxyusers_name_member_id' in params:
            path_params['ProxyusersNameMemberId'] = params['proxyusers_name_member_id']  # noqa: E501
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'proxyusers_name_member' in params:
            body_params = params['proxyusers_name_member']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId}', 'PUT',
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
