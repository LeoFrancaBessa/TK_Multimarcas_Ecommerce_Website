# urls.py
from django.urls import path
from .views import IndexView, ClothingDetailsView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('roupa/', ClothingDetailsView.as_view(), name='clothing-detail'),
]