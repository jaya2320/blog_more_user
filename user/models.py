from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)
class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)   
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    




