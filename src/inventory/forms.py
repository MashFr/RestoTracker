from dataclasses import fields
from django import forms
from .models import Ingredients, MenuItem

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ("name", "quantity", "unit", "unit_price")

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("title", "price")