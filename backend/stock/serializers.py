from rest_framework import serializers

class HtsStarterSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=10)


class HtsCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()

class StocksSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)
    qty = serializers.IntegerField()
    yd = serializers.DecimalField()