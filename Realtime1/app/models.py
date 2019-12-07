from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    gen=models.CharField(max_length=30)
    gmail=models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    Repassword=models.CharField(max_length=30)

class hotal(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.CharField(max_length=30)
    std=models.DateTimeField()
    end=models.DateField()
    Room=models.IntegerField()

class Room(models.Model):
    Room=models.IntegerField(primary_key=True)
    phone=models.CharField(max_length=30)
class Calculetar(models.Model):
    year = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    Ammount = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
class Login(models.Model):
    gmail=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

