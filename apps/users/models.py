from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))

    first_name = None
    last_name = None
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
