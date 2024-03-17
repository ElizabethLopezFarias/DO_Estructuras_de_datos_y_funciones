import requests

def get_users_data(api_url):
    """
    Función que obtiene los datos dela api señalada por api_url 
    """
    # Realizar una solicitud GET para obtener los datos del usuario
    response = requests.get(api_url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el diccionario de usuario
        users_data = response.json()
        print(users_data)
    else:
        #Imprime error en caso de que la solicitud no haya sido exitosa
        print(f"Error Status code: {response.status_code}")
