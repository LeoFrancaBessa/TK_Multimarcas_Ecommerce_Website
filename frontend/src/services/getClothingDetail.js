export async function getClothingDetail(clothingID) {
    const API_URL_GET = `http://127.0.0.1:8000/api/clothing_detail/${clothingID}/`
    const response = await fetch(API_URL_GET, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: "include",
    });

    const data = await response.json();
    if (!response.ok) return null;
    return data;
}