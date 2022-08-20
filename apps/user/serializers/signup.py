from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(min_length=3)
    last_name = serializers.CharField(min_length=3)
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    birthday = serializers.DateField()
    about = serializers.CharField()

