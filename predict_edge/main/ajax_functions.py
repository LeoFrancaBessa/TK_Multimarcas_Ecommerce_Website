from .models import Clothing, Clothes_Sizes, Clothes_Colors, Cart, CartItem, Favorites
from django.http import JsonResponse


def add_clothing_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart.objects.create(
            user = request.user
        )

    clothing = Clothing.objects.get(pk=int(request.POST.get('clothing')))
    size = Clothes_Sizes.objects.get(pk=int(request.POST.get('size'))) 
    color = Clothes_Colors.objects.get(pk=int(request.POST.get('color')))

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

    message = {
        'message': 'roupa adicionada com sucesso ao carrinho!'
    }
    return JsonResponse(message)


def remove_clothing_cart(request):
    cartItem = CartItem.objects.get(pk=int(request.POST.get('cartItem')))
    cartItem.delete()

    message = {
        'message': 'item removido com sucesso do carrinho!'
    }
    return JsonResponse(message)


def change_quantity_clothing_cart(request):
    cartItem = CartItem.objects.get(pk=int(request.POST.get('cartItem')))
    quantity = int(request.POST.get('quantity'))

    cartItem.quantity = quantity
    cartItem.save()

    message = {
        'message': 'item alterado com sucesso!'
    }
    return JsonResponse(message)


def add_remove_favorite_user(request):
    clothing = Clothing.objects.get(pk=int(request.POST.get('clothing')))
    user=request.user

    favorite = Favorites.objects.filter(user=user, clothing=clothing).first()
    if favorite:
        favorite.delete()
    else:
        Favorites.objects.create(
            user=user,
            clothing=clothing
        )
    
    message = {
        'message': 'Favorito alterado com sucesso!'
    }
    return JsonResponse(message)