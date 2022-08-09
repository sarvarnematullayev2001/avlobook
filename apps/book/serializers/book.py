from rest_framework import serializers
from book.models import Book
from book.serializers.category import CategorySerializer


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(many=True)
        return super(BookSerializer, self).to_representation(instance)