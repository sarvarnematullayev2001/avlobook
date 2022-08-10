# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BLOCKED = 'blocked'
    ACTIVE = 'active'
    MALE = 'male'
    FEMALE = 'female'
    USER = 'user'
    OPEN_SHELF = 'open_shelf'
    LIBRARY_STANDARD = 'library_standard'
    LIBRARY_OFFICE = 'library_office'
    LIBRARY_CAFE = 'library_cafe'

    STATUS = (
        (BLOCKED, BLOCKED),
        (ACTIVE, ACTIVE),
    )
    GENDER = (
        (MALE, MALE),
        (FEMALE, FEMALE),
    )
    TYPE = (
        (USER, USER),
        (OPEN_SHELF, OPEN_SHELF),
        (LIBRARY_STANDARD, LIBRARY_STANDARD),
        (LIBRARY_OFFICE, LIBRARY_OFFICE),
        (LIBRARY_CAFE, LIBRARY_CAFE),
    )
    user_status = models.CharField(max_length=20, choices=STATUS)
    user_type = models.CharField(max_length=25, choices=TYPE, default=TYPE[0][0])
    phone_number = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    birth_date = models.DateField(null=True)
    find_option = models.CharField(max_length=100)

