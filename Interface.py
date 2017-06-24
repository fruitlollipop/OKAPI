#!/usr/bin/python
# -*- coding: utf-8 -*-

from OKRest import OKFuture, OKSpot
import logging
import logging.config

# Loggers for collecting logs
LOG_FILE = 'log.cfg'
with open(LOG_FILE, encoding='utf-8') as fp:
    logging.config.fileConfig(fp)
debug_logger = logging.getLogger('debug')
info_logger = logging.getLogger('info')
warn_logger = logging.getLogger('warn')
error_logger = logging.getLogger('error')
critical_logger = logging.getLogger('critical')

# User's apikey，secretkey, home URL and template of resource URL
OKEX_API_KEY = 'xxxx'
OKEX_SECRET_KEY = 'xxxx'
OKEX_HOME_URL = 'https://www.okex.com'
OKEX_RESOURCE_TEMPLATE = '/api/v1/{}.do'
OKCOIN_API_KEY = 'xxxx'
OKCOIN_SECRET_KEY = 'xxxx'
OKCOIN_HOME_URL = 'https://www.okcoin.cn'
OKCOIN_RESOURCE_TEMPLATE = '/api/v1/{}.do'

# Https request headers
HTTPS_REQUEST_HEADERS = {
    'Content-type': 'application/x-www-form-urlencoded',
}


class OKRestAPI(object):

    def __init__(self):
        self.future = OKFuture(OKEX_HOME_URL, OKEX_API_KEY, OKEX_SECRET_KEY)
        self.spot = OKSpot(OKCOIN_HOME_URL, OKCOIN_API_KEY, OKCOIN_SECRET_KEY)
