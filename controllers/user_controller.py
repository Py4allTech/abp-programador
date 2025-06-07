from model.user import check_username, check_password, check_email,save
from typing import Dict

# Controlador de loguin
def login(user_data: Dict) -> str:
    if check_email(user_data["email"]) and check_password( user_data["password"]):
        return f"Usuario logueado Exitosamente"
    else:
        return f"Vuelve a ingresar los datos"

# Controlador de registro
def register(user_data: Dict) -> str:
    save(user_data)
    return f"Usuario {user_data['username']} Registrado Exitosamente"
