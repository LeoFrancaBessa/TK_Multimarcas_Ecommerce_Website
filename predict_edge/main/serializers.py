from rest_framework import serializers
from .models import Clothing, ClothingImage, Clothes_Sizes, Clothes_Colors, Cart, CartItem, Favorites, UserProfile


class ClothingListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    favorite = serializers.SerializerMethodField()

    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image', 'favorite')

    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.images.first()
        if image:
            return request.build_absolute_uri(image.image.url)
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
        favorite = serializers.SerializerMethodField(read_only=True)

        class Meta:
             model = Clothing
             fields = ('id', 'name', 'description', 'price', 'gender', 'brand', 'category', 'material', 'type', 'subtype', 'images', 'sizes', 'colors', 'favorite')

        def get_favorite(self, obj):
            request = self.context.get('request')
            if not request.user.is_authenticated:
                return None
            return Favorites.objects.filter(user=request.user, clothing=obj).exists()


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


class CartItemListSerializer(serializers.ModelSerializer):
    clothing = ClothingCartSerializer(read_only=True)
    size = ClothesSizesSerializer(read_only=True)
    color = ClothesColorsSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'clothing', 'size', 'color', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    cartItems = CartItemListSerializer(many=True)

    class Meta:
        model = Cart 
        fields = ('id', 'cartItems')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'clothing', 'size', 'color', 'quantity')
    
    def create(self, validated_data):
        user = self.context.get('user')
        cart = Cart.objects.filter(user=user).first()
        if not cart:
            cart = Cart.objects.create(
                user = user
            )

        clothing = validated_data['clothing']
        size = validated_data['size']
        if size.count == 0:
            return "Size isn't available."
        
        color = validated_data['color']
        if color.count == 0:
            return "Color isn't available."
        
        cartItem = CartItem.objects.filter(cart=cart, clothing=clothing, size=size, color=color).first()
        if not cartItem:
            cartItem = CartItem.objects.create(
                cart = cart,
                clothing = clothing,
                size = size,
                color = color,
                quantity = 1
            )
        else:
            cartItem.quantity += 1
            cartItem.save()
        return "Clothing add to cart."
    

class ClothingFavoriteSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image')

    def get_image(self, obj):
        image = obj.images.first()
        if image:
            return image.image.path
        return None


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('id', 'user', 'clothing')


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def create(self, validated_data):
        UserProfile.objects.create(**validated_data)
        return super().create(validated_data)