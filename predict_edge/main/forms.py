from django import forms
from .models import UserProfile

class UserProfileForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = '__all__'