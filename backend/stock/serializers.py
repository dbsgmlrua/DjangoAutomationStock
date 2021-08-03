from rest_framework import serializers
from .models import Stocks

class HtsStarterSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=10)

class HtsCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()