from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views.book import *
from book.views.genre import *


router = DefaultRouter()
router.register('genre', GenreViewSet, basename='genre')
router.register('', BookViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
]
