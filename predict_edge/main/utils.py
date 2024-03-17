import requests

def get_clothing_data():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.status_code == 200:
        clothing_data = response.json()
        return clothing_data
    else:
        # Trate o erro de solicitação aqui
        print('Erro ao obter dados de roupas:', response.status_code)
        return None