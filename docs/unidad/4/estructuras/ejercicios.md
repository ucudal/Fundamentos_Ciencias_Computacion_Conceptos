# Práctico — Estructuras de Datos
### Fundamentos en Ciencias de la Computación · Unidad 4
 
> **Instrucciones generales**
> - No se programa. Todas las respuestas son en **pseudocódigo**, diagramas de cajas/flechas o texto escrito.
> - Para los diagramas usá cajas del estilo `[ valor | next→ ]` para listas enlazadas, o simplemente `[A] → [B] → [C] → null`.
> - Justificá brevemente tus decisiones cuando el ejercicio lo pida.
> - No hay una única respuesta correcta: lo que importa es el **razonamiento**.
 
---
 
## Parte 1 — Operaciones básicas sobre listas
 
### Ejercicio 1 🙂
 
Dada la siguiente lista:
 
```
[ 10 ] → [ 20 ] → [ 30 ] → null
```
 
Escribí el pseudocódigo para insertar el valor `15` en la posición 1 (entre el 10 y el 20), usando `insert(x, pos)`.  
Luego dibujá cómo queda la lista después de la operación.
 
---
 
### Ejercicio 2 🙂
 
Dada la lista:
 
```
[ 5 ] → [ 8 ] → [ 13 ] → [ 21 ] → null
```
 
Escribí el pseudocódigo para eliminar el elemento `8` usando `remove(x)`.  
Dibujá el estado de la lista antes y después.
 
---
 
### Ejercicio 3 🙂
 
Dada la lista:
 
```
[ "Ana" ] → [ "Luis" ] → [ "Sol" ] → [ "Teo" ] → null
```
 
Indicá qué retorna cada una de estas operaciones **sin modificar la lista**:
 
- `find("Sol")`
- `findKth(0)`
- `findKth(3)`
- `next(1)`
- `previous(2)`
---
 
### Ejercicio 4 🫨🫨
 
Dada la lista:
 
```
[ 1 ] → [ 2 ] → [ 3 ] → [ 4 ] → [ 5 ] → null
```
 
Seguí paso a paso la siguiente secuencia de operaciones y dibujá el estado de la lista **después de cada una**:
 
1. `insert(0, 0)`
2. `remove(3)`
3. `insert(99, 4)`
---
 
### Ejercicio 5 🫨🫨
 
Dada la lista:
 
```
[ 7 ] → [ 14 ] → [ 21 ] → [ 28 ] → null
```
 
Escribí el pseudocódigo completo para **invertir** esta lista usando únicamente las operaciones `insert(x, pos)` y `remove(x)`.  
Mostrá el estado de la lista al final de cada paso relevante.
 
> _Pista: podés apoyarte en una variable auxiliar para guardar el valor que vas a mover._
 
---
 
## Parte 2 — Elegir la implementación correcta
 
> Para cada situación describí si conviene usar una **lista basada en arreglo** o una **lista enlazada simple**, y justificá en 2–3 oraciones.
 
---
 
### Ejercicio 6 🙂
 
Una aplicación guarda el historial de páginas visitadas en un navegador. El usuario puede volver atrás o avanzar. Las inserciones siempre ocurren al final y las eliminaciones ocurren al principio o al final.
 
¿Qué implementación elegís? ¿Por qué?
 
---
 
### Ejercicio 7 🙂
 
Un sistema universitario almacena las materias de un estudiante. Se consulta frecuentemente la materia número `k` (por posición). Las inscripciones y bajas son raras.
 
¿Qué implementación elegís? ¿Por qué?
 
---
 
### Ejercicio 8 🫨🫨
 
Un editor de texto necesita representar las líneas de un documento. Se insertan y eliminan líneas en cualquier posición con frecuencia. El acceso por número de línea también es importante.
 
¿Qué implementación elegís? ¿Habría alguna alternativa intermedia? Justificá.
 
---
 
### Ejercicio 9 🫨🫨
 
Una playlist de música se recorre siempre de principio a fin. Sin embargo, el usuario puede agregar canciones en cualquier posición y eliminar la canción que está sonando en ese momento.
 
¿Qué implementación elegís? ¿Cambiaría algo si la playlist fuera circular (al terminar vuelve al inicio)?
 
---
 
## Parte 3 — Pilas y Colas
 
### Ejercicio 10 🙂
 
Dada una pila vacía, seguí la siguiente secuencia y dibujá el estado de la pila después de cada operación:
 
```
push(3)
push(7)
push(1)
pop()
push(5)
top()
```
 
¿Qué valor retorna `top()` al final? ¿La pila se modifica con `top()`?
 
---
 
### Ejercicio 11 🙂
 
Dada una cola vacía, seguí la siguiente secuencia y dibujá el estado de la cola (indicando frente y final) después de cada operación:
 
```
enqueue("A")
enqueue("B")
enqueue("C")
dequeue()
enqueue("D")
dequeue()
```
 
¿Qué elemento queda al frente al final?
 
---
 
### Ejercicio 12 🫨🫨
 
Tenés esta secuencia de operaciones sobre una **pila**:
 
```
push(10)
push(20)
push(30)
pop()
pop()
push(40)
pop()
pop()
```
 
¿En qué orden salen los elementos? Escribí la secuencia de valores retornados por cada `pop()`.
 
---
 
### Ejercicio 13 🫨🫨
 
Se te pide modelar el sistema de **deshacer/rehacer** (undo/redo) de un editor de texto simple.
 
- Describí qué estructura de datos usarías para cada función.
- Escribí el pseudocódigo de las operaciones `realizar_accion(a)`, `deshacer()` y `rehacer()`.
- Dibujá el estado de las estructuras tras esta secuencia de acciones:
  1. Escribir "Hola"
  2. Escribir "Mundo"
  3. Deshacer
  4. Escribir "Todo"
  5. Rehacer _(¿qué pasa aquí? justificá)_
---
 
## Parte 4 — Desafíos integradores
 
### Ejercicio 14 🤬🤬🤬
 
Dada la siguiente lista enlazada simple:
 
```
[ 1 ] → [ 2 ] → [ 3 ] → [ 4 ] → [ 5 ] → null
```
 
Escribí el pseudocódigo para invertirla **usando una pila** como estructura auxiliar.  
El resultado debe ser una lista enlazada con los mismos nodos en orden inverso:
 
```
[ 5 ] → [ 4 ] → [ 3 ] → [ 2 ] → [ 1 ] → null
```
 
Mostrá el estado de la pila y de la lista en cada paso relevante.
 
---
 
### Ejercicio 15 🤬🤬🤬
 
Se quiere simular la **atención en una caja de supermercado**. Los clientes llegan y hacen fila (cola). Sin embargo, si un cliente tiene el carrito semi-vacío (5 ítems), puede pasar directo al frente de la fila.
 
1. Describí qué estructura(s) de datos usarías y por qué.
2. Escribí el pseudocódigo de las operaciones:
   - `llega_cliente(nombre, tiene_carrito_vacio)`
   - `atender_siguiente()`
3. Simulá la siguiente secuencia y dibujá el estado de la(s) estructura(s) después de cada evento:
   - Llega Ana (con carrito)
   - Llega Bob (con carrito)
   - Llega Carol (carrito vacío)
   - Llega David (con carrito)
   - Llega Eva (carrito vacío)
   - Se atiende un cliente → ¿quién es?
   - Se atiende otro cliente → ¿quién es?
> _¿Cambiará tu respuesta si los clientes con carrito semi-vacío también deben respetar el orden entre ellos?_
 
---
 
*Fundamentos en Ciencias de la Computación — 2026*  
*Material basado en: Weiss, M. A. (2014). Data Structures and Algorithm Analysis in C++ (4th ed.)*
