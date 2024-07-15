import getCookie from './getCookieService'

const API_URL_ADD_CLOTHING_CART = 'http://127.0.0.1:8000/api/cartItens/';

export async function addClothingCart(clothing, size, color){
    const csrftoken = getCookie('csrftoken');
    const quantity = 1
    const response = await fetch(API_URL_ADD_CLOTHING_CART, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({clothing, size, color, quantity}),
        credentials: 'include',
    });

    const data = await response.json()
    return [data, response.ok];
}