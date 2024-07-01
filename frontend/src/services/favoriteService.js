const API_URL_FAVORITE = 'http://127.0.0.1:8000/api/favorites/'

export async function createFavorite(clothing){
    const csrftoken = getCookie('csrftoken');
    const response = await fetch(API_URL_FAVORITE, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({clothing}),
        credentials: 'include',
    });

    const data = response.json()
    return data;
}

export async function deleteFavorite(clothing){
    const csrftoken = getCookie('csrftoken');
    const response = await fetch(API_URL_FAVORITE + clothing, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'include',
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}