# coding: utf-8

"""
SnapshotSnapshotsApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SnapshotSnapshotsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_snapshot_lock(self, snapshot_lock, sid, **kwargs):
        """
        
        Create a new lock on this snapshot.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_snapshot_lock(snapshot_lock, sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SnapshotLockCreateParams snapshot_lock:  (required)
        :param str sid:  (required)
        :return: CreateSnapshotLockResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock', 'sid']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'snapshot_lock' is set
        if ('snapshot_lock' not in params) or (params['snapshot_lock'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock` when calling `create_snapshot_lock`")
        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `create_snapshot_lock`")


        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks'.replace('{format}', 'json')
        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'snapshot_lock' in params:
            body_params = params['snapshot_lock']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateSnapshotLockResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_snapshot_lock(self, snapshot_lock_id, sid, **kwargs):
        """
        
        Delete the snapshot lock.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_snapshot_lock(snapshot_lock_id, sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str snapshot_lock_id: Delete the snapshot lock. (required)
        :param str sid:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock_id', 'sid']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params) or (params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `delete_snapshot_lock`")
        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `delete_snapshot_lock`")


        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}'.replace('{format}', 'json')
        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_snapshot_locks(self, sid, **kwargs):
        """
        
        Delete all locks. Will try to drain count of recursively held locks so that the snapshot can be deleted.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_snapshot_locks(sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sid:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_snapshot_locks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `delete_snapshot_locks`")


        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks'.replace('{format}', 'json')
        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_snapshot_lock(self, snapshot_lock_id, sid, **kwargs):
        """
        
        Retrieve lock information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_snapshot_lock(snapshot_lock_id, sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str snapshot_lock_id: Retrieve lock information. (required)
        :param str sid:  (required)
        :return: SnapshotLocks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock_id', 'sid']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params) or (params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `get_snapshot_lock`")
        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `get_snapshot_lock`")


        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}'.replace('{format}', 'json')
        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SnapshotLocks',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def list_snapshot_locks(self, sid, **kwargs):
        """
        
        List all locks.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_snapshot_locks(sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sid:  (required)
        :param str sort: The field that will be used for sorting.  Choices are id, expires, and comment.  Default is id.
        :param int limit: Return no more than this many results at once (see resume).
        :param str dir: The direction of the sort.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: SnapshotLocksExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sid', 'sort', 'limit', 'dir', 'resume']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_snapshot_locks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `list_snapshot_locks`")

        if 'limit' in params and params['limit'] < 1.0: 
            raise ValueError("Invalid value for parameter `limit` when calling `list_snapshot_locks`, must be a value greater than or equal to `1.0`")

        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks'.replace('{format}', 'json')
        path_params = {}
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'dir' in params:
            query_params['dir'] = params['dir']
        if 'resume' in params:
            query_params['resume'] = params['resume']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SnapshotLocksExtended',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_snapshot_lock(self, snapshot_lock, snapshot_lock_id, sid, **kwargs):
        """
        
        Modify lock. All input fields are optional, but one or more must be supplied.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_snapshot_lock(snapshot_lock, snapshot_lock_id, sid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SnapshotLock snapshot_lock:  (required)
        :param str snapshot_lock_id: Modify lock. All input fields are optional, but one or more must be supplied. (required)
        :param str sid:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_lock', 'snapshot_lock_id', 'sid']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_snapshot_lock" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'snapshot_lock' is set
        if ('snapshot_lock' not in params) or (params['snapshot_lock'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock` when calling `update_snapshot_lock`")
        # verify the required parameter 'snapshot_lock_id' is set
        if ('snapshot_lock_id' not in params) or (params['snapshot_lock_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_lock_id` when calling `update_snapshot_lock`")
        # verify the required parameter 'sid' is set
        if ('sid' not in params) or (params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `update_snapshot_lock`")


        resource_path = '/platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId}'.replace('{format}', 'json')
        path_params = {}
        if 'snapshot_lock_id' in params:
            path_params['SnapshotLockId'] = params['snapshot_lock_id']
        if 'sid' in params:
            path_params['Sid'] = params['sid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'snapshot_lock' in params:
            body_params = params['snapshot_lock']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response