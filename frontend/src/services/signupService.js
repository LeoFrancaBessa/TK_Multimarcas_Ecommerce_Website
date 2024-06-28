const API_URL_SIGNUP = 'http://127.0.0.1:8000/auth/api/signup/'

export async function signup(email, name, password1, password2) {
    const response = await fetch(API_URL_SIGNUP, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({email, name, password1, password2}),
    });

    const data = await response.json();
    return [data, response.ok];
}