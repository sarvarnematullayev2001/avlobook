from django.db import models

from core.base_model import BaseModel
from user.models.base import User
from book.models.book import BookInstance


class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    book_intance = models.ForeignKey(BookInstance, on_delete=models.CASCADE, related_name='notification')
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ('-created_datetime', 'is_read')