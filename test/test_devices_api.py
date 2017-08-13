# coding: utf-8

"""
    ARTIK Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import artikcloud
from artikcloud.rest import ApiException
from artikcloud.apis.devices_api import DevicesApi


class TestDevicesApi(unittest.TestCase):
    """ DevicesApi unit test stubs """

    def setUp(self):
        self.api = artikcloud.apis.devices_api.DevicesApi()

    def tearDown(self):
        pass

    def test_add_device(self):
        """
        Test case for add_device

        Add Device
        """
        pass

    def test_delete_device(self):
        """
        Test case for delete_device

        Delete Device
        """
        pass

    def test_delete_device_token(self):
        """
        Test case for delete_device_token

        Delete Device Token
        """
        pass

    def test_get_device(self):
        """
        Test case for get_device

        Get Device
        """
        pass

    def test_get_device_presence(self):
        """
        Test case for get_device_presence

        Get device presence information
        """
        pass

    def test_get_device_token(self):
        """
        Test case for get_device_token

        Get Device Token
        """
        pass

    def test_update_device(self):
        """
        Test case for update_device

        Update Device
        """
        pass

    def test_update_device_token(self):
        """
        Test case for update_device_token

        Update Device Token
        """
        pass


if __name__ == '__main__':
    unittest.main()
