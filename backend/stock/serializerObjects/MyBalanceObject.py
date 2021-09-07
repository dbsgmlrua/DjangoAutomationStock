class MyBalanceObject(object):
    def __init__(self, totalBalance, totalProfit, stockList):
        self.totalBalance = totalBalance
        self.totalProfit = totalProfit
        self.stockList = stockList

class MyBalanceStockListObject(object):
    def __init__(self, name, price, profit, qty):
        self.name = name
        self.price = price
        self.profit = profit
        self.qty = qty
