# Práctico Excel: F1 Results Dataset

## Objetivo
Trabajar con datos reales de Fórmula 1 para aprender los conceptos fundamentales de Excel.

Este dataset ha sido extraído de Kaggle: https://www.kaggle.com/datasets/lakshayjain611/f1-races-results-dataset-1950-to-2024

Descripción del dataset:

> El conjunto de datos incluye un registro exhaustivo de los ganadores de las carreras de Fórmula 1, desde la temporada inaugural en 1950 hasta los últimos datos disponibles en 2024. Documenta meticulosamente a los pilotos triunfadores, sus respectivos equipos y los circuitos en los que se alzaron con la victoria, ofreciendo una rica perspectiva histórica sobre la evolución de este prestigioso deporte de motor. Esta extensa recopilación no solo sirve como testimonio de la habilidad y la determinación de los pilotos que han subido al podio a lo largo de las décadas, sino que también ofrece una valiosa visión de la dinámica competitiva y los avances tecnológicos que han dado forma a la narrativa de este deporte a lo largo de su ilustre historia. Ya sea para el análisis estadístico, la investigación histórica o la mera curiosidad de los aficionados, este conjunto de datos constituye un recurso definitivo para explorar la fascinante saga de las carreras de Fórmula 1.

## Ejercicios

### Ejercicio 1: Exploración de datos

1. Abre la hoja con los datos de F1 y examina las columnas
   - ¿Qué información ves? ¿Qué representa cada columna?
   
2. Mira la primera fila de datos
   - ¿De qué año es?
   - ¿Cuál fue la primera carrera?

3. Una pregunta importante: ¿Cuántos registros (filas) de carreras hay en total?
   - Busca una forma de calcularlo usando una función de Excel

4. Identifica coordenadas de celdas específicas:
   - Busca la celda que contiene el nombre del piloto Daniel Ricciardo en la temporada 2021
   - ¿Cuál es la coordenada de esa celda?
   - Ahora, ¿qué dato está en la celda D1601? ¿Qué representa?

---

### Ejercicio 2: Preguntas numéricas básicas

Responde estas preguntas usando cálculos en Excel

1. ¿Cuál es el promedio de puntos que un piloto obtiene por carrera?
   - Necesitas calcular el promedio de la columna `DriverPoints`

2. ¿Cuántos pilotos diferentes ganaron al menos una carrera?
   - Piensa: ¿Cómo sé si un piloto ganó? ¿Qué valor tendría en la columna `DriverPoints`?
   - Intenta contar valores únicos usando filtros primero, luego con una fórmula

3. ¿Cuál es el total de puntos de campeonato acumulados?
   - Mira la columna `TeamChampionshipPoints`

---

### Ejercicio 3: Filtrado y búsqueda de datos

1. Busca todas las carreras de Mónaco
   - Aplica un filtro automático a los datos
   - Filtra la columna `Grand Prix` solo para "Monaco"
   - ¿Cuántas carreras de Mónaco hay registradas?
   - ¿En qué años se corrieron?

2. ¿Cuántas veces ganó Max Verstappen en su país?
   - Necesitas buscar carreras en "Netherlands" (Países Bajos)
   - Donde el piloto sea Verstappen y haya ganado (DriverPoints > 0)
   - Pista: Usa múltiples filtros, uno en cada columna
   - Cuenta cuántas carreras coinciden

¿Cuál fue la carrera más reciente del dataset?
   - Ordena los datos por `Date` en orden descendente (más recientes primero)
   - ¿Cuál es el año y nombre del Gran Premio más reciente?

---

### Ejercicio 4: Análisis con cálculos avanzados

1. ¿Cuál es el tiempo promedio de la vuelta más rápida en Monza?
   - Primero, filtra todas las carreras del circuito de Monza (Grand Prix = "Italy")
   - Luego, observa la columna `FastestLapTime`
   - Calcula el promedio de esos tiempos
   - Desafío: ¿Puedes hacerlo con una fórmula única sin usar filtros?

2. ¿Cuántas carreras ganó Lewis Hamilton?
   - Pregunta extra: ¿En qué rango de años ganó Hamilton?

3. ¿Qué equipo acumuló más puntos en campeonato de todos los tiempos?
   - Busca el valor máximo en `TeamChampionshipPoints`
   - Ahora, ¿en qué fila está ese máximo?
   - ¿A qué equipo pertenece?

---

### Ejercicio 5: Crear resúmenes y tablas

1. Top 5: ¿Cuáles son los 5 pilotos con más puntos de todos los tiempos?
   - En una nueva área de tu hoja, crea dos columnas: `Piloto` y `Puntos Totales`
   - Necesitas calcular la suma de puntos para cada piloto
   - Identifica 5 pilotos con la mayor cantidad de puntos
   - Ordena tu tabla de mayor a menor puntos
   - Pregunta: ¿Reconoces algunos de estos nombres?

2. ¿Qué nacionalidad tiene más victorias?
   - Crea otra tabla: `Nacionalidad` y `Número de Victorias`
   - Cuenta cuántas carreras ganó cada nacionalidad
   - ¿Cuál es la más ganadora?
   - Bonus: ¿Puedes graficar esto?

3. Estadísticas por año
   - ¿Cuál fue el año con más carreras disputadas?
   - ¿Cuál fue el año con menos carreras?
   - ¿En qué años hubo cambios significativos?

---

### Ejercicio 6: Análisis comparativo

1. Elige dos pilotos que te interesen (pueden ser de épocas diferentes)
   - Ejemplos: Senna vs. Prost, Fangio vs. Ascari, Hamilton vs. Verstappen

2. Crea una tabla comparativa con la siguiente información:
   - Total de carreras que corrió cada uno
   - Total de victorias
   - Promedio de puntos por carrera
   - Año de su primera carrera
   - Año de su última carrera

3. Responde: ¿Quién tuvo mejor rendimiento? ¿Por qué?
   - No es solo el que ganó más, sino cómo fue tu análisis
   - Intenta justificar tu respuesta con números

---

## Reto (opcional)

### Investiga y crea tu propia pregunta

Elige una pregunta sobre F1 que TE INTERESE. Usando Excel, intenta responderla.

Algunos ejemplos:
- ¿Cuál es el circuito que ha producido más victorias de pilotos diferentes?
- ¿Qué equipo tiene el mejor promedio de puntos sin contar años recientes?
- ¿Hay algún patrón en cuándo ganan los pilotos (años, épocas)?
- ¿Cuál es el piloto más "consistente"? (que termina muchas carreras)

Importante: Documenta tu pregunta, tu proceso y tus conclusiones.

---

## Entregables:

- Documento con las respuestas.
- Hoja de Excel con las fórmulas aplicadas, tablas generadas, etc.


## Recursos útiles

### Funciones Excel que necesitarás:

| Función | ¿Para qué sirve? | Ejemplo |
|---------|-----------------|---------|
| `CONTAR()` | Cuenta cuántas celdas tienen datos | `=CONTAR(A1:A100)` |
| `SUMA()` | Suma todos los números en un rango | `=SUMA(B1:B100)` |
| `PROMEDIO()` | Calcula el promedio | `=PROMEDIO(B1:B100)` |
| `CONTAR.SI()` | Cuenta con una condición | `=CONTAR.SI(A1:A100,"Hamilton")` |
| `SUMAR.SI()` | Suma con una condición | `=SUMAR.SI(A1:A100,"Hamilton",B1:B100)` |
| `MAX()` | Encuentra el valor máximo | `=MAX(B1:B100)` |
| `MIN()` | Encuentra el valor mínimo | `=MIN(B1:B100)` |

---
