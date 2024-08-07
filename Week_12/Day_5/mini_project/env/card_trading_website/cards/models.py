from django.db import models
import random

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    amount_of_money = models.IntegerField(default=1000)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name_character = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    image_url = models.URLField()
    date_of_birth = models.DateTimeField(null=True)
    patronus = models.CharField(max_length=100)
    price = models.IntegerField(random.randint(200, 2000))
    xp_points = models.IntegerField(random.randint(1, 10))
    current_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='current_owner')
    previous_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='previous_owner')

    def __str__(self):
        return self.name_character


class Transaction(models.Model):
    name_character = models.CharField(max_length=100)
    current_owner = models.ForeignKey(
        User, related_name='current_cards', on_delete=models.SET_NULL, null=True,)
    previous_owner = models.ForeignKey(
        User, related_name='previous_cards', on_delete=models.SET_NULL, null=True,)
    price = models.IntegerField(random.randint(200, 2000))
