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
from artikcloud.models.presence_model import PresenceModel


class TestPresenceModel(unittest.TestCase):
    """ PresenceModel unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPresenceModel(self):
        """
        Test PresenceModel
        """
        model = artikcloud.models.presence_model.PresenceModel()


if __name__ == '__main__':
    unittest.main()