# Rest-Framework
from rest_framework import serializers

# Project
from user.models import User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    password = serializers.CharField()
