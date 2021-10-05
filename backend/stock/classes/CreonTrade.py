import os, sys, ctypes
import win32com.client
import pandas as pd
import time, calendar
from stock.classes.core.Singleton import Singleton


class CreonTradeBase(metaclass=Singleton):
    def CheckBuying(self, code):
        print("CheckBuying!")
        return False
    def BuyingStock(self, code, qty, value):
        print("Buy!")
    def CheckSelling(self, code):
        print("CheckSelling!")
        return False
    def SellingStock(self, code, qty):
        print("Sell!")
    def InitTrade(self):
        print("InitTrade!")
    def AutoTrade(self):
        self.InitTrade()
        while True:
            time.sleep(1)
            if self.CheckBuying("CODE"):
                self.BuyingStock("CODE", 1, 100)
            if self.CheckSelling("CODE"):
                self.SellingStock("CODE", 100)
            break
