from django.db import models

# Create your models here.

class UserData(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    role = models.CharField(max_length=20)


class UserDetails(models.Model):
    firstName = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    fklogin = models.ForeignKey(UserData, on_delete=models.CASCADE)
