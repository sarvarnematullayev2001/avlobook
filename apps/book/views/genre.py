# Serializers
from book.serializers import GenreSerializer

# Views
from rest_framework.viewsets import ModelViewSet

# Models
from book.models import Genre


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


__all__ = ['GenreViewSet',]