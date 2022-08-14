from django.db import models

from core.base_model import BaseModel
from user.models.base import User


class Message(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return f"from {self.sender} to {self.receiver}"
