#!/usr/bin/python
# -*- coding: utf-8 -*-

# To access the REST API of OK sites

from HttpsUtil import HttpsRequest
from cfg import HTTPS_REQUEST_HEADERS, OKEX_RESOURCE_TEMPLATE, OKCOIN_RESOURCE_TEMPLATE
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
        Get information for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_ticker'))

    # 获取OKEX合约深度信息
    def market_future_depth(self, symbol, contract_type, size, merge=0):
        """
        Get depth for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param size: Integer, in range(1, 201)
        :param merge: Integer
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, 201)))
        self.rest_interface.add_param_to_query('merge', merge, (1,))
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_depth'))

    # 获取OKEX合约交易记录信息
    def market_future_trades(self, symbol, contract_type):
        """
        Get information of trades' records for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_trades'))

    # 获取OKEX合约指数信息
    def market_future_index(self, symbol):
        """
        Get information of trades' index for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_index'))

    # 获取美元人民币汇率
    def market_exchange_rate(self):
        """
        Get exchange rate of USD to RMB
        :return: GET response
        """
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('exchange_rate'))

    # 获取交割预估价
    def market_future_estimated_price(self, symbol):
        """
        Get estimated price for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_estimated_price'))

    # 获取虚拟合约的K线数据
    def market_future_kline(self, symbol, time_type, contract_type, size=0, since=0):
        """
        Get data for k line for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param time_type: String, in OKRestBase.TimeTypes
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param size: Integer
        :param since: Long, get data after this time stamp
        :return: GET response
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
        Get the hold amount for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_hold_amount'))

    # 获取合约最高买价和最低卖价
    def market_future_price_limit(self, symbol, contract_type):
        """
        Get price limit for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_query('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.get(OKEX_RESOURCE_TEMPLATE.format('future_price_limit'))

    # 获取OKEX合约账户信息 （全仓）
    def deals_future_userinfo(self):
        """
        Get information of users for future
        :return: POST response
        """
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_userinfo'), self.__api_key,
                                        self.__secret_key)

    # 获取用户持仓获取OKEX合约账户信息 （全仓）
    def deals_future_position(self, symbol, contract_type):
        """
        Get information of users for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_position'), self.__api_key,
                                        self.__secret_key)

    # 合约下单
    def deals_future_trade(self, symbol, contract_type, price, amount, trade_type, match_price='', lever_rate=''):
        """
        Place order for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param price: String
        :param amount: String
        :param trade_type: String, choices are '1', '2', '3', '4'
        :param match_price: String, choices are '0', '1', when it's '1', price makes no sense
        :param lever_rate: String, choices are "10", "20", by default is "10"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('price', price, ())
        self.rest_interface.add_param_to_body('amount', amount, ())
        self.rest_interface.add_param_to_body('type', trade_type, ('1', '2', '3', '4'))
        self.rest_interface.add_param_to_body('match_price', match_price, ('0', '1'))
        self.rest_interface.add_param_to_body('lever_rate', lever_rate, ('10', '20'))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_trade'), self.__api_key,
                                        self.__secret_key)

    # 获取OKEX合约交易历史（非个人）
    def deals_future_trades_history(self, symbol, date, since):
        """
        Get information of history trades for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param date: String, like "yyyy-MM-dd"
        :param since: Long, get items of data from this trade id
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('date', date, ())
        self.rest_interface.add_param_to_body('since', since, ())
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_trades_history'), self.__api_key,
                                        self.__secret_key)

    # 批量下单
    def deals_future_batch_trade(self, symbol, contract_type, orders_data, lever_rate=''):
        """
        Place multiple orders for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param orders_data: String, "[{price:3,amount:5,type:'sell'},{price:3,amount:3,type:'buy'}]", no more than 5
        :param lever_rate: String, choices are "10", "20", by default is "10"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('orders_data', orders_data, ())
        self.rest_interface.add_param_to_body('lever_rate', lever_rate, ('10', '20'))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_batch_trade'), self.__api_key,
                                        self.__secret_key)

    # 取消合约订单
    def deals_future_cancel(self, symbol, contract_type, order_id):
        """
        Cancel order for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param order_id: String, multiple order IDs is separated by ',' but no more than 3
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_cancel'), self.__api_key,
                                        self.__secret_key)

    # 获取合约订单信息
    def deals_future_order_info(self, symbol, contract_type, status, order_id, current_page='0', page_length='0'):
        """
        Get information of order for users for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param status: String, '1' for for uncompleted orders, ''2' for completed orders
        :param order_id: Long, -1 for uncompleted orders otherwise a certain order ID
        :param current_page: Integer
        :param page_length: Integer, items in each page, no more than 50
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('status', status, ('1', '2'))
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        self.rest_interface.add_param_to_body('current_page', current_page, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(map(str, range(1, 51))))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_order_info'), self.__api_key,
                                        self.__secret_key)

    # 批量获取合约订单信息
    def deals_future_orders_info(self, symbol, contract_type, order_id):
        """
        Get information of multiple orders for users for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param order_id: String, IDs for orders are separated by ',' and no more than 50 orders at one time
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('order_id', order_id, ())
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_orders_info'), self.__api_key,
                                        self.__secret_key)

    # 获取逐仓合约账户信息
    def deals_future_userinfo_4fix(self):
        """
        Get 4fix userinfo for future
        :return: POST response
        """
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_userinfo_4fix'), self.__api_key,
                                        self.__secret_key)

    # 逐仓用户持仓查询
    def deals_future_position_4fix(self, symbol, contract_type, trade_type='0'):
        """
        Get 4fix position for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param trade_type: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('type', trade_type, ('1',))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_position_4fix'), self.__api_key,
                                        self.__secret_key)

    # 获取合约爆仓单
    def deals_future_explosive(self, symbol, contract_type, status, current_page='0', page_number='0', page_length='0'):
        """
        Get explosive for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param contract_type: String, choices are "this_week", "next_week", "quarter"
        :param status: String, '0' for completed in recent seven days, '1' for uncompleted in recent seven days
        :param current_page: Integer
        :param page_number: Integer
        :param page_length: Integer, items in each page, no more than 50
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('contract_type', contract_type, OKRestBase.FutureContractTypes)
        self.rest_interface.add_param_to_body('status', status, ('0', '1'))
        self.rest_interface.add_param_to_body('current_page', current_page, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_number', page_number, tuple(map(str, range(1, sys.maxsize))))
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(map(str, range(1, 51))))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('future_explosive'), self.__api_key,
                                        self.__secret_key)

    # 提币BTC/LTC
    def deals_future_withdraw(self, symbol, chargefee, trade_pwd, withdraw_address, withdraw_amount, target):
        """
        Withdraw currencies for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param chargefee: Double, Internet >=0, BTC in [0.0001，0.01], LTC in [0.001，0.2], Internal: 0
        :param trade_pwd: String
        :param withdraw_address: String, Authorized address, E-mail or telephone number
        :param withdraw_amount: Double, BTC>=0.01 LTC>=0.1
        :param target: String, Domestic："okcn", International："okcom", OKEX："okex", External："address"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('chargefee', chargefee, tuple())
        self.rest_interface.add_param_to_body('trade_pwd', trade_pwd, tuple())
        self.rest_interface.add_param_to_body('withdraw_address', withdraw_address, tuple())
        self.rest_interface.add_param_to_body('withdraw_amount', withdraw_amount, tuple())
        self.rest_interface.add_param_to_body('target', target, ('okcn', 'okcom', 'okex', 'address'))
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('withdraw'), self.__api_key, self.__secret_key)

    # 取消提币BTC/LTC
    def deals_future_cancel_withdraw(self, symbol, withdraw_id):
        """
        Cancel withdraw for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param withdraw_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, tuple())
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('cancel_withdraw'), self.__api_key,
                                        self.__secret_key)

    # 查询提币BTC/LTC信息
    def deals_future_withdraw_info(self, symbol, withdraw_id):
        """
        Get information of withdraw for future
        :param symbol: String, choices are "btc_usd", "ltc_usd"
        :param withdraw_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.FutureSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, tuple())
        return self.rest_interface.post(OKEX_RESOURCE_TEMPLATE.format('withdraw_info'), self.__api_key,
                                        self.__secret_key)


class OKSpot(object):

    def __init__(self, url, api_key, secret_key):
        """
        Constructor for class of OKSpot
        :param url: Base URL for REST API of OK Future
        :param api_key: String of API KEY
        :param secret_key: String of SECRET KEY
        :return: Object of OKSpot
        """
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.rest_interface = OKRestBase(url)

    # 获取OKCoin行情
    def market_spot_ticker(self, symbol):
        """
        Get information for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('ticker'))

    # 获取OKCoin市场深度
    def market_spot_depth(self, symbol, size, merge=0):
        """
        Get depth for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param size: Integer, in range(1, 201)
        :param merge: Integer
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, 201)))
        self.rest_interface.add_param_to_query('merge', merge, (1,))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('depth'))

    # 获取OKEX合约交易记录信息
    def market_spot_trades(self, symbol, since=0):
        """
        Get information of trades' records for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param since: Long, get data after this trade ID except this ID and no more than 600
        :return: GET response
        """
        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('since', since, tuple(range(1, sys.maxsize)))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('trades'))

    # 获取虚拟合约的K线数据
    def market_spot_kline(self, symbol, time_type, size=0, since=0):
        """
        Get data for k line for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param time_type: String, in OKRestBase.TimeTypes
        :param size: Integer
        :param since: Long, get data after this time stamp
        :return: GET response
        """

        self.rest_interface.add_param_to_query('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_query('type', time_type, OKRestBase.TimeTypes)
        self.rest_interface.add_param_to_query('size', size, tuple(range(1, sys.maxsize)))
        self.rest_interface.add_param_to_query('since', since, tuple(range(1, int(time.time()))))
        return self.rest_interface.get(OKCOIN_RESOURCE_TEMPLATE.format('kline'))

    # 获取用户信息
    def deals_spot_userinfo(self):
        """
        Get information of users for spot
        :return: POST response
        """
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('userinfo'), self.__api_key,
                                        self.__secret_key)

    # 下单交易
    def deals_spot_trade(self, symbol, order_type, price='', amount=''):
        """
        Place order for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param order_type: String, choices are "buy", "sell", "buy_market", "sell_market"
        :param price: Double, please refer to https://www.okcoin.cn/rest_api.html
        :param amount: Double, please refer to https://www.okcoin.cn/rest_api.html
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('type', order_type, ('buy', 'sell', 'buy_market', 'sell_market'))
        self.rest_interface.add_param_to_body('price', price, tuple())
        self.rest_interface.add_param_to_body('amount', amount, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('trade'), self.__api_key, self.__secret_key)

    # 获取OKCoin历史交易信息（非个人）
    def deals_spot_trade_history(self, symbol, since):
        """
        Get information of history trades for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param since: Long, get 600 items of data from this trade id
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('since', since, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('trade_history'), self.__api_key,
                                        self.__secret_key)

    # 批量下单
    def deals_spot_batch_trade(self, symbol, orders_data, order_type=''):
        """
        Place multiple orders for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param orders_data: String, "[{price:3,amount:5,type:'sell'},{price:3,amount:3,type:'buy'}]", no more than 5
        :param order_type: String, choices are 'buy', "sell"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('type', order_type, ('buy', 'sell'))
        self.rest_interface.add_param_to_body('orders_data', orders_data, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('batch_trade'), self.__api_key,
                                        self.__secret_key)

    # 撤销订单
    def deals_spot_cancel_order(self, symbol, order_id):
        """
        Cancel order for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param order_id: String, multiple order IDs is separated by ',' but no more than 3
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('order_id', order_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('cancel_order'), self.__api_key,
                                        self.__secret_key)

    # 获取用户的订单信息
    def deals_spot_order_info(self, symbol, order_id):
        """
        Get information of order for users for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param order_id: Long, -1 for uncompleted orders otherwise a certain order ID
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('order_id', order_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('order_info'), self.__api_key,
                                        self.__secret_key)

    # 批量获取用户订单
    def deals_spot_orders_info(self, symbol, order_type, order_id):
        """
        Get information of multiple orders for users for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param order_type: Integer, 0 for uncompleted orders, 1 for completed orders
        :param order_id: String, IDs for orders are separated by ',' and no more than 50 orders at one time
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('type', order_type, (0, 1))
        self.rest_interface.add_param_to_body('order_id', order_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('orders_info'), self.__api_key,
                                        self.__secret_key)

    # 获取历史订单信息，只返回最近两天的信息
    def deals_spot_order_history(self, symbol, status, current_page, page_length):
        """
        Get information of orders in history, only the recent two days for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param status: Integer, 0 for for uncompleted orders, 1 for completed orders
        :param current_page: Integer
        :param page_length: Integer, items in the page, no more than 200
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('status', status, (0, 1))
        self.rest_interface.add_param_to_body('current_page', current_page)
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(range(1, 201)))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('order_history'), self.__api_key,
                                        self.__secret_key)

    # 提币BTC/LTC/ETH
    def deals_spot_withdraw(self, symbol, chargefee, trade_pwd, withdraw_address, withdraw_amount, target):
        """
        Withdraw currencies for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param chargefee: Double, Internet >=0, BTC in [0.0001，0.01], LTC in [0.001，0.2], ETH in [0.01], Internal: 0
        :param trade_pwd: String
        :param withdraw_address: String, Authorized address, E-mail or telephone number
        :param withdraw_amount: Double, BTC>=0.01 LTC>=0.1 ETH>=0.01
        :param target: String, Domestic："okcn", International："okcom", OKEX："okex", External："address"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('chargefee', chargefee, tuple())
        self.rest_interface.add_param_to_body('trade_pwd', trade_pwd, tuple())
        self.rest_interface.add_param_to_body('withdraw_address', withdraw_address, tuple())
        self.rest_interface.add_param_to_body('withdraw_amount', withdraw_amount, tuple())
        self.rest_interface.add_param_to_body('target', target, ('okcn', 'okcom', 'okex', 'address'))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('withdraw'), self.__api_key, self.__secret_key)

    # 取消提币BTC/LTC
    def deals_spot_cancel_withdraw(self, symbol, withdraw_id):
        """
        Cancel withdraw for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param withdraw_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('cancel_withdraw'), self.__api_key,
                                        self.__secret_key)

    # 查询提币BTC/LTC信息
    def deals_spot_withdraw_info(self, symbol, withdraw_id):
        """
        Get information of withdraw for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param withdraw_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('withdraw_id', withdraw_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('withdraw_info'), self.__api_key,
                                        self.__secret_key)

    # 获取放款深度前10
    def deals_spot_lend_depth(self, symbol):
        """
        Get top ten lend depth for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('lend_depth'), self.__api_key,
                                        self.__secret_key)

    # 查询用户借款信息
    def deals_spot_borrows_info(self, symbol):
        """
        Get information of users' borrows for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('borrows_info'), self.__api_key,
                                        self.__secret_key)

    # 申请借款
    def deals_spot_borrow_money(self, symbol, days, amount, rate):
        """
        Borrow_money for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param days: String
        :param amount: Double
        :param rate: String, in [0.0001, 0.01]
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('days', days, tuple())
        self.rest_interface.add_param_to_body('amount', amount, tuple())
        self.rest_interface.add_param_to_body('rate', rate, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('borrow_money'), self.__api_key,
                                        self.__secret_key)

    # 取消借款申请
    def deals_spot_cancel_borrow(self, symbol, borrow_id):
        """
        Cancel borrow for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param borrow_id: Long
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('borrow_id', borrow_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('cancel_borrow'), self.__api_key,
                                        self.__secret_key)

    # 获取借款订单记录
    def deals_spot_borrow_order_info(self, borrow_id):
        """
        Get information of borrow order for spot
        :param borrow_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('borrow_id', borrow_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('borrow_order_info'), self.__api_key,
                                        self.__secret_key)

    # 用户还全款
    def deals_spot_repayment(self, borrow_id):
        """
        Pay off for spot
        :param borrow_id: String
        :return: POST response
        """
        self.rest_interface.add_param_to_body('borrow_id', borrow_id, tuple())
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('repayment'), self.__api_key, self.__secret_key)

    # 未还款列表
    def deals_spot_unrepayments_info(self, symbol, current_page, page_length):
        """
        Get information of unrepayments for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param current_page: Integer
        :param page_length: Integer, items in the page, no more than 50
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('current_page', current_page, tuple())
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(range(1, 51)))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('unrepayments_info'), self.__api_key,
                                        self.__secret_key)

    # 获取用户提现/充值记录
    def deals_spot_account_records(self, symbol, order_type, current_page, page_length):
        """
        Get information of records for spot
        :param symbol: String, choices are "btc_cny", "ltc_cny" or "eth_cny"
        :param order_type: Integer, 0 for deposit and 1 for withdrawal
        :param current_page: Integer
        :param page_length: Integer, items in the page, no more than 50
        :return: POST response
        """
        self.rest_interface.add_param_to_body('symbol', symbol, OKRestBase.SpotSymbols)
        self.rest_interface.add_param_to_body('order_type', order_type, (0, 1))
        self.rest_interface.add_param_to_body('current_page', current_page, tuple())
        self.rest_interface.add_param_to_body('page_length', page_length, tuple(range(1, 51)))
        return self.rest_interface.post(OKCOIN_RESOURCE_TEMPLATE.format('account_records'), self.__api_key,
                                        self.__secret_key)
