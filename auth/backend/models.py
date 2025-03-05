from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class User(models.Model):
<<<<<<< HEAD
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
=======
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.name
>>>>>>> 9c87f8e8e4bfc6280d58201443aaf90cb50187e4
