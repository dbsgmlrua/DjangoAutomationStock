from rest_framework import serializers

class HtsStarterSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=10)

class HtsCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()

class StockListSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    market = serializers.IntegerField()

class StockDetailSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    stdPrice = serializers.IntegerField()
    # ohlclist = OhlcSerializer(many=True)

class StockDetailOhlcSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=10)
    o = serializers.FloatField()
    h = serializers.FloatField()
    l = serializers.FloatField()
    c = serializers.FloatField()

class MyBalanceStockListSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    profit = serializers.FloatField()
    qty = serializers.IntegerField()

class MyBalanceSerializer(serializers.Serializer):
    balance = serializers.IntegerField()
    value = serializers.IntegerField()
    profit = serializers.FloatField()
    stockList = MyBalanceStockListSerializer(many=True)