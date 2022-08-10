from book.serializers import GenreSerializer
from rest_framework.viewsets import ModelViewSet
from book.models import Genre


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


__all__ = ['GenreViewSet',]