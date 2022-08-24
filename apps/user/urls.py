from django.urls import path

# Views
from user.views.login import LoginAPIView
from user.views.signup import SignupView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', SignupView.as_view()),
]
