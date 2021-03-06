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
    
    def get_stock_detail(self, code):
        creonClients = CreonClients()
        objStockMst = getattr(creonClients,'StockMst')
        objStockMst.SetInputValue(0, code) 
        objStockMst.BlockRequest()

        code = objStockMst.GetHeaderValue(0)  # 종목코드
        name = objStockMst.GetHeaderValue(1)  # 종목명
        time = objStockMst.GetHeaderValue(4)  # 시간
        cprice = objStockMst.GetHeaderValue(11)  # 종가
        diff = objStockMst.GetHeaderValue(12)  # 대비
        op = objStockMst.GetHeaderValue(13)  # 시가
        high = objStockMst.GetHeaderValue(14)  # 고가
        low = objStockMst.GetHeaderValue(15)  # 저가
        offer = objStockMst.GetHeaderValue(16)  # 매도호가
        bid = objStockMst.GetHeaderValue(17)  # 매수호가
        vol = objStockMst.GetHeaderValue(18)  # 거래량
        vol_value = objStockMst.GetHeaderValue(19)  # 거래대금

        stockDetail = StockDetail(code=code, name=name, stdPrice=bid)
        
        return stockDetail 
    
    def get_stock_detail_ohlc(self, code, qty):
        creonClients = CreonClients()
        cpOhlc = getattr(creonClients, 'StockChart')

        cpOhlc.SetInputValue(0, code)           # 종목코드
        cpOhlc.SetInputValue(1, ord('2'))        # 1:기간, 2:개수
        cpOhlc.SetInputValue(4, qty)             # 요청개수
        cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5]) # 0:날짜, 2~5:OHLC
        cpOhlc.SetInputValue(6, ord('D'))        # D:일단위
        cpOhlc.SetInputValue(9, ord('1'))        # 0:무수정주가, 1:수정주가

        ohlcList = []
        for i in range(count): 
            data = StockDetailOhlc(date=cpOhlc.GetDataValue(0, i), o=cpOhlc.GetDataValue(1, i), h=cpOhlc.GetDataValue(2, i), l=cpOhlc.GetDataValue(3, i), c=cpOhlc.GetDataValue(4, i))
            ohlcList.append(data)

        return ohlcList
