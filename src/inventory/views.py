import imp
from msilib.schema import ListView
from django.shortcuts import render
from .models import Ingredients, MenuItem, Purchase
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredients
    template_name = "inventory/ingredient_list.html"