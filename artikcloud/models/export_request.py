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

from pprint import pformat
from six import iteritems
import re


class ExportRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, end_date=None, format=None, order=None, sdids=None, sdtids=None, start_date=None, trial_id=None, uids=None):
        """
        ExportRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_date': 'int',
            'format': 'str',
            'order': 'str',
            'sdids': 'str',
            'sdtids': 'str',
            'start_date': 'int',
            'trial_id': 'str',
            'uids': 'str'
        }

        self.attribute_map = {
            'end_date': 'endDate',
            'format': 'format',
            'order': 'order',
            'sdids': 'sdids',
            'sdtids': 'sdtids',
            'start_date': 'startDate',
            'trial_id': 'trialId',
            'uids': 'uids'
        }

        self._end_date = end_date
        self._format = format
        self._order = order
        self._sdids = sdids
        self._sdtids = sdtids
        self._start_date = start_date
        self._trial_id = trial_id
        self._uids = uids

    @property
    def end_date(self):
        """
        Gets the end_date of this ExportRequest.


        :return: The end_date of this ExportRequest.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ExportRequest.


        :param end_date: The end_date of this ExportRequest.
        :type: int
        """

        self._end_date = end_date

    @property
    def format(self):
        """
        Gets the format of this ExportRequest.


        :return: The format of this ExportRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ExportRequest.


        :param format: The format of this ExportRequest.
        :type: str
        """

        self._format = format

    @property
    def order(self):
        """
        Gets the order of this ExportRequest.


        :return: The order of this ExportRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this ExportRequest.


        :param order: The order of this ExportRequest.
        :type: str
        """

        self._order = order

    @property
    def sdids(self):
        """
        Gets the sdids of this ExportRequest.


        :return: The sdids of this ExportRequest.
        :rtype: str
        """
        return self._sdids

    @sdids.setter
    def sdids(self, sdids):
        """
        Sets the sdids of this ExportRequest.


        :param sdids: The sdids of this ExportRequest.
        :type: str
        """

        self._sdids = sdids

    @property
    def sdtids(self):
        """
        Gets the sdtids of this ExportRequest.


        :return: The sdtids of this ExportRequest.
        :rtype: str
        """
        return self._sdtids

    @sdtids.setter
    def sdtids(self, sdtids):
        """
        Sets the sdtids of this ExportRequest.


        :param sdtids: The sdtids of this ExportRequest.
        :type: str
        """

        self._sdtids = sdtids

    @property
    def start_date(self):
        """
        Gets the start_date of this ExportRequest.


        :return: The start_date of this ExportRequest.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ExportRequest.


        :param start_date: The start_date of this ExportRequest.
        :type: int
        """

        self._start_date = start_date

    @property
    def trial_id(self):
        """
        Gets the trial_id of this ExportRequest.


        :return: The trial_id of this ExportRequest.
        :rtype: str
        """
        return self._trial_id

    @trial_id.setter
    def trial_id(self, trial_id):
        """
        Sets the trial_id of this ExportRequest.


        :param trial_id: The trial_id of this ExportRequest.
        :type: str
        """

        self._trial_id = trial_id

    @property
    def uids(self):
        """
        Gets the uids of this ExportRequest.


        :return: The uids of this ExportRequest.
        :rtype: str
        """
        return self._uids

    @uids.setter
    def uids(self, uids):
        """
        Sets the uids of this ExportRequest.


        :param uids: The uids of this ExportRequest.
        :type: str
        """

        self._uids = uids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
