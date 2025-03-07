from django.db import models
from django.core.validators import MinLengthValidator


#one to one relationship in django

'''
Example - 1
In this example I created a Table called countries and made a capital tables that has 
as one to one relationship with country , and capital is also unique.
'''

class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)

class Capital(models.Model):
    country = models.OneToOneField(Country,on_delete=models.CASCADE)
    capital = models.CharField(max_length=100,unique=True)

'''
Example - 2
A product is having a name , and a product can have only one warranty.
So we need a one to one relationship with Product
'''

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True)

class Warranty(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    period=models.DateField()

'''
Example - 3

'''
class User(models.Model):
    name=models.CharField(max_length=100,unique=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=100,blank=True)

'''
Example - 4
An employee can only work on one workstation therefore this example
'''
class Employee(models.Model):
    name=models.CharField(max_length=25,unique=True)

class Workstation(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
    desk_number=models.CharField(max_length=10,unique=True)

'''
Example - 5
'''
class Student(models.Model):
    name=models.CharField(max_length=25,unique=True)

class IDcard(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    card_no=models.CharField(max_length=10,unique=True)

'''
Example - 6
'''

class Car(models.Model):
    name=models.CharField(max_length=25,unique=True)
    model=models.CharField(max_length=25,unique=True)

class Registration(models.Model):
    car= models.OneToOneField(Car,on_delete=models.CASCADE)
    reg_number=models.CharField(max_length=8,unique=True)

'''
Example - 7
'''
class Doctor(models.Model):
    name=models.CharField(max_length=25,unique=True)
    specializtion = models.CharField(max_length=25)

class MedicalLicences(models.Model):
    doc=models.OneToOneField(Doctor,on_delete=models.CASCADE)
    lic_number=models.CharField(max_length=15,unique=True)
