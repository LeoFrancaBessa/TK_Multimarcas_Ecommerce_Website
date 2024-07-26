from .models import Clothing, Cart, CartItem, Favorites
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import ClothingListSerializer, ClothingDetailSerializer, CartSerializer, CartItemSerializer, FavoritesSerializer, UserProfileCreateSerializer
from rest_framework.permissions import IsAuthenticated


class ClothingListView(ListAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingListSerializer
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filters = {}

        name = self.request.query_params.get('name', None)
        if name:
            filters['name__icontains'] = name
        
        min_price = self.request.query_params.get('min_price', None)
        if min_price:
            filters['price__gte'] = min_price
        
        max_price = self.request.query_params.get('max_price', None)
        if max_price:
            filters['price__lte'] = max_price
        
        if filters:
            queryset = queryset.filter(**filters)

        return queryset

class ClothindDetailView(RetrieveAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingDetailSerializer


class CartView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user).first()
        else:
            cart = Cart.objects.filter(session_id=request.session.session_key).first()
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data)
    

class CartItemView(APIView):
    def post(self, request):
        data = request.data
        data['user'] = request.user
        serializer = CartItemSerializer(data=request.data, context={"request" : request})
        if serializer.is_valid():
            message = serializer.save()
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response({"message" : ["Selecione um tamanho e uma cor."]}, status=status.HTTP_400_BAD_REQUEST)
    
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
            return Response({"message" : ["Update successful."]}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : ["Not found"]}, status=status.HTTP_404_NOT_FOUND)


class FavoritesView(APIView):    
    def post(self, request):
        data = request.data
        data["user"] = request.user.pk
        serializer = FavoritesSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        clothing = Clothing.objects.filter(pk=pk).first()
        if request.user.is_authenticated:
            favorite = Favorites.objects.filter(clothing=clothing, user=request.user).first()
        else:
            favorite = Favorites.objects.filter(clothing=clothing, session_id=request.session.session_key).first()
        if favorite:
            favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        data["user"] = request.user
        serializer = UserProfileCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)