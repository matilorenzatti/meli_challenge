import os
import pandas as pd
from meli_project.logic.utils.utils import setup_logger



class TransformadorWB:


    def __init__(self, dfs: dict):
        """
        Recibe el diccionario de DataFrames limpio (extraído de los JSONs).
        """
        self.dfs = dfs

        # Definimos la ruta a silver
        self.silver_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o2_silver")
        )
        os.makedirs(self.silver_path, exist_ok=True)



        # Diccionario para categorizar los indicadores
        self.categorias_indicadores = {
            "ACCESO_USO": ["HH_INT"],
            "INFRAESTRUCTURA": ["CONN_BAND", "POP_COV", "FIX_SUB", "MOB_SUB"],
            "TECNOLOGIA": ["HH_COMP", "PRI_", "FIX_", "MOB_"],
            "HABILIDADES": ["SKLS", "COMP_INT"],
        }

        self.nombre_legible_indicadores = {
            "ITU_DH_HH_INT": "Hogares con acceso a Internet",
            "ITU_DH_TRAF_MOB_BB": "Tráfico total de banda ancha móvil",
            "ITU_DH_PRI_FIX_BB_5G": "Suscripciones fijas de banda ancha con tecnología 5G",
            "ITU_DH_INT_USER_PT": "Porcentaje de usuarios de Internet por tipo de tecnología",
            "ITU_DH_INT_BAND_PER_CAP": "Banda ancha internacional per cápita",
            "ITU_DH_PRI_DO_MOB": "Uso privado de dispositivos móviles",
            "ITU_DH_HH_COMP": "Hogares con computadora",
            "ITU_DH_PRI_HU_VD": "Uso privado de herramientas digitales como videollamadas",
            "ITU_DH_PRI_LU_MOB": "Uso privado de dispositivos móviles",
            "ITU_DH_INT_BAND_PER_INT_USR": "Banda ancha internacional por usuario de Internet",
            "ITU_DH_FIX_TEL_OR_MOB": "Suscripciones de telefonía fija o móvil",
            "ITU_DH_INT_CONN_BAND_MBIT": "Ancho de banda internacional total (Mbps)",
            "ITU_DH_PRI_LU_VD": "Uso privado de videollamadas",
            "ITU_DH_FIX_SUB_PER_100": "Suscripciones de telefonía fija por cada 100 habitantes",
            "ITU_DH_POP_COV_3G": "Cobertura de red 3G",
            "ITU_DH_FIX_BR_SUB_PER_100": "Suscripciones de banda ancha fija por cada 100 habitantes",
            "ITU_DH_MOB_SUB_PER_100": "Suscripciones móviles por cada 100 habitantes",
            "ITU_DH_POP_COV_4G": "Cobertura de red 4G",
            "ITU_DH_INV_COMP": "Inversión en computadoras (como % del PBI)",
            "ITU_DH_INT_CONN_BAND": "Capacidad total de conexión internacional (Gbps)",
            "ITU_DH_COMP_INT_SER": "Computadoras conectadas a servicios de Internet",
            "ITU_DH_POP_COV_2G": "Cobertura de red 2G",
            "ITU_DH_COMP_INT_GTW": "Computadoras conectadas a gateways de Internet"
        }




    def asignar_categoria_indicador(self, indicador: str) -> str:
        """
        Detecta la categoría de un indicador basándose en su código.
        """
        for categoria, keywords in self.categorias_indicadores.items():
            if any(kw in indicador for kw in keywords):
                return categoria
        return "OTROS"



    def transformar_df(self, df: pd.DataFrame, nombre: str) -> pd.DataFrame:
        """
        Aplica limpieza, selección de columnas y enriquecimiento a un DataFrame individual.
        """
        columnas_interes = [
            "OBS_VALUE", "TIME_PERIOD", "REF_AREA", "INDICATOR"
        ]

        df = df[columnas_interes].copy()

        # Convertir a los tipos de datos correctos
        df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")
        df["TIME_PERIOD"] = df["TIME_PERIOD"].astype(str)
        df["REF_AREA"] = df["REF_AREA"].astype(str)
        df["INDICATOR"] = df["INDICATOR"].astype(str)

        # Enriquecer con legibilidad
        df["INDICATOR_NAME"] = df["INDICATOR"].apply(lambda x: x.replace("ITU_DH_", "").replace("_", " ").title())

        df["CATEGORY"] = df["INDICATOR"].apply(self.asignar_categoria_indicador)

        df["INDICATOR_DESC"] = df["INDICATOR"].map(self.nombre_legible_indicadores).fillna("Descripción no disponible")


        return df



    def transformar_todos(self):
        """
        Transforma todos los DataFrames, limpia, normaliza y guarda en silver.
        """

        logger = setup_logger('o3_transformation_logs/transformar_dfs.log')

        logger.info("INICIO transformación de DataFrames hacia capa silver")

        for nombre, df in self.dfs.items():

            try:
                df_transformado = self.transformar_df(df, nombre)

                file_path = os.path.join(self.silver_path, f"df_{nombre}.parquet")
                df_transformado.to_parquet(file_path, index=False)

                logger.info(f"✅ {nombre} transformado y guardado en silver.")

            except Exception as e:
                logger.error(f"❌ Error transformando {nombre}: {e}")
