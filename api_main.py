"""
Progama que llama a las funciones contenidas en los archivos apiget, api_create, api_update y api_delete
los que contienen las funciones correspondientes al Desafío solicitado de administración de APIs
"""

import requests
from api_get import get_users_data
from api_create import create_user
from api_update import update_user
from api_delete import delete_user

api_url = "https://reqres.in/api/users"

#Obtener la información de la Api
get_users_data(api_url)

#crear un usuario
user_data = {
    "name": "Ignacio",
    "job": "Profesor"
}
create_user(api_url, user_data)

#Actualizar usuario indicado
username = "morpheus"
update_user (api_url, username)

#Elimina a usuario indicado
username = "Tracey"
delete_user (api_url, username)