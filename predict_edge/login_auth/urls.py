# urls.py
from django.urls import path
from .views import LoginView, SignupView, LogoutView, CheckAuthentication

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/checkAuth/', CheckAuthentication.as_view(), name='checkAuth')
]