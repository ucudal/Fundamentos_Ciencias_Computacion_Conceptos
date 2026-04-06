status: COMPLETE
responsable: @pilasguru
ultima_actualizacion: 2026-03-19

# Sistemas de numeración

## Introducción

Las computadoras trabajan exclusivamente con información digital.  
Sin embargo, para comprender cómo lo hacen, primero es necesario entender cómo se representan los números.

Este capítulo sigue una idea central:

> toda la información en una computadora se representa como números, y esos números se expresan en binario.

Para llegar a esa conclusión, recorreremos tres pasos:

1. Cómo se representan los números  
2. Cómo se representa la información  
3. Cómo operan las computadoras con esos valores  

---

## 1. Representación de números

### El sistema decimal

El sistema decimal es el que utilizamos habitualmente.  

Está basado en diez símbolos: 0 al 9.

Su característica principal es que es **posicional**: el valor de cada dígito depende de su posición dentro del número.

Por ejemplo:

```
9240 = 9×10³ + 2×10² + 4×10¹ + 0×10⁰
```

Esto significa que cada dígito “pesa” según una potencia de 10.

Esta idea —el valor posicional— es la base de todos los sistemas de numeración.

---

### Generalización: sistemas en base B

El sistema decimal no es el único posible.  
Podemos construir sistemas con cualquier base.

Un sistema en base B tiene:

- dígitos desde 0 hasta B-1  
- posiciones con pesos de potencias de B  

En general, cualquier número puede escribirse como:

> suma de (dígito × potencia de la base)

Esta forma de pensar permite entender todos los sistemas de numeración de manera unificada.

---

### El sistema binario

El sistema binario es el más importante en computación.

- Base: 2  
- Dígitos: 0 y 1  

Ejemplo:

```
101₂ = 1×2² + 0×2¹ + 1×2⁰ = 5₁₀
```

Aquí no hay nada “mágico”: es exactamente el mismo mecanismo que en decimal, pero con base 2.

La razón por la cual las computadoras utilizan binario es física:  
los circuitos electrónicos pueden representar fácilmente dos estados (por ejemplo, encendido y apagado).

---

### Conversión entre decimal y binario

Para convertir un número decimal a binario se utiliza un procedimiento mecánico:

- dividir sucesivamente por 2  
- anotar los restos  
- leerlos de abajo hacia arriba  

Ejemplo:

```
12 → 1100₂
```

Este método no es un truco: refleja cómo se descompone el número en potencias de 2.

Para fracciones, el proceso es el inverso:

- multiplicar por 2  
- tomar la parte entera  
- repetir  

---

### Idea clave del bloque

Hasta aquí, lo importante es comprender que:

> los números no dependen del sistema, sino de cómo se representan

---

## 2. Representación de información

Hasta ahora hemos trabajado con números.  
Pero las computadoras también manejan texto, símbolos, imágenes y sonidos.

La idea fundamental es:

> toda la información se representa como números

---

### El problema del binario

El binario es adecuado para las computadoras, pero poco práctico para las personas:

```
110010101011
```

Este tipo de representación es difícil de leer y manipular.

Para simplificarlo, se utiliza el sistema hexadecimal.

---

### Sistema hexadecimal

El sistema hexadecimal tiene:

- Base: 16  
- Dígitos: 0–9 y A–F  

A = 10, B = 11, ..., F = 15

Su ventaja principal es su relación directa con el binario:

> 1 dígito hexadecimal representa exactamente 4 bits

Ejemplo:

```
1010₂ = A₁₆
1111₂ = F₁₆
```

Esto permite escribir números binarios de forma más compacta y legible.

---

### Representación de texto: ASCII

Una computadora no “entiende” letras.  
Para representar texto, se utiliza un código que asigna un número a cada carácter.

Uno de los primeros estándares es ASCII.

Ejemplo:

```
'A' = 65
'd' = 100
'@' = 64
```

Estos números luego se representan en binario.

Por lo tanto:

> un texto es, en realidad, una secuencia de números

---

### Bits y bytes

La unidad mínima de información es el **bit**:

- puede valer 0 o 1  

Un conjunto de 8 bits forma un **byte**:

```
1 byte = 8 bits
```

En muchos sistemas, un carácter ocupa un byte.

Por ejemplo:

- "Hola" → 4 caracteres → 4 bytes  

---

### Unidades de almacenamiento

Para medir cantidades mayores de información se utilizan múltiplos del byte:

- 1 KB = 1024 bytes  
- 1 MB = 1024 KB  
- 1 GB = 1024 MB  

Estas unidades permiten cuantificar la información que se almacena o transmite.

---

### Idea clave del bloque

Aquí ocurre un cambio importante:

> las computadoras no manejan “cosas”, sino representaciones numéricas de esas cosas

---

## 3. Operaciones en sistema binario

Una vez que la información está representada, la computadora puede operar sobre ella.

---

### Suma binaria

Las reglas son simples:

- 0 + 0 = 0  
- 0 + 1 = 1  
- 1 + 1 = 10 (acarreo)

Ejemplo:

```
   1011
 + 0110
 -------
  10001
```

La lógica es la misma que en decimal, pero con base 2.

---

### Limitaciones: overflow

Las computadoras trabajan con una cantidad fija de bits (por ejemplo, 8, 16 o 32 bits).

Esto implica un límite en los valores que pueden representarse.

Cuando el resultado de una operación supera ese límite ocurre un **desbordamiento (overflow)**.

Ejemplo conceptual:

```
1111 + 1 → 0000
```

El resultado “vuelve a cero” porque no hay más espacio para representarlo.

---

### Representación de números negativos

A diferencia del sistema decimal, en binario no existe un signo “-” natural.

Se necesitan estrategias para representar números negativos.

Existen varios métodos:

- signo-magnitud  
- complemento a 1  
- complemento a 2  

---

### Complemento a 2

El método más utilizado es el complemento a 2.

Para obtener el negativo de un número:

1. invertir los bits  
2. sumar 1  

Ejemplo:

```
0001 → 1110 → 1111
```

Este sistema tiene una gran ventaja:

> permite realizar restas utilizando sumas

---

### Idea clave del bloque

Las computadoras simplifican las operaciones:

> en el nivel más bajo, todo se reduce a operaciones con bits

---

## Conclusión

A lo largo de este sección vemos tres ideas fundamentales:

- los números se representan mediante sistemas de base  
- la información se codifica como números  
- las computadoras operan sobre esas representaciones  

La idea central que unifica todo es:

> todo en una computadora —números, texto o imágenes— se reduce a bits

Comprender este modelo es esencial para avanzar en el estudio de programación y sistemas.


[🔙 Inicio de la unidad](../readme.md)
