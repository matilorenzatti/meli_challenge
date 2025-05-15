import os
import logging



# Usamos la libreria OS para crear las rutas correctamente
# y poder usar este PATH para guardar el DataFrame en formato Pickle
# No hacemos un hardcode para que cada persona que lo ejecute pueda formar su propia path
# independientemente del sistema operativo, carpetas anteriores, etc.

directory = os.path.dirname(os.path.abspath(__file__))
path_pickle = os.path.join(os.path.sep.join(directory.split(os.path.sep)[:-2]),'data','pickle','df_contacts.pkl')






def setup_logger(log_relative_path: str):
    """
    Configura un logger con formato y nivel fijo, que guarda logs en logs/{log_relative_path}.

    Parameters:
    - log_relative_path (str): ruta relativa, ej: 'cleaning/clean_contacts.log'
    """
    # Ruta absoluta a la carpeta logs/ en el root
    logs_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "logs"))
    full_log_path = os.path.join(logs_root, log_relative_path)

    os.makedirs(os.path.dirname(full_log_path), exist_ok=True)

    # Crear logger específico para este archivo
    logger_name = os.path.splitext(os.path.basename(log_relative_path))[0]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(full_log_path, mode="a", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False  # evita duplicación en consola

    return logger
