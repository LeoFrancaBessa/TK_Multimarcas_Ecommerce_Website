import uuid
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse as HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        #get_user
        email = request.data['username']
        user = User.objects.filter(email=email).first()
        if user:
            request.data['username'] = user.username

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise BaseException(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)