from django.urls import path
from rest_framework.routers import DefaultRouter

# Views
from user.views.login import LoginAPIView
from user.views.signup import SignupView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', SignupView.as_view()),
]
