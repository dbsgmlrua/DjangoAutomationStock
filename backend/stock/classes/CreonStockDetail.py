import os, sys, ctypes
#serializers
from stock.serializerObjects.StockDetailObject import StockList, StockDetail, StockDetailOhlc

from stock.classes.CreonClients import CreonClients
from stock.classes.core.Singleton import Singleton

class CreonStockDetail(metaclass=Singleton):
    def get_stock_list(self):
        creonClients = CreonClients()
        objCpCodeMgr = getattr(creonClients,'CpCodeMgr')
        codeList = objCpCodeMgr.GetStockListByMarket(1) #거래소
        codeList2 = objCpCodeMgr.GetStockListByMarket(2) #코스닥

        stocklist = []
        for i, code in enumerate(codeList):
            name = objCpCodeMgr.CodeToName(code)
            stdPrice = objCpCodeMgr.GetStockStdPrice(code)
            stock = StockList(code, name, 1)
            stocklist.append(stock)

        for i, code in enumerate(codeList2):
            secondCode = objCpCodeMgr.GetStockSectionKind(code)
            name = objCpCodeMgr.CodeToName(code)
            stdPrice = objCpCodeMgr.GetStockStdPrice(code)
            stock = StockList(code, name, 2)
            stocklist.append(stock)
        return stocklist