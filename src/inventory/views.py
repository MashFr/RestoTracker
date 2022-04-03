from ast import Delete
from audioop import reverse
from dataclasses import field
import imp
from msilib.schema import ListView
from pyexpat import model
from re import template
from typing import List
from django.shortcuts import render
from .models import Ingredients, MenuItem, Purchase, RecipeRequirement
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import IngredientCreateForm, MenuItemCreateForm

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

class IngredientCreate(CreateView):
    model = Ingredients
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm
    success_url = reverse_lazy('ingredientlist')

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

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreateForm
    success_url = reverse_lazy('menuitemlist')

class MenuItemCreateRecipe(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = reverse_lazy('menuitemlist')
    context_object_name = 'menuitem_to_delete'

#Purchase View

class PurchasesList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
    context_object_name = 'purchases'

#Profit and revenu report

def Profit(request):

    every_purchase = Purchase.objects.all()
    total_revenue = 0
    for purchase in every_purchase:
        total_revenue  += purchase.menu_item.price
    

    total_cost = 0
    for purchase in every_purchase:
        recipe_requirement = RecipeRequirement.objects.filter(menu_item = purchase.menu_item)
        
        for requirement in recipe_requirement:
            requirement_price = requirement.quantity * requirement.ingredient.unit_price
            print(requirement_price)
            total_cost += requirement_price

    profit = total_revenue - total_cost

    context = {"revenue": total_revenue, "profit": profit}
    return render(request, "inventory/profit.html", context)
