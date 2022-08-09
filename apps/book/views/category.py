from book.serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from book.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


__all__ = ['CategoryViewSet',]