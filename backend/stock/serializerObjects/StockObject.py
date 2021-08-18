
class Stock(object):
    def __init__(self, code, name, qty, yd):
        self.code = code
        self.name = name
        self.qty = qty
        self.yd = yd

class StockList(object):
    def __init__(self, code, name, stdprice, market):
        self.code = code
        self.name = name
        self.stdprice = stdprice
        self.market = market

class Balance(object):
    def __init__(self, name, balance, value, profit, qty, yld, stocks):
        self.name = name
        self.balance = balance
        self.value = value
        self.profit = profit
        self.qty = qty
        self.yld = yld
        self.stocks = stocks

class StockDetail(object):
    def __init__(self, name, code, ohlc):
        self.name = name
        self.code = code
        self.ohlclist = ohlc

class OhlcDetail(object):
    def __init__(self, date, o, h, l, c):
        self.date = date
        self.o = o
        self.h = h
        self.l = l
        self.c = c