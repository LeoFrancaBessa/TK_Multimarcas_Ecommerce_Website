const API_URL = 'http://127.0.0.1:8000/auth/api/token/'

export async function login(username, password) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password})
    });
    
    const data = await response.json();
    return data;
}