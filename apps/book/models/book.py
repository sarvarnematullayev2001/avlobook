# Models
from apps.core.base_model import BaseModel
from django.contrib.gis.db import models as gis_models
from file.models import File
from django.db import models
from .genre import Genre
from user.models import User


# Model fields
from .fields import ISBNField
from .choices import BOOK_TYPE, REGION, CITY, LANGUAGE, BOOK_QUALITY


class Book(BaseModel):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
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
