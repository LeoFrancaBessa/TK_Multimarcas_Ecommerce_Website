# urls.py
from django.urls import path
from .views import IndexView, ClothingDetailsView, CartView
from .ajax_functions import add_clothing_cart, remove_clothing_cart, change_quantity_clothing_cart

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('roupa/<int:pk>/', ClothingDetailsView.as_view(), name='clothing-detail'),
    path('carrinho/', CartView.as_view(), name='cart'),
    #ajax
    path('add-clothing-cart/',add_clothing_cart, name='add_clothing_cart'),
    path('remove_clothing_cart/', remove_clothing_cart, name="remove_clothing_cart"),
    path('change_quantity_clothing_cart/', change_quantity_clothing_cart, name="change_quantity_clothing_cart"),
]