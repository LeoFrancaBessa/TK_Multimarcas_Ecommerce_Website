# urls.py
from django.urls import path
from .views import IndexView, ClothingDetailsView, CartView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('roupa/<int:pk>/', ClothingDetailsView.as_view(), name='clothing-detail'),
    path('carrinho/', CartView.as_view(), name='cart'),
]