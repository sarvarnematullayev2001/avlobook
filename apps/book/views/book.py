from book.serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from book.models import Book

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

__all__ = ['BookViewSet',]