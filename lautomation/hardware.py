import RPi.GPIO as GPIO

# Configuração inicial do GPIO
GPIO.setmode(GPIO.BCM)
pins = {21: 9, 22: 11, 23: 25, 24: 8}  # Mapeamento dos pinos GPIO para seus números

# Configurar os pinos como saída e colocar em estado LOW
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Função para definir o estado do pino
def set_pin_state(pin, state):
    if pin in pins:
        GPIO.output(pins[pin], GPIO.HIGH if state else GPIO.LOW)

# Função para obter o estado do pino
def get_pin_state(pin):
    if pin in pins:
        return GPIO.input(pins[pin]) == GPIO.HIGH
    return None
