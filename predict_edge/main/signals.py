from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart
from .login_signals_utils import merge_cart, merge_favorites

@receiver(user_logged_in)
def merge_itens(sender, request, user, **kwargs):
    # Recupera o session_id armazenado antes do login
    pre_login_session_id = request.session.pop('pre_login_session_id', None)
    
    #Sicronizar favoritos e carrinho
    merge_favorites(user, pre_login_session_id)
    merge_cart(user, pre_login_session_id)