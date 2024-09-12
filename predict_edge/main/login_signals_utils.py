from .models import Cart, Favorites, CartItem

def merge_favorites(user, session_id):
    anonymous_favorites = Favorites.objects.filter(session_id=session_id)

    for item in anonymous_favorites:
        #Se usuario já possuir o favorito, apagar item
        if Favorites.objects.filter(user=user, clothing=item.clothing).exists():
            item.delete()
            continue
        item.user = user
        item.session_id = None
        item.save()


def merge_cart(user, session_id):
    anonymous_cart = Cart.objects.filter(session_id=session_id).first()
    
    if anonymous_cart:
        user_cart = Cart.objects.filter(user=user).first()
        if user_cart:
            # Mover os itens do carrinho anônimo para o carrinho do usuário
            for item in anonymous_cart.cartItems.all():
                #Se o carrinho do usuario já possuir a mesma roupa com o mesmo tamanho e cor
                user_item_cart = CartItem.objects.filter(cart=user_cart, 
                                                         clothing=item.clothing, 
                                                         color=item.color, 
                                                         size=item.size).first()
                if user_item_cart:
                    #Adicionar +1 a quantidade do item original
                    #Apagar item do carrinho anonimo
                    user_item_cart.quantity += 1
                    user_item_cart.save()
                    item.delete()
                    continue
                
                item.cart = user_cart
                item.save()

            anonymous_cart.delete()  # Apaga o carrinho anônimo
        else:
            # Associa o carrinho anônimo ao usuário
            anonymous_cart.user = user
            anonymous_cart.session_id = None
            anonymous_cart.save()