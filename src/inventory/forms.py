from dataclasses import field, fields
from django import forms
from .models import Ingredients, MenuItem, RecipeRequirement, Purchase

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ("name", "quantity", "unit", "unit_price")

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("title", "price")

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ("menu_item", "ingredient", "quantity")
        
class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['timestamp']
        # fields = ("menu_item", '')

