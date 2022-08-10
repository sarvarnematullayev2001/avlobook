from rest_framework import serializers
from book.models import Book
from apps.book.serializers.genre import GenreSerializer


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['genre'] = GenreSerializer(many=True)
        return super(BookSerializer, self).to_representation(instance)