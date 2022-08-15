from rest_framework import serializers
from chat.models import Message
from user.models.base import User


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender_name', 'receiver_name', 'description', 'time']