from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views.book import *
from book.views.category import *


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('', BookViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
]
