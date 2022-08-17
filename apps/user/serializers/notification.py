from rest_framework import serializers
from user.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created_datetime = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Notification
        exclude = ['modified_datetime', 'user']