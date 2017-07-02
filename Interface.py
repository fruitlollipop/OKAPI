#!/usr/bin/python
# -*- coding: utf-8 -*-

from OKRest import OKFuture, OKSpot
from cfg import OKEX_HOME_URL, OKEX_API_KEY, OKEX_SECRET_KEY, OKCOIN_HOME_URL, OKCOIN_API_KEY, OKCOIN_SECRET_KEY


class OKRestAPI(object):

    def __init__(self):
        self.future = OKFuture(OKEX_HOME_URL, OKEX_API_KEY, OKEX_SECRET_KEY)
        self.spot = OKSpot(OKCOIN_HOME_URL, OKCOIN_API_KEY, OKCOIN_SECRET_KEY)
