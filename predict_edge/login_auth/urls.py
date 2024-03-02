# urls.py
from django.urls import path
from .views import SignupView, LoginView, logout_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]