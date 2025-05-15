# 📊 Resolución del Challenge: Análisis del crecimiento de Internet en Argentina

## 🎯 Objetivo del Proyecto

Construir un **dashboard interactivo** en una herramienta de visualización (Tableau, Looker, Power BI, etc.) que permita **analizar la evolución, el crecimiento del acceso y uso de Internet en Argentina**, comparándolo con los valores globales (WLD), e identificando sus posibles causas o condicionantes.

---

## 🧠 Contexto técnico y desafíos del proyecto

Al comenzar el proyecto, uno de los principales desafíos fue la **falta de documentación clara y estructurada** por parte del Banco Mundial en relación a la nueva API de datos (`data360api.worldbank.org`). La documentación oficial es limitada, confusa y en muchos casos inconsistente, lo que exigió un proceso de prueba y error para entender:

- Cómo construir correctamente los endpoints.
- Qué indicadores estaban realmente disponibles para cada país.
- Cómo interpretar correctamente los valores y metadatos de los JSON retornados.
- Qué filtros eran obligatorios para ciertos indicadores.

Dado que esta API aún se encuentra en desarrollo y sin estandarización plena, se optó por **documentar todo el funcionamiento desde cero**, incluyendo:

- Diccionario de datos de cada indicador.
- Lista de indicadores válidos por país.
- Parámetros disponibles y obligatorios de la API.
- Estructura de respuesta y campos relevantes.

Este trabajo permitió construir una base sólida para avanzar en la extracción, limpieza y análisis de la información.

---

## 🧱 Estructura profesional y enfoque modular

Se trabajó bajo **buenas prácticas de ingeniería de datos**, creando una arquitectura clara y escalable del proyecto:

- **Organización de carpetas** por capas del pipeline (`/data`, `/logic`, `/notebooks`, etc.).
- **Modularización del código** para separar funciones de extracción, transformación, modelado y análisis.
- Creación de **clases reutilizables** para consumir la API y convertir los datos en DataFrames.
- Implementación de **logs automáticos** por indicador y por proceso.
- Estructura compatible con orquestadores ETL futuros (Airflow, Prefect, etc.) mediante scripts ejecutables desde `main.py`.

Este enfoque garantiza escalabilidad, mantenimiento sencillo y facilidad para automatizar los procesos de extracción y transformación.

---


---

## 🧩 Paso 1: Análisis exploratorio de los datos disponibles

Antes de comenzar con el desarrollo del dashboard, el primer paso fue **verificar la disponibilidad de datos concretos para Argentina** a través de la API del Banco Mundial (`ITU_DH`), que contiene decenas de indicadores relacionados con conectividad, infraestructura digital, adopción tecnológica y habilidades digitales.

Tras realizar una extracción automática de los datos para `REF_AREA = ARG`, se filtraron únicamente aquellos indicadores cuyo JSON incluía datos reales (`"count" > 0`). Luego, se descargaron los mismos indicadores pero con `REF_AREA = WLD` para poder contar con un punto de comparación a nivel global.

---

## ✅ Lista de Indicadores Válidos para Argentina

Los siguientes indicadores fueron validados como disponibles y relevantes para Argentina. Estos mismos también están disponibles para `WLD`, por lo que se podrán comparar:

### 📶 Acceso y penetración de Internet

- `ITU_DH_HH_INT`: Porcentaje de hogares con acceso a Internet.
- `ITU_DH_HH_COMP`: Porcentaje de hogares con computadora.
- `ITU_DH_FIX_TEL_OR_MOB`: Penetración de telefonía fija o móvil por cada 100 hab.

### 🌐 Infraestructura y conectividad

- `ITU_DH_INT_CONN_BAND_MBIT`: Ancho de banda internacional total (Mbps).
- `ITU_DH_INT_CONN_BAND`: Capacidad total de conectividad internacional.
- `ITU_DH_INT_BAND_PER_CAP`: Ancho de banda internacional por habitante.
- `ITU_DH_INT_BAND_PER_INT_USR`: Ancho de banda por usuario de Internet.
- `ITU_DH_POP_COV_2G`: Cobertura de red móvil 2G.
- `ITU_DH_POP_COV_3G`: Cobertura de red móvil 3G.
- `ITU_DH_POP_COV_4G`: Cobertura de red móvil 4G.
- `ITU_DH_PRI_FIX_BB_5G`: Suscripciones de banda ancha fija con tecnología 5G.
- `ITU_DH_FIX_SUB_PER_100`: Suscripciones de líneas fijas por cada 100 hab.
- `ITU_DH_FIX_BR_SUB_PER_100`: Suscripciones de banda ancha fija por cada 100 hab.

### 📱 Uso de tecnologías móviles

- `ITU_DH_MOB_SUB_PER_100`: Total de suscripciones móviles por cada 100 hab.
- `ITU_DH_TRAF_MOB_BB`: Tráfico de banda ancha móvil.
- `ITU_DH_PRI_LU_MOB`: Uso privado de dispositivos móviles.
- `ITU_DH_PRI_DO_MOB`: Uso doméstico de dispositivos móviles.

### 📡 Conectividad digital avanzada

- `ITU_DH_COMP_INT_GTW`: Computadoras con conexión a internet vía gateway.
- `ITU_DH_COMP_INT_SER`: Computadoras con servicios de internet.
- `ITU_DH_INT_USER_PT`: Porcentaje de usuarios de Internet.

### 💻 Otras variables relevantes

- `ITU_DH_INV_COMP`: Inversión en computadoras.
- `ITU_DH_PRI_HU_VD`: Uso privado de videollamadas.

---

## 🔍 Paso 2: Criterios de selección y estrategia de análisis

### ¿Por qué estos indicadores?

1. **Evidencia directa del acceso y uso de Internet**: Se priorizaron indicadores que reflejan directamente el acceso a Internet (`HH_INT`, `INT_USER_PT`, `MOB_SUB_PER_100`, etc.).
2. **Infraestructura subyacente**: Indicadores como el ancho de banda internacional o la cobertura 3G/4G permiten interpretar si la infraestructura disponible acompaña el crecimiento del uso.
3. **Tecnología disponible**: El acceso a computadoras, suscripciones de banda ancha fija y móvil indican el nivel de adopción de herramientas que posibilitan la conectividad.
4. **Comparabilidad global**: Todos los indicadores seleccionados cuentan con datos tanto para Argentina como para el total mundial (WLD), lo que permitirá obtener **insights comparativos**.

---

## 🧼 Paso 3: Limpieza y transformación de los datos

Una vez convertidos los JSON en DataFrames, se procederá con las siguientes acciones de limpieza:

### 🧽 Limpieza general por cada archivo:

- Convertir las columnas `OBS_VALUE` a numéricas.
- Filtrar solo las columnas relevantes:
  - `INDICATOR`, `REF_AREA`, `TIME_PERIOD`, `OBS_VALUE`, `UNIT_MEASURE`
- Eliminar duplicados y valores nulos.
- Estandarizar el tipo de dato de `TIME_PERIOD` como entero (año).

### 🧾 Columnas clave a mantener

| Columna         | Descripción                              |
|------------------|-------------------------------------------|
| `INDICATOR`      | Identificador del indicador               |
| `REF_AREA`       | Región geográfica (`ARG`, `WLD`)          |
| `TIME_PERIOD`    | Año del dato                              |
| `OBS_VALUE`      | Valor observado del indicador             |
| `UNIT_MEASURE`   | Unidad de medida (porcentaje, por 100 hab, etc.) |

---

## 🔗 Paso 4: Unificación de DataFrames

Se unificarán todos los DataFrames individuales en un solo **DF maestro (`df_all`)** que contenga todos los indicadores con las columnas clave mencionadas anteriormente.

Además, se generará una columna adicional `indicator_readable` que permite mapear el código técnico (`ITU_DH_*`) a un nombre legible para usar en el dashboard.

También se podrá generar una columna `indicador_categoria` con valores como:

- `"Acceso y uso de Internet"`
- `"Infraestructura"`
- `"Móviles"`
- `"Inversión tecnológica"`

Esto permitirá luego segmentar los análisis por categoría.

---

## 📈 Paso 5: Métricas y visualizaciones sugeridas

### 🔹 Evolución temporal

- Evolución del porcentaje de hogares con Internet vs. WLD.
- Tendencia de suscripciones móviles por cada 100 hab.
- Evolución de la cobertura de redes móviles 3G/4G.

### 🔹 Comparación regional

- Comparativa ARG vs. WLD para indicadores clave:
  - `HH_INT`
  - `INT_USER_PT`
  - `POP_COV_4G`
  - `INT_CONN_BAND_MBIT`

### 🔹 Relación causal

- Relación entre `INV_COMP` e indicadores de uso.
- Análisis de correlación entre ancho de banda per cápita y porcentaje de usuarios.

---

## 🧪 Paso 6: Exportación a capa Silver y análisis final

Una vez finalizado el procesamiento, los DataFrames limpios se guardarán como archivos `.parquet` en la carpeta `/data/o2_silver`.

Los archivos se nombrarán con el patrón:
`indicador_{nombre}.parquet`
Por ejemplo: `indicador_HH_INT.parquet`

---

---

## 🏁 Paso 7: Unificación de datos y creación de capa Gold

Una vez limpios todos los indicadores y transformados los DataFrames individuales, se procederá a:

1. **Unificar todos los datos en un solo DataFrame maestro (`df_maestro`)**, que contenga:
   - Año (`TIME_PERIOD`)
   - Indicador (`INDICATOR`)
   - Región (`REF_AREA`)
   - Valor (`OBS_VALUE`)
   - Unidad de medida (`UNIT_MEASURE`)
   - Códigos adicionales si son necesarios (por ejemplo: `FREQ`, `AGE`, etc.)

2. **Normalizar los nombres** y mapear los códigos técnicos a nombres legibles para facilitar su interpretación en el dashboard.

3. **Guardar el `df_maestro` como archivo `.parquet` en la carpeta `/data/o3_gold`**, listo para su uso final.

---

## ☁️ Paso 8: Subida a Google BigQuery

Con el DataFrame finalizado en la **capa Gold**, se cargará a **Google BigQuery**, lo que permitirá:

- Conectar Tableau u otra herramienta directamente a la tabla.
- Usar SQL sobre el dataset para análisis avanzados.
- Crear métricas dinámicas y visualizaciones interactivas de forma eficiente.

Este flujo completo garantiza que el pipeline de datos pase por todas las etapas del proceso **ETL (Extracción, Transformación, Carga)** siguiendo las mejores prácticas de ingeniería y analítica de datos.

---


## 📌 Conclusión

Este enfoque garantiza que:

- Solo se trabaja con datos disponibles y validados.
- Se estructura la información de forma clara y comparable.
- Se mantienen las buenas prácticas en la limpieza y transformación de datos.
- Se prepara la información de forma eficiente para su visualización en herramientas como Tableau.

El resultado será un dashboard robusto, preciso y contextualizado sobre el crecimiento digital en Argentina, con posibilidad de benchmark global.



---

# 📌 Posdata: Decisiones prácticas por limitaciones de tiempo

Es importante aclarar que, por cuestiones de tiempo y foco en la entrega del desafío, se tomaron algunas decisiones prácticas que podrían ampliarse en una instancia futura de desarrollo más colaborativo y profunda. Entre las tareas que **no se realizaron**, pero que serían altamente recomendables para una versión productiva o para escalar el análisis, se encuentran:

- Conectar y enriquecer los datos con **otras fuentes complementarias**, como:
  - Datos del **ENACOM (Ente Nacional de Comunicaciones)**.
  - Datos del **Censo Nacional de Argentina** (INDEC).
  - Fuentes privadas o académicas sobre penetración de tecnologías.

- Crear un **modelo dimensional robusto** con sus correspondientes:
  - **Tablas de dimensiones** (`dim_indicator`, `dim_region`, `dim_tiempo`, etc.).
  - **Tabla de hechos** que concentre las mediciones (`fact_internet_metricas`).
  - Relaciones formales para explotar correctamente la información en herramientas como Tableau o Power BI.

- Subir **cada DataFrame como tabla individual** en BigQuery, lo cual facilitaría aún más la modularidad, el versionado y el control de calidad de cada métrica de forma independiente.

- Aplicar técnicas avanzadas de análisis o modelado, como:
  - Series temporales.
  - Segmentaciones por tipo de conectividad o cobertura.
  - Modelos predictivos sobre evolución del acceso o brechas digitales.

---

### 🎯 En resumen

El objetivo principal era demostrar **criterio técnico, buenas prácticas de ingeniería de datos y capacidad de análisis profesional**, más allá de la cantidad de métricas modeladas. Este proyecto está completamente preparado para escalar, integrarse a flujos productivos y formar parte de un equipo donde las tareas puedan dividirse y ejecutarse de forma colaborativa.

Estoy listo para sumarme a un equipo de trabajo donde el aporte técnico y estratégico se traduzca en impacto real a través de los datos.

---
