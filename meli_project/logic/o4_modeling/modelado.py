import os
import pandas as pd



class ModeladorWB:

    """
    Clase encargada de unificar los DataFrames procesados (capa silver) en un único DataFrame maestro,
    y guardarlo en la capa gold como archivo .parquet.
    """



    def __init__(self):
        self.silver_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o2_silver")
        )
        self.gold_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../data/o3_gold")
        )
        os.makedirs(self.gold_path, exist_ok=True)




    def cargar_todos_df_silver(self):

        """
        Carga todos los archivos .parquet de la carpeta silver en un diccionario.
        """

        dfs = {}

        if not os.path.exists(self.silver_path):
            return dfs

        for file in os.listdir(self.silver_path):

            if file.endswith(".parquet"):

                nombre = os.path.splitext(file)[0]
                file_path = os.path.join(self.silver_path, file)

                try:
                    dfs[nombre] = pd.read_parquet(file_path)

                except Exception:
                    dfs[nombre] = None  # O guardar el error como string

        return dfs



    def unificar_dataframes(self, dfs: dict):

        """
        Unifica todos los DataFrames válidos en uno solo.
        """

        df_list = [df for df in dfs.values() if isinstance(df, pd.DataFrame) and not df.empty]

        df_master = pd.concat(df_list, ignore_index=True)

        return df_master




    def guardar_df_gold(self, df: pd.DataFrame, nombre_archivo="df_master.parquet"):

        """
        Guarda el DataFrame unificado en la capa gold.
        """

        output_path = os.path.join(self.gold_path, nombre_archivo)


        try:

            df.to_parquet(output_path, index=False)

            return f"✅ Archivo guardado en: {output_path}"

        except Exception as e:

            return f"❌ Error al guardar el archivo: {e}"




    def ejecutar_pipeline_gold(self):

        """
        Ejecuta el flujo completo: carga los .parquet de silver, unifica y guarda en gold.
        """


        dfs = self.cargar_todos_df_silver()

        if not dfs:
            return "⚠️ No se encontraron archivos en silver para unificar."


        df_master = self.unificar_dataframes(dfs)


        if df_master.empty:
            return "⚠️ Todos los DataFrames están vacíos."


        resultado = self.guardar_df_gold(df_master)

        return resultado #Es el mensaje que arroja la funcion de guardar_df_gold
