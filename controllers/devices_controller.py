from model.devices_data import devices
from model.usersxhomes_data import userxhome

from utils.devices_utils import (
    generate_device_id, 
    is_user_authorized_for_home
)


def add_device(email_user, name, selected_state, selected_type, selected_location, selected_home) -> bool:
    """Agrega un nuevo dispositivo si el usuario está autorizado para el hogar seleccionado."""
    home_id = selected_home['id']
    if not is_user_authorized_for_home(email_user, home_id, userxhome):
        return False  # No se permite agregar si el hogar no pertenece al usuario

    device_id = generate_device_id()  # Generar un ID único para el dispositivo

    device = {
        'id': device_id,
        'name': name,
        'id_state': selected_state['id'],
        'id_type': selected_type['id'],
        'id_location': selected_location['id'],
        'id_home': home_id
    }

    devices.append(device)  # Guardar el dispositivo en la "base de datos"
    return True