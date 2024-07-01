const API_URL_GET = 'http://127.0.0.1:8000/api/clothing_list/'

export async function getClothingList() {
    const response = await fetch(API_URL_GET, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    const data = await response.json();
    return data;
}