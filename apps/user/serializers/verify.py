from rest_framework import serializers


class UserVerifySerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class ReSendVerifyUserSerializer(serializers.Serializer):
    username = serializers.CharField()
