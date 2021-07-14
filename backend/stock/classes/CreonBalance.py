import os, sys, ctypes
import win32com.client
import pandas as pd
from stock.classes.core.Singleton import Singleton

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
class CreonBalance(metaclass=Singleton):
    def get_stock_balance(self):
        """인자로 받은 종목의 종목명과 수량을 반환한다."""
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
        cpBalance.BlockRequest()     
        
        print('계좌명: ' + str(cpBalance.GetHeaderValue(0)))
        print('결제잔고수량 : ' + str(cpBalance.GetHeaderValue(1)))
        print('평가금액: ' + str(cpBalance.GetHeaderValue(3)))
        print('평가손익: ' + str(cpBalance.GetHeaderValue(4)))
        print('종목수: ' + str(cpBalance.GetHeaderValue(7)))
        print('수익률: ' + str(cpBalance.GetHeaderValue(8)))

        stocks = []
        for i in range(cpBalance.GetHeaderValue(7)):
            stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
            stock_name = cpBalance.GetDataValue(0, i)   # 종목명
            stock_qty = cpBalance.GetDataValue(15, i)   # 수량
            stock_yield = cpBalance.GetDataValue(11, i)   # 수익률
            print(str(i+1) + ' ' + stock_code + '(' + stock_name + ')' + ':' + str(stock_qty))
            
            stocks.append({'code': stock_code, 'name': stock_name, 
                'qty': stock_qty, 'yield': stock_yield})
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