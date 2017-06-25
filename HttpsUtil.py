#!/usr/bin/python
# -*- coding: utf-8 -*-

# 用于进行https请求，以及MD5加密，生成签名的工具类

import http.client
import urllib.parse
import json
import hashlib
from Interface import debug_logger


class HttpsRequest(object):

    def __init__(self, url, headers):
        """
        Constructor for class HttpsRequest.
        :param url: The base url for https request
        :param headers: The headers for the request
        :return: Object of class HttpsRequest
        """
        self.__url = url
        self.__headers = headers
        self.__body = None
        self.__body_params = {}
        self.__query_string = ''

    def add_param_to_query(self, param, value, choices=()):
        """
        Add parameter to the query string.
        :param param: Parameter to be added
        :param value: Value for the parameter
        :param choices: Tuple of valid choices for the value
        :return: None
        """
        if HttpsRequest.validate_param(value, choices):
            self.__query_string += '&' + param + '=' + str(value) if self.__query_string else param + '=' + str(value)
        else:
            debug_logger.debug('{0} is invalid for {1} in the query string'.format(value, param))

    def clear_query_string(self):
        """
        Clear the query string.
        :return: None
        """
        self.__query_string = ''

    def add_param_to_body(self, param, value, choices=()):
        """
        Add parameter to the dict of request body.
        :param param: Parameter to be added
        :param value: Value for the parameter
        :param choices: Tuple of valid choices for the value
        :return: None
        """
        if HttpsRequest.validate_param(value, choices):
            self.__body_params[param] = str(value)
        else:
            debug_logger.debug('{0} is invalid for {1} in the request body'.format(value, param))

    def clear_body_params(self):
        """
        Clear the parameters dict of request body.
        :return: None
        """
        self.__body_params = {}

    @staticmethod
    def validate_param(value, choices=()):
        """
        Validate that value is in the choices tuple.
        :param value: Input to be validated
        :param choices: Tuple of valid choices for value
        :return: True: value is valid, False: value is invalid
        """
        validation = False
        if value:
            if choices == ():
                validation = True
            else:
                if value in choices:
                    validation = True
                else:
                    debug_logger.debug('{0} should be in {1}'.format(value, choices))
        return validation

    def build_sign(self, api_key, secret_key):
        """
        To build MD5 sign for user's parameters.
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: Signed string encrypted by MD5
        """
        sign = ''
        self.add_param_to_body('api_key', api_key)
        for key in sorted(self.__body_params.keys()):
            sign += key + '=' + str(self.__body_params[key]) + '&'
        data = sign + 'secret_key=' + secret_key
        self.add_param_to_body('sign', hashlib.md5(data.encode('utf8')).hexdigest().upper())

    def get(self, resource):
        """
        GET method to request resources.
        :param resource: String of URL for resources
        :return: JSON of the response of the GET request
        """
        conn = http.client.HTTPSConnection(self.__url, timeout=10)
        debug_logger.debug('Start to POST resource from: {}'.format(self.__url + resource))
        resource += '?' + self.__query_string if self.__query_string else ''
        conn.request('GET', resource)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        conn.close()
        self.clear_query_string()
        return json.loads(data)

    def post(self, resource, api_key, secret_key):
        """
        POST method to request resources.
        :param resource: String of URL for resources
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: Response of the GET request
        """
        conn = http.client.HTTPSConnection(self.__url, timeout=10)
        self.build_sign(api_key, secret_key)
        self.__body = urllib.parse.urlencode(self.__body_params)
        debug_logger.debug('Start to POST resource from: {}'.format(self.__url + resource))
        conn.request('POST', resource, self.__body, self.__headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        conn.close()
        self.clear_body_params()
        return data

    @staticmethod
    def get_response(conn):
        """
        Dispose the https response.
        :param conn: HTTPSConnection object
        :return: Decoded and formatted response
        """
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        conn.close()
        return json.loads(data)
