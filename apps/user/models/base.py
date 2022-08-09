# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BLOCKED = 'blocked'
    ACTIVE = 'active'
    MALE = 'male'
    FEMALE = 'female'
    STATUS = (
        (BLOCKED, BLOCKED),
        (ACTIVE, ACTIVE),
    )
    GENDER = (
        (MALE, MALE),
        (FEMALE, FEMALE),
    )
    user_status = models.CharField(max_length=20, choices=STATUS)
    phone_number = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    birth_date = models.DateField(null=True)
    # find_option = models.CharField()


