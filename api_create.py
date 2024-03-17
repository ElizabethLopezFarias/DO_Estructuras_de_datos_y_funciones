import requests

def create_user(api_url, user_data):
    """
    Función que crea un usuario en la api señalada por api_url a partir de los datos entregados en user_data 
    """
    response = requests.post(api_url, json=user_data)
    # Verificar si la solicitud fue exitosa (código de estado 201)
    if response.status_code == 201:
        created_user = response.json()
        print("Usuario creado:")
        print(created_user)
    else:
        #Imprime error en caso de que la solicitud no haya sido exitosa
        print(f"Error al crear el usuario. Código de estado: {response.status_code}")
