from .models import Clothing, Cart, CartItem, Favorites
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClothingListSerializer, ClothingDetailSerializer, CartSerializer, CartItemSerializer, FavoritesSerializer
from rest_framework.permissions import IsAuthenticated


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
    

class CartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartItemSerializer(data=request.data, context={"user" : request.user})
        if serializer.is_valid():
            message = serializer.save()
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cartItem = CartItem.objects.filter(pk=pk).first()
        if cartItem:
            cartItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        cartItem = CartItem.objects.filter(pk=pk).first()
        if cartItem:
            serializer = CartItemSerializer(cartItem, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({"message" : "Update successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Not found"}, status=status.HTTP_404_NOT_FOUND)


class FavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Favorites.objects.filter(user=request.user)
        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        data["user"] = request.user.pk
        serializer = FavoritesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Favorite clothing added to user."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        favorite = Favorites.objects.filter(pk=pk)
        if favorite:
            favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
