const API_URL = 'http://127.0.0.1:8000/auth/api/login/'
const API_LOGOUT = 'http://127.0.0.1:8000/auth/api/logout/'

export async function login(username, password) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password}),
        credentials : "include"
    });

    const data = await response.json();
    return data;
}

export async function logout() {
    const response = await fetch(API_LOGOUT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    const data = await response.json();
    return data;
}