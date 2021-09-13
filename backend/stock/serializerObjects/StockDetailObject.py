class StockList(object):
    def __init__(self, code, name, market):
        self.code = code
        self.name = name
        self.market = market

class StockDetail(object):
    def __init__(self, code, name, stdPrice):
        self.code = code
        self.name = name
        self.stdPrice = stdPrice

class StockDetailOhlc(object):
    def __init__(self, date, o, h, l, c):
        self.date = date
        self.o = o
        self.h = h
        self.l = l
        self.c = c