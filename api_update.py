import requests

def update_user (api_url,username):
    """
    Función que actualiza un usuario en la api señalada por api_url a partir de los datos entregados en user_data 
    """
    # Realizar una solicitud GET para obtener los datos del usuario
    response = requests.get(f"{api_url}/{username}")

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el diccionario de usuario
        user_data = response.json()
    
        # Actualizar el campo 'residence' con el valor 'zion'
        user_data['residence'] = 'zion'
    
    # Imprimir el diccionario actualizado
        print("Usuario actualizado:")
        print(user_data)
    
    # Guardar el diccionario actualizado en una variable
        updated_user = user_data

    else:
        #Imprime error en caso de que la solicitud no haya sido exitosa
        print(f"Error: No se pudo obtener los datos del usuario {username}. Código de estado: {response.status_code}")
