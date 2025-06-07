device_id_counter = 1  # Variable global para contar los IDs

def get_user_input(message: str) -> str:
    return input(message).strip().lower()


def generate_device_id() -> int:
    global device_id_counter
    device_id = device_id_counter
    device_id_counter += 1
    return device_id
