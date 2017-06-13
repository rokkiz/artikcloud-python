# coding: utf-8

"""
    ARTIK Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DevicessharesApi(object):
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

    def create_share_for_device(self, device_id, device_share_info, **kwargs):
        """
        Share a device 
        Share a device 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_share_for_device(device_id, device_share_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param DeviceShareInfo device_share_info: Device object that needs to be added (required)
        :return: DeviceSharingId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_share_for_device_with_http_info(device_id, device_share_info, **kwargs)
        else:
            (data) = self.create_share_for_device_with_http_info(device_id, device_share_info, **kwargs)
            return data

    def create_share_for_device_with_http_info(self, device_id, device_share_info, **kwargs):
        """
        Share a device 
        Share a device 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_share_for_device_with_http_info(device_id, device_share_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param DeviceShareInfo device_share_info: Device object that needs to be added (required)
        :return: DeviceSharingId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'device_share_info']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_share_for_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `create_share_for_device`")
        # verify the required parameter 'device_share_info' is set
        if ('device_share_info' not in params) or (params['device_share_info'] is None):
            raise ValueError("Missing the required parameter `device_share_info` when calling `create_share_for_device`")


        collection_formats = {}

        resource_path = 'in/api/devices/{deviceId}/shares'.replace('{format}', 'json')
        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'device_share_info' in params:
            body_params = params['device_share_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceSharingId',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_sharing_for_device(self, device_id, share_id, **kwargs):
        """
        Delete specific share of the given device id
        Delete specific share of the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_sharing_for_device(device_id, share_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param str share_id: Share ID. (required)
        :return: DeviceSharingId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_sharing_for_device_with_http_info(device_id, share_id, **kwargs)
        else:
            (data) = self.delete_sharing_for_device_with_http_info(device_id, share_id, **kwargs)
            return data

    def delete_sharing_for_device_with_http_info(self, device_id, share_id, **kwargs):
        """
        Delete specific share of the given device id
        Delete specific share of the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_sharing_for_device_with_http_info(device_id, share_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param str share_id: Share ID. (required)
        :return: DeviceSharingId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'share_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sharing_for_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `delete_sharing_for_device`")
        # verify the required parameter 'share_id' is set
        if ('share_id' not in params) or (params['share_id'] is None):
            raise ValueError("Missing the required parameter `share_id` when calling `delete_sharing_for_device`")


        collection_formats = {}

        resource_path = 'in/api/devices/{deviceId}/shares/{shareId}'.replace('{format}', 'json')
        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']
        if 'share_id' in params:
            path_params['shareId'] = params['share_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceSharingId',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_shares_for_device(self, device_id, **kwargs):
        """
        List all shares for the given device id
        List all shares for the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_shares_for_device(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param int count: Desired count of items in the result set.
        :param int offset: Offset for pagination.
        :return: DeviceSharingEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_shares_for_device_with_http_info(device_id, **kwargs)
        else:
            (data) = self.get_all_shares_for_device_with_http_info(device_id, **kwargs)
            return data

    def get_all_shares_for_device_with_http_info(self, device_id, **kwargs):
        """
        List all shares for the given device id
        List all shares for the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_shares_for_device_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param int count: Desired count of items in the result set.
        :param int offset: Offset for pagination.
        :return: DeviceSharingEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'count', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_shares_for_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_all_shares_for_device`")


        collection_formats = {}

        resource_path = 'in/api/devices/{deviceId}/shares'.replace('{format}', 'json')
        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = {}
        if 'count' in params:
            query_params['count'] = params['count']
        if 'offset' in params:
            query_params['offset'] = params['offset']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceSharingEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_sharing_for_device(self, device_id, share_id, **kwargs):
        """
        Get specific share of the given device id
        Get specific share of the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sharing_for_device(device_id, share_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param str share_id: Share ID. (required)
        :return: DeviceSharing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sharing_for_device_with_http_info(device_id, share_id, **kwargs)
        else:
            (data) = self.get_sharing_for_device_with_http_info(device_id, share_id, **kwargs)
            return data

    def get_sharing_for_device_with_http_info(self, device_id, share_id, **kwargs):
        """
        Get specific share of the given device id
        Get specific share of the given device id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sharing_for_device_with_http_info(device_id, share_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :param str share_id: Share ID. (required)
        :return: DeviceSharing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'share_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sharing_for_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_sharing_for_device`")
        # verify the required parameter 'share_id' is set
        if ('share_id' not in params) or (params['share_id'] is None):
            raise ValueError("Missing the required parameter `share_id` when calling `get_sharing_for_device`")


        collection_formats = {}

        resource_path = 'in/api/devices/{deviceId}/shares/{shareId}'.replace('{format}', 'json')
        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']
        if 'share_id' in params:
            path_params['shareId'] = params['share_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceSharing',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)