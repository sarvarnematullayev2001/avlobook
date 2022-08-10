from django.db import models
from .genre import Genre
from apps.core.base_model import BaseModel


class Book(BaseModel):
    
    TYPE_BOOK = (
        ('Erkin', 'Erkin'), 
        ('Ijara', 'Ijara')
    )
    
    STATUS = (
        ('Olingan', 'Olingan'),
        ('Olinmagan', 'Olinmagan')
    )
    
    LANGUAGE = (
        ("O'zbek", "O'zbek"),
        ("Ingliz", "Ingliz"),
        ("Rus", "Rus")
    )
    
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    types = models.CharField(max_length=5, choices=TYPE_BOOK)
    status = models.CharField(max_length=9, choices=STATUS, default='Olinmagan')
    location = models.CharField(max_length=100)
    language = models.CharField(max_length=6, choices=LANGUAGE)
    pub_date = models.DateField()
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title