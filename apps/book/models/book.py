# Django
from django.contrib.gis.db import models as gis_models
from django.db import models

# Locals
from file.models import File
from book.models.genre import Genre
from user.models import User
from core.base_model import BaseModel

# Fields
from book.models.fields import ISBNField
from book.models.choices import BOOK_TYPE, REGION, CITY, LANGUAGE, BOOK_QUALITY, LOAN_STATUS



class Book(BaseModel):

    BOOK_TYPE = (
        ('Erkin', 'Erkin'),
        ('Ijara', 'Ijara')
    )

    LANGUAGE = (
        ("O'zbek", "O'zbek"),
        ("Ingliz", "Ingliz"),
        ("Rus", "Rus")
    )


class Book(BaseModel):

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', null=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    image = models.OneToOneField(File, on_delete=models.CASCADE, related_name='image')
    language = models.CharField(max_length=6, choices=LANGUAGE)
    pub_date = models.DateField()
    types = models.CharField(max_length=5, choices=BOOK_TYPE)
    isbn = ISBNField()
    region = models.CharField(max_length=50, choices=REGION)
    city = models.CharField(max_length=50, choices=CITY)
    address = models.CharField(max_length=100)
    location = gis_models.PointField(srid=4326) # INPUT: "location" : {"type": "Point", "coordinates": [41, 30]}
    description = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField()
    quality = models.CharField(max_length=8, choices=BOOK_QUALITY)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class BookInstance(BaseModel):

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    loan_status = models.CharField(max_length=9, choices=LOAN_STATUS, default='Olinmagan')

    class Meta:
        verbose_name = 'book instance'
        verbose_name_plural = 'book instances'

    def __str__(self) -> str:
        return self.book
    
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    due_by = models.DateField()
    loan_status = models.CharField(max_length=15, choices=LOAN_STATUS)
    current_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='current_user', null=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='borrower', null=True)
    
    class Meta:
        verbose_name = 'Book Instance'
        verbose_name_plural = 'Book Instances'
    
    def __str__(self):
        return self.book.title
