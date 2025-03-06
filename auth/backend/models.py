from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
