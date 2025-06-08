from model.states_data import states
from model.types_data import types_device
from model.locations_data import locations
from model.homes_data import homes

from view.devices_view import (
    show_main_menu, 
    display_device_addition_result, 
    show_user_devices,
    show_device_detail,
    display_device_deletion_result
)

from controllers.devices_controller import (
    add_device, 
    get_user_devices, 
    search_device_by_name,
    delete_device_by_name
)

from utils.devices_utils import request_and_validate_element


def main():
    while True:
        show_main_menu()
        option = input("Seleccione una opción: ").strip()
        
        if option == '1':
            email_user = 'juan@example.com'  # Usuario simulando sesión activa
            name = input("Nombre del dispositivo: ").strip()

            # Solicita y valida cada dato requerido del dispositivo
            selected_state = request_and_validate_element('Estado (Ej: Encendido, Apagado): ', states, 'name')
            selected_type = request_and_validate_element('Tipo de dispositivo (Ej: Luz, Termostato): ', types_device, 'name')
            selected_location = request_and_validate_element('Ubicación (Ej: Sala, Cocina): ', locations, 'name')
            selected_home = request_and_validate_element('Hogar (Ej: Casa Principal): ', homes, 'name')
            
            # Envía los datos al controlador para intentar agregar el dispositivo
            success = add_device(email_user, name, selected_state, selected_type, selected_location, selected_home)
            display_device_addition_result(success)

        elif option == '2':
            email_user = 'juan@example.com'

            # Obtiene y muestra todos los dispositivos del usuario
            results = get_user_devices(email_user, states, types_device, locations, homes)
            show_user_devices(results)

        elif option == '3':
            email_user = 'juan@example.com'
            name = input("Nombre del dispositivo: ").strip()

            # Busca un dispositivo por nombre
            results = search_device_by_name(email_user, name, states, types_device, locations, homes)
            show_device_detail(results)

        elif option == '4':
            email_user = 'juan@example.com'
            name = input("Nombre del dispositivo: ").strip()

            # Intenta eliminar el dispositivo y muestra el resultado
            success = delete_device_by_name(email_user, name)
            display_device_deletion_result(success)

        elif option == '0':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
