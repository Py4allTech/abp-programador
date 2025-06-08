from model.devices_data import devices
from model.usersxhomes_data import userxhome

from utils.devices_utils import (
    generate_device_id, 
    is_user_authorized_for_home,
    get_home_ids_by_email,
    map_device_data_for_view
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


def get_user_devices(email_user: str, states: dict, types_device: dict, locations: dict, homes: dict) -> list[dict]:
    """Devuelve una lista de dispositivos asociados a los hogares del usuario, mapeados con datos legibles."""
    home_ids = get_home_ids_by_email(email_user, userxhome)
    
    # Filtrar solo los dispositivos que pertenecen a hogares del usuario
    user_devices = [device for device in devices if device['id_home'] in home_ids]

    # Mapear los datos para visualización (convertir IDs en nombres)
    return [map_device_data_for_view(d, states, types_device, locations, homes) for d in user_devices]