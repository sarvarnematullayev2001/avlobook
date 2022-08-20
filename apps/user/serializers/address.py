from rest_framework import serializers
from user.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'city',
            'region',
            'street_home',
            'building_number',
            'building_floor',
            'phone_number',
            'is_default'
        ]

    def create(self, validated_data):
        addresses_count = Address.objects.filter(user=validated_data['user']).count()
        if addresses_count == 0:
            validated_data['is_default'] = True
        return super(AddressSerializer, self).create(validated_data)
