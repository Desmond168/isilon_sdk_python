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


class ZonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_zone(self, zone, **kwargs):  # noqa: E501
        """create_zone  # noqa: E501

        Create a new access zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_zone(zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param ZoneCreateParams zone: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_zone_with_http_info(zone, **kwargs)  # noqa: E501
        else:
            (data) = self.create_zone_with_http_info(zone, **kwargs)  # noqa: E501
            return data

    def create_zone_with_http_info(self, zone, **kwargs):  # noqa: E501
        """create_zone  # noqa: E501

        Create a new access zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_zone_with_http_info(zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param ZoneCreateParams zone: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone' is set
        if ('zone' not in params or
                params['zone'] is None):
            raise ValueError("Missing the required parameter `zone` when calling `create_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'zone' in params:
            body_params = params['zone']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/zones', 'POST',
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

    def delete_zone(self, zone_id, **kwargs):  # noqa: E501
        """delete_zone  # noqa: E501

        Delete the access zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_zone(zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int zone_id: Delete the access zone. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_zone_with_http_info(zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_zone_with_http_info(zone_id, **kwargs)  # noqa: E501
            return data

    def delete_zone_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """delete_zone  # noqa: E501

        Delete the access zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_zone_with_http_info(zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int zone_id: Delete the access zone. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `delete_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in params:
            path_params['ZoneId'] = params['zone_id']  # noqa: E501

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
            '/platform/3/zones/{ZoneId}', 'DELETE',
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

    def get_zone(self, zone_id, **kwargs):  # noqa: E501
        """get_zone  # noqa: E501

        Retrieve the access zone information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zone(zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int zone_id: Retrieve the access zone information. (required)
        :return: Zones
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_zone_with_http_info(zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zone_with_http_info(zone_id, **kwargs)  # noqa: E501
            return data

    def get_zone_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """get_zone  # noqa: E501

        Retrieve the access zone information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zone_with_http_info(zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int zone_id: Retrieve the access zone information. (required)
        :return: Zones
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `get_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in params:
            path_params['ZoneId'] = params['zone_id']  # noqa: E501

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
            '/platform/3/zones/{ZoneId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Zones',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_zones(self, **kwargs):  # noqa: E501
        """list_zones  # noqa: E501

        List all access zones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_zones(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ZonesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_zones_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_zones_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_zones_with_http_info(self, **kwargs):  # noqa: E501
        """list_zones  # noqa: E501

        List all access zones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_zones_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ZonesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_zones" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/platform/3/zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZonesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_zone(self, zone, zone_id, **kwargs):  # noqa: E501
        """update_zone  # noqa: E501

        Modify the access zone. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_zone(zone, zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param Zone zone: (required)
        :param int zone_id: Modify the access zone. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_zone_with_http_info(zone, zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_zone_with_http_info(zone, zone_id, **kwargs)  # noqa: E501
            return data

    def update_zone_with_http_info(self, zone, zone_id, **kwargs):  # noqa: E501
        """update_zone  # noqa: E501

        Modify the access zone. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_zone_with_http_info(zone, zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param Zone zone: (required)
        :param int zone_id: Modify the access zone. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone', 'zone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone' is set
        if ('zone' not in params or
                params['zone'] is None):
            raise ValueError("Missing the required parameter `zone` when calling `update_zone`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `update_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in params:
            path_params['ZoneId'] = params['zone_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'zone' in params:
            body_params = params['zone']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/zones/{ZoneId}', 'PUT',
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
