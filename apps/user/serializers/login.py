# Rest-Framework
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField()