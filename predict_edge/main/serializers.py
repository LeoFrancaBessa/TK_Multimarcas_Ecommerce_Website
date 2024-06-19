from rest_framework import serializers
from .models import Clothing, ClothingImage, Clothes_Sizes, Clothes_Colors, Cart, CartItem, Favorites


class ClothingListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    favorite = serializers.SerializerMethodField()

    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image', 'favorite')

    def get_image(self, obj):
        image = obj.images.first()
        if image:
            return image.image.path
        return None
    
    def get_favorite(self, obj):
        request = self.context.get('request')
        if not request.user.is_authenticated:
            return None
        return Favorites.objects.filter(user=request.user, clothing=obj).exists()


class ClothingImageSerializer(serializers.ModelSerializer):
     class Meta:
          model = ClothingImage
          fields = ('image',)


class ClothesSizesSerializer(serializers.ModelSerializer):
     class Meta:
          model = Clothes_Sizes
          fields = ('id', 'size', 'count')


class ClothesColorsSerializer(serializers.ModelSerializer):
     class Meta:
          model = Clothes_Colors
          fields = ('id', 'color', 'count')


class ClothingDetailSerializer(serializers.ModelSerializer):
        brand = serializers.CharField(source="brand.name", read_only=True)
        category = serializers.CharField(source="category.name", read_only=True)
        material = serializers.CharField(source="material.name", read_only=True)
        type = serializers.CharField(source="type.name", read_only=True)
        subtype = serializers.CharField(source="subtype.name", read_only=True)
        images = ClothingImageSerializer(many=True, read_only=True)
        sizes = ClothesSizesSerializer(many=True, read_only=True)
        colors = ClothesColorsSerializer(many=True, read_only=True)

        class Meta:
             model = Clothing
             fields = ('id', 'name', 'description', 'price', 'gender', 'brand', 'category', 'material', 'type', 'subtype', 'images', 'sizes', 'colors')


class ClothingCartSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image')  

    def get_image(self, obj):
        image = obj.images.first()
        if image:
            return image.image.path
        return None


class CartItemSerializer(serializers.ModelSerializer):
    clothing = ClothingCartSerializer(read_only=True)
    size = ClothesSizesSerializer(read_only=True)
    color = ClothesColorsSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'clothing', 'size', 'color', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    cartItems = CartItemSerializer(many=True)

    class Meta:
        model = Cart 
        fields = ('id', 'cartItems')