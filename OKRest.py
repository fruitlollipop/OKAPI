#!/usr/bin/python
# -*- coding: utf-8 -*-

# To access the REST API of OK sites

from HttpsUtil import HttpsRequest
from Interface import HTTPS_REQUEST_HEADERS, OKEX_RESOURCE_TEMPLATE, OKCOIN_RESOURCE_TEMPLATE
import sys
import time


class OKRestBase(HttpsRequest):

    FutureSymbols = ('btc_usd', 'ltc_usd')
    FutureContractTypes = ('this_week', 'next_week', 'quarter')
    TimeTypes = ('1min',
                 '3min',
                 '5min',
                 '15min',
                 '30min',
                 '1day',
                 '3day',
                 '1week',
                 '1hour',
                 '2hour',
                 '4hour',
                 '6hour',
                 '12hour'
                 )
    SpotSymbols = ('btc_cny', 'ltc_cny', 'eth_cny')

    def __init__(self, url):
        """
        Constructor for class of OKCoinBase.
        :param url: Base URL for REST API of Future
        :return: Object of OKRestBase
        """
        super(OKRestBase, self).__init__(url, HTTPS_REQUEST_HEADERS)


class OKFuture(object):

    def __init__(self, url, api_key, secret_key):
        """
        Constructor for class of OKFuture.
        :param url: Base URL for REST API of OK Future
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: Object of OKFuture
        """
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.rest_interface = OKRestBase(url)

    # 获取OKEX合约行情
    def market_future_ticker(self, symbol, contract_type):
        """

        :param symbol:
        :param contract_type:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_ticker'))

    # 获取OKEX合约深度信息
    def market_future_depth(self, symbol, contract_type, size, merge=0):
        """

        :param symbol:
        :param contract_type:
        :param size:
        :param merge:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, 201)))
        self.rest_interface.add_param_to_query('merge', merge, (1,))
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_depth'))

    # 获取OKEX合约交易记录信息
    def market_future_trades(self, symbol, contract_type):
        """

        :param symbol:
        :param contract_type:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_trades'))

    # 获取OKEX合约指数信息
    def market_future_index(self, symbol):
        """

        :param symbol:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_index'))

    # 获取美元人民币汇率
    def market_exchange_rate(self):
        """

        :return:
        """
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('exchange_rate'))

    # 获取交割预估价
    def market_future_estimated_price(self, symbol):
        """

        :param symbol:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_estimated_price'))

    # 获取虚拟合约的K线数据
    def market_future_kline(self, symbol, time_type, contract_type, size=0, since=0):
        """

        :param symbol:
        :param time_type:
        :param contract_type:
        :param size:
        :param since:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('type', time_type, OKRestBase.TimeTypes)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, sys.maxsize)))
        self.rest_interface.add_param_to_query('since', since, tuple(range(1, int(time.time()))))
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_kline'))

    # 获取当前可用合约总持仓量
    def market_future_hold_amount(self, symbol, contract_type):
        """

        :param symbol:
        :param contract_type:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_hold_amount'))

    # 获取合约最高买价和最低卖价
    def market_future_price_limit(self, symbol, contract_type):
        """

        :param symbol:
        :param contract_type:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_price_limit'))

    # 获取OKEX合约账户信息 （全仓）
    def deals_future_userinfo(self):
        """

        :return:
        """
        self.rest_interface.add_param_to_body('api_key', self.__api_key, (self.__api_key,))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_userinfo'), self.__secret_key)

    # 获取用户持仓获取OKEX合约账户信息 （全仓）
    def deals_future_position(self, symbol, contract_type):
        """

        :param symbol:
        :param contract_type:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('api_key', self.__api_key, (self.__api_key,))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_position'), self.__secret_key)

    # 合约下单
    def deals_future_trade(self, symbol, contract_type, price, amount, trade_type, match_price='', lever_rate=''):
        """

        :param symbol:
        :param contract_type:
        :param price:
        :param amount:
        :param trade_type:
        :param match_price:
        :param lever_rate:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('price', price, ())
        self.rest_interface.add_param_to_body('amount', amount, ())
        self.rest_interface.add_param_to_body('type', trade_type, ('1', '2', '3', '4'))
        self.rest_interface.add_param_to_body('match_price', match_price, ('0', '1'))
        self.rest_interface.add_param_to_body('lever_rate', lever_rate, ('10', '20'))
        self.rest_interface.add_param_to_body('api_key', self.__api_key, (self.__api_key,))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_trade'), self.__secret_key)

    # 获取OKEX合约交易历史（非个人）
    def deals_future_trades_history(self, symbol, date, since):
        """

        :param symbol:
        :param date:
        :param since:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('date', date, ())
        self.rest_interface.add_param_to_body('since', since, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_trades_history'), self.__secret_key)

    # 批量下单
    def deals_future_batch_trade(self, symbol, contract_type, orders_data, lever_rate=''):
        """

        :param symbol:
        :param contract_type:
        :param orders_data:
        :param lever_rate:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('orders_data', orders_data, ())
        self.rest_interface.add_param_to_body('lever_rate', lever_rate, ('10', '20'))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_batch_trade'), self.__secret_key)

    # 取消合约订单
    def deals_future_cancel(self, symbol, contract_type, order_id):
        """

        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_cancel'), self.__secret_key)

    # 获取合约订单信息
    def deals_future_order_info(self, symbol, contract_type, status, order_id, current_page='0', page_length='0'):
        """

        :param symbol:
        :param contract_type:
        :param status:
        :param order_id:
        :param current_page:
        :param page_length:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('status', status, ('1', '2'))
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('current_page', current_page, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(map(str, range(1, 51))))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_order_info'), self.__secret_key)

    # 批量获取合约订单信息
    def deals_future_orders_info(self, symbol, contract_type, order_id):
        """

        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_orders_info'), self.__secret_key)

    # 获取逐仓合约账户信息
    def deals_future_userinfo_4fix(self):
        """

        :return:
        """
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_userinfo_4fix'), self.__secret_key)

    # 逐仓用户持仓查询
    def deals_future_position_4fix(self, symbol, contract_type, trade_type='0'):
        """

        :param symbol:
        :param contract_type:
        :param trade_type:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('type', trade_type, ('1',))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_position_4fix'), self.__secret_key)

    # 获取合约爆仓单
    def deals_future_explosive(self, symbol, contract_type, status, current_page='0', page_number='0', page_length='0'):
        """

        :param symbol:
        :param contract_type:
        :param status:
        :param current_page:
        :param page_number:
        :param page_length:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('status', status, ('0', '1'))
        self.rest_interface.add_param_to_body('current_page', current_page, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_number', page_number, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(map(str, range(1, 51))))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_explosive'), self.__secret_key)

    # 提币BTC/LTC
    def deals_withdraw(self, symbol, chargefee, trade_pwd, withdraw_address, withdraw_amount, target):
        """

        :param symbol:
        :param chargefee:
        :param trade_pwd:
        :param withdraw_address:
        :param withdraw_amount:
        :param target:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('chargefee', chargefee, ())
        self.rest_interface.add_param_to_body('trade_pwd', trade_pwd, ())
        self.rest_interface.add_param_to_body('withdraw_address', withdraw_address, ())
        self.rest_interface.add_param_to_body('withdraw_amount', withdraw_amount, ())
        self.rest_interface.add_param_to_body('target', target, ('okcn', 'okcom', 'okex', 'address'))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('withdraw'), self.__secret_key)

    # 取消提币BTC/LTC
    def deals_cancel_withdraw(self, symbol, contract_type, trade_type='0'):
        """

        :param symbol:
        :param contract_type:
        :param trade_type:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('trade_type', trade_type, ('1',))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('cancel_withdraw'), self.__secret_key)

    # 查询提币BTC/LTC信息
    def deals_withdraw_info(self, symbol, withdraw_id):
        """

        :param symbol:
        :param withdraw_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('withdraw_info'), self.__secret_key)


class OKSpot(object):

    def __init__(self, url, api_key, secret_key):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.rest_interface = OKRestBase(url)

    # 获取OKCoin行情
    def market_spot_ticker(self, symbol):
        """

        :param symbol:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('ticker'))

    # 获取OKCoin市场深度
    def market_spot_depth(self, symbol, size, merge=0):
        """

        :param symbol:
        :param size:
        :param merge:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, 201)))
        self.rest_interface.add_param_to_query('merge', merge, (1,))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('depth'))

    # 获取OKEX合约交易记录信息
    def market_spot_trades(self, symbol, since=0):
        """

        :param symbol:
        :param since:
        :return:
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('since', since, tuple(range(1, sys.maxsize)))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('trades'))

    # 获取虚拟合约的K线数据
    def market_spot_kline(self, symbol, time_type, size=0, since=0):
        """

        :param symbol:
        :param time_type:
        :param size:
        :param since:
        :return:
        """

        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('type', time_type, OKRestBase.TimeTypes)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, sys.maxsize)))
        self.rest_interface.add_param_to_query('since', since, tuple(range(1, int(time.time()))))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('kline'))

    # 获取用户信息
    def deals_spot_userinfo(self):
        """

        :return:
        """
        self.rest_interface.add_param_to_body('api_key', self.__api_key, (self.__api_key,))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('userinfo'), self.__secret_key)

    # 下单交易
    def deals_future_trade(self, symbol, trade_type, price, amount):
        """

        :param symbol:
        :param trade_type:
        :param price:
        :param amount:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('type', trade_type, ('buy', 'sell', 'buy_market', 'sell_market'))
        self.rest_interface.add_param_to_body('price', price, ())
        self.rest_interface.add_param_to_body('amount', amount, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key, (self.__api_key,))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('trade'), self.__secret_key)

    # 获取OKCoin历史交易信息（非个人）
    def deals_spot_trade_history(self, symbol, date, since):
        """

        :param symbol:
        :param date:
        :param since:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('date', date, ())
        self.rest_interface.add_param_to_body('since', since, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('trades_history'), self.__secret_key)

    # 批量下单
    def deals_spot_batch_trade(self, symbol, contract_type, orders_data, lever_rate=''):
        """

        :param symbol:
        :param contract_type:
        :param orders_data:
        :param lever_rate:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('orders_data', orders_data, ())
        self.rest_interface.add_param_to_body('lever_rate', lever_rate, ('10', '20'))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('batch_trade'), self.__secret_key)

    # 撤销订单
    def deals_spot_cancel_order(self, symbol, contract_type, order_id):
        """

        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('cancel_order'), self.__secret_key)

    # 获取用户的订单信息
    def deals_spot_order_info(self, symbol, contract_type, status, order_id, current_page='0', page_length='0'):
        """

        :param symbol:
        :param contract_type:
        :param status:
        :param order_id:
        :param current_page:
        :param page_length:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('status', status, ('1', '2'))
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('current_page', current_page, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(map(str, range(1, 51))))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('order_info'), self.__secret_key)

    # 批量获取用户订单
    def deals_spot_orders_info(self, symbol, contract_type, order_id):
        """

        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('orders_info'), self.__secret_key)

    # 获取历史订单信息，只返回最近两天的信息
    def deals_spot_order_history(self, symbol, contract_type, order_id):
        """

        :param symbol:
        :param contract_type:
        :param order_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('order_history'), self.__secret_key)

    # 提币BTC/LTC/ETH
    def deals_withdraw(self, symbol, chargefee, trade_pwd, withdraw_address, withdraw_amount, target):
        """

        :param symbol:
        :param chargefee:
        :param trade_pwd:
        :param withdraw_address:
        :param withdraw_amount:
        :param target:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('chargefee', chargefee, ())
        self.rest_interface.add_param_to_body('trade_pwd', trade_pwd, ())
        self.rest_interface.add_param_to_body('withdraw_address', withdraw_address, ())
        self.rest_interface.add_param_to_body('withdraw_amount', withdraw_amount, ())
        self.rest_interface.add_param_to_body('target', target, ('okcn', 'okcom', 'okex', 'address'))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('withdraw'), self.__secret_key)

    # 取消提币BTC/LTC
    def deals_cancel_withdraw(self, symbol, contract_type, trade_type='0'):
        """

        :param symbol:
        :param contract_type:
        :param trade_type:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('trade_type', trade_type, ('1',))
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('cancel_withdraw'), self.__secret_key)

    # 查询提币BTC/LTC信息
    def deals_withdraw_info(self, symbol, withdraw_id):
        """

        :param symbol:
        :param withdraw_id:
        :return:
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, ())
        self.rest_interface.add_param_to_body('api_key', self.__api_key)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('withdraw_info'), self.__secret_key)
