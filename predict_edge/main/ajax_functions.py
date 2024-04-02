from .models import Clothing, Clothes_Sizes, Clothes_Colors, Cart, CartItem
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