# urls.py
from django.urls import path
from .views import ClothingListView, ClothindDetailView, CartView, CartItemView, FavoritesView

urlpatterns = [
    path('api/clothing_list/', ClothingListView.as_view(), name='clothing_list'),
    path('api/clothing_detail/<int:pk>/', ClothindDetailView.as_view(), name='clothing_detail'),
    path('api/cart/', CartView.as_view(), name='cart'),
    path('api/cartItens/',CartItemView.as_view(), name='cartItens_post'),
    path('api/cartItens/<int:pk>',CartItemView.as_view(), name='cartItens_update'),
    path('api/favorites/', FavoritesView.as_view(), name="favorites_user"),
    path('api/favorites/<int:pk>', FavoritesView.as_view(), name="favorites_user_delete"),
]