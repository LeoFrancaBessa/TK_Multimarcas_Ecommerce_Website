# urls.py
from django.urls import path
from .views import CustomTokenObtainPairView, SignupView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]