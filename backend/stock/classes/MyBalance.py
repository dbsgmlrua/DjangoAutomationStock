from stock.classes.core.Singleton import Singleton
from stock.serializerObjects.StockObject import Stock

class MyBalance(metaclass=Singleton):
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.value = 0
        self.profit = 0
        self.qty = 0
        self.yld = 0
        self.stocks = []

    def getName(self):
        print(self.name)
    def setName(self, name):
        self.name = name
