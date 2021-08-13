from rest_framework import serializers
from .models import Stocks

class HtsStarterSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=10)

class HtsCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()

class StockListSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)
    market = serializers.CharField(max_length=10)