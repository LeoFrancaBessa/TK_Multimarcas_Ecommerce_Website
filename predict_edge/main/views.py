from typing import Any
from django.views.generic import TemplateView
from .models import Clothing, Clothes_Sizes, Clothes_Colors, ClothingImage, Cart, CartItem
from django.http import JsonResponse

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        clothes = Clothing.objects.all()
        context['clothes'] = clothes
        
        return context


class ClothingDetailsView(TemplateView):
    template_name = 'main/clothing-detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        
        clothing = Clothing.objects.get(id=pk)
        context['clothing'] = clothing
        
        images = ClothingImage.objects.filter(clothing=clothing)
        context['images'] = images
        
        colors = Clothes_Colors.objects.filter(clothing=clothing)
        context['colors'] = colors
        
        sizes = Clothes_Sizes.objects.filter(clothing=clothing)
        context['sizes'] = sizes
        
        clothes = Clothing.objects.all()
        context['clothes'] = clothes
        
        return context
    
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            cart = Cart.objects.filter(user=request.user).last()
            if not cart:
                cart = Cart.objects.create(
                    user = request.user
                )

            clothing = Clothing.objects.get(pk=self.kwargs.get('pk'))
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
        
        # Se não for uma request AJAX, continue com o processamento padrão
        return super().post(request, *args, **kwargs)
    

class CartView(TemplateView):
    template_name = 'main/cart-page.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        cart = Cart.objects.filter(user=self.request.user.id).first()
        context['cart'] = cart
        
        cartItems = CartItem.objects.filter(cart=cart)
        context['cartItems'] = cartItems
        
        return context