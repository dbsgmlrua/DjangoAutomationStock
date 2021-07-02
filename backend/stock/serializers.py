from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class RunningCheckerSerializer(serializers.Serializer):
    running = serializers.BooleanField()