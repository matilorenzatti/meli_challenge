import os
import json
import pandas as pd
from meli_project.logic.utils.utils import *



class DFsWB:

    def __init__(self):

        self.bronze_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o1_bronze")
        )




    def listar_jsons_validos(self):
        """
        Lista todos los archivos JSON válidos (con count > 0) dentro de la carpeta bronze.
        """

        logger = setup_logger('o2_cleaning_logs/API_WB/listar_jsons_validos.log')

        archivos_validos = []

        logger.info("INICIO listado de JSON's validos")

        for file in os.listdir(self.bronze_path):

            if file.endswith(".json"):
                path = os.path.join(self.bronze_path, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        if data.get("count", 0) > 0:
                            archivos_validos.append(path)
                            logger.info(f"✅ El archivo {file} es valido.")

                        else:

                            logger.warning(f"⚠️ El archivo {file} NO tiene datos (count = 0).")


                except Exception as e:

                    logger.error(f"❌ Error al leer el archivo {file}: {e}")

        logger.info("FIN listado de JSON's validos")

        return archivos_validos



    def convertir_json_a_df(self, json_path):
        """
        Convierte un archivo JSON específico (con count > 0) en un DataFrame.
        """

        json_file = os.path.basename(json_path)

        logger = setup_logger('o2_cleaning_logs/API_WB/convertir_json_a_df.log')

        logger.info(f"INICIO conversion del JSON {json_file}")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if data.get("count", 0) > 0 and "value" in data:

                df = pd.json_normalize(data["value"])
                df["source_file"] = json_file

                logger.info(f"FIN conversion. ✅ Archivo convertido exitosamente: {json_file}")


                return df

            else:

                logger.warning(f"FIN conversion. ⚠️ Archivo sin datos o sin campo 'value': {json_path}")

                return pd.DataFrame()



        except Exception as e:

            logger.error(f"❌ Error procesando {json_path}: {e}")
            return pd.DataFrame()


    def obtener_todos_df(self):
        """
        Convierte todos los JSON válidos en un diccionario de DataFrames.
        """

        logger = setup_logger('o2_cleaning_logs/API_WB/obtener_todos_df.log')


        logger.info("INICIO conversión de JSONs válidos a DataFrames.")

        dfs = {}

        try:
            archivos = self.listar_jsons_validos()

            for path in archivos:

                nombre = os.path.basename(path).replace(".json", "")

                df = self.convertir_json_a_df(path)

                if not df.empty:
                    dfs[nombre] = df
                    logger.info(f"✅ Archivo {nombre} convertido a DF.")
                else:
                    self.logger.warning(f"⚠️ No se generó DataFrame para: {nombre}")

            logger.info(f"FIN conversión de JSONs. Total de DataFrames generados: {len(dfs)}")

            return dfs

        except Exception as e:

            logger.error(f"❌ Error crítico al convertir JSONs a DataFrames: {e}")

            return {}
