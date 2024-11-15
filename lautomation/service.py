from lautomation import hardware, logger
from datetime import datetime
import socket

# Helper para obter o hostname
def get_hostname():
    return socket.gethostname()

# Função para controlar o estado dos pinos
def control_pin(pin, action):
    if pin in hardware.pins:
        if action == "on":
            hardware.set_pin_state(pin, False)
            logger.log_info(f"Pin {pin} turned on")
            return {f"relay_{pin}": "on"}
        elif action == "off":
            hardware.set_pin_state(pin, True)
            logger.log_info(f"Pin {pin} turned off")
            return {f"relay_{pin}": "off"}
    return {"error": "Invalid pin"}

# Função para obter o status de todos os pinos
def get_status():
    status = {
        f"relay_{pin}": "on" if hardware.get_pin_state(pin) else "off"
        for pin in hardware.pins
    }
    status.update({
        "datetime": datetime.now().isoformat(),
        "who": get_hostname()
    })
    logger.log_info("Status retrieved")
    return status
