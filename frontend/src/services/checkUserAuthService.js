const API_CHECK_AUTH_URL = 'http://127.0.0.1:8000/auth/api/checkAuth/'

export async function checkUserAuth(){
    const response = await fetch(API_CHECK_AUTH_URL, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });

    const data = await response.json()
    return data;
}