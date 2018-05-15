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


class LicenseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_license_license(self, license_license, **kwargs):  # noqa: E501
        """create_license_license  # noqa: E501

        Install a new license file and/or activate evaluation licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_license_license(license_license, async=True)
        >>> result = thread.get()

        :param async bool
        :param LicenseLicenseCreateParams license_license: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_license_license_with_http_info(license_license, **kwargs)  # noqa: E501
        else:
            (data) = self.create_license_license_with_http_info(license_license, **kwargs)  # noqa: E501
            return data

    def create_license_license_with_http_info(self, license_license, **kwargs):  # noqa: E501
        """create_license_license  # noqa: E501

        Install a new license file and/or activate evaluation licenses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_license_license_with_http_info(license_license, async=True)
        >>> result = thread.get()

        :param async bool
        :param LicenseLicenseCreateParams license_license: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_license']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_license_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_license' is set
        if ('license_license' not in params or
                params['license_license'] is None):
            raise ValueError("Missing the required parameter `license_license` when calling `create_license_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_license' in params:
            body_params = params['license_license']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/5/license/licenses', 'POST',
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

    def get_license_generate(self, **kwargs):  # noqa: E501
        """get_license_generate  # noqa: E501

        Generate license activation file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_license_generate(async=True)
        >>> result = thread.get()

        :param async bool
        :param str action: enum: license_list_only (default), generate_activation, download_activation. Generate an activation file or return a list of activated licenses. If generating an activation file and no licenses are specified, the default configuration is to generate an activation file with the current set of licensed features. download_activation returns HTTP headers and the same XML content as seen in the response activation.
        :param str licenses_to_include: Licenses to include in activation file.
        :param str licenses_to_exclude: Licenses to omit from activation file.
        :param str only_these_licenses: Activate only the defined licenses. This setting overrides all other license activation settings.
        :return: LicenseGenerate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_license_generate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_license_generate_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_license_generate_with_http_info(self, **kwargs):  # noqa: E501
        """get_license_generate  # noqa: E501

        Generate license activation file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_license_generate_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str action: enum: license_list_only (default), generate_activation, download_activation. Generate an activation file or return a list of activated licenses. If generating an activation file and no licenses are specified, the default configuration is to generate an activation file with the current set of licensed features. download_activation returns HTTP headers and the same XML content as seen in the response activation.
        :param str licenses_to_include: Licenses to include in activation file.
        :param str licenses_to_exclude: Licenses to omit from activation file.
        :param str only_these_licenses: Activate only the defined licenses. This setting overrides all other license activation settings.
        :return: LicenseGenerate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['action', 'licenses_to_include', 'licenses_to_exclude', 'only_these_licenses']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_generate" % key
                )
            params[key] = val
        del params['kwargs']

        if ('action' in params and
                len(params['action']) < 0):
            raise ValueError("Invalid value for parameter `action` when calling `get_license_generate`, length must be greater than or equal to `0`")  # noqa: E501
        if ('licenses_to_include' in params and
                len(params['licenses_to_include']) > 2500):
            raise ValueError("Invalid value for parameter `licenses_to_include` when calling `get_license_generate`, length must be less than or equal to `2500`")  # noqa: E501
        if ('licenses_to_include' in params and
                len(params['licenses_to_include']) < 1):
            raise ValueError("Invalid value for parameter `licenses_to_include` when calling `get_license_generate`, length must be greater than or equal to `1`")  # noqa: E501
        if 'licenses_to_include' in params and not re.search('.+', params['licenses_to_include']):  # noqa: E501
            raise ValueError("Invalid value for parameter `licenses_to_include` when calling `get_license_generate`, must conform to the pattern `/.+/`")  # noqa: E501
        if ('licenses_to_exclude' in params and
                len(params['licenses_to_exclude']) > 2500):
            raise ValueError("Invalid value for parameter `licenses_to_exclude` when calling `get_license_generate`, length must be less than or equal to `2500`")  # noqa: E501
        if ('licenses_to_exclude' in params and
                len(params['licenses_to_exclude']) < 1):
            raise ValueError("Invalid value for parameter `licenses_to_exclude` when calling `get_license_generate`, length must be greater than or equal to `1`")  # noqa: E501
        if 'licenses_to_exclude' in params and not re.search('.+', params['licenses_to_exclude']):  # noqa: E501
            raise ValueError("Invalid value for parameter `licenses_to_exclude` when calling `get_license_generate`, must conform to the pattern `/.+/`")  # noqa: E501
        if ('only_these_licenses' in params and
                len(params['only_these_licenses']) > 2500):
            raise ValueError("Invalid value for parameter `only_these_licenses` when calling `get_license_generate`, length must be less than or equal to `2500`")  # noqa: E501
        if ('only_these_licenses' in params and
                len(params['only_these_licenses']) < 1):
            raise ValueError("Invalid value for parameter `only_these_licenses` when calling `get_license_generate`, length must be greater than or equal to `1`")  # noqa: E501
        if 'only_these_licenses' in params and not re.search('.+', params['only_these_licenses']):  # noqa: E501
            raise ValueError("Invalid value for parameter `only_these_licenses` when calling `get_license_generate`, must conform to the pattern `/.+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in params:
            query_params.append(('action', params['action']))  # noqa: E501
        if 'licenses_to_include' in params:
            query_params.append(('licenses_to_include', params['licenses_to_include']))  # noqa: E501
        if 'licenses_to_exclude' in params:
            query_params.append(('licenses_to_exclude', params['licenses_to_exclude']))  # noqa: E501
        if 'only_these_licenses' in params:
            query_params.append(('only_these_licenses', params['only_these_licenses']))  # noqa: E501

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
            '/platform/5/license/generate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseGenerate',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_license_license(self, license_license_id, **kwargs):  # noqa: E501
        """get_license_license  # noqa: E501

        Retrieve license information for the feature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_license_license(license_license_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str license_license_id: Retrieve license information for the feature. (required)
        :return: LicenseLicenses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_license_license_with_http_info(license_license_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_license_license_with_http_info(license_license_id, **kwargs)  # noqa: E501
            return data

    def get_license_license_with_http_info(self, license_license_id, **kwargs):  # noqa: E501
        """get_license_license  # noqa: E501

        Retrieve license information for the feature.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_license_license_with_http_info(license_license_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str license_license_id: Retrieve license information for the feature. (required)
        :return: LicenseLicenses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_license_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_license" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'license_license_id' is set
        if ('license_license_id' not in params or
                params['license_license_id'] is None):
            raise ValueError("Missing the required parameter `license_license_id` when calling `get_license_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'license_license_id' in params:
            path_params['LicenseLicenseId'] = params['license_license_id']  # noqa: E501

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
            '/platform/5/license/licenses/{LicenseLicenseId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseLicenses',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_license_licenses(self, **kwargs):  # noqa: E501
        """list_license_licenses  # noqa: E501

        Retrieve license information for all licensable products.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_license_licenses(async=True)
        >>> result = thread.get()

        :param async bool
        :return: LicenseLicensesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_license_licenses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_license_licenses_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_license_licenses_with_http_info(self, **kwargs):  # noqa: E501
        """list_license_licenses  # noqa: E501

        Retrieve license information for all licensable products.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_license_licenses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: LicenseLicensesExtended
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
                    " to method list_license_licenses" % key
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
            '/platform/5/license/licenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicenseLicensesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
