from tkinter import CASCADE
from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=35)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=35)
    price = models.FloatField()

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return self.menu_item.title + " - " +self.ingredient.name

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.menu_item.title + " - " + self.timestamp.strftime("%d/%m/%Y - %H:%M:%S")


    