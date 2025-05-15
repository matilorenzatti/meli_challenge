import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from meli_project.params import *





class CargadorBigQuery:

    def __init__(
        self,
        nombre_archivo_parquet="df_master.parquet",
        tabla_destino="df_maestro",
        dataset="dataframes_meli",
        project_id="reportes-bedoya-389011"
    ):
        """
        Inicializa el cargador con parámetros por defecto para BigQuery.
        """


        # Inicializar credenciales de BigQuery
        self.credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS)
        self.project_id = project_id
        self.dataset = dataset
        self.tabla_destino = tabla_destino
        self.nombre_archivo_parquet = nombre_archivo_parquet


        # Construir ruta absoluta al archivo parquet en gold
        self.gold_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o3_gold", nombre_archivo_parquet)
        )



    def cargar_a_bigquery(self):

        """
        Carga el archivo parquet a BigQuery, sobrescribiendo la tabla si existe.
        """

        if not os.path.exists(self.gold_path):

            return f"❌ Archivo parquet no encontrado: {self.gold_path}"

        try:
            df = pd.read_parquet(self.gold_path)

            df.to_gbq(
                destination_table=f"{self.dataset}.{self.tabla_destino}",
                project_id=self.project_id,
                credentials=self.credentials,
                if_exists="replace"  # reemplazar si ya existe
            )

            return f"✅ Archivo '{self.nombre_archivo_parquet}' cargado con éxito a BigQuery en '{self.dataset}.{self.tabla_destino}'."


        except Exception as e:
            return f"❌ Error al cargar el archivo a BigQuery: {e}"
