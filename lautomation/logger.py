import logging
from datetime import datetime

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("gpio_log.txt"),
        logging.StreamHandler()  # Para imprimir no console
    ]
)

logger = logging.getLogger("GPIOLogger")

# Função de log que pode ser usada externamente
def log_info(message):
    logger.info(message)
