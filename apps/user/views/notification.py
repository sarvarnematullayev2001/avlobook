from user.serializers import NotificationSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from user.models import Notification
from rest_framework.response import Response


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def read(self, request):
        self.get_queryset().filter(is_read=False).update(is_read=True)
        return Response({"is_read": True})

    @action(detail=False, methods=['get'])
    def count_of_unread(self, request):
        count = self.get_queryset().filter(is_read=False).count()
        return Response({"count": count})