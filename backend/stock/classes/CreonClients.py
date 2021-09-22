import os, sys, ctypes
import win32com.client
import os
import time
import json
from django.core.exceptions import ImproperlyConfigured
from pywinauto import application
from stock.classes.core.Singleton import Singleton

# 크레온 플러스 공통 OBJECT
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpStock = win32com.client.Dispatch('DsCbo1.StockMst')
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')

class CreonClients(metaclass=Singleton):
    def __init__(self):
        self.CpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
        self.CpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
        self.CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
        self.StockMst = win32com.client.Dispatch('DsCbo1.StockMst')
        self.StockChart = win32com.client.Dispatch('CpSysDib.StockChart')
        self.CpTd6033 = win32com.client.Dispatch('CpTrade.CpTd6033')
        self.CpTdNew5331A = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
        self.CpTd0311 = win32com.client.Dispatch('CpTrade.CpTd0311') 
        self.CpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
        self.StockChart = win32com.client.Dispatch('CpSysDib.StockChart')

