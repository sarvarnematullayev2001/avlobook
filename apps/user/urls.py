from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from views.notification import NotificationViewSet

router = DefaultRouter()
router.register('notification', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
