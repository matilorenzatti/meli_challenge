import os
import json
import requests
import pandas as pd
from meli_project.logic.utils.utils import *



class DataWB:


    # Definimos el metodo INIT (constructor) con los parametros comunes a usar
    def __init__(
        self,
        database_id = "ITU_DH",
        ref_area= "ARG",
        base_url = "https://data360api.worldbank.org/data360/data"
    ):
        """
        Parametros genericos y basicos para iniciar la clase sin problemas.

        """

        self.base_url = base_url
        self.database_id = database_id
        self.ref_area = ref_area



        # Ruta absoluta a /data/1_bronze, no se hardcodea, sino que usamos OS

        self.bronze_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o1_bronze")
        )

        # Creo la carpeta en caso de no estar creada, controlo errores con el exist_ok
        os.makedirs(self.bronze_path, exist_ok=True)



    def get_params(self, indicator, **kwargs):

        """Armar el diccionario de parámetros segun que parametros necesitemos usar.
        """

        params = {
            "DATABASE_ID": self.database_id,
            "INDICATOR": indicator,
            "REF_AREA": self.ref_area,
        }


        opcionales = {
            "SEX": kwargs.get("sex"),
            "AGE": kwargs.get("age"),
            "URBANISATION": kwargs.get("urbanisation"),
            "COMP_BREAKDOWN_1": kwargs.get("comp_breakdown_1"),
            "COMP_BREAKDOWN_2": kwargs.get("comp_breakdown_2"),
            "COMP_BREAKDOWN_3": kwargs.get("comp_breakdown_3"),
            "timePeriodFrom": kwargs.get("time_from"),
            "timePeriodTo": kwargs.get("time_to"),
            "FREQ": kwargs.get("freq"),
            "UNIT_MEASURE": kwargs.get("unit_measure"),
            "UNIT_TYPE": kwargs.get("unit_type"),
            "UNIT_MULT": kwargs.get("unit_mult"),
        }

        for k, v in opcionales.items():
            if v is not None:
                params[k] = v

        return params



    def obtener_json(self, indicator, **kwargs):

        """Realiza la consulta a la API y guarda el resultado como JSON en la carpeta bronze."""

        logger = setup_logger(f'o1_extraction_logs/API_WB/{indicator}.log')

        params = self.get_params(indicator, **kwargs)

        headers = {
            "Accept": "application/json"
        }

        logger.info(f"INICIANDO descarga del indicador {indicator}-{self.ref_area} a la API del WB")

        response = requests.get(self.base_url, params=params, headers=headers)


        if response.status_code == 200:

            # Definimos el nombre del archivo JSON
            file_name = f"{indicator}_{self.ref_area}.json"

            # Definimos el path
            output_path = os.path.join(self.bronze_path, file_name)

            # Guardamos el JSON en la carpeta bronze, para traer la fuente tal cual la obtenemos
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(response.json(), f, indent=4, ensure_ascii=False)

            # Registramos el log en caso de estar todo ok para tener un control

            logger.info(f"✅ FIN de la petición: indicador {indicator}-{self.ref_area} descargado correctamente.")


            return f"✅ JSON guardado correctamente en {output_path}"

        else:

            # Registramos log en caso de error para saber que sucedio
            logger.error(f"❌ FIN con error: indicador {indicator}-{self.ref_area}. Código {response.status_code}")

            return f"❌ Error {response.status_code}: {response.text}"




    def obtener_lista_indicadores_disponibles(self, dataset_id="ITU_DH"):

        """
        Consulta la API del Banco Mundial y devuelve la lista de indicadores disponibles
        para un dataset específico (por defecto ITU_DH).
        """

        logger = setup_logger('o1_extraction_logs/API_WB/listado_indicadores_disponibles.log')

        url = "https://data360api.worldbank.org/data360/indicators"

        params = {"datasetId": dataset_id}

        logger.info(f"INICIO consulta de indicadores para {dataset_id}")

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:

                indicadores = response.json()

                logger.info(f"FIN consulta. ✅ {len(indicadores)} indicadores disponibles para el dataset {dataset_id}.")
                return indicadores

            else:
                logger.error(f"FIN consulta. ❌ Error al consultar indicadores. Código: {response.status_code}")
                return []

        except Exception as e:
            logger.critical(f"Error inesperado al obtener indicadores: {e}")
            return []




    def obtener_all_data(self,indicadores: list = None):

        """
        Descarga todos los indicadores definidos y guarda su resultado como JSON.
        Registra un log general del proceso.
        """

        logger = setup_logger('o1_extraction_logs/API_WB/0_todos_indicadores.log')

        if (indicadores is None) or (not isinstance(indicadores,list)):
            indicadores = self.obtener_lista_indicadores_disponibles()


        logger.info(f"{self.ref_area} - INICIO de extracción masiva de indicadores del Banco Mundial")

        descargados_ok = []
        errores = []

        for ind in indicadores:

            try:
                resultado = self.obtener_json(ind)

                if resultado.startswith("✅"):
                    descargados_ok.append(ind)
                else:
                    errores.append(ind)

            except Exception as e:
                errores.append(ind)
                logger.error(f"❌ Excepción inesperada al descargar {ind}: {e}")


        # Log final con resumen

        logger.info(f"✅ Indicadores descargados correctamente: {len(descargados_ok)}")
        logger.info(f"❌ Indicadores con error: {len(errores)}")
        logger.info(f"{self.ref_area} - FIN Proceso de descarga")

        if errores:
            logger.warning(f"⚠️ Indicadores fallidos: {errores}")
            return f"❌ Error: No se pudieron extraer todos los indicadores. Fallaron {len(errores)} de {len(indicadores)}."
        else:
            return f"✅ Todos los {len(indicadores)} indicadores fueron extraídos correctamente."
