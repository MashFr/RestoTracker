from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('ingredient/', views.IngredientList.as_view(), name="ingredientlist"),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name="ingredientdelete"),
    path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),

    path('menuitem/', views.MenuItemList.as_view(), name="menuitemlist"),
    path('menuitem/delete/<pk>', views.MenuItemDelete.as_view(), name="menuitemdelete"),
    path('menuitem/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),

    path('purchase/', views.PurchasesList.as_view(), name="purchaselist"),
    
    path('profit/', views.Profit, name="profit"),
]