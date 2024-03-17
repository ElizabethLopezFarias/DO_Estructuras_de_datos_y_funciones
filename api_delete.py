import requests

def delete_user (api_url, username): 
    """
    Función que crea un borra un usuario en la api señalada por api_url a partir de los datos entregados en username 
    """
    # Realizar una solicitud GET para obtener los datos del usuario
    response = requests.get(api_url)

# Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        # Obtener la lista de usuarios del campo "data" en la respuesta
        users = data.get("data", [])
    
        # Buscar el usuario con el nombre "Tracey" y obtener su ID
        user_id = None
        for user in users:
            if user.get("first_name") == username:
                user_id = user.get("id")
                break

        if user_id:
            # Realizar una solicitud DELETE para eliminar el usuario por su ID
            response_delete = requests.delete(f"{api_url}/{user_id}")
            # Imprimir el código de respuesta en pantalla
            print("Código de respuesta:", response_delete.status_code)
            if response_delete.status_code == 204:  # Cambiado a 204 para este caso específico por la validación de la respuesta de la api
                print(f"Usuario {username} eliminado exitosamente.")
            else:
                #Imprime error en caso de que la solicitud no haya sido exitosa
                print(f"Error al eliminar el usuario {username}. Código de estado: {response_delete.status_code}")
        else:
            #Imprime error en caso de que la solicitud no haya sido exitosa
            print(f"El usuario {username} no fue encontrado en la API.")
    else:
        #Imprime error en caso de que la solicitud no haya sido exitosa
        print(f"Error: No se pudo obtener los datos de la API. Código de estado: {response.status_code}")
