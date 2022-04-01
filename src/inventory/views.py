from ast import Delete
from audioop import reverse
import imp
from msilib.schema import ListView
from re import template
from typing import List
from django.shortcuts import render
from .models import Ingredients, MenuItem, Purchase
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, "inventory/home.html")

#Ingredients View

class IngredientList(ListView):
    model = Ingredients
    template_name = "inventory/ingredient_list.html"
    context_object_name = 'ingredients'

class IngredientDelete(DeleteView):
    model = Ingredients
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('ingredientlist')
    context_object_name = 'ingredient_to_delete'

#Menu Item View

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"
    context_object_name = 'menuitems'

class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = reverse_lazy('menuitemlist')
    context_object_name = 'menuitem_to_delete'

#Purchase View

class PurchasesList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
    context_object_name = 'purchases'
