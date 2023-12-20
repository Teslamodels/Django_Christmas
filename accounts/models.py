from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    middlename = models.CharField(max_length=200)
    birth_year = models.CharField(max_length=200)
    birth_month = models.PositiveIntegerField(null=True, blank=True)
    birth_day = models.PositiveIntegerField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    