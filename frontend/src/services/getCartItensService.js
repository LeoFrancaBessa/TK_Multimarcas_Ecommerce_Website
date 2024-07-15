import getCookie from './getCookieService'

const API_URL_GET_CART_ITENS = 'http://127.0.0.1:8000/api/cart/';

export async function getCartItens(){
    const csrftoken = getCookie('csrftoken');
    const response = await fetch(API_URL_GET_CART_ITENS, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
    });

    const data = await response.json()
    return data;
}