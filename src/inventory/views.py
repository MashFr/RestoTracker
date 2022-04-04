from ast import Delete
from audioop import reverse
from dataclasses import field
import imp
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from re import template
from typing import List
from django.shortcuts import render, redirect
from .models import Ingredients, MenuItem, Purchase, RecipeRequirement
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import IngredientCreateForm, MenuItemCreateForm, RecipeRequirementCreateForm, PurchaseCreateForm, RecipeRequirementUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    return render(request, "inventory/home.html")

def carte(request):
    every_menue_item = MenuItem.objects.all()
    context = {"menuitems": every_menue_item}
    return render(request, "inventory/carte.html",context)

#Ingredients View

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = "inventory/ingredient_list.html"
    context_object_name = 'ingredients'

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredients
    template_name = "inventory/ingredient_delete_form.html"
    success_url = reverse_lazy('ingredientlist')
    context_object_name = 'ingredient_to_delete'

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredients
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm
    success_url = reverse_lazy('ingredientlist')

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredients
    fields = '__all__'
    template_name = "inventory/ingredient_update_form.html"
    success_url = reverse_lazy('ingredientlist')

#Menu Item View
@login_required
def MenuItemView(request):

    every_menue_item = MenuItem.objects.all()
    every_menue_requirement = RecipeRequirement.objects.all()

    context = {"menuitems": every_menue_item, "requirements": every_menue_requirement}
    return render(request, "inventory/menuitem.html", context)

# class MenuItemList(ListView):
#     model = MenuItem
#     template_name = "inventory/menuitem_list.html"
#     context_object_name = 'menuitems'

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = reverse_lazy('menuitemlist')
    context_object_name = 'menuitem_to_delete'

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreateForm
    success_url = reverse_lazy('menuitemlist')

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    fields = '__all__'
    template_name = "inventory/menuitem_update_form.html"
    success_url = reverse_lazy('menuitemlist')

#Recipe View

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    form_class = RecipeRequirementCreateForm
    success_url = reverse_lazy('menuitemlist')

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    form_class = RecipeRequirementUpdateForm
    success_url = reverse_lazy('menuitemlist')


#Purchase View

class PurchasesList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
    context_object_name = 'purchases'

class PurchasesCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseCreateForm
    success_url = reverse_lazy('purchaselist')

#Profit and revenu report

@login_required
def Profit(request):

    every_purchase = Purchase.objects.all()
    total_revenue = 0
    for purchase in every_purchase:
        if purchase.menu_item == None :
            continue
        total_revenue  += purchase.menu_item.price
    

    total_cost = 0
    for purchase in every_purchase:
        if purchase.menu_item == None :
            continue
        recipe_requirement = RecipeRequirement.objects.filter(menu_item = purchase.menu_item)
        
        for requirement in recipe_requirement:
            requirement_price = requirement.quantity * requirement.ingredient.unit_price
            print(requirement_price)
            total_cost += requirement_price

    profit = total_revenue - total_cost

    context = {"revenue": total_revenue, "profit": profit}
    return render(request, "inventory/profit.html", context)

#Login

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url =  reverse_lazy("login")
    template_name = "registration/signup.html"

def logout_request(request):
  logout(request)
  return redirect("home")