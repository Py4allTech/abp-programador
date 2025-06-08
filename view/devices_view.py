def display_device_addition_result(success: bool) -> None:
    """Muestra un mensaje dependiendo del resultado de agregar un dispositivo."""
    if success:
        print('\nDispositivo agregado correctamente.\n')
    else:
        print('\nNo se pudo agregar el dispositivo.\n')