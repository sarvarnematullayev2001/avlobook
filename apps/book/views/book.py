# Serializers
from book.serializers import BookSerializer

# Views
from rest_framework.viewsets import ModelViewSet

# Models
from book.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


__all__ = ['BookViewSet',]