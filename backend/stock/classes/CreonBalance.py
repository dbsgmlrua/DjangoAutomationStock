import os, sys, ctypes
import win32com.client
from stock.classes.core.Singleton import Singleton

cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
class CreonBalance(metaclass=Singleton):
    def get_stock_balance(self, code):
        """인자로 받은 종목의 종목명과 수량을 반환한다."""
        cpTradeUtil.TradeInit()
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
        cpBalance.SetInputValue(0, acc)         # 계좌번호
        cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
        cpBalance.BlockRequest()     
        if code == 'ALL':
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
            if code == 'ALL' or code == 'NONE':
                if code == 'ALL':
                    print(str(i+1) + ' ' + stock_code + '(' + stock_name + ')' + ':' + str(stock_qty))
                stocks.append({'code': stock_code, 'name': stock_name, 
                    'qty': stock_qty, 'yield': stock_yield})
            if stock_code == code:  
                return stock_name, stock_qty
        if code == 'ALL' or code == 'NONE':
            return stocks
        else:
            stock_name = cpCodeMgr.CodeToName(code)
            return stock_name, 0