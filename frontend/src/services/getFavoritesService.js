import getCookie from './getCookieService'

const API_URL_LIST_FAVORITES = 'http://127.0.0.1:8000/api/favorites_list/';
const csrftoken = getCookie('csrftoken');

export async function getFavorites(){
    const response = await fetch(API_URL_LIST_FAVORITES, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
    });

    const data = response.json()
    return data;
}