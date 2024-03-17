from django.contrib.auth import authenticate, login, get_user_model
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import logout
User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login bem-sucedido'})
        else:
            return JsonResponse({'message': 'Credenciais inválidas'}, status=400)
    else:
        return JsonResponse({'message': 'Método não permitido'}, status=405)


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('signup_email')
        password1 = request.POST.get('signup_password1')
        password2 = request.POST.get('signup_password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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
                        user = authenticate(request, email=email, password=password1)
                        login(request, user)
                        return JsonResponse({'message': 'Usuário criado!'})
                    else:
                        return JsonResponse({'message': 'Dados inválidos'}, status=400)
    else:                
        return JsonResponse({'message': 'Método não permitido'}, status=405)


def logout_view(request):
    logout(request)
    return redirect('index')