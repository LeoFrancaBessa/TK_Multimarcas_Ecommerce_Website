import uuid
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse as HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
User = get_user_model()


class LoginView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        #Salvar session_id antes do login para realizar a sicronização de dados
        if not request.user.is_authenticated:
            request.session['pre_login_session_id'] = request.session.session_key

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, email=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return Response({}, status=status.HTTP_200_OK)
                else:
                    return Response({"message" : ["Usuário está desativado."]}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"message" : ["Usuário ou senha incorretos"]}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message" : ["Dados incorretos."]}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(LoginRequiredMixin, APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        logout(request)
        return Response({}, status=status.HTTP_200_OK)


class CheckAuthentication(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'authenticated': request.user.is_authenticated}, status=status.HTTP_200_OK)


class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user = authenticate(request, email=request.data['email'], password=request.data['password1'])
            login(request, user)
            return Response({}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)