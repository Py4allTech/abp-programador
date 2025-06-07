from view.users_view import show_welcome, show_login_message, show_login, show_register
from model.user import isExist
from controllers.user_controller import login, register


def main():
  
  # Mensaje de Bienvenida
  show_welcome()
  
  #Se le presenta el login al usuario 
  show_login_message()
  
  while True: 
      user_login_data = show_login()
      if not isExist(user_login_data["email"]):
          print("No tienes cuenta, registrate a continuacion...")
          user_register_data=show_register()
          message=register(user_register_data)
          print(message)
          continue
      else:
          message=login(user_login_data)
          print(message)
          break






if __name__ =="__main__":
  main()