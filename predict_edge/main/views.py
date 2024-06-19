from .models import Clothing, Cart
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClothingListSerializer, ClothingDetailSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class ClothingListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Clothing.objects.all()
    serializer_class = ClothingListSerializer
    
    def get_queryset(self):
        return super().get_queryset()
    

class ClothindDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Clothing.objects.all()
    serializer_class = ClothingDetailSerializer


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)