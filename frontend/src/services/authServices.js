import getCookie from './getCookieService'

const API_URL_LOGIN = 'http://127.0.0.1:8000/auth/api/login/'
const API_LOGOUT = 'http://127.0.0.1:8000/auth/api/logout/'
const csrftoken = getCookie('csrftoken');


export async function login(username, password) {
    const response = await fetch(API_URL_LOGIN, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({username, password}),
        credentials: "include",
    });

    const data = await response.json();
    return [data, response.ok];
}

export async function logout() {
    await fetch(API_LOGOUT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: "include",
    });
}