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
from artikcloud.apis.devicestatus_api import DevicestatusApi


class TestDevicestatusApi(unittest.TestCase):
    """ DevicestatusApi unit test stubs """

    def setUp(self):
        self.api = artikcloud.apis.devicestatus_api.DevicestatusApi()

    def tearDown(self):
        pass

    def test_get_device_status(self):
        """
        Test case for get_device_status

        Get Device Status
        """
        pass

    def test_get_devices_status(self):
        """
        Test case for get_devices_status

        Get Devices Status
        """
        pass

    def test_put_device_status(self):
        """
        Test case for put_device_status

        Update Device Status
        """
        pass


if __name__ == '__main__':
    unittest.main()