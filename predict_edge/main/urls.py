# urls.py
from django.urls import path
from .views import ClothingListView, ClothindDetailView, CartView
from .ajax_functions import add_clothing_cart, remove_clothing_cart, change_quantity_clothing_cart, add_remove_favorite_user, get_cart_itens

urlpatterns = [
    path('api/clothing_list/', ClothingListView.as_view(), name='clothing_list'),
    path('api/clothing_detail/<int:pk>/', ClothindDetailView.as_view(), name='clothing_detail'),
    path('api/cartItems/', CartView.as_view(), name='cartItems'),
    #ajax
    path('add-clothing-cart/',add_clothing_cart, name='add_clothing_cart'),
    path('remove_clothing_cart/', remove_clothing_cart, name="remove_clothing_cart"),
    path('change_quantity_clothing_cart/', change_quantity_clothing_cart, name="change_quantity_clothing_cart"),
    path('add_remove_favorite_user/', add_remove_favorite_user, name="add_remove_favorite_user"),
]