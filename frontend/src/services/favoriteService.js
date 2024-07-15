import getCookie from './getCookieService'

const API_URL_FAVORITE = 'http://127.0.0.1:8000/api/favorites/';
const csrftoken = getCookie('csrftoken');

export async function createFavorite(clothing){
    const response = await fetch(API_URL_FAVORITE, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({clothing}),
        credentials: 'include',
    });

    const data = response.json()
    return data;
}

export async function deleteFavorite(clothing){
    const response = await fetch(API_URL_FAVORITE + clothing, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
    });
}