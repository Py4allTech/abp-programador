from model.rol import roles
from typing import Dict

# Usuario almacenado en la tabla users
users=[{
  "email":"fernandomoyano21@gmail.com",
  "name":"Fernando",
  "password":"admin123",
  "id_rol": roles[0]["id"]
}]

# Funcion que valida si el usuario ya existe
def isExist(email) -> bool:
  for user in users:
    if user["email"] == email:
      return True
  return False

# Funcion que valida si el username coincide
def check_username(username):
    for user in users:
        if user["name"] == username:
            return True
    return False

# Funcion que valida si el email coincide
def check_email(email):
  for user in users:
    if user["email"] == email:
      return True
  return False

# Funcion que valida si la contraseña coincide
def check_password(password):
  for user in users:
    if user["password"] == password:
      return True
  return False

def save(user: Dict):
    user_to_save = {
        "email": user["email"],
        "name": user["username"],   
        "password": user["password"],
        "id_rol": roles[1]["id"] 
    }
    users.append(user_to_save)
