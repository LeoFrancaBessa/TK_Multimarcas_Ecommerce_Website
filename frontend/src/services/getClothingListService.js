const API_URL_GET = 'http://127.0.0.1:8000/api/clothing_list/'

export async function getClothingList(filters = {}, page_size = null) {
    const queryParams = new URLSearchParams(filters).toString();
    const apiUrl = `${API_URL_GET}?${queryParams}`
    const response = await fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: "include",
    });

    if (!response.ok) return null;

    //Gambiarra
    let data = await response.json();
    if (page_size){
        data = data.slice(0, page_size);
    }
    return data;
}