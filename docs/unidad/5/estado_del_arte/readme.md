status: COMPLETE
responsable: @LylCB, @aleaurre
ultima_actualizacion: 2026-05-31

# Fundamentos teóricos, Unidad 5: Estado del Arte en IA
### Fundamentos en Ciencias de la Computación (UCU)

Acceso a las slides mediante: https://canva.link/djv2eo4cwe1g1lj 

Este material desarrolla los fundamentos teóricos detrás de cada slide de la presentación. El recorrido es deliberadamente acumulativo: las primeras secciones establecen las representaciones básicas (tokens y embeddings), sobre ellas se construye la arquitectura *Transformer*, y a partir de ahí se derivan los grandes paradigmas de la IA contemporánea —modelos generativos, aprendizaje por refuerzo y modelos de lenguaje— hasta llegar al estado del arte de 2026.

---

## 1. Representación del texto: del símbolo al número (Slides 2–4)

### 1.1. El problema de la representación

Una red neuronal es, en esencia, una función que transforma vectores de números en otros vectores de números. No opera sobre símbolos lingüísticos: opera sobre magnitudes. Por lo tanto, todo el trabajo con lenguaje natural (NLP, *Natural Language Processing*) comienza resolviendo un problema previo: cómo convertir una secuencia de caracteres en una secuencia de vectores numéricos que la red pueda procesar. Este proceso tiene dos etapas conceptualmente distintas: la **tokenización** y el **embedding**.

### 1.2. Tokenización (Slide 3)

La tokenización segmenta el texto en unidades discretas llamadas *tokens*. Un token no equivale necesariamente a una palabra: según el algoritmo, puede ser una palabra, una sub-palabra (un morfema o fragmento) o un carácter. Los tokenizadores modernos —por ejemplo, los de tipo *Byte-Pair Encoding*— construyen un vocabulario de unidades frecuentes y descomponen las palabras en función de él. Por eso un término como *tomatoes* puede partirse en *tomato* + *es*.

Esta segmentación sub-léxica tiene una justificación teórica importante: permite cubrir un vocabulario abierto con un conjunto finito y manejable de unidades. Palabras nunca vistas durante el entrenamiento pueden representarse como combinación de fragmentos conocidos, lo que evita el problema de las palabras fuera de vocabulario (*out-of-vocabulary*) que afectaba a los enfoques basados en palabras completas. El costo de un texto procesado por un modelo, además, se mide en tokens, no en palabras, lo que tiene consecuencias prácticas de eficiencia y costo.

### 1.3. Embeddings (Slide 4)

Cada token se asocia a un vector de números reales de dimensión fija: su *embedding*. La propiedad central de los embeddings es que la posición de cada vector en el espacio codifica significado: tokens semánticamente relacionados ocupan posiciones cercanas. La cercanía se mide habitualmente mediante la similitud del coseno o la distancia euclídea entre vectores.

Lo decisivo es que estos vectores no se asignan manualmente, sino que se *aprenden*. Durante el entrenamiento, la red ajusta las coordenadas de cada token de modo que aquellos que aparecen en contextos similares terminen próximos en el espacio. Esto materializa la hipótesis distribucional de la lingüística: el significado de una palabra está determinado por las palabras con las que tiende a co-ocurrir. La consecuencia es que el espacio de embeddings exhibe estructura geométrica: regiones agrupan conceptos afines (en la slide, los términos del dominio de datos quedan agrupados), y ciertas relaciones semánticas se reflejan en operaciones vectoriales.

Una vez que cada token es un vector, todas las operaciones posteriores del modelo se reducen a álgebra lineal sobre esos vectores. La representación numérica deja de ser un mero requisito técnico y se convierte en el sustrato sobre el que opera todo el razonamiento del modelo.

---

## 2. La arquitectura Transformer (Slides 5–12)

### 2.1. Motivación: el límite de las redes recurrentes (Slides 5–6)

Antes de 2017, el procesamiento de secuencias se basaba en las **redes recurrentes** (RNN) y sus variantes con memoria, como las LSTM. Estas arquitecturas procesan la secuencia de forma estrictamente secuencial: un token a la vez, manteniendo un estado interno (*hidden state*) que resume lo procesado hasta el momento. Las LSTM incorporan compuertas (*gates*) que regulan qué información del estado se conserva y cuál se descarta, lo que mitiga el problema de la pérdida de información a largo plazo.

Sin embargo, las redes recurrentes presentan dos limitaciones estructurales. Primero, las **dependencias de largo alcance** se degradan: cuanto más distantes están dos elementos en la secuencia, más difícil resulta para el modelo relacionarlos, porque la información debe propagarse paso a paso a través de muchos estados intermedios (problema asociado al desvanecimiento del gradiente). Segundo, el procesamiento secuencial impide la **paralelización**: cada paso depende del anterior, lo que vuelve el entrenamiento lento sobre secuencias largas.

El Transformer, introducido en 2017 ("Attention Is All You Need"), resuelve ambos problemas eliminando la recurrencia y reemplazándola por un mecanismo que procesa todos los elementos de la secuencia simultáneamente y permite que cualquier par de posiciones interactúe directamente, sin importar la distancia entre ellas.

### 2.2. Self-attention (Slides 7–8)

El mecanismo central del Transformer es la **auto-atención** (*self-attention*). Su función es recalcular la representación de cada token incorporando información de los demás tokens de la secuencia, ponderada según su relevancia.

Para cada token se derivan, mediante transformaciones lineales aprendidas, tres vectores: una **consulta** (*query*, Q), una **clave** (*key*, K) y un **valor** (*value*, V). La interpretación es la siguiente: la consulta representa "qué información busca" un token; la clave representa "qué información ofrece" cada token; y el valor es el contenido que efectivamente se transmite. El grado de atención que un token presta a otro se calcula como el producto escalar entre la consulta del primero y la clave del segundo —de ahí el nombre *dot-product attention*—. Este producto mide la afinidad entre ambos.

Los puntajes de afinidad resultantes se normalizan mediante la función **softmax**, que los convierte en una distribución de probabilidad: valores no negativos que suman 1. Por eso, en la slide del *dot product self-attention*, los pesos asociados a cada salida suman la unidad. La nueva representación de un token es entonces el promedio ponderado de los valores de todos los tokens, usando esos pesos. Cada token construye así una representación contextualizada: una misma palabra adquiere representaciones distintas según las palabras que la rodean, lo que permite resolver ambigüedades léxicas y sintácticas.

La propiedad teórica clave es que la self-attention establece **conexiones directas entre todas las posiciones**, con un camino de longitud constante entre cualquier par de tokens. Esto elimina la degradación de las dependencias de largo alcance y, al no haber recurrencia, todo el cómputo puede realizarse en paralelo.

### 2.3. Positional encoding (Slide 9)

La self-attention, por su construcción, es invariante al orden: si se permutan los tokens de entrada, los promedios ponderados producen los mismos resultados reordenados. Pero el orden es constitutivo del significado en el lenguaje. Para reintroducir la información posicional sin recurrir a la recurrencia, se suma a cada embedding un vector de **codificación posicional** (*positional encoding*) que depende únicamente de la posición del token en la secuencia.

En la formulación original, estos vectores se generan mediante funciones sinusoidales de distintas frecuencias, lo que produce un patrón único para cada posición y permite al modelo representar tanto posiciones absolutas como distancias relativas. Cada token queda así representado por la suma de dos componentes: su contenido semántico (el embedding) y su ubicación (la codificación posicional).

### 2.4. El bloque Transformer completo (Slide 10)

Un bloque Transformer combina la self-attention con varios componentes adicionales. Tras la capa de atención se aplica una **red feed-forward** que procesa cada posición de forma independiente, aumentando la capacidad de representación del modelo. Dos mecanismos garantizan que esta arquitectura, apilada en muchas capas, pueda entrenarse de forma estable:

- Las **conexiones residuales** (*residual connections*) suman la entrada de cada sub-bloque a su salida. Esto crea un camino directo para el flujo del gradiente durante el entrenamiento, lo que evita su desvanecimiento en redes profundas y permite apilar muchas capas.
- La **normalización por capa** (*LayerNorm*) reescala las activaciones para mantener su distribución controlada, lo que estabiliza y acelera el entrenamiento.

Estos dos elementos no aportan capacidad expresiva por sí mismos, pero son condición necesaria para entrenar redes profundas. El bloque se repite N veces (la notación "×N" del diagrama): la profundidad —la cantidad de bloques apilados— es uno de los factores que determina la potencia del modelo.

### 2.5. Generalidad: texto e imágenes (Slides 11–12)

La arquitectura Transformer es agnóstica respecto del tipo de dato: opera sobre cualquier secuencia de vectores. Esto explica su aplicación tanto a texto como a imágenes.

Para **texto** (Slide 11), un Transformer generativo se entrena como modelo de lenguaje autorregresivo: dada una secuencia de tokens, predice una distribución de probabilidad sobre el vocabulario para el token siguiente. Genera texto de forma iterativa, prediciendo un token, anexándolo a la secuencia y repitiendo el proceso. Para que cada posición solo atienda a los tokens anteriores —y no a los futuros, que aún no existen al generar— se emplea **atención enmascarada** (*masked attention*).

Para **imágenes** (Slide 12), el *Vision Transformer* (ViT) divide la imagen en parches (*patches*) rectangulares, proyecta cada parche a un vector mediante una capa lineal —obteniendo *patch embeddings*— y trata la secuencia de parches exactamente igual que una secuencia de tokens. Se añade un token especial de clasificación (*cls*) cuya representación final resume la imagen para la tarea de clasificación. La idea unificadora es que segmentar el dato en unidades discretas y representarlas como vectores funciona de manera idéntica para distintas modalidades.

---

## 3. Modelos generativos (Slides 13–23)

### 3.1. Marco general (Slide 13)

Un **modelo generativo** aprende la distribución de probabilidad subyacente a un conjunto de datos, de modo que pueda muestrear de ella elementos nuevos. Esto lo distingue de los modelos **discriminativos**, que solo aprenden a separar o etiquetar datos existentes (por ejemplo, decidir si una imagen contiene un gato). El modelo generativo no asigna etiquetas: produce instancias originales —texto, imágenes, audio, video— que son plausibles según los patrones aprendidos del conjunto de entrenamiento. Las dos grandes familias para la generación de imágenes son las redes generativas adversarias (GANs) y los modelos de difusión.

### 3.2. Redes generativas adversarias — GANs (Slides 14–18)

Una **GAN** (*Generative Adversarial Network*) consta de dos redes entrenadas de forma simultánea con objetivos opuestos (Slide 14). El **generador** toma ruido aleatorio como entrada y produce muestras sintéticas; su objetivo es que esas muestras sean indistinguibles de los datos reales. El **discriminador** recibe muestras —reales o generadas— y estima la probabilidad de que sean reales; su objetivo es clasificarlas correctamente.

El entrenamiento constituye un juego de suma cero formalizado como un problema **minimax**: el discriminador maximiza su capacidad de distinguir, mientras el generador minimiza esa misma capacidad. En el equilibrio teórico, el generador reproduce la distribución real de los datos y el discriminador no puede hacer mejor que el azar. El resultado son muestras indistinguibles de las reales. En la práctica, este entrenamiento adversario es notoriamente inestable y constituye una dificultad técnica central de las GANs.

Las slides ilustran variantes y aplicaciones que muestran la versatilidad del paradigma:

- **Crecimiento progresivo** (Slide 15): para generar imágenes de alta resolución de forma estable, el entrenamiento comienza con resoluciones muy bajas (4×4 píxeles) y añade capas progresivamente para aumentar la resolución. Esto descompone un problema difícil en una secuencia de problemas más simples y mejora la estabilidad.
- **Traducción de imágenes** (Slide 16): en lugar de generar desde ruido, el modelo aprende un mapeo entre dos dominios (mapa↔satélite, boceto↔objeto, gris↔color), condicionando la generación en una imagen de entrada.
- **CycleGAN** (Slide 17): permite la traducción entre dominios **sin datos emparejados**. Como en muchos casos no existen pares correspondientes (no hay una foto pintada por Monet del mismo paisaje), CycleGAN introduce una restricción de **consistencia cíclica**: traducir una imagen al otro dominio y luego de vuelta debe recuperar la imagen original. Esta restricción permite aprender el mapeo a partir de colecciones no alineadas de cada dominio.
- **StyleGAN** (Slide 18): reestructura el generador para **separar los factores de variación** en distintas escalas. Los rasgos de gran escala (estructura facial, pose, edad) se controlan de forma independiente de los detalles finos (textura, mechones de pelo). Esto otorga control desacoplado sobre los atributos de la imagen generada, una propiedad valiosa para la edición controlada.

### 3.3. Modelos de difusión (Slides 19–22)

Los **modelos de difusión** constituyen la familia generativa dominante en la actualidad. Su principio es generar imágenes aprendiendo a revertir un proceso de degradación por ruido (Slide 19). El procedimiento se define en dos fases (Slides 20–21):

1. **Proceso forward (difusión).** A una imagen real se le añade ruido gaussiano de forma gradual, en una secuencia de pasos, hasta que la imagen se transforma en ruido prácticamente puro. Este proceso es **fijo y no se aprende**; está definido matemáticamente como una cadena de pasos que destruyen progresivamente la estructura de la imagen. Su función es generar pares (imagen ruidosa, ruido añadido) que sirven como datos de entrenamiento.

2. **Proceso reverse (generación).** Una red neuronal se entrena para **revertir** cada paso: dado un estado ruidoso, estima el ruido presente para poder removerlo y recuperar un estado menos ruidoso. Una vez aprendida esta operación de *denoising*, la generación consiste en partir de ruido puro muestreado al azar y aplicar el proceso reverse paso a paso hasta obtener una imagen nueva y coherente.

La asimetría entre ambas fases es conceptualmente central: el proceso de destrucción es trivial y fijo, mientras que el aprendizaje se concentra íntegramente en aprender a reconstruir. La generación condicionada por texto (Slide 22) se logra guiando el proceso reverse con una representación del texto, de modo que la imagen reconstruida sea consistente con la descripción solicitada. Esta capacidad de componer conceptos no vistos conjuntamente durante el entrenamiento —generar una escena improbable a partir de elementos conocidos— es una de las propiedades más notables de estos modelos.

### 3.4. Convergencia de paradigmas: Diffusion Transformers (Slide 23)

Las arquitecturas de generación más recientes combinan los dos pilares de la unidad: el **proceso de difusión** como mecanismo de generación y el **Transformer** como red que ejecuta el *denoising*. Esta combinación se conoce como **DiT** (*Diffusion Transformer*). Los DiT operan típicamente en un espacio latente comprimido (de ahí "latent diffusion") en lugar de sobre los píxeles directamente, lo que reduce el costo computacional. El bloque DiT incorpora la información del paso de ruido y de la condición (la etiqueta o el texto) mediante mecanismos de condicionamiento como *adaptive LayerNorm* o atención cruzada. Esta arquitectura es la base de los sistemas de generación de imagen y video de última generación, y representa la integración de las dos grandes líneas teóricas que estructuran esta unidad.

---

## 4. Aprendizaje por refuerzo (Slides 24–28)

### 4.1. El marco formal (Slides 24–27)

El **aprendizaje por refuerzo** (*Reinforcement Learning*, RL) aborda un problema distinto al del aprendizaje supervisado. No se aprende a partir de ejemplos etiquetados, sino a partir de la **interacción** con un entorno y de una señal de recompensa. Un **agente** percibe el **estado** del **entorno**, ejecuta una **acción**, y el entorno responde con un nuevo estado y una **recompensa** escalar. El agente debe aprender qué hacer para maximizar la recompensa acumulada en el tiempo.

Formalmente, el problema se modela como un **proceso de decisión de Markov** (MDP), caracterizado por (Slide 27): un conjunto de estados, un conjunto de acciones, una **función de transición** *Pr(s<sub>t+1</sub> | s<sub>t</sub>, a<sub>t</sub>)* que describe cómo evoluciona el entorno, y una **función de recompensa** *Pr(r<sub>t+1</sub> | s<sub>t</sub>, a<sub>t</sub>)*. La estrategia del agente es su **política** (*policy*) *π(a<sub>t</sub> | s<sub>t</sub>)*: una función que asigna a cada estado una distribución de probabilidad sobre las acciones. Aprender equivale a optimizar esta política.

Los conceptos de trayectoria y retorno (Slides 25–26) completan el marco. Una **trayectoria** (*τ*) es la secuencia de estados, acciones y recompensas que el agente experimenta a lo largo de una interacción. El **retorno** es la suma de las recompensas obtenidas a lo largo de la trayectoria, frecuentemente con un factor de descuento que pondera más las recompensas inmediatas que las lejanas. El objetivo del agente, expresado con precisión, es encontrar la política que maximice el retorno **esperado**. La dificultad característica del RL reside en que las recompensas pueden ser escasas y diferidas: una acción puede tener consecuencias positivas o negativas que solo se manifiestan muchos pasos después, lo que plantea el problema de la asignación de crédito.

### 4.2. Del refuerzo a los LLMs: RLHF (Slide 28)

El **RLHF** (*Reinforcement Learning from Human Feedback*) aplica el marco del refuerzo al ajuste de modelos de lenguaje, y es uno de los componentes que permitió alinear los LLMs con las expectativas humanas. El desafío que resuelve es que la calidad de una respuesta —su utilidad, claridad, adecuación— es difícil de especificar mediante una función matemática explícita. RLHF sortea esta dificultad aprendiendo la función de recompensa a partir de juicios humanos.

El procedimiento tiene tres componentes. Primero, se recopila un **conjunto de preferencias**: a evaluadores humanos se les presentan pares de respuestas del modelo y eligen cuál prefieren. Segundo, con esos datos se entrena un **modelo de recompensa**, que aprende a predecir qué respuestas preferirían los humanos, asignando un puntaje a cada par (prompt, respuesta). Tercero, ese modelo de recompensa proporciona la señal de refuerzo con la que se ajusta el modelo de lenguaje (la *policy*), de modo que tienda a generar respuestas mejor valoradas. La recompensa, en este contexto, es una aproximación aprendida de la preferencia humana.

---

## 5. Modelos de lenguaje grandes (Slides 29–31)

### 5.1. Definición (Slide 29)

Un **LLM** (*Large Language Model*) es un modelo de lenguaje basado en la arquitectura Transformer, entrenado sobre corpus de texto de escala masiva, capaz de comprender y generar lenguaje natural. El adjetivo "grande" remite tanto al volumen de datos de entrenamiento como a la cantidad de parámetros del modelo. Funcionalmente, un LLM realiza la operación descrita en la sección 2.5 —predecir el siguiente token— pero a una escala tal que de esa operación elemental emergen capacidades complejas: comprensión de instrucciones, traducción, resumen, razonamiento, generación de código. La aparición de capacidades no programadas explícitamente al aumentar la escala se conoce como comportamiento emergente.

### 5.2. Arquitectura completa (Slide 30)

El diagrama de la arquitectura completa corresponde al Transformer original e integra todos los componentes vistos: embeddings de entrada, codificación posicional, atención multi-cabeza (*multi-head attention* —varias self-attentions en paralelo que capturan distintos tipos de relación—), conexiones residuales, normalización, redes feed-forward, y una capa final lineal seguida de softmax que produce la distribución de probabilidad sobre el vocabulario. La arquitectura original incluye una rama *encoder* y una rama *decoder*; muchos LLMs actuales utilizan únicamente la rama decoder con atención enmascarada. Lo relevante a nivel conceptual es que ningún componente del diagrama es nuevo respecto de lo desarrollado en la sección 2: la arquitectura completa es la composición de las piezas ya estudiadas.

### 5.3. Las tres etapas de entrenamiento (Slide 31)

El entrenamiento de un LLM se organiza en tres fases sucesivas, cada una con un propósito distinto:

1. **Pre-entrenamiento.** El modelo aprende a predecir el siguiente token sobre cantidades enormes de texto no etiquetado. En esta fase, la más costosa en cómputo, adquiere el conocimiento del lenguaje, los hechos del mundo y las regularidades estadísticas del texto. El aprendizaje es auto-supervisado: la supervisión proviene del propio texto, ya que el token siguiente actúa como etiqueta.

2. **Fine-tuning supervisado.** El modelo pre-entrenado posee competencia lingüística, pero no necesariamente el comportamiento de un asistente útil. Esta fase lo ajusta con ejemplos curados de instrucciones y buenas respuestas, enseñándole el formato y el estilo de la asistencia.

3. **RLHF.** La fase final, descrita en la sección 4.2, afina el modelo según preferencias humanas para optimizar la utilidad y la adecuación de sus respuestas.

Esta secuencia refleja una división de trabajo: el pre-entrenamiento aporta conocimiento, el fine-tuning aporta comportamiento, y el RLHF aporta alineación con las preferencias.

---

## 6. Estado del arte (2026) (Slides 32–35)

### 6.1. Tendencias actuales (Slide 32)

El panorama de 2026 se caracteriza por cuatro líneas de desarrollo:

- **Modelos de razonamiento.** Modelos que generan cadenas intermedias de razonamiento antes de producir la respuesta final, asignando más cómputo en el momento de la inferencia. Este desplazamiento del cómputo desde el entrenamiento hacia la inferencia (*test-time compute*) mejora sustancialmente el desempeño en tareas que requieren razonamiento de múltiples pasos.

- **Agentes.** Sistemas que, en lugar de limitarse a responder, ejecutan tareas de varios pasos de forma autónoma: planifican, utilizan herramientas externas, observan resultados y ajustan su curso de acción. Extienden el modelo de un sistema reactivo a uno capaz de perseguir objetivos.

- **Mixture-of-Experts (MoE).** Arquitectura que permite escalar el número de parámetros sin que crezca proporcionalmente el costo de cómputo por inferencia. El modelo se divide en múltiples sub-redes "expertas", y un mecanismo de enrutamiento activa solo un subconjunto de ellas para cada entrada. Así se obtiene un modelo de gran capacidad total pero con cómputo activado reducido por consulta.

- **Contexto largo y multimodalidad nativa.** Capacidad de procesar entradas muy extensas (documentos completos) y de manejar de forma integrada distintas modalidades —texto, imagen, audio, video— sin requerir sistemas separados.

### 6.2. RAG y agentes (Slide 33)

Un LLM almacena su conocimiento de forma implícita en sus parámetros, fijado en el momento del entrenamiento. Esto implica dos limitaciones: el conocimiento tiene una fecha de corte y no incluye información privada o específica de un dominio. La **generación aumentada por recuperación** (*Retrieval Augmented Generation*, RAG) aborda estas limitaciones acoplando al modelo un componente de recuperación: ante una consulta, el sistema recupera información relevante de una base de datos externa —típicamente una base vectorial que indexa documentos mediante embeddings y permite búsqueda semántica— y la incorpora al contexto antes de generar la respuesta. La respuesta se fundamenta así en información recuperada en tiempo de inferencia, lo que mejora la actualidad y reduce las afirmaciones infundadas. El gráfico de la slide ordena las técnicas según complejidad y flexibilidad crecientes, desde prompts estáticos hasta agentes autónomos, situando a RAG y a los agentes en el extremo de mayor sofisticación.

### 6.3. Modelos multimodales (Slide 34)

Una **modalidad** es un tipo de dato (texto, imagen, audio, video). Un **modelo multimodal** procesa y combina información de varias modalidades de forma simultánea. La factibilidad técnica de estos modelos descansa sobre un principio ya establecido en la unidad: distintas modalidades pueden representarse como secuencias de vectores en un espacio común mediante el esquema de tokenización y embedding correspondiente a cada tipo de dato. Una vez proyectadas a un espacio compartido, la arquitectura Transformer puede operar sobre ellas de manera uniforme, integrando información heterogénea. Esto habilita tareas que cruzan modalidades, como responder en texto preguntas sobre una imagen o interpretar conjuntamente audio y texto.

### 6.4. Modelos Visión-Lenguaje-Acción — VLA (Slide 35)

Los modelos **VLA** (*Vision-Language-Action*) extienden la multimodalidad al dominio físico, integrando tres capacidades: percepción visual del entorno (visión), comprensión de instrucciones en lenguaje natural (lenguaje) y generación de acciones motoras (acción). El ejemplo de la slide, *Gemini Robotics*, ilustra la aplicación de un modelo multimodal al control de robots, dotándolos de razonamiento sobre el mundo real y capacidad de manipulación. Conceptualmente, los VLA representan la convergencia de las líneas desarrolladas a lo largo de la unidad —comprensión del lenguaje, comprensión visual y toma de decisiones secuenciales— conectadas a un sistema físico que actúa sobre el entorno. Constituyen una de las fronteras actuales de la disciplina: el traslado de las capacidades de los modelos generativos y de razonamiento desde el dominio digital hacia la interacción con el mundo material.

---

## Síntesis

El recorrido teórico de esta unidad parte de un problema de representación —convertir símbolos en vectores con significado— y construye sobre él una secuencia coherente de abstracciones. La arquitectura Transformer, con la self-attention como mecanismo central, proporciona un modo general y paralelizable de procesar secuencias de cualquier modalidad. Sobre esa base se erigen los grandes paradigmas contemporáneos: los modelos generativos (GANs y, especialmente, difusión) que aprenden a producir datos nuevos; el aprendizaje por refuerzo que aprende mediante interacción y recompensa; y los modelos de lenguaje que, entrenados a escala masiva y alineados mediante RLHF, dan lugar a los sistemas que definen el estado del arte. La integración progresiva de estas líneas —difusión con Transformers, refuerzo con LLMs, multimodalidad con acción física— es la característica distintiva del momento actual de la disciplina.
