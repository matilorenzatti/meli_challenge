


# 📊 Guía de Consumo de Datos: API Data360 del Banco Mundial

## 📌 Objetivo del documento

Este archivo tiene como finalidad documentar de forma clara y ordenada el uso de las fuentes de datos que alimentan el análisis realizado en este proyecto. Se explican los endpoints utilizados de la **API pública Data360** del Banco Mundial, así como el **diccionario de datos asociado**, para que cualquier persona que trabaje con el código pueda entender qué datos se utilizan, cómo se obtienen, qué representa cada campo y cómo interpretarlos correctamente.

---

## 🌐 Fuente de los datos

Los datos utilizados en este análisis provienen de la plataforma [Data360 del Banco Mundial](https://data360.worldbank.org), una iniciativa enfocada en indicadores de transformación digital, conectividad, infraestructura tecnológica y desarrollo digital a nivel global.

- API base: `https://data360api.worldbank.org/v1/`
- Documentación técnica (OpenAPI): `https://raw.githubusercontent.com/worldbank/open-api-specs/refs/heads/main/Data360%20Open_API.json`

---

## 🌐 Guía para consumir la API de Data360 (Banco Mundial)

La API pública de Data360 permite acceder a conjuntos de datos e indicadores oficiales sobre conectividad, adopción digital, telecomunicaciones y desarrollo tecnológico a nivel mundial. Esta guía detalla cómo utilizar el endpoint principal y qué parámetros están disponibles para filtrar la información.

---

### 🔗 Endpoint principal

GET `https://data360api.worldbank.org/data360/data`


Este endpoint devuelve datos estructurados en base a filtros definidos en la consulta. Es posible recuperar información para uno o varios indicadores dentro de una base de datos específica.

---

### 📌 Parámetros disponibles

| Nombre del Parámetro       | Tipo     | Requerido | Descripción                                                                                      | Ejemplo                         |
|----------------------------|----------|-----------|--------------------------------------------------------------------------------------------------|----------------------------------|
| `DATABASE_ID`              | string   | ✅ Sí      | Identificador de la base de datos. Para TIC usar: `ITU_DH`.                                      | `ITU_DH`                         |
| `INDICATOR`                | string   | Opcional  | Código del indicador a consultar (uno o más).                                                    | `ITU_DH_MOB_SUB_PER_100`         |
| `REF_AREA`                 | string   | Opcional  | Código del país o región (ISO 3 letras).                                                         | `ARG`                            |
| `SEX`                      | string   | Opcional  | Género (si aplica). Valores típicos: `T` = total, `M` = masculino, `F` = femenino.               | `T`                              |
| `AGE`                      | string   | Opcional  | Rango de edad si el indicador lo contempla.                                                      | `Y15-24`                         |
| `URBANISATION`             | string   | Opcional  | Nivel de urbanización (`U` = urbano, `R` = rural, `T` = total).                                  | `U`                              |
| `COMP_BREAKDOWN_1/2/3`     | string   | Opcional  | Subdimensiones del indicador (proveedor, tecnología, etc.).                                      | `FTTH`, `LTE`                    |
| `TIME_PERIOD`              | string   | Opcional  | Periodo de tiempo puntual (formato flexible).                                                    | `2022`, `2023-Q1`                |
| `timePeriodFrom`           | string   | Opcional  | Fecha de inicio del rango de tiempo.                                                             | `2015`                           |
| `timePeriodTo`             | string   | Opcional  | Fecha de fin del rango de tiempo.                                                                | `2023`                           |
| `FREQ`                     | string   | Opcional  | Frecuencia de la medición. Valores comunes: `A` (anual), `Q` (trimestral).                       | `A`                              |
| `UNIT_MEASURE`             | string   | Opcional  | Unidad de medida. Ej: `ABS` (valor absoluto), `PC` (porcentaje).                                 | `PC`                             |
| `UNIT_TYPE`                | string   | Opcional  | Tipo de unidad (`percentage`, `absolute`, etc.).                                                 | `percentage`                     |
| `UNIT_MULT`                | string   | Opcional  | Multiplicador para la unidad. Por ejemplo `3` = multiplicar por `10^3`.                          | `3`                              |
| `skip`                     | integer  | Opcional  | Cuántos registros omitir. Sirve para paginación de resultados (máximo 1000 por llamada).         | `0`, `1000`, `2000`              |

---

### ✅ Parámetros obligatorios mínimos

Para obtener resultados válidos, deberás incluir al menos:

```bash
DATABASE_ID=ITU_DH
```


---
---

## 📥 Indicadores disponibles para usar con la Base de datos de indicadores de las TIC

| Código del Indicador           | Nombre Legible                                           | Descripción Ampliada                                                                                     |
|-------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ITU_DH_INT_CONN_BAND_MBIT     | Ancho de banda internacional (Mbps)                      | Capacidad total de ancho de banda internacional de Internet en Mbps, indicando la infraestructura disponible para la conectividad internacional. |
| ITU_DH_SKLS_SFTY              | Habilidades de seguridad digital                         | Porcentaje de personas con habilidades básicas en seguridad digital, como la gestión de contraseñas y la protección contra malware. |
| ITU_DH_HH_COMP                | Hogares con computadora                                  | Porcentaje de hogares que poseen una computadora, incluyendo desktops, laptops o tablets. |
| ITU_DH_PRI_LU_MOB             | Uso privado de dispositivos móviles                      | Porcentaje de individuos que utilizan dispositivos móviles para uso privado, reflejando la adopción de tecnología móvil. |
| ITU_DH_POP_COV_5G             | Cobertura de red 5G                                      | Porcentaje de la población cubierta por una red móvil 5G, indicando la disponibilidad de tecnología de última generación. |
| ITU_DH_INT_CONN_BAND_CAP      | Capacidad de conexión internacional                      | Capacidad total de conexión internacional de Internet en Gbps, mostrando la infraestructura de conectividad global. |
| ITU_DH_POP_COV_3G             | Cobertura de red 3G                                      | Porcentaje de la población cubierta por una red móvil 3G, reflejando la penetración de tecnologías móviles intermedias. |
| ITU_DH_ACT_MOB_PER_100        | Suscripciones móviles activas por cada 100 habitantes    | Número de suscripciones móviles activas por cada 100 personas, indicando la penetración del servicio móvil. |
| ITU_DH_INV_COMP               | Inversión en computadoras                                | Inversión total en computadoras como porcentaje del PIB, mostrando el compromiso económico con la tecnología. |
| ITU_DH_HH_RAD                 | Hogares con radio                                        | Porcentaje de hogares que poseen una radio, reflejando el acceso a medios de comunicación tradicionales. |
| ITU_DH_PRI_HU_VD              | Uso privado de videollamadas                             | Porcentaje de individuos que utilizan videollamadas para uso privado, indicando la adopción de herramientas de comunicación digital. |
| ITU_DH_POP_COV_2G             | Cobertura de red 2G                                      | Porcentaje de la población cubierta por una red móvil 2G, mostrando la disponibilidad de tecnologías móviles básicas. |
| ITU_DH_SKLS_INF_DATA          | Habilidades en manejo de información y datos             | Porcentaje de personas con habilidades para manejar información y datos digitales, como la búsqueda y evaluación de información en línea. |
| ITU_DH_INT_CONN_BAND          | Ancho de banda internacional total                       | Capacidad total de ancho de banda internacional de Internet en Gbps, indicando la infraestructura disponible para la conectividad global. |
| ITU_DH_COMP_MOB_BB            | Computadoras con banda ancha móvil                       | Porcentaje de computadoras conectadas a banda ancha móvil, reflejando la movilidad en el acceso a Internet. |
| ITU_DH_FIX_TEL_OR_MOB         | Teléfonos fijos o móviles                                | Porcentaje de hogares con acceso a teléfono fijo o móvil, indicando la disponibilidad de servicios de comunicación básicos. |
| ITU_DH_HH_TV                  | Hogares con televisión                                   | Porcentaje de hogares que poseen una televisión, reflejando el acceso a medios de entretenimiento e información. |
| ITU_DH_PRI_FIX_BB_5G          | Uso privado de banda ancha fija 5G                       | Porcentaje de individuos que utilizan banda ancha fija 5G para uso privado, mostrando la adopción de tecnologías de alta velocidad. |
| ITU_DH_FIX_BR_SUB_PER_100     | Suscripciones de banda ancha fija por cada 100 habitantes| Número de suscripciones de banda ancha fija por cada 100 personas, indicando la penetración del servicio de Internet fijo. |
| ITU_DH_SKLS_DIG_CONT          | Habilidades en creación de contenido digital             | Porcentaje de personas con habilidades para crear contenido digital, como blogs, videos o publicaciones en redes sociales. |
| ITU_DH_INT_USR_WKL            | Usuarios de Internet semanales                           | Porcentaje de individuos que utilizan Internet al menos una vez por semana, reflejando la frecuencia de uso. |
| ITU_DH_COMP_INT_GTW           | Computadoras conectadas a la red                         | Porcentaje de computadoras conectadas a la red de Internet, indicando la disponibilidad de acceso en dispositivos. |
| ITU_DH_PRI_LU_VD              | Uso privado de video bajo demanda                        | Porcentaje de individuos que utilizan servicios de video bajo demanda para uso privado, mostrando la adopción de plataformas de streaming. |
| ITU_DH_SKLS_COMN_COLAB        | Habilidades de comunicación y colaboración digital       | Porcentaje de personas con habilidades para comunicarse y colaborar en entornos digitales, como el uso de correo electrónico y herramientas colaborativas. |
| ITU_DH_HH_INT                 | Hogares con acceso a Internet                            | Porcentaje de hogares que tienen acceso a Internet, reflejando la penetración del servicio en el ámbito doméstico. |
| ITU_DH_INT_BAND_PER_INT_USR   | Ancho de banda por usuario de Internet                   | Promedio de ancho de banda internacional disponible por usuario de Internet, indicando la calidad del servicio. |
| ITU_DH_COMP_FIB               | Computadoras con conexión de fibra óptica                | Porcentaje de computadoras conectadas a través de fibra óptica, mostrando la adopción de tecnologías de alta velocidad. |
| ITU_DH_INT_BAND_PER_CAP       | Ancho de banda per cápita                                | Promedio de ancho de banda internacional disponible por persona, reflejando la capacidad de la infraestructura en relación con la población. |
| ITU_DH_INT_USR_DAY            | Usuarios diarios de Internet                             | Porcentaje de individuos que utilizan Internet diariamente, indicando la intensidad de uso. |
| ITU_DH_MOB_SUB_PER_100        | Suscripciones móviles por cada 100 habitantes            | Número de suscripciones móviles por cada 100 personas, mostrando la penetración del servicio móvil. |
| ITU_DH_COMP_INT_SER           | Computadoras con servicios de Internet                   | Porcentaje de computadoras que utilizan servicios de Internet, reflejando la funcionalidad y uso de los dispositivos. |
| ITU_DH_SKLS_PRB_SOLV          | Habilidades para resolver problemas en entornos digitales| Porcentaje de personas con habilidades para resolver problemas en entornos digitales, como la solución de errores o la configuración de dispositivos. |
| ITU_DH_TRAF_FIX_BB            | Tráfico de banda ancha fija                              | Volumen total de tráfico de banda ancha fija en GB, indicando el uso de servicios de Internet fijo. |
| ITU_DH_TRAF_MOB_BB            | Tráfico de banda ancha móvil                             | Volumen total de tráfico de banda ancha móvil en GB, mostrando el uso de servicios de Internet móvil. |
| ITU_DH_PRI_DO_MOB             | Uso privado de descarga móvil                            | Porcentaje de individuos que descargan contenido a través de dispositivos móviles para uso privado, reflejando la adopción de servicios móviles. |
| ITU_DH_INT_USR_MON            | Usuarios mensuales de Internet                           | Porcentaje de individuos que utilizan Internet al menos una vez al mes, indicando la frecuencia de uso. |
| ITU_DH_POP_COV_4G             | Cobertura de red 4G                                      | Porcentaje de la población cubierta por una red móvil 4G, mostrando la disponibilidad de tecnologías móviles avanzadas. |
| ITU_DH_INT_USER_PT            | Usuarios de Internet por tipo de dispositivo             | Distribución porcentual de usuarios de Internet según el tipo de dispositivo utilizado, como computadoras, tablets o smartphones. |
| ITU_DH_FIX_SUB_PER_100        | Suscripciones de telefonía fija por cada 100 habitantes  | Número de suscripciones de telefonía fija por cada 100 personas, indicando la penetración del servicio de telefonía fija. |


---


### 🧠 Consejos prácticos para utilizar la API correctamente

- ✅ **Consultá múltiples indicadores**: Podés hacer consultas más completas combinando distintos indicadores en una sola llamada a la API. Esto te permitirá comparar métricas relacionadas y optimizar tus visualizaciones.

- 🌍 **Filtrá por país**: Usá el parámetro `REF_AREA=ARG` para limitar los resultados exclusivamente a Argentina (código ISO3). Si querés comparar entre países, podés omitir ese filtro o cambiarlo según el país deseado (Ej: `BRA`, `CHL`, etc.).

- 📅 **Aplicá filtros de tiempo**: Para analizar la evolución de un indicador, utilizá `timePeriodFrom` y `timePeriodTo` para definir el rango temporal. Por ejemplo, podés consultar desde 2010 hasta 2023 con:
  `timePeriodFrom=2010&timePeriodTo=2023`.

- ❗️ **Tené en cuenta filtros específicos por indicador**: Algunos indicadores requieren parámetros adicionales como sexo (`SEX`), edad (`AGE`) o nivel de urbanización (`URBANISATION`). Si no recibís datos, es posible que falte uno de estos filtros clave.

- 📊 **Validá los códigos**: Los valores de los filtros deben estar escritos en el formato exacto esperado (por ejemplo, `T` para total, `M` para masculino, `F` para femenino, etc.). Consultá el diccionario de datos para entender los valores válidos.

- 🔄 **Paginación**: Si tu consulta devuelve más de 1000 registros, usá el parámetro `skip` para paginar los resultados (`skip=0`, `skip=1000`, etc.).

Con estos tips vas a poder evitar errores comunes y aprovechar al máximo el potencial de esta API para tus análisis y dashboards.




---

## 📖 Diccionario de datos · API Data360 del Banco Mundial

Este documento detalla el significado de los campos disponibles al consultar la API pública de indicadores del Banco Mundial a través de su Data360. El objetivo es facilitar la comprensión del contenido, estructura y metadatos para su uso en análisis exploratorios o visualizaciones.

---

## 📌 Campos principales del diccionario de datos

Estos son los campos esenciales para interpretar correctamente los registros devueltos por la API de Data360 del Banco Mundial:

| Campo                     | Traducción                         | Significado técnico / Cómo interpretarlo                                                               |
|---------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------|
| `FREQ`                    | Frecuencia                         | Código de la frecuencia de los datos: anual, trimestral, etc. Ej: `"A"` para "Anual".                  |
| `FREQ_LABEL`              | Frecuencia (Nombre)                | Nombre legible de la frecuencia. Ej: `"Annual"` o `"Monthly"`.                                         |
| `REF_AREA`                | Área de referencia                 | Código ISO3 del país o región a la que se refiere el dato. Ej: `"ARG"` para Argentina.                 |
| `REF_AREA_LABEL`          | Área de referencia (Nombre)        | Nombre del país o región, como `"Argentina"`, `"Brasil"`, etc.                                         |
| `INDICATOR`               | Indicador estadístico              | Código interno del indicador. Ej: `IT_NET_USER_ZS` (Usuarios de internet por cada 100 personas).       |
| `INDICATOR_LABEL`         | Indicador (Nombre)                 | Nombre legible del indicador estadístico.                                                              |
| `SEX`                     | Sexo                               | Código del sexo (si aplica). Ej: `"T"` = total, `"M"` = masculino, `"F"` = femenino.                   |
| `SEX_LABEL`               | Sexo (Nombre)                      | Nombre legible del sexo.                                                                               |
| `AGE`                     | Edad                               | Código o categoría de edad (si aplica). Ej: `"Y15-24"` = entre 15 y 24 años.                           |
| `AGE_LABEL`               | Edad (Nombre)                      | Nombre legible de la categoría de edad.                                                                |
| `URBANISATION`            | Urbanización                       | Categoría que indica si el dato es rural, urbano o total. Ej: `"U"` = urbano.                          |
| `URBANISATION_LABEL`      | Urbanización (Nombre)              | Texto descriptivo del nivel de urbanización: `"Urban"`, `"Rural"`, `"Total"`.                          |
| `UNIT_MEASURE`            | Unidad de medida                   | Código de la unidad. Ej: `"PC"` = porcentaje, `"ABS"` = valor absoluto.                                |
| `UNIT_MEASURE_LABEL`      | Unidad de medida (Nombre)          | Texto legible de la unidad de medida, como `"Porcentaje"` o `"Número absoluto"`.                       |
| `COMP_BREAKDOWN_1`        | Dimensión personalizada 1          | Variable adicional (como región, tecnología, proveedor, etc.). Puede estar vacía si no aplica.         |
| `COMP_BREAKDOWN_1_LABEL`  | Dimensión personalizada 1 (Nombre) | Nombre descriptivo de esa dimensión si aplica.                                                         |
| `COMP_BREAKDOWN_2`        | Dimensión personalizada 2          | Idem anterior pero segunda dimensión.                                                                  |
| `COMP_BREAKDOWN_2_LABEL`  | Dimensión personalizada 2 (Nombre) | Nombre descriptivo si aplica.                                                                          |
| `COMP_BREAKDOWN_3`        | Dimensión personalizada 3          | Idem anterior pero tercera dimensión.                                                                  |
| `COMP_BREAKDOWN_3_LABEL`  | Dimensión personalizada 3 (Nombre) | Nombre descriptivo si aplica.                                                                          |


## 📊 Campos adicionales del diccionario de datos

| Campo               | Traducción                          | Significado técnico / Cómo interpretarlo                                                                  |
|---------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| `TIME_PERIOD`       | Período de tiempo                    | Año, mes o fecha específica a la que corresponde la observación. Ej: `2022`, `2023-Q1`.                  |
| `OBS_VALUE`         | Valor observado                      | Valor numérico de la observación. Ej: `87.6` (puede ser % o cantidad según unidad).                      |
| `AGG_METHOD`        | Método de agregación (código)        | Código del método usado para agregar datos. Ej: media, suma, etc. Puede venir vacío si no aplica.        |
| `AGG_METHOD_LABEL`  | Método de agregación (nombre)        | Nombre descriptivo del método de agregación.                                                             |
| `DECIMALS`          | Decimales                            | Número de dígitos a la derecha del punto decimal. Ej: `2` implica valores como `10.25`.                  |
| `DECIMALS_LABEL`    | Decimales (texto)                    | Repite el significado anterior, pero en forma más legible.                                               |
| `DATABASE_ID`       | ID de base de datos                  | Código de la base de datos original. Ej: `ITU`, `WB`, etc.                                               |
| `DATABASE_ID_LABEL` | Nombre base de datos                 | Nombre completo de la base de datos fuente. Ej: “World Bank Open Data”, “ITU Dataset”.                   |
| `COMMENT_TS`        | Comentario de la serie               | Descripción técnica de la serie o comentario adicional. Útil para entender contexto o cobertura.         |
| `UNIT_MULT`         | Multiplicador de unidad (número)     | Exponente en base 10 que indica por cuánto multiplicar el número. Ej: `3` = multiplicar por `10^3`.      |
| `UNIT_MULT_LABEL`   | Multiplicador de unidad (texto)      | Texto legible para `UNIT_MULT`. Ej: `Mil`, `Millón`.                                                     |
| `DATA_SOURCE`       | Fuente de datos (código)             | Código interno del proveedor o repositorio de datos.                                                     |
| `DATA_SOURCE_LABEL` | Fuente de datos (nombre)             | Nombre completo de la fuente que originó el dato. Ej: ITU, World Bank, etc.                              |
| `UNIT_TYPE`         | Tipo base de unidad (código)         | Código que describe si es un porcentaje, número absoluto, etc.                                           |
| `UNIT_TYPE_LABEL`   | Tipo base de unidad (texto)          | Nombre legible del tipo de unidad. Ej: "Porcentaje", "Cantidad", "Índice".                               |
| `TIME_FORMAT`       | Formato de tiempo (código)           | Código técnico del formato temporal. Ej: `"P1Y"` = cada año, `"P1M"` = cada mes.                         |
| `TIME_FORMAT_LABEL` | Formato de tiempo (nombre)           | Explicación del código anterior en texto plano.                                                          |
| `COMMENT_OBS`       | Comentario sobre la observación      | Información adicional sobre el valor observado. Ej: notas sobre si es estimación, proyección, etc.       |
| `OBS_STATUS`        | Estado de la observación (código)    | Código sobre la calidad del dato. Ej: si es estimado, provisional, revisado, etc.                        |
| `OBS_STATUS_LABEL`  | Estado de la observación (texto)     | Explicación legible del estado anterior. Ej: `"Preliminar"`, `"Definitivo"`, `"Estimado"`.               |
| `OBS_CONF`          | Confidencialidad (código)            | Código sobre la confidencialidad o sensibilidad del dato.                                                |
| `OBS_CONF_LABEL`    | Confidencialidad (texto)             | Descripción del nivel de confidencialidad de la observación. Ej: `"Público"`, `"Restringido"`.           |
