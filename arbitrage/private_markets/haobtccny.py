# Copyright (C) 2013, Maxime Biais <maxime@biais.org>

from .market import Market, TradeException
import time
import base64
import hmac
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import hashlib
import sys
import json
import config
from lib.exchange import exchange
from lib.settings import HAOBTC_API_URL

import logging

class PrivateHaobtcCNY(Market):
    haobtc = None

    def __init__(self, HAOBTC_API_KEY, HAOBTC_SECRET_TOKEN):
        super().__init__()
        self.haobtc =  exchange(HAOBTC_API_URL, HAOBTC_API_KEY, HAOBTC_SECRET_TOKEN, 'haobtc')

        self.currency = "CNY"
        self.get_info()

    def _buy(self, amount, price):
        """Create a buy limit order"""
        response = self.haobtc.buy(amount, price)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def _sell(self, amount, price):
        """Create a sell limit order"""
        response = self.haobtc.sell(amount, price)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def _buy_maker(self, amount, price):
        response = self.haobtc.bidMakerOnly(amount, price)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def _sell_maker(self, amount, price):
        response = self.haobtc.askMakerOnly(amount, price)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def _get_order(self, order_id):
        response = self.haobtc.orderInfo(order_id)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def _cancel_order(self, order_id):
        response = self.haobtc.cancel(order_id)
        if "code" in response:
            print (response)
            return False
            raise TradeException(response["code"])
        return response

    def get_info(self):
        """Get balance"""
        response = self.haobtc.accountInfo()
        if "code" in response:
            logging.warn("get_info failed", response)
            return
            raise TradeException(response["error"])
        if response:
            self.btc_balance = float(response["exchange_btc"])
            self.cny_balance = float(response["exchange_cny"])
            self.btc_frozen = float(response["exchange_frozen_btc"])
            self.cny_frozen = float(response["exchange_frozen_cny"])

        return response
