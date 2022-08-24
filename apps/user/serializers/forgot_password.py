from rest_framework import serializers


class SendForgotPasswordCodeSerializer(serializers.Serializer):
    username = serializers.CharField()


class CheckForgotPasswordCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class ForgotPasswordCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()
    new_password = serializers.CharField()
