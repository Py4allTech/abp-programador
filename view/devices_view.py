def display_device_addition_result(success: bool) -> None:
    """Muestra un mensaje dependiendo del resultado de agregar un dispositivo."""
    if success:
        print('\nDispositivo agregado correctamente.\n')
    else:
        print('\nNo se pudo agregar el dispositivo.\n')


def show_user_devices(devices: list[dict]) -> None:
    """Muestra todos los dispositivos del usuario de forma legible."""
    if not devices:
        print('\nNo se encontraron dispositivos.\n')
        return

    for device in devices:
        print(f'\nNombre: {device["name"]}')
        print(f'Estado: {device["state"]}')
        print(f'Tipo: {device["type"]}')
        print(f'Ubicación: {device["location"]}')
        print(f'Hogar: {device["home"]}')
        print('-' * 40)