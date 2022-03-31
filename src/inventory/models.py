from tkinter import CASCADE
from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=35)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

class MenuItem(models.Model):
    title = models.CharField(max_length=35)
    price = models.FloatField()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=True)


    