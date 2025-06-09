from model.automaions_data import automations
from model.devices_data import devices
from utils.devices_utils import get_home_ids_by_email
from model.usersxhomes_data import userxhome


def get_user_automations(email_user: str) -> list[dict]:
    """Obtiene automatizaciones del usuario"""
    user_home_ids = get_home_ids_by_email(email_user, userxhome)
    
    return [auto for auto in automations if auto['id_hogar'] in user_home_ids]

def execute_automation(automation_id: int, email_user: str) -> str:
    """Ejecuta una automatización"""
    user_automations = get_user_automations(email_user)
    automation = next((a for a in user_automations if a['id'] == automation_id), None)
    
    if not automation:
        return "No tienes acceso a esta automatización"
    
    if not automation['activa']:
        return "Automatización desactivada"
    
    
    if automation_id == 1:  # Encender luces del salón
        # Buscar dispositivo "Luz del Salón" y encenderlo
        for device in devices:
            if device['name'] == 'Luz del Salón':
                device['id_state'] = 1  # Encendido
                return f" {automation['nombre']} ejecutada: Luz del Salón encendida"
    
    elif automation_id == 2:  # Apagar todas las luces
        # Buscar todas las luces y apagarlas
        lights_off = []
        for device in devices:
            if 'Luz' in device['name']:
                device['id_state'] = 2  # Apagado
                lights_off.append(device['name'])
        
        if lights_off:
            return f" {automation['nombre']} ejecutada: {', '.join(lights_off)} apagadas"
        else:
            return " No se encontraron luces para apagar"
    
    elif automation_id == 3:  # Encender luz de oficina
        for device in devices:
            if device['name'] == 'Luz de la Oficina':
                device['id_state'] = 1  # Encendido
                return f" {automation['nombre']} ejecutada: Luz de la Oficina encendida"
    
    return " Automatización no implementada"