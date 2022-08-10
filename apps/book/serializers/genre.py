# Serializers
from rest_framework import serializers

# Models
from book.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'