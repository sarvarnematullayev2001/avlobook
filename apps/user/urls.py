from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views.notification import NotificationViewSet

# Views
from user.views.login import LoginAPIView
from user.views.signup import SignupView

router = DefaultRouter()
router.register('notification', NotificationViewSet, basename='notification')

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', SignupView.as_view()),
    path('', include(router.urls)),
]
