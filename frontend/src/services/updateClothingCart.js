import getCookie from './getCookieService'

const API_URL_UPDATE_CLOTHING_CART = 'http://127.0.0.1:8000/api/cartItens/';
const csrftoken = getCookie('csrftoken');

export async function updateClothingCartItem(cartItemId, quantity){
    const response = await fetch(API_URL_UPDATE_CLOTHING_CART + cartItemId, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({quantity}),
        credentials: 'include',
    });

    const data = await response.json()
    return data;
}

export async function deleteClothingCartItem(cartItemId){
    const response = await fetch(API_URL_UPDATE_CLOTHING_CART + cartItemId, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
    });

    return;
}

