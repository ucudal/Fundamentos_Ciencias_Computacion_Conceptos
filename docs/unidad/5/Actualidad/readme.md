status: DRAFT
responsable: @LylCB, @aleaurre
ultima_actualizacion: 2026-05-31

# [Estado del Arte](./2.1_estado_del_arte.md)

### Fundamentos en Ciencias de la Computación (UCU)

El contenido del documento ofrece un recorrido exhaustivo por los pilares fundamentales, las arquitecturas revolucionarias y las fronteras tecnológicas que definen la inteligencia artificial contemporánea. A continuación, se detallan los grandes ejes temáticos que componen este análisis:

#### 1. Procesamiento del Lenguaje Natural (NLP) y Representación de Datos

El texto introduce la premisa de que las redes neuronales operan estrictamente en el dominio numérico y no lingüístico. Para salvar esta brecha, se examina el proceso de **tokenización**, mediante el cual el texto se fragmenta en unidades menores (palabras, subpalabras o caracteres). Posteriormente, estos elementos se transforman en **embeddings**, que son vectores numéricos de alta dimensión capaces de capturar relaciones semánticas y de significado profundo, permitiendo que el sistema comprenda el contexto más allá de una simple coincidencia exacta de caracteres.

#### 2. La Arquitectura Transformer y Mecanismos de Atención

Se destaca la arquitectura **Transformer** (introducida en 2017) como el motor fundamental de la IA generativa moderna. El documento analiza cómo esta estructura superó las limitaciones de las redes recurrentes tradicionales (como RNN y LSTM) gracias al mecanismo de **self-attention** (autoatención) y al cálculo del *dot product*. Estos componentes, junto con la codificación posicional (*positional encoding*), permiten al modelo procesar secuencias completas de información de manera paralela, evaluando la influencia y relación mutua de todas las palabras o elementos dentro de un contexto global. Asimismo, se subraya su versatilidad para expandirse exitosamente desde el procesamiento de texto hasta el análisis de imágenes.

#### 3. Modelos Generativos de Imágenes (GANs y Difusión)

El núcleo de la creación de contenido original se divide en dos enfoques principales dentro del material:

* **Redes Generativas Adversarias (GANs):** Explicadas a través de la dinámica de un juego minimax, donde un *generador* intenta crear imágenes falsas realistas y un *discriminador* compite para detectar los engaños. Se mencionan sus evoluciones clave, como *CycleGAN* y *StyleGAN*.
* **Modelos de Difusión (*Diffusion*):** Descritos como sistemas que generan alta calidad visual mediante un proceso dual. Primero, un proceso de avance (*forward*) que añade ruido matemático de forma progresiva a una imagen; segundo, un proceso inverso (*reverse*) entrenado por una red neuronal para eliminar dicho ruido y reconstruir una imagen nítida. El panorama actual culmina en la convergencia de ambos mundos: el uso de transformers aplicados a los procesos de difusión.

#### 4. Aprendizaje por Refuerzo y Alineación Humana (RL y RLHF)

Se introduce el **Aprendizaje por Refuerzo (RL)** como un paradigma donde un agente interactúa con un entorno dinámico, tomando decisiones basadas en la exploración y la explotación para maximizar una recompensa acumulada a largo plazo (retornos) a través de distintas trayectorias. Esta metodología es la base del **RLHF** (Aprendizaje por Refuerzo a partir de la Retroalimentación Humana), un proceso crítico de alineación donde se entrena un modelo de recompensa a partir de las preferencias de evaluadores humanos para refinar el comportamiento de los modelos lingüísticos, asegurando que sean útiles y seguros.

#### 5. Modelos de Lenguaje Grandes (LLMs)

El documento conceptualiza los **LLMs** como sistemas avanzados dedicados a la comprensión y generación de lenguaje natural. Se detalla de forma precisa su ciclo de desarrollo y entrenamiento, el cual consta de tres etapas secuenciales e indispensables:

1. **Pre-entrenamiento:** El aprendizaje base a gran escala mediante la predicción del próximo token sobre volúmenes masivos de datos textuales.
2. **Ajuste fino supervisado (*Fine-tuning*):** El entrenamiento especializado con ejemplos curados de preguntas y buenas respuestas.
3. **RLHF:** La optimización final basada en las preferencias y directrices del criterio humano.

#### 6. Fronteras Tecnológicas y Tendencias Actuales (2026)

Hacia el cierre, el material proyecta el estado del arte técnico, caracterizado por una evolución hacia la autonomía y la eficiencia:

* **Sistemas RAG y Agentes:** La integración de la Generación Aumentada por Recuperación (RAG) para conectar los modelos con fuentes externas de conocimiento, y el diseño de agentes autónomos capaces de descomponer y ejecutar tareas complejas de múltiples pasos.
* **Modelos de Razonamiento:** Sistemas diseñados para "pensar" y evaluar alternativas antes de emitir una respuesta, trasladando una mayor carga de cómputo hacia la fase de inferencia.
* **Eficiencia Arquitectónica:** El uso de estructuras del tipo *Mixture-of-Experts* (MoE), que activan solo subconjuntos del modelo para mantener la potencia reduciendo el costo computacional, acompañado de capacidades para procesar contextos de longitud extendida.
* **Multimodalidad Nativa y Robótica:** Modelos construidos desde su origen para asimilar y combinar simultáneamente texto, imagen, audio y video, sirviendo de puente para tecnologías avanzadas como los modelos VLA (Vision-Language-Action) y su aplicación directa en la robótica y la interacción con el mundo físico.

[🔙 Inicio de la unidad](../readme.md)


