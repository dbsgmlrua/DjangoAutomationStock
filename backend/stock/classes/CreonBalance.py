import os, sys, ctypes
import win32com.client
import pandas as pd
import time, calendar
from stock.classes.core.Singleton import Singleton
from stock.serializerObjects.StockObject import Stock, StockList, Balance, StockDetail, OhlcDetail

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

class CreonBalance(metaclass=Singleton):
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
        ohlcList = []
        for i in range(10):
            ohlcgraph = OhlcDetail(i,1,1,1,1)
            ohlcList.append(ohlcgraph)
        
        stockDetail = StockDetail("Name", code, ohlcList)
        
        return stockDetail

    def get_balance(self):
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
        cpBalance.BlockRequest()    
        stocks = []
        for i in range(cpBalance.GetHeaderValue(7)):
            stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
            stock_name = cpBalance.GetDataValue(0, i)   # 종목명
            stock_qty = cpBalance.GetDataValue(15, i)   # 수량
            stock_yield = cpBalance.GetDataValue(11, i)   # 수익률
            print(str(i+1) + ' ' + stock_code + '(' + stock_name + ')' + ':' + str(stock_qty))
            
            stock = Stock(code=stock_code, name=stock_name, qty=stock_qty, yd=stock_yield)

            stocks.append(stock) 
        
        balance = Balance(name=cpBalance.GetHeaderValue(0), balance=cpBalance.GetHeaderValue(1), value=cpBalance.GetHeaderValue(3), profit=cpBalance.GetHeaderValue(4), qty=cpBalance.GetHeaderValue(7), yld=cpBalance.GetHeaderValue(8), stocks=stocks)
        return balance
        
    def get_stock_balance(self):
        """인자로 받은 종목의 종목명과 수량을 반환한다."""
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
        cpBalance.BlockRequest()
        stocks = []
        for i in range(cpBalance.GetHeaderValue(7)):
            stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
            stock_name = cpBalance.GetDataValue(0, i)   # 종목명
            stock_qty = cpBalance.GetDataValue(15, i)   # 수량
            stock_yield = cpBalance.GetDataValue(11, i)   # 수익률
            print(str(i+1) + ' ' + stock_code + '(' + stock_name + ')' + ':' + str(stock_qty))
            
            stock = Stock(code=stock_code, name=stock_name, qty=stock_qty, yd=stock_yield)

            stocks.append(stock)
        return stocks

    def get_stock_info(self, code):
        """인자로 받은 종목의 종목명과 수량을 반환한다."""
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
        cpBalance.BlockRequest()   

        for i in range(cpBalance.GetHeaderValue(7)):
            stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
            stock_name = cpBalance.GetDataValue(0, i)   # 종목명
            stock_qty = cpBalance.GetDataValue(15, i)   # 수량
            if stock_code == code:  
                return stock_name, stock_qty  
        
        stock_name = cpCodeMgr.CodeToName(code)
        return stock_name, 0

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

    def sell_sthing(self, code, qty):
        """일부 종목을 최유리 지정가 IOC 조건으로 매도한다."""
        try:
            stocks = get_stock_balance('NONE')
            items = []
            for s in stocks:
                items.append(s['code'])
            
            if code in items:
                qty = 0
                for s in stocks:
                    if code in s['code']:
                        qty = s['qty']
                        break
                if qty > 0:
                    acc = cpTradeUtil.AccountNumber[0]       # 계좌번호
                    accFlag = cpTradeUtil.GoodsList(acc, 1)  # -1:전체, 1:주식, 2:선물/옵션   
                    cpOrder.SetInputValue(0, "1")         # 1:매도, 2:매수
                    cpOrder.SetInputValue(1, acc)         # 계좌번호
                    cpOrder.SetInputValue(2, accFlag[0])  # 주식상품 중 첫번째
                    cpOrder.SetInputValue(3, code)   # 종목코드
                    cpOrder.SetInputValue(4, qty)    # 매도수량
                    cpOrder.SetInputValue(7, "1")   # 조건 0:기본, 1:IOC, 2:FOK
                    cpOrder.SetInputValue(8, "12")  # 호가 12:최유리, 13:최우선 
                    ret = cpOrder.BlockRequest()
                    print('최유리 IOC 매도' + str(s['code']) + str(s['name']) + str(s['qty']) + '-> cpOrder.BlockRequest() -> returned' + str(ret))
                    if ret == 4:
                        remain_time = cpStatus.LimitRequestRemainTime
                        print('주의: 연속 주문 제한, 대기시간: ' + str(remain_time/1000))
                        return False
                    return True
            return False
        except Exception as ex:
            print("sell_sthing() -> exception! " + str(ex))
            return False