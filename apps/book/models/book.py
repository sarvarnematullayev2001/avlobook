from .genre import Genre
from apps.core.base_model import BaseModel
from django.contrib.gis.db import models
from .fields import ISBNField


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

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    types = models.CharField(max_length=5, choices=BOOK_TYPE)
    location = models.PointField() # INPUT: "point": "POINT (30 10)"
    address = models.CharField(max_length=100)
    language = models.CharField(max_length=6, choices=LANGUAGE)
    isbn = ISBNField()
    pub_date = models.DateField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class BookInstance(BaseModel):

    LOAN_STATUS = (
        ('Olingan', 'Olingan'),
        ('Olinmagan', 'Olinmagan')
    )

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    loan_status = models.CharField(max_length=9, choices=LOAN_STATUS, default='Olinmagan')

    class Meta:
        verbose_name = 'book instance'
        verbose_name_plural = 'book instances'

    def __str__(self) -> str:
        return self.book
