from django.db import models

# Create your models here.

class Task(models.Model):
    # schema of the database will be defined here
    title=models.CharField(name="title",max_length=200)
    description=models.TextField(name="descrition",null=True,max_length=700)
    completed=models.BooleanField(name="completed",default=False)
    createat=models.DateTimeField(name="createdat",auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.description}"

