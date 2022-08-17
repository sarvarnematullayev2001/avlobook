from django.db import models

from user.models.base import User
from core.base_model import BaseModel
from file.models import File


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ForeignKey(File, on_delete=models.CASCADE, related_name='profile')


    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"