# coding: utf-8

"""
    ARTIK Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git

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

import os
import sys
import unittest

import artikcloud
from artikcloud.rest import ApiException
from artikcloud.apis.device_types_api import DeviceTypesApi
from test.test_artik_base import TestArtikBase

class TestDeviceTypesApi(TestArtikBase):
    """ DeviceTypesApi unit test stubs """

    def setUp(self):
        artikcloud.configuration.access_token = self.properties['device1.token']
        self.api = artikcloud.apis.device_types_api.DeviceTypesApi()

    def tearDown(self):
        pass

    def test_get_available_manifest_versions(self):
        """
        Test case for get_available_manifest_versions

        Get Available Manifest Versions
        """
        pass

    def test_get_device_type(self):
        """
        Test case for get_device_type

        Get Device Type
        """
        pass

    def test_get_device_types(self):
        """
        Test case for get_device_types

        Get Device Types
        """
        pass

    def test_get_device_types_by_application(self):
        """
        Test case for get_device_types_by_application

        Get Device Types by Application
        """
        pass

    def test_get_latest_manifest_properties(self):
        """
        Test case for get_latest_manifest_properties

        Get Latest Manifest Properties
        """
        pass

    def test_get_manifest_properties(self):
        """
        Test case for get_manifest_properties

        Get manifest properties
        """
        pass


if __name__ == '__main__':
    unittest.main()
