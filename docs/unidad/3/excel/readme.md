status: DRAFT
responsable: @rafafil
ultima_actualizacion: 2026-04-13
 

## Excel y plantillas electrónicas

Son un tipo de software que tienen como objetivo permitir la administración y manipulación de datos de distinto tipo ubicados en tablas con filas y columnas.

#### Componentes:

CELDA: Es la unidad básica de información dentro de una plantilla electrónica. Puede contener datos (texto, números, fechas) o fórmulas.

FILAS: Son las divisiones horizontales de la plantilla. Se identifican mediante números (1, 2, 3, ...).

COLUMNAS: Son las divisiones verticales de la plantilla. Se identifican mediante letras (A, B, C, ...).

La intersección entre una fila y una columna nos da una celda. La combinación entre el identificador de la fila y la columna nos da el identificador de la celda. Ejemplo: columna A y fila 1, se obtiene la celda con identificador A1. (Conocer el identificador de la celda será necesario para luego referirnos a la misma al momento de realizar distintas operaciones).

Si bien esta es la forma por defecto de establecer el identificador de una celda, también es posible darle un "alias" a la celda, establecido por el usuario.


### Ejemplos en el mercado:

- Excel (Microsoft)
- Calc (Apache Open Office)
- Numbers (Apple)
- Google Spreadsheets (Google)



## Limpieza de datos

:: TODO

## Fórmulas y Funciones

### Fórmula:

Una fórmula es una expresión que el programa evalúa para obtener un resultado. Siempre comienza con el signo igual (`=`) y puede incluir valores, referencias de celdas, operadores y funciones.

Ejemplo:

- `=6+7`

### Funciones:

Una función es una fórmula predefinida que realiza un cálculo específico utilizando uno o más argumentos.

Ejemplo:

-`SUMA(6;7)`


### Fórmulas y Funciones:

Es importante destacar que para que una función retorne un resultado y este se muestre en la celda es necesario invocarla dentro de una fórmula, como se ve en el ejemplo:

Ejemplo:

-`=SUMA(6;7)` (En donde = indica que la expresión es una fórmula y dentro de la fórmula se invoca la función SUMA con los parámetros 6 y 7)


## Tablas

Es una forma de facilitar la administración y el análisis de un grupo de datos relacionados.

### Componentes

Una tabla puede incluir los siguientes elementos:

- Fila de encabezado: fila superior que contiene los nombres de las columnas y permite ordenar y filtrar los datos.
- Filas con bandas: formato visual de filas alternadas que mejora la lectura de los datos.
- Columnas calculadas: columnas donde una fórmula se aplica automáticamente a todas sus celdas.
- Fila de totales: fila opcional que permite calcular totales o resúmenes (suma, promedio, etc.) de forma automática.
- Controlador de tamaño: esquina de la tabla que permite cambiar su tamaño arrastrándola.

### Operaciones comunes:

- Ordenar datos (de menor a mayor, alfabéticamente, etc.)
- Filtrar información según criterios
- Aplicar formatos (colores, bordes)
- Referenciar datos dentro de fórmulas

### Inicialización:

Para crear una tabla se debe:

1. Seleccionar las celdas o el rango de datos que queremos convertir a tabla.
2. Inicio > Dar formato tabla
3. (Opcional) configuración de la tabla
4. Aceptar


## Buscar

Es una función que permite encontrar un valor dentro de un conjunto de datos y devolver un resultado relacionado.

Se utiliza cuando se desea localizar información dentro de una fila o columna de forma automática.

`=BUSCAR(valor_buscado; vector_busqueda; [vector_resultado])`

Donde:

- valor_buscado: dato que se desea encontrar
- vector_busqueda: rango donde se realiza la búsqueda
- vector_resultado (opcional): rango desde donde se devuelve el resultado

Ejemplo:

Supongamos la siguiente tabla:

| A (Código) | B (Precio) |
|------------|-----------|
| 1          | 100       |
| 2          | 200       |
| 3          | 300       |

Si queremos obtener el precio del código 2:

`=BUSCAR(2; A1:A3; B1:B3)`

Retorna 200

## Tablas dinámicas:

Una tabla dinámica es una herramienta de Excel que permite resumir, analizar y explorar grandes volúmenes de datos de forma interactiva, sin modificar los datos originales.

## Referencia de celdas:

Las referencias permiten utilizar el valor de una celda dentro de otra, principalmente en la construcción de fórmulas. En lugar de trabajar con valores fijos, se trabaja con direcciones de celdas, lo que permite que los resultados se actualicen automáticamente cuando cambian los datos.

Para referenciar una celda basta con agregar en la celda a referir la siguiente sintaxis `=REFERENCIA_CELDA`; en caso de hacerlo dentro de una fórmula, basta con agregar solo la referencia. Ejemplo: `=REFERENCIA_CELDA_A +REFERENCIA_CELDA_B`

Ejemplo: Columna A Fila 1 `=A1`

También se pueden utilizar referencias dentro de fórmulas más complejas:
`=A1 + B1`


### Referencia a un rango de celdas:

Se puede referenciar un conjunto de celdas contiguas utilizando el operador `:`.

Sintaxis:
`CELDA_INICIO:CELDA_FIN`

Ejemplo:
A1:A7

Esto representa todas las celdas desde A1 hasta A7.


### Fijar la referencia:

Para lograr que una referencia quede fija se utiliza el símbolo `$` delante de la fila y/o columna.

Ejemplos:

- `$A1` → fija la columna
- `A$1` → fija la fila
- `$A$1` → referencia absoluta (no cambia al copiar la fórmula)

Esto es útil cuando se copian fórmulas y se desea que ciertas referencias no cambien, como por ejemplo al trabajar con constantes o valores de referencia.




[🔙 Inicio de la unidad](../readme.md)
