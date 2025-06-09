from model.user import check_username, check_password, check_email, validate_login, get_user_by_email, save
from model.rol import roles
from typing import Dict


""" def login(user_data: Dict) -> str:
    if check_email(user_data["email"]) and check_password( user_data["password"]):
        return f"Usuario logueado Exitosamente"
    else:
        return f"Algunos datos no son validos, Vuelve a intentar" """


""" def register(user_data: Dict) -> str:
    save(user_data)
    return f"Usuario {user_data['username']} Registrado Exitosamente" """


def login(user_data: Dict) -> Dict:
    """Controlador de login """
    if validate_login(user_data["email"], user_data["password"]):
        user_info = get_user_by_email(user_data["email"])
        return {
            "success": True,
            "message": "Usuario logueado exitosamente",
            "user_data": user_info
        }
    else:
        return {
            "success": False,
            "message": "Algunos datos no son válidos, vuelve a intentar",
            "user_data": None
        }



def register(user_data: Dict) -> Dict:
    """Controlador de registro"""
    try:
        save(user_data)
        return {
            "success": True,
            "message": f"Usuario {user_data['username']} registrado exitosamente",
            "user_data": {
                "email": user_data["email"],
                "name": user_data["username"],
                "id_rol": roles[1]["id"]  # Rol de usuario normal
            }
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al registrar usuario: {str(e)}",
            "user_data": None
        }


