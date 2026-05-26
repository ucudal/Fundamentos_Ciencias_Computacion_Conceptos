# Actividad de clase: Quiz de control de lectura
## Unidad 5 — Aprendizaje Automático

### Fundamentos en Ciencias de la Computación

---

## Material de lectura obligatoria

**Prince, Simon J.D. (2023). _Understanding Deep Learning_. MIT Press. Capítulo 1: "Introduction" (páginas 1–18).**

Disponible gratuitamente bajo licencia Creative Commons en:
`https://udlbook.github.io/udlbook/`

Secciones a leer:

- 1.1 Supervised learning
- 1.2 Unsupervised learning
- 1.3 Reinforcement learning
- 1.4 Ethics
- 1.5 Structure of book
- 1.6 Other books

**Tiempo estimado de lectura:** 40 a 50 minutos.

---

## Quiz

### Pregunta 1

Según Prince, el aprendizaje automático moderno se divide en tres grandes áreas. ¿Cuáles son?

A) Clasificación, regresión y agrupamiento.

B) Aprendizaje supervisado, no supervisado y por refuerzo.

C) Aprendizaje profundo, aprendizaje superficial y aprendizaje estadístico.

D) Visión por computadora, procesamiento de lenguaje natural y robótica.

---

### Pregunta 2

En el marco del aprendizaje supervisado, Prince define un modelo como una ecuación que relaciona entradas y salidas. ¿Cuál es el rol específico de los parámetros del modelo?

A) Son los datos de entrenamiento utilizados para evaluar el desempeño del modelo.

B) Son las entradas que el modelo recibe en tiempo de inferencia.

C) Son valores internos ajustables que determinan la relación particular entre entrada y salida dentro de la familia de funciones elegida.

D) Son las salidas que el modelo predice una vez entrenado.

---

### Pregunta 3

Prince introduce una distinción entre los datos disponibles antes y después del despliegue de un modelo de aprendizaje supervisado. ¿Cuál de las siguientes afirmaciones describe correctamente esta distinción?

A) Durante el entrenamiento se dispone de pares entrada-salida etiquetados; en el momento de la inferencia, el modelo recibe entradas nuevas y debe producir salidas que no se conocen de antemano.

B) Tanto durante el entrenamiento como durante la inferencia, el modelo dispone de los pares entrada-salida etiquetados.

C) Durante el entrenamiento el modelo solo dispone de entradas; los pares etiquetados se reciben después, durante la inferencia.

D) El modelo nunca recibe salidas etiquetadas, ni durante el entrenamiento ni durante la inferencia.

---

### Pregunta 4

Prince describe que el entrenamiento de un modelo supervisado implica definir una "función de pérdida" (loss function). ¿Cuál es su rol conceptual?

A) Mide la cantidad de datos perdidos durante el preprocesamiento.

B) Cuantifica el desacuerdo entre las predicciones del modelo y las salidas verdaderas en los datos de entrenamiento, y se busca minimizarla ajustando los parámetros.

C) Define la cantidad de información que el modelo descarta al hacer predicciones sobre datos nuevos.

D) Representa el costo computacional asociado al entrenamiento del modelo.

---

### Pregunta 5

En el capítulo, Prince advierte sobre la diferencia entre el desempeño de un modelo sobre los datos de entrenamiento y su desempeño sobre datos nuevos. ¿Por qué esta distinción es central?

A) Porque los datos de entrenamiento contienen errores que el modelo memoriza, mientras que los datos nuevos son siempre perfectos.

B) Porque el modelo se evalúa únicamente sobre los datos de entrenamiento.

C) Porque el verdadero objetivo del aprendizaje es generalizar a datos no vistos, y un buen desempeño en entrenamiento no garantiza un buen desempeño en datos nuevos.

D) Porque los datos nuevos siempre provienen de una distribución distinta a la de entrenamiento.

---

### Pregunta 6

Prince ejemplifica el aprendizaje no supervisado mencionando, entre otras tareas, los modelos generativos. ¿Cuál es la característica esencial que distingue al aprendizaje no supervisado del supervisado?

A) El aprendizaje no supervisado requiere más datos que el supervisado para funcionar correctamente.

B) En el aprendizaje no supervisado los datos no incluyen salidas etiquetadas; el modelo debe descubrir estructura en las entradas por sí mismo.

C) El aprendizaje no supervisado solo se usa para problemas de clasificación.

D) El aprendizaje no supervisado utiliza datos etiquetados pero ignora las etiquetas durante el entrenamiento.

---

### Pregunta 7

Según el capítulo, ¿cuál es la idea fundamental detrás del aprendizaje por refuerzo?

A) Un agente recibe ejemplos etiquetados de acciones correctas e incorrectas, y aprende a imitar las correctas.

B) Un modelo encuentra patrones ocultos en datos no etiquetados utilizando recompensas estadísticas.

C) Un agente interactúa con un entorno tomando acciones, recibe recompensas como consecuencia, y aprende una política que maximiza la recompensa acumulada en el tiempo.

D) Un sistema reentrena periódicamente un modelo supervisado con datos nuevos para reforzar el aprendizaje anterior.

---

### Pregunta 8

Prince discute en la sección de ética que los modelos de aprendizaje automático pueden producir resultados sesgados. ¿Cuál de las siguientes describe correctamente el origen del problema según el texto?

A) Los modelos son inherentemente neutrales; cualquier sesgo proviene exclusivamente de la elección del algoritmo.

B) Los modelos pueden heredar y amplificar sesgos presentes en los datos de entrenamiento, así como reflejar decisiones humanas tomadas a lo largo del pipeline.

C) El sesgo es siempre un problema matemático que se resuelve con técnicas de regularización.

D) Los sesgos surgen únicamente cuando los modelos se aplican a poblaciones distintas a las de origen, no durante el entrenamiento.

---

### Pregunta 9

En el aprendizaje supervisado, Prince distingue entre problemas de regresión y problemas de clasificación. ¿Cuál es el criterio que los diferencia?

A) La regresión usa más datos que la clasificación.

B) La clasificación es siempre supervisada, mientras que la regresión puede ser no supervisada.

C) En regresión, la salida que se busca predecir es un valor continuo; en clasificación, es una etiqueta tomada de un conjunto discreto de categorías.

D) La regresión utiliza modelos lineales, mientras que la clasificación utiliza modelos no lineales.

---

### Pregunta 10

Prince menciona que el aprendizaje profundo se ha convertido en el enfoque dominante en las tres áreas del aprendizaje automático. ¿Cuál es la razón conceptual principal que ofrece el texto?

A) Las redes profundas son siempre más rápidas de entrenar que cualquier otro modelo.

B) Las redes profundas son una familia de funciones suficientemente flexible para representar relaciones complejas, y combinadas con grandes cantidades de datos y poder de cómputo han producido los mejores resultados empíricos en supervisado, no supervisado y refuerzo.

C) Las redes profundas eliminan completamente la necesidad de ingeniería de variables y de datos etiquetados.

D) Las redes profundas son la única familia de modelos matemáticamente capaz de generalizar.

---

## Clave de respuestas 

### Pregunta 1 — Respuesta correcta: **B**

Las tres áreas que Prince establece desde la primera página del capítulo son aprendizaje supervisado, no supervisado y por refuerzo. La opción A confunde paradigmas con técnicas: clasificación, regresión y clustering son tipos de problemas dentro de los paradigmas. La opción C mezcla niveles taxonómicos. La opción D enumera áreas de aplicación, no paradigmas.

### Pregunta 2 — Respuesta correcta: **C**

Los parámetros son los grados de libertad que la familia de funciones expone para adaptarse a los datos. Conviene volver aquí a la notación de la unidad, donde el modelo se escribe como una función de la entrada parametrizada por theta. Las opciones A, B y D confunden parámetros con datos, entradas y salidas respectivamente, tres confusiones extremadamente frecuentes.

### Pregunta 3 — Respuesta correcta: **A**

La asimetría entre entrenamiento e inferencia es central. Esta distinción suele estar implícita y conviene hacerla explícita. Las opciones B, C y D capturan malentendidos donde se confunden ambas fases.

### Pregunta 4 — Respuesta correcta: **B**

La función de pérdida es el puente entre el desempeño deseado y la optimización. Las opciones A y C juegan con el significado coloquial de la palabra pérdida, una confusión recurrente entre principiantes hispanohablantes. La opción D confunde pérdida con costo computacional.

### Pregunta 5 — Respuesta correcta: **C**

La generalización es la meta verdadera, no la memorización. La opción A invierte la realidad sobre la calidad de los datos. La opción B reduce el aprendizaje al entrenamiento. La opción D introduce la noción de cambio de distribución, real pero no central a la distinción que pregunta.

### Pregunta 6 — Respuesta correcta: **B**

La ausencia de etiquetas es la característica definitoria. Las opciones A y C son afirmaciones populares pero falsas. La opción D es particularmente interesante porque describe una situación que sí ocurre en algunos contextos, pero no es la definición del paradigma.

### Pregunta 7 — Respuesta correcta: **C**

La interacción agente-entorno y la recompensa diferida son los rasgos distintivos. La opción A describe el aprendizaje supervisado. La opción B mezcla refuerzo con no supervisado. La opción D describe un proceso de mantenimiento de modelos, no el paradigma.

### Pregunta 8 — Respuesta correcta: **B**

Prince adopta una postura matizada: los modelos no son neutrales y reflejan tanto sus datos como las decisiones humanas en cada etapa. La opción A es la postura ingenua que conviene desarmar. La opción C reduce un problema sociotécnico a uno matemático. La opción D restringe el sesgo solo a problemas de despliegue, lo cual es parcial.

### Pregunta 9 — Respuesta correcta: **C**

La naturaleza de la salida define el tipo de problema. La opción A es una observación empírica sin sustento. La opción B es falsa: ambos son supervisados. La opción D confunde el tipo de problema con la familia de modelos utilizada, error muy frecuente.

### Pregunta 10 — Respuesta correcta: **B**

La respuesta combina los tres elementos que Prince destaca: expresividad de la familia, escala de datos y poder de cómputo. La opción A es falsa: las redes profundas suelen ser costosas de entrenar. La opción C es una sobreafirmación frecuente entre estudiantes nuevos. La opción D incurre en absolutismo: muchos modelos no profundos generalizan bien.

