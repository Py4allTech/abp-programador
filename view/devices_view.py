def show_main_menu() -> None:
    """Muestra el menú principal de opciones al usuario."""
    print('Bienvenido al sistema de gestión de dispositivos.')
    print('1. Agregar dispositivo')
    print('2. Listar Dispositivos')
    print('3. Buscar Dispositivo')
    print('4. Eliminar Dispositivo')
    print('0. Salir')
    

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


def show_device_detail(device: dict) -> None:
    """Muestra los detalles de un dispositivo individual."""
    if not device:
        print('\nNo se encontró el dispositivo.\n')
        return

    print(f'\nNombre: {device["name"]}')
    print(f'Estado: {device["state"]}')
    print(f'Tipo: {device["type"]}')
    print(f'Ubicación: {device["location"]}')
    print(f'Hogar: {device["home"]}')
    print('-' * 40)


def display_device_deletion_result(success: bool) -> None:
    """Muestra un mensaje dependiendo del resultado de eliminar un dispositivo."""
    if success:
        print('\nDispositivo eliminado correctamente.\n')
    else:
        print('\nNo se pudo eliminar el dispositivo.\n')