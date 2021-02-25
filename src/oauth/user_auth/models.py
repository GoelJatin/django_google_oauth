from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    salt = models.BinaryField(unique=True)


class UserAuth(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    password = models.BinaryField(unique=True)
