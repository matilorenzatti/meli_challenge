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




diccionario_indicadores_info = {
        "ITU_DH_INT_CONN_BAND_MBIT": {
            "indicator_label": "Ancho de banda internacional (Mbps)",
            "indicator_description": "Capacidad total de ancho de banda internacional de Internet en Mbps, indicando la infraestructura disponible para la conectividad internacional."
        },
        "ITU_DH_SKLS_SFTY": {
            "indicator_label": "Habilidades de seguridad digital",
            "indicator_description": "Porcentaje de personas con habilidades básicas en seguridad digital, como la gestión de contraseñas y la protección contra malware."
        },
        "ITU_DH_HH_COMP": {
            "indicator_label": "Hogares con computadora",
            "indicator_description": "Porcentaje de hogares que poseen una computadora, incluyendo desktops, laptops o tablets."
        },
        "ITU_DH_PRI_LU_MOB": {
            "indicator_label": "Uso privado de dispositivos móviles",
            "indicator_description": "Porcentaje de individuos que utilizan dispositivos móviles para uso privado, reflejando la adopción de tecnología móvil."
        },
        "ITU_DH_POP_COV_5G": {
            "indicator_label": "Cobertura de red 5G",
            "indicator_description": "Porcentaje de la población cubierta por una red móvil 5G, indicando la disponibilidad de tecnología de última generación."
        },
        "ITU_DH_INT_CONN_BAND_CAP": {
            "indicator_label": "Capacidad de conexión internacional",
            "indicator_description": "Capacidad total de conexión internacional de Internet en Gbps, mostrando la infraestructura de conectividad global."
        },
        "ITU_DH_POP_COV_3G": {
            "indicator_label": "Cobertura de red 3G",
            "indicator_description": "Porcentaje de la población cubierta por una red móvil 3G, reflejando la penetración de tecnologías móviles intermedias."
        },
        "ITU_DH_ACT_MOB_PER_100": {
            "indicator_label": "Suscripciones móviles activas por cada 100 habitantes",
            "indicator_description": "Número de suscripciones móviles activas por cada 100 personas, indicando la penetración del servicio móvil."
        },
        "ITU_DH_INV_COMP": {
            "indicator_label": "Inversión en computadoras",
            "indicator_description": "Inversión total en computadoras como porcentaje del PIB, mostrando el compromiso económico con la tecnología."
        },
        "ITU_DH_HH_RAD": {
            "indicator_label": "Hogares con radio",
            "indicator_description": "Porcentaje de hogares que poseen una radio, reflejando el acceso a medios de comunicación tradicionales."
        },
        "ITU_DH_PRI_HU_VD": {
            "indicator_label": "Uso privado de videollamadas",
            "indicator_description": "Porcentaje de individuos que utilizan videollamadas para uso privado, indicando la adopción de herramientas de comunicación digital."
        },
        "ITU_DH_POP_COV_2G": {
            "indicator_label": "Cobertura de red 2G",
            "indicator_description": "Porcentaje de la población cubierta por una red móvil 2G, mostrando la disponibilidad de tecnologías móviles básicas."
        },
        "ITU_DH_SKLS_INF_DATA": {
            "indicator_label": "Habilidades en manejo de información y datos",
            "indicator_description": "Porcentaje de personas con habilidades para manejar información y datos digitales, como la búsqueda y evaluación de información en línea."
        },
        "ITU_DH_INT_CONN_BAND": {
            "indicator_label": "Ancho de banda internacional total",
            "indicator_description": "Capacidad total de ancho de banda internacional de Internet en Gbps, indicando la infraestructura disponible para la conectividad global."
        },
        "ITU_DH_COMP_MOB_BB": {
            "indicator_label": "Computadoras con banda ancha móvil",
            "indicator_description": "Porcentaje de computadoras conectadas a banda ancha móvil, reflejando la movilidad en el acceso a Internet."
        },
        "ITU_DH_FIX_TEL_OR_MOB": {
            "indicator_label": "Teléfonos fijos o móviles",
            "indicator_description": "Porcentaje de hogares con acceso a teléfono fijo o móvil, indicando la disponibilidad de servicios de comunicación básicos."
        },
        "ITU_DH_HH_TV": {
            "indicator_label": "Hogares con televisión",
            "indicator_description": "Porcentaje de hogares que poseen una televisión, reflejando el acceso a medios de entretenimiento e información."
        },
        "ITU_DH_PRI_FIX_BB_5G": {
            "indicator_label": "Uso privado de banda ancha fija 5G",
            "indicator_description": "Porcentaje de individuos que utilizan banda ancha fija 5G para uso privado, mostrando la adopción de tecnologías de alta velocidad."
        },
        "ITU_DH_FIX_BR_SUB_PER_100": {
            "indicator_label": "Suscripciones de banda ancha fija por cada 100 habitantes",
            "indicator_description": "Número de suscripciones de banda ancha fija por cada 100 personas, indicando la penetración del servicio de Internet fijo."
        },
        "ITU_DH_SKLS_DIG_CONT": {
            "indicator_label": "Habilidades en creación de contenido digital",
            "indicator_description": "Porcentaje de personas con habilidades para crear contenido digital, como blogs, videos o publicaciones en redes sociales."
        },
        "ITU_DH_INT_USR_WKL": {
            "indicator_label": "Usuarios de Internet semanales",
            "indicator_description": "Porcentaje de individuos que utilizan Internet al menos una vez por semana, reflejando la frecuencia de uso."
        },
        "ITU_DH_COMP_INT_GTW": {
            "indicator_label": "Computadoras conectadas a la red",
            "indicator_description": "Porcentaje de computadoras conectadas a la red de Internet, indicando la disponibilidad de acceso en dispositivos."
        },
        "ITU_DH_PRI_LU_VD": {
            "indicator_label": "Uso privado de video bajo demanda",
            "indicator_description": "Porcentaje de individuos que utilizan servicios de video bajo demanda para uso privado, mostrando la adopción de plataformas de streaming."
        },
        "ITU_DH_SKLS_COMN_COLAB": {
            "indicator_label": "Habilidades de comunicación y colaboración digital",
            "indicator_description": "Porcentaje de personas con habilidades para comunicarse y colaborar en entornos digitales, como el uso de correo electrónico y herramientas colaborativas."
        },
        "ITU_DH_HH_INT": {
            "indicator_label": "Hogares con acceso a Internet",
            "indicator_description": "Porcentaje de hogares que tienen acceso a Internet, reflejando la penetración del servicio en el ámbito doméstico."
        },
        "ITU_DH_INT_BAND_PER_INT_USR": {
            "indicator_label": "Ancho de banda por usuario de Internet",
            "indicator_description": "Promedio de ancho de banda internacional disponible por usuario de Internet, indicando la calidad del servicio."
        },
        "ITU_DH_COMP_FIB": {
            "indicator_label": "Computadoras con conexión de fibra óptica",
            "indicator_description": "Porcentaje de computadoras conectadas a través de fibra óptica, mostrando la adopción de tecnologías de alta velocidad."
        },
        "ITU_DH_INT_BAND_PER_CAP": {
            "indicator_label": "Ancho de banda per cápita",
            "indicator_description": "Promedio de ancho de banda internacional disponible por persona, reflejando la capacidad de la infraestructura en relación con la población."
        },
        "ITU_DH_INT_USR_DAY": {
            "indicator_label": "Usuarios diarios de Internet",
            "indicator_description": "Porcentaje de individuos que utilizan Internet diariamente, indicando la intensidad de uso."
        },
        "ITU_DH_MOB_SUB_PER_100": {
            "indicator_label": "Suscripciones móviles por cada 100 habitantes",
            "indicator_description": "Número de suscripciones móviles por cada 100 personas, mostrando la penetración del servicio móvil."
        },
        "ITU_DH_COMP_INT_SER": {
            "indicator_label": "Computadoras con servicios de Internet",
            "indicator_description": "Porcentaje de computadoras que utilizan servicios de Internet, reflejando la funcionalidad y uso de los dispositivos."
        },
        "ITU_DH_SKLS_PRB_SOLV": {
            "indicator_label": "Habilidades para resolver problemas en entornos digitales",
            "indicator_description": "Porcentaje de personas con habilidades para resolver problemas en entornos digitales, como la solución de errores o la configuración de dispositivos."
        },
        "ITU_DH_TRAF_FIX_BB": {
            "indicator_label": "Tráfico de banda ancha fija",
            "indicator_description": "Volumen total de tráfico de banda ancha fija en GB, indicando el uso de servicios de Internet fijo."
        },
        "ITU_DH_TRAF_MOB_BB": {
            "indicator_label": "Tráfico de banda ancha móvil",
            "indicator_description": "Volumen total de tráfico de banda ancha móvil en GB, mostrando el uso de servicios de Internet móvil."
        },
        "ITU_DH_PRI_DO_MOB": {
            "indicator_label": "Uso privado de descarga móvil",
            "indicator_description": "Porcentaje de individuos que descargan contenido a través de dispositivos móviles para uso privado, reflejando la adopción de servicios móviles."
        },
        "ITU_DH_INT_USR_MON": {
            "indicator_label": "Usuarios mensuales de Internet",
            "indicator_description": "Porcentaje de individuos que utilizan Internet al menos una vez al mes, indicando la frecuencia de uso."
        },
        "ITU_DH_POP_COV_4G": {
            "indicator_label": "Cobertura de red 4G",
            "indicator_description": "Porcentaje de la población cubierta por una red móvil 4G, mostrando la disponibilidad de tecnologías móviles avanzadas."
        },
        "ITU_DH_INT_USER_PT": {
            "indicator_label": "Usuarios de Internet por tipo de dispositivo",
            "indicator_description": "Distribución porcentual de usuarios de Internet según el tipo de dispositivo utilizado, como computadoras, tablets o smartphones."
        },
        "ITU_DH_FIX_SUB_PER_100": {
            "indicator_label": "Suscripciones de telefonía fija por cada 100 habitantes",
            "indicator_description": "Número de suscripciones de telefonía fija por cada 100 personas, indicando la penetración del servicio de telefonía fija."
        }
    }




def convertir_parquet_a_csv():

    """
    Convierte todos los archivos .parquet de la capa gold (data/o3_gold)
    a archivos .csv y los guarda en la carpeta data/o4_external con el mismo nombre.
    """

    gold_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../data/o3_gold")
    )

    external_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../data/o4_external")
    )

    os.makedirs(external_path, exist_ok=True)

    archivos_convertidos = 0

    for file in os.listdir(gold_path):

        if file.endswith(".parquet"):

            try:
                parquet_path = os.path.join(gold_path, file)
                df = pd.read_parquet(parquet_path)

                nombre_csv = file.replace(".parquet", ".csv")
                csv_path = os.path.join(external_path, nombre_csv)

                df.to_csv(csv_path, index=False)

                archivos_convertidos += 1




            except Exception as e:

                continue


    if archivos_convertidos == 0:

        return "⚠️ No se encontraron archivos .parquet en la carpeta gold."


    else:
        return f"🎯 Total archivos convertidos: {archivos_convertidos}"
