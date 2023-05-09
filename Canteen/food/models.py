from django.db import models
from .models import *

from django.contrib.auth.models import User


class Foodmenu(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    fimage = models.ImageField(upload_to='pics/')

class Signup(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')


class Lunch(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    limage = models.ImageField(upload_to='pics/')

class FastFood(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Fimage = models.ImageField(upload_to='pics/')

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimage = models.ImageField(upload_to='pics/')
class ComboOffer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cimage = models.ImageField(upload_to='pics/')

class FreshJuice(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fimage = models.ImageField(upload_to='pics/')

class ChatItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cimage = models.ImageField(upload_to='pics/')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breakfast = models.ForeignKey(Breakfast,on_delete=models.CASCADE)
    breakfast_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)