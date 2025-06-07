from typing import Dict
from utils.helpers import get_user_input


def show_welcome():
  print("--------------#-------------")
  print("Bienvenido a 🕹️Hogar Boot🕹️")
  print("--------------#-------------")

def show_login_message() -> None:
  print("Inicia sesion para continuar o crea una cuenta si no tienes")

def show_login() -> Dict:
  email :str = get_user_input("Ingresa tu email")
  password :str = get_user_input("ingresa tu contraseña")
  return {
    "email":email,
    "password":password
  }
  
def show_register() -> Dict:
  username :str = get_user_input("Ingresa tu nombre de usuario")
  email:str = get_user_input("Ingresa tu email")
  password :str = get_user_input("ingresa tu contraseña")
  return {
    "username":username,
    "email":email,
    "password":password
  }