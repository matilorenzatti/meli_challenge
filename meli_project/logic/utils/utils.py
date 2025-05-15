import os
import logging
import pickle
import pandas as pd


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




def cargar_todos_df_silver():
    """
    Carga todos los archivos .parquet de la capa silver (data/o2_silver)
    y los devuelve como un diccionario de DataFrames o errores.

    Retorna:
    - dict: {nombre_archivo_sin_extension: DataFrame | None}
    """
    dfs = {}

    silver_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../data/o2_silver")
    )

    if not os.path.exists(silver_path):
        return dfs  # Devuelve diccionario vacío si la carpeta no existe

    for file in os.listdir(silver_path):

        if file.endswith(".parquet"):

            nombre = os.path.splitext(file)[0]

            file_path = os.path.join(silver_path, file)

            try:
                dfs[nombre] = pd.read_parquet(file_path)

            except Exception as e:

                # Guardamos None o el mensaje de error, según lo prefieras
                dfs[nombre] = f"Error al cargar: {e}"

    return dfs




def cargar_df_silver(nombre_archivo: str):
    """
    Carga un archivo .parquet específico desde la capa silver.

    Parámetros:
    - nombre_archivo (str): Nombre del archivo .parquet (ej: 'df_conectividad_arg.parquet')

    Retorna:
    - pd.DataFrame: El DataFrame cargado desde el archivo.
    """

    silver_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../data/o2_silver")
    )

    file_path = os.path.join(silver_path, nombre_archivo)

    if os.path.exists(file_path):

        try:
            return pd.read_parquet(file_path)

        except Exception as e:

            return f"❌ Error al cargar {nombre_archivo}: {e}"

    else:

        return f"⚠️ El archivo '{nombre_archivo}' no existe en la carpeta silver."





def cargar_df_master_gold(nombre_archivo: str = "df_master.parquet") -> pd.DataFrame:

    """
    Carga el archivo maestro unificado desde la capa gold.

    Parámetros:
    - nombre_archivo (str): Nombre del archivo .parquet a cargar. Por defecto, 'df_master.parquet'.

    Retorna:
    - pd.DataFrame: DataFrame cargado desde la capa gold.
    - En caso de error, devuelve un DataFrame vacío.
    """

    # Ruta absoluta a la carpeta gold
    gold_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../data/o3_gold")
    )

    file_path = os.path.join(gold_path, nombre_archivo)


    if os.path.exists(file_path):

        try:
            return pd.read_parquet(file_path)


        except Exception as e:

            return f"❌ Error al cargar el archivo '{nombre_archivo}': {e}"

    else:

        return f"⚠️ El archivo '{nombre_archivo}' no existe en la carpeta gold."
