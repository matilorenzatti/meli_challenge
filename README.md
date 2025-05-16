# 🌐 Proyecto de Análisis de Indicadores de Conectividad e Inclusión Digital (Argentina + Mundo)

---

## 🧠 ¿De qué trata este proyecto?

Este proyecto tiene como objetivo principal construir un **pipeline de datos completo y modular**, capaz de consumir datos públicos desde la **API oficial del Banco Mundial**, procesarlos de forma estructurada, generar un **modelo dimensional**, y facilitar su visualización en herramientas de Business Intelligence (BI), como Looker Studio o Power BI.

La pregunta guía del proyecto es:

> 📈 ¿Cómo ha evolucionado el acceso a Internet y la infraestructura digital en Argentina en comparación con el resto del mundo?

---

## 🎯 Objetivos principales

- Explorar y consumir datos digitales y de conectividad desde el Banco Mundial (API `Data360`).
- Identificar y seleccionar indicadores válidos y con datos disponibles para Argentina.
- Documentar y entender a fondo el funcionamiento de la API.
- Crear un **ETL profesional** con buenas prácticas de ingeniería de datos.
- Transformar y modelar la información en un **modelo dimensional analítico**.
- Subir la información a **Google BigQuery** y **visualizarla en Looker Studio**.
- Permitir futuras integraciones y comparaciones con otras fuentes como INDEC o ENACOM.

---

## 📦 ¿Qué incluye este repositorio?

| Componente                     | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `main.py`                     | Orquestador ETL completo con logs por etapa.                                |
| `data/o1_bronze/`             | JSON crudos descargados desde la API.                                       |
| `data/o2_silver/`             | DataFrames limpios y normalizados listos para modelar.                      |
| `data/o3_gold/`               | Tablas de hechos y dimensiones modeladas (formato `.parquet`).              |
| `data/o4_external/`           | Exportación de las tablas en `.csv` para uso inmediato en herramientas BI.  |
| `logic/o1_extraction/`        | Módulo de extracción vía API REST (configurable y reutilizable).            |
| `logic/o2_cleaning/`          | Conversión de JSON a DataFrames, validación de estructura y conteo.         |
| `logic/o3_transformation/`    | Limpieza, tipado, enriquecimiento con nombres legibles y categorías.        |
| `logic/o4_modeling/`          | Generación del modelo dimensional (dimensiones + tabla de hechos).          |
| `logic/o5_serving/`           | Envío automático de los datos procesados a BigQuery.                        |
| `utils/`                      | Diccionarios, funciones auxiliares, configuración de logs, helpers, etc.    |

---

## 🔍 Desafíos enfrentados

- **Falta de documentación oficial** sobre la API del Banco Mundial.
- La estructura del JSON era inconsistente según el indicador consultado.
- Filtros como sexo, edad o urbanización afectaban la existencia de los datos.
- El proceso de determinar **cuáles indicadores tienen datos para Argentina** fue manual y costoso.
- Implementé una estrategia para **consultar solo indicadores con `count > 0`** y repetir el proceso para `WLD` (world).
- El dashboard en Tableau no permitía compartirlo fácilmente, por eso se optó por Looker Studio.

---

## 🚀 Proceso técnico

1. **🔍 Análisis de la API**
   - Investigación de endpoints, parámetros y estructura de respuesta.
   - Documentación propia generada a partir del análisis.

2. **📥 Extracción**
   - Clase genérica `DataWB` para consumir la API usando `requests`.
   - Validación de indicadores válidos para ARG y WLD.

3. **🧼 Limpieza**
   - Conversión de JSON a DataFrame solo si `count > 0`.
   - Normalización de campos y homogeneización de estructuras.

4. **🛠️ Transformación**
   - Conversión de tipos de datos.
   - Enriquecimiento con nombres legibles (`indicator_label`, `category`, `description`).
   - Mapeo usando un diccionario externo para mayor claridad en BI.

5. **📦 Modelado**
   - Construcción de un **modelo dimensional**:
     - `d_time`: períodos (años).
     - `d_area`: país o región (`ARG` o `WLD`).
     - `d_indicadores`: metadatos enriquecidos del indicador.
     - `f_valores`: tabla de hechos con observaciones y foreign keys.

6. **☁️ Carga a BigQuery**
   - Uso de `pandas_gbq` y claves de servicio seguras desde `.env`.
   - Configuración para reemplazar la tabla automáticamente.

7. **📊 Visualización**
   - Dashboard creado en **Looker Studio**, conectado a BigQuery.
   - Comparación visual entre Argentina y datos globales.

---

## 📈 Dashboard final

👉 [Acceder al Dashboard en Looker Studio](https://lookerstudio.google.com/reporting/cf469ef4-9c26-4a88-aa4e-2aca2b534626)
(Versión conectada a BigQuery con tablas de hechos y dimensiones)

---

## 🛠️ Buenas prácticas implementadas

- Modularización por etapa (`extraction`, `cleaning`, `transformation`, `modeling`, `serving`).
- Uso de carpetas tipo `bronze`, `silver`, `gold` (inspirado en el modelo de medallones de Databricks).
- Uso de `.env` y `os.path` para portabilidad y seguridad.
- Diccionario de datos externo para desacoplar lógica y significado.
- Logs por etapa con estructura por carpetas.
- Funciones genéricas reutilizables para evitar duplicación.

---
