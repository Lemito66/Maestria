import requests

url = "https://api.gameofthronesquotes.xyz/v1/random/100"


def get_data(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print("Error al obtener los datos de la API: " + str(e))
        return None

for i, name in enumerate(get_data(url)):
    print(i, name)

