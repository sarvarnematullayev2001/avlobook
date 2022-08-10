from django.db import models
from core.base_model import BaseModel
from user.models.base import User


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    street_home = models.CharField(max_length=256)
    building_number = models.IntegerField(null=True, blank=True)
    building_floor = models.IntegerField()
    phone_number = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)
    is_default = models.BooleanField(default=False)

