
class Stock(object):
    def __init__(self, code, name, qty, yd):
        self.code = code
        self.name = name
        self.qty = qty
        self.yd = yd
        
class Balance(object):
    def __init__(self, name, balance, value, profit, qty, yld, stocks):
        self.name = name
        self.balance = balance
        self.value = value
        self.profit = profit
        self.qty = qty
        self.yld = yld
        self.stocks = stocks