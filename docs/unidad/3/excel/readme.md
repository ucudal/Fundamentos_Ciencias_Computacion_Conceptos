status: COMPLETE
responsable: @rafafil
ultima_actualizacion: 2026-04-13
 
## Excel y plantillas electrónicas

Son un tipo de software que tienen como objetivo permitir la administración y manipulación de datos de distinto tipo ubicados en tablas con filas y columnas.

#### Componentes:

|              | A (Columna) | B (Columna) | C (Columna) |
|--------------|-------------|-------------|-------------|
| 1 (Fila)     | Celda A1    | Celda B1    | Celda C1    |
| 2 (Fila)     | Celda A2    | Celda B2    | Celda C2    |
| 3 (Fila)     | Celda A3    | Celda B3    | Celda C3    |

Columnas, filas y celdas son los componentes básicos de una planilla electrónica.

Una celda es la intersección entre una fila y una columna. Puede contener datos (texto, números, fechas, etc.) o fórmulas.

El identificador de una celda (por ejemplo, A1) se construye combinando columna y fila, y permite referenciarla en operaciones y fórmulas.

Además, es posible asignar nombres definidos (rangos con nombre) para referirse a celdas o conjuntos de celdas de forma más descriptiva.


### Ejemplos en el mercado:

- Excel (Microsoft)
- Calc (Apache Open Office)
- Numbers (Apple)
- Google Spreadsheets (Google)



## Limpieza de datos

Es el proceso de preparar la información para poder trabajar con ella de forma correcta. Es común que los datos tengan problemas como espacios innecesarios, errores de escritura o formatos incorrectos, y estos programas ofrecen herramientas para corregirlos.

> ¿Qué es un dato?
Un dato es un valor que se guarda en una celda. Puede ser Texto, Números, Fechas, etc. 

Los datos no siempre se van a encontrar de una forma en la cual se puedan trabajar, por lo cual se realiza un proceso de limpieza antes de utilizarlos.  

Algunas acciones comunes son:

- Eliminar espacios innecesarios.
- Unificar formatos.
- Eliminar datos duplicados.
- Completar datos faltantes.

### Autocompletar datos:

Es la función de completar datos automáticamente a partir de un patrón o secuencia.

Ejemplo si tenemos una secuencia:

- 1,2,3

Podemos seleccionar esas celdas y arrastrar desde la esquina inferior derecha para que la serie continúe automáticamente:

- 4,5,6

Esta funcionalidad también es aplicable a otros tipos de datos como: Días, Meses, Fechas

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

-`=SUMA(6;7)` (En donde = indica que la expresión es una fórmula y dentro de la fórmula se invoca la función SUMA con los parámetros 6 y 7). Es lo mismo a escribir `=6+7`.


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

Es una función que permite encontrar un valor dentro de un conjunto de datos.

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

Existen variantes más utilizadas como BUSCARV y BUSCARX.

## Referencia de celdas:

Las referencias permiten utilizar el valor de una celda dentro de otra, principalmente en las fórmulas. En lugar de trabajar con valores fijos, se trabaja con direcciones de celdas, lo que permite que los resultados se actualicen automáticamente cuando cambian los datos.

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

### Fórmulas, referencias y rangos:

Las fórmulas no solo permiten operar con valores individuales, sino también trabajar con conjuntos de datos completos mediante rangos de celdas.

Ejemplos:

`=SUMA(A1:A10)` → Suma todos los valores desde la celda A1 hasta la A10.
`=PROMEDIO(A1:A10)` → Calcula el promedio de los valores en ese rango.

### Copiar Fórmulas:

El autocompletado, también funciona para las fórmulas. Cuando se copia una fórmula, se ajustan automáticamente las referencias de celdas según la nueva posición.

Ejemplo:

En la celda C1 tenemos la fórmula:

`=A1 + B1`

Al copiarla hacia abajo (por ejemplo, a la celda C2), la fórmula se transforma automáticamente en:

`=A2 + B2`

En algunos casos, puede ser necesario que ciertas referencias no cambien al copiar la fórmula. Para esto es necesario fijar la referencia (como se mencionó anteriormente).

[🔙 Inicio de la unidad](../readme.md)
