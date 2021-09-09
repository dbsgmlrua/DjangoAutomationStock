import sys
from PyQt5.QtWidgets import *
import win32com.client
import pandas as pd
import os
from stock.serializerObjects.StockObject import StockList, StockDetail, OhlcDetail
from stock.classes.core.Singleton import Singleton

objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')

class CreonStockDetail(metaclass=Singleton):
    def get_stockList(self):
        codeList = objCpCodeMgr.GetStockListByMarket(1) #거래소
        codeList2 = objCpCodeMgr.GetStockListByMarket(2) #코스닥

        stocklist = []
        for i, code in enumerate(codeList):
            name = objCpCodeMgr.CodeToName(code)
            stdPrice = objCpCodeMgr.GetStockStdPrice(code)
            stock = StockList(code, name, stdPrice, 1)
            stocklist.append(stock)

        for i, code in enumerate(codeList2):
            secondCode = objCpCodeMgr.GetStockSectionKind(code)
            name = objCpCodeMgr.CodeToName(code)
            stdPrice = objCpCodeMgr.GetStockStdPrice(code)
            stock = StockList(code, name, stdPrice, 2)
            stocklist.append(stock)
        
        return stocklist
    
    def getStockDetail(self, code):        
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

        stockDetail = StockDetail(code, name, time, cprice, diff, op, high, low, offer, bid, vol, vol_value)
        
        return stockDetail    

    def get_ohlc(self, code, qty):
        """인자로 받은 종목의 OHLC 가격 정보를 qty 개수만큼 반환한다."""
        cpOhlc.SetInputValue(0, code)           # 종목코드
        cpOhlc.SetInputValue(1, ord('2'))        # 1:기간, 2:개수
        cpOhlc.SetInputValue(4, qty)             # 요청개수
        cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5]) # 0:날짜, 2~5:OHLC
        cpOhlc.SetInputValue(6, ord('D'))        # D:일단위
        cpOhlc.SetInputValue(9, ord('1'))        # 0:무수정주가, 1:수정주가
        cpOhlc.BlockRequest()
        count = cpOhlc.GetHeaderValue(3)   # 3:수신개수
        columns = ['open', 'high', 'low', 'close']
        index = []
        rows = []
        for i in range(count): 
            index.append(cpOhlc.GetDataValue(0, i)) 
            rows.append([cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),
                cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i)]) 
        df = pd.DataFrame(rows, columns=columns, index=index) 
        return df
