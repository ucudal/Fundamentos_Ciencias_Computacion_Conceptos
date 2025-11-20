# Expresiones Regulares

## ¿Qué es una expresión regular? (2 min)

Una forma de describir patrones de texto.

No busca texto literal, busca texto que coincida con una forma.

Ejemplos de ideas:

```
“Todas las líneas que empiecen con ERROR”
“Cualquier número”
“Direcciones de correo simples”
```

## Elementos básicos (4–5 min)

Presentar solo los esenciales:

1. Caracteres especiales

```
. → un carácter cualquiera
* → cero o más repeticiones
+ → una o más repeticiones
? → opcional
```

2. Grupos y rangos

```
[abc] → a, b o c
[0-9] → cualquier dígito
[A-Za-z] → letras
```

3. Anclas

```
^ → principio de línea
$ → fin de línea
```

## Demostraciones ultra prácticas (3–4 min)

Usando grep -E:

1. Líneas que comienzan con ERROR

`grep -E '^ERROR' log.txt`

2. Buscar números

`grep -E '[0-9]+' datos.txt`

3. Coincidir un email muy simple (no técnico, solo ilustrativo)

`grep -E '.+@.+\..+' archivo.txt`

4. Coincidir archivos terminados en .sh

`ls | grep -E '\.sh$'`


[🔙 Inicio de la unidad](../readme.md)