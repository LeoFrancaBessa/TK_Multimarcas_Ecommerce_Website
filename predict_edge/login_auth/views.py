from django.contrib.auth import authenticate, login, get_user_model
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import logout

User = get_user_model()

class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if email and password:
                user = authenticate(email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('index')
        
        return render(request, 'login.html', {'form' : form})


class SignupView(TemplateView):
    template_name = 'signup.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = SignupForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = email[:30]

            if password1 and password2:
                if password1 == password2:
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password = password1,
                            first_name=first_name,
                            last_name=last_name,
                        )

                        if user:
                            return redirect('login')
        else:
            return render(request, 'signup.html', {'form' : form})


def logout_view(request):
    logout(request)
    return redirect('login')