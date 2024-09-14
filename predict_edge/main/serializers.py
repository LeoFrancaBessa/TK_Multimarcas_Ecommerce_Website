from rest_framework import serializers
from .models import Clothing, ClothingImage, Clothes_Sizes, Clothes_Colors, Cart, CartItem, Favorites, UserProfile, AttributeValue


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
        if request.user.is_authenticated:
            return Favorites.objects.filter(user=request.user, clothing=obj).exists()
        else:
            return Favorites.objects.filter(session_id=request.session.session_key, clothing=obj).exists()


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute_name = serializers.CharField(source="attribute.name")
    class Meta:
        model = AttributeValue
        fields = ('attribute_name', 'value')


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
        attributes = AttributeValueSerializer(many=True, read_only=True)
        images = ClothingImageSerializer(many=True, read_only=True)
        sizes = ClothesSizesSerializer(many=True, read_only=True)
        colors = ClothesColorsSerializer(many=True, read_only=True)
        favorite = serializers.SerializerMethodField(read_only=True)

        class Meta:
             model = Clothing
             fields = ('id', 'name', 'description', 'price', 'gender', 'brand', 'category', 'material', 'attributes', 'images', 'sizes', 'colors', 'favorite')

        def get_favorite(self, obj):
            request = self.context.get('request')
            if request.user.is_authenticated:
                return Favorites.objects.filter(user=request.user, clothing=obj).exists()
            else:
                return Favorites.objects.filter(session_id=request.session.session_key, clothing=obj).exists()


class ClothingCartSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image')  

    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.images.first()
        if image:
            return request.build_absolute_uri(image.image.url)
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
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart 
        fields = ('id', 'cartItems', 'price')

    def get_price(self, obj):
        total_price = 0
        for item in obj.cartItems.all():
            clothing_price = item.quantity * item.clothing.price
            total_price += clothing_price
        return total_price


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'clothing', 'size', 'color', 'quantity')
    
    def create(self, validated_data):
        request = self.context.get('request')
        session_id = request.session.session_key
        user = request.user
        
        if user.is_authenticated:
            cart = Cart.objects.filter(user=user).first()
            if not cart:
                cart = Cart.objects.create(
                    user = user
                )
        else:
            cart = Cart.objects.filter(session_id=session_id).first()
            if not cart:
                cart = Cart.objects.create(
                    session_id = session_id
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
    

class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('id', 'clothing')
    
    def create(self, validated_data):
        request = self.context.get('request')
        session_id = request.session.session_key
        user = request.user

        if user.is_authenticated:
            favorite = Favorites.objects.filter(user=user, clothing=validated_data['clothing']).first()
            if not favorite:
                Favorites.objects.create(
                    user = user,
                    clothing = validated_data['clothing']
                )
        else:
            favorite = Favorites.objects.filter(session_id=session_id, clothing=validated_data['clothing']).first()
            if not favorite:
                Favorites.objects.create(
                    session_id = session_id,
                    clothing = validated_data['clothing']
                )
        
        return "Favorite created"


class ClothingFavoriteSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Clothing
        fields = ('id', 'name', 'price', 'image')

    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.images.first()
        if image:
            return request.build_absolute_uri(image.image.url)
        return None


class FavoritesListSerializer(serializers.ModelSerializer):
    clothing = ClothingFavoriteSerializer()

    class Meta:
        model = Favorites
        fields = ('clothing',)


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def create(self, validated_data):
        UserProfile.objects.create(**validated_data)
        return super().create(validated_data)