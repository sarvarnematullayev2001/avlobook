# Serializers
from rest_framework import serializers
from apps.book.serializers.genre import GenreSerializer

# Models
from book.models import Book, BookInstance


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['genre'] = GenreSerializer(many=True)
        return super(BookSerializer, self).to_representation(instance)


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = [
            'book', 
            'due_by', 
            'load_status', 
            'current_user', 
            'borrower'
        ]
        depth = 2