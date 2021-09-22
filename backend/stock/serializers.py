from rest_framework import serializers

class HtsStarterSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=10)

class HtsCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()

class StockListSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    market = serializers.IntegerField()

class OhlcSerializer(serializers.Serializer):
    date = serializers.IntegerField()
    o = serializers.IntegerField()
    h = serializers.IntegerField()
    l = serializers.IntegerField()
    c = serializers.IntegerField()

class StockDetailSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    # ohlclist = OhlcSerializer(many=True)

class MyBalanceStockListSerializer(serializers.Serializer):
    name = serializers.IntegerField()
    price = serializers.IntegerField()
    profit = serializers.FloatField()
    qty = serializers.IntegerField()

class MyBalanceSerializer(serializers.Serializer):
    balance = serializers.IntegerField()
    value = serializers.IntegerField()
    profit = serializers.FloatField()
    stockList = MyBalanceStockListSerializer(many=True)
