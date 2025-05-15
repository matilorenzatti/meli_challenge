import os
import logging
import pickle



# directory = os.path.dirname(os.path.abspath(__file__))
# path_pickle = os.path.join(os.path.sep.join(directory.split(os.path.sep)[:-2]),'data','pickle','df_contacts.pkl')





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





def cargar_indicadores_validos_arg():
    """
    Carga la lista de indicadores válidos para Argentina desde el archivo pickle
    ubicado en data/o1_bronze/jsons_validos_ARG.pickle, y retorna solo el nombre
    limpio del indicador (sin path, sin _ARG, sin .json).

    Retorna:
    - list: Lista de nombres de indicadores válidos como strings.
    """

    try:
        ruta_pickle = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o1_bronze/jsons_validos_ARG.pickle")
        )

        with open(ruta_pickle, "rb") as f:
            archivos_validos = pickle.load(f)

        # Limpiar nombres de archivos
        indicadores = [
            os.path.basename(ruta).replace("_ARG.json", "")
            for ruta in archivos_validos
        ]

        return indicadores

    except Exception as e:
        return []



def cargar_paths_wld_desde_arg():
    """
    A partir de los archivos válidos de Argentina, genera los paths esperados
    para los mismos indicadores pero con ref_area = WLD.

    Retorna:
    - list: Lista de paths completos hacia archivos con sufijo _WLD.json
    """

    try:
        ruta_pickle = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o1_bronze/jsons_validos_ARG.pickle")
        )

        with open(ruta_pickle, "rb") as f:
            archivos_validos_arg = pickle.load(f)

        # Reemplazar "_ARG.json" por "_WLD.json" en cada path
        archivos_wld = [
            ruta.replace("_ARG.json", "_WLD.json")
            for ruta in archivos_validos_arg
        ]

        return archivos_wld

    except Exception as e:
        return []
