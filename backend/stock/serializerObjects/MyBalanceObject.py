class MyBalanceObject(object):
    def __init__(self, balance, value, profit, stockList):
        self.balance = balance
        self.value = value
        self.profit = profit
        self.stockList = stockList

class MyBalanceStockListObject(object):
    def __init__(self, code, name, price, profit, qty):
        self.code = code
        self.name = name
        self.price = price
        self.profit = profit
        self.qty = qty
