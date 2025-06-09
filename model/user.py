from model.rol import roles
from typing import Dict, Optional

# Usuario ADMIN almacenado en la tabla users
users = [
    {
        "email": "fernandomoyano21@gmail.com",
        "name": "Fernando",
        "password": "admin123",
        "id_rol": roles[0]["id"],
    }
]


def isExist(email) -> bool:
    """Funcion que valida si el usuario ya existe"""
    for user in users:
        if user["email"] == email:
            return True
    return False


def check_username(username):
    """Funcion que valida si el username coincide"""
    for user in users:
        if user["name"] == username:
            return True
    return False



def check_email(email):
    """Funcion que valida si el email coincide"""
    for user in users:
        if user["email"] == email:
            return True
    return False



def check_password(password):
    """Funcion que valida si la contraseña coincide"""
    for user in users:
        if user["password"] == password:
            return True
    return False



def get_user_by_email(email: str) -> Optional[Dict]:
    """Obtener usuario completo por email"""
    for user in users:
        if user["email"] == email:
            # se retorna una copia del usuario sin la contraseña por seguridad
            return {
                "email": user["email"],
                "name": user["name"],
                "id_rol": user["id_rol"]
            }
    return None



def validate_login(email: str, password: str) -> bool:
    """Validar login completo (email Y contraseña del mismo usuario)"""
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True
    return False


def save(user: Dict):
    """guardar un usuario en la base de datos"""
    user_to_save = {
        "email": user["email"],
        "name": user["username"],
        "password": user["password"],
        "id_rol": roles[1]["id"],
    }
    users.append(user_to_save)
