device_id_counter = 1  # Contador global para generar IDs únicos de dispositivos

def generate_device_id() -> int:
    """Genera un ID único para un nuevo dispositivo."""
    global device_id_counter
    device_id = device_id_counter
    device_id_counter += 1
    return device_id


def get_home_ids_by_email(email_user: str, user_home_data: list[dict]) -> list[int]:
    """Devuelve una lista de IDs de hogares asociados a un usuario."""
    return [entry['home_id'] for entry in user_home_data if entry['email'] == email_user]


def is_user_authorized_for_home(email_user: str, home_id: int, user_home_data: list[dict]) -> bool:
    """Verifica si el usuario tiene acceso al hogar especificado."""
    return home_id in get_home_ids_by_email(email_user, user_home_data)


def get_element_by_name(data_base: list[dict], key_name: str, user_input: str) -> dict | None:
    """Busca un elemento en la base de datos por nombre (case-insensitive)."""
    for item in data_base:
        if item[key_name].lower() == user_input.lower():
            return item
    return None


def request_and_validate_element(prompt: str, data_base: list[dict], key_name: str) -> dict:
    """
    Solicita al usuario un valor y valida que exista en la base de datos.
    Se repite hasta que el usuario ingrese un valor válido.
    """
    while True:
        user_input = input(prompt).strip()
        element = get_element_by_name(data_base, key_name, user_input)
        if element:
            return element
        print('Entrada inválida. Intente nuevamente.')


def get_name_by_id(data_base: list[dict], id_value: int, id_key: str = 'id', name_key: str = 'name') -> str:
    """Obtiene el nombre de un elemento en base a su ID."""
    for item in data_base:
        if item[id_key] == id_value:
            return item[name_key]


def map_device_data_for_view(device: dict, states: dict, types_device: dict, locations: dict, homes: dict) -> dict:
    """
    Convierte los IDs de un dispositivo a sus nombres legibles,
    para ser mostrados en la vista.
    """
    return {
        'name': device['name'],
        'state': get_name_by_id(states, device['id_state']),
        'type': get_name_by_id(types_device, device['id_type']),
        'location': get_name_by_id(locations, device['id_location']),
        'home': get_name_by_id(homes, device['id_home'], id_key='id', name_key='name')
    }
