# 📊 Análisis de Indicadores para Dashboard de Conectividad en Argentina

## 🧩 Desafío del challenge

El objetivo de este proyecto es construir un dashboard en alguna herramienta de visualización de datos como **Tableau**, **Power BI** o **Looker**, que permita analizar de forma clara y efectiva la **evolución del acceso a Internet, el crecimiento del número de usuarios y suscriptores en Argentina**, así como explorar las posibles causas detrás de estos fenómenos.

El análisis deberá basarse en fuentes oficiales y actualizadas, principalmente provenientes del **Banco Mundial (Data360 API)**, y deberá responder preguntas clave como:

- ¿Qué porcentaje de la población argentina tiene acceso a Internet?
- ¿Con qué frecuencia lo utilizan?
- ¿Cómo ha evolucionado la infraestructura de conectividad?
- ¿Qué nivel de adopción tecnológica y habilidades digitales posee la población?
- ¿Existen correlaciones entre estos indicadores y el crecimiento del uso?

---

## 🎯 Estrategia general

Para abordar este desafío, se propone una selección curada de indicadores divididos por áreas temáticas. Esta organización facilitará la visualización, el análisis por dimensión y la construcción de narrativas en el dashboard.

---

## 📈 Indicadores de acceso y uso de Internet

Estos indicadores nos muestran el grado de penetración del Internet y la frecuencia de uso en los hogares argentinos. Son fundamentales para entender el nivel de conectividad en la vida cotidiana:

- **`ITU_DH_HH_INT`**: Hogares con acceso a Internet.
- **`ITU_DH_INT_USR_DAY`**: Porcentaje de personas que usan Internet diariamente.
- **`ITU_DH_INT_USR_WKL`**: Porcentaje de personas que usan Internet semanalmente.
- **`ITU_DH_INT_USR_MON`**: Porcentaje de personas que usan Internet mensualmente.

➡️ **¿Por qué incluirlos?**
Permiten segmentar el uso según frecuencia y evaluar cómo ha evolucionado el acceso al servicio en el tiempo.

---

## 📡 Indicadores de infraestructura y conectividad

Estos reflejan el estado y evolución de la infraestructura técnica que soporta la conectividad digital en el país:

- **`ITU_DH_INT_CONN_BAND_MBIT`**: Ancho de banda internacional total (Mbps).
- **`ITU_DH_INT_CONN_BAND_CAP`**: Capacidad total de conexión internacional (Gbps).
- **`ITU_DH_POP_COV_4G`**: Cobertura de red 4G.
- **`ITU_DH_POP_COV_5G`**: Cobertura de red 5G.

➡️ **¿Por qué incluirlos?**
Nos permiten ver si la infraestructura técnica acompaña el crecimiento del uso, y qué tan equitativamente está distribuida la conectividad avanzada en el país.

---

## 📱 Indicadores de adopción tecnológica

Estos indicadores representan el grado en que la población argentina ha incorporado dispositivos y servicios necesarios para conectarse:

- **`ITU_DH_HH_COMP`**: Porcentaje de hogares con computadora.
- **`ITU_DH_ACT_MOB_PER_100`**: Número de suscripciones móviles activas por cada 100 habitantes.
- **`ITU_DH_MOB_SUB_PER_100`**: Número total de suscripciones móviles por cada 100 habitantes.

➡️ **¿Por qué incluirlos?**
Ayudan a explicar las condiciones materiales necesarias para que la gente acceda y utilice Internet.

---

## 🧠 Indicadores de habilidades digitales

Estos datos permiten evaluar el nivel de alfabetización digital de la población, clave para entender el uso real y efectivo de la conectividad:

- **`ITU_DH_SKLS_SFTY`**: Habilidades de seguridad digital (gestión de contraseñas, protección contra malware, etc.).
- **`ITU_DH_SKLS_INF_DATA`**: Habilidades para manejar información y datos (búsqueda, filtrado, análisis).
- **`ITU_DH_SKLS_DIG_CONT`**: Habilidades para crear contenido digital (escritura en línea, edición multimedia).

➡️ **¿Por qué incluirlos?**
La inclusión digital no depende solo del acceso a la red, sino también de la capacidad de las personas para usarla de manera segura y productiva.

---

## 🧭 Conclusión

Esta selección de indicadores abarca las **cuatro dimensiones clave** que explican el estado actual del ecosistema digital en Argentina:

1. **Penetración y frecuencia de uso**
2. **Disponibilidad de infraestructura**
3. **Adopción de tecnologías**
4. **Capacidades digitales de la población**

Combinando estos datos será posible construir un dashboard sólido, comparativo y explicativo, que no solo muestre **qué está pasando** con la conectividad en Argentina, sino que también aporte pistas sobre **por qué** sucede.

---

---

## ❌ Indicadores descartados por falta de datos para Argentina

Durante la extracción de datos de la base `ITU_DH` para el país `ARG`, varios indicadores devolvieron un `count = 0` (es decir, no se encontraron registros disponibles). Estos indicadores fueron:

- `ITU_DH_ACT_MOB_PER_100`
- `ITU_DH_INT_CONN_BAND_CAP`
- `ITU_DH_INT_USR_DAY`
- `ITU_DH_INT_USR_WKL`
- `ITU_DH_INT_USR_MON`
- `ITU_DH_POP_COV_5G`
- `ITU_DH_SKLS_DIG_CONT`
- `ITU_DH_SKLS_INF_DATA`
- `ITU_DH_SKLS_SFTY`

Esto puede deberse a que el indicador **no tiene cobertura histórica para Argentina**, **requiere filtros específicos adicionales (edad, género, etc.)** o simplemente **no fue reportado** por la fuente para este país.

---

## ✅ Indicadores utilizados en el análisis

A partir de la validación previa, los siguientes indicadores **sí devolvieron datos válidos** (`count > 0`) y se utilizarán para el desarrollo del dashboard:

### 📶 Indicadores de acceso a Internet

- `ITU_DH_HH_INT`: **Hogares con acceso a Internet**
  Permite conocer el grado de conectividad de los hogares argentinos.

### 🌐 Indicadores de infraestructura de red

- `ITU_DH_INT_CONN_BAND_MBIT`: **Ancho de banda internacional (Mbps)**
  Evalúa la capacidad de infraestructura global de Internet disponible para el país.

- `ITU_DH_POP_COV_4G`: **Cobertura de red 4G**
  Mide el alcance poblacional de tecnologías móviles avanzadas.

### 💻 Indicadores de adopción tecnológica

- `ITU_DH_HH_COMP`: **Hogares con computadora**
  Evalúa la penetración de dispositivos necesarios para conectarse.

- `ITU_DH_MOB_SUB_PER_100`: **Suscripciones móviles por cada 100 habitantes**
  Mide el nivel de adopción de telefonía móvil en la población.

---

## 🧭 Conclusión y aplicación para el dashboard

Estos indicadores seleccionados permiten construir un dashboard que refleje:

- El **nivel de acceso** a Internet en Argentina (`HH_INT`)
- La **infraestructura técnica** disponible (`INT_CONN_BAND_MBIT`, `POP_COV_4G`)
- La **adopción tecnológica** en términos de dispositivos y conectividad (`HH_COMP`, `MOB_SUB_PER_100`)

Este conjunto de métricas es suficiente para analizar **cómo ha evolucionado el acceso a Internet**, qué **factores técnicos y materiales lo han permitido**, y cómo varió la **penetración tecnológica** en el tiempo.

Podemos complementar estos indicadores con variables sociodemográficas externas (por ejemplo, del INDEC), si deseamos enriquecer el análisis de causalidad o segmentación.
