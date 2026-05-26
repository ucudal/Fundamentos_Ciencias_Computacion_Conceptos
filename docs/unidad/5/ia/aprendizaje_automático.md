# Unidad 5. Aprendizaje Automático

## Guía docente y notas de clase ampliadas

### Fundamentos en Ciencias de la Computación

---

## Introducción general a la unidad

Esta unidad tiene como propósito introducir al estudiante en el universo conceptual del aprendizaje automático, partiendo desde la materia prima de toda la disciplina, el dato, hasta llegar a las nociones más sutiles relativas a la calidad y los límites de los modelos predictivos.
Acceso a las diapositivas mediante: https://canva.link/agn8zrp4c4hf24l 

---

## 1. El ciclo de vida del dato

### El dato como materia prima

Toda discusión seria sobre aprendizaje automático debe comenzar reconociendo que el dato no es un punto de partida neutro ni espontáneo. El dato es el resultado de decisiones previas: alguien decidió qué medir, cómo medirlo, con qué instrumentos, en qué condiciones y con qué frecuencia. Este principio, que parece obvio, suele ser ignorado en la enseñanza tradicional y constituye una de las fuentes más fértiles de errores en proyectos reales. Conviene insistir desde el primer momento en que un modelo nunca puede ser mejor que los datos que lo alimentan, y que los datos siempre llevan consigo las huellas del proceso social y técnico que los produjo.

### Las siete etapas

El esquema presentado en la diapositiva describe el ciclo en siete etapas, que conviene introducir como un marco mental flexible y no como una receta lineal. En la práctica, las etapas se solapan, retroalimentan y se visitan varias veces. La presentación cíclica subraya precisamente esa naturaleza iterativa.

La **comprensión del negocio** es la etapa donde se traducen necesidades organizacionales en preguntas susceptibles de ser respondidas con datos. Aquí conviene transmitir que la mayoría de los proyectos de aprendizaje automático fracasan no por razones técnicas, sino porque la pregunta de negocio nunca fue formulada con suficiente precisión. Una analogía útil es la de un médico que receta sin diagnosticar. Pedir al estudiante que reformule un objetivo vago como "queremos predecir el churn de clientes" en una pregunta operacional concreta es un ejercicio enormemente productivo.

La **extracción y recolección del dato**, también llamada minería de datos en el esquema, comprende todas las técnicas para obtener los datos desde sus fuentes originales. Es importante señalar que esta etapa no es solamente técnica: implica también decisiones legales, éticas y de privacidad que pueden condicionar todo el proyecto. En esta etapa surgen también las primeras decisiones sobre representatividad del muestreo, que tendrán consecuencias profundas en etapas posteriores.

La **limpieza del dato** es la etapa que ocupa, según las estimaciones más citadas en la industria, entre el sesenta y el ochenta por ciento del tiempo total de un proyecto de ciencia de datos. Aquí se enfrentan valores faltantes, inconsistencias entre fuentes, duplicaciones, errores de tipeo, formatos heterogéneos y cualquier patología imaginable del dato. Conviene transmitir al estudiante que esta etapa no es un trámite, sino una actividad intelectualmente exigente donde se toman decisiones que afectan los resultados finales. La pregunta "¿qué hago con los valores faltantes?" no tiene una respuesta única, y la elección entre imputar, eliminar o tratar el faltante como una categoría informativa depende del problema concreto.

La **exploración de los datos** es la fase donde el analista forma hipótesis a partir de visualizaciones y estadísticas descriptivas. Es una etapa de pensamiento divergente y curiosidad, donde se buscan patrones, anomalías, correlaciones inesperadas y relaciones entre variables. Conviene presentarla al estudiante como un diálogo con los datos, no como una rutina de comandos. La capacidad de hacerse preguntas útiles frente a un conjunto de datos es una habilidad que se cultiva con el tiempo.

La **ingeniería de variables**, conocida como feature engineering, es la etapa donde se construyen representaciones más informativas a partir de las variables crudas. Esta etapa concentra gran parte del valor agregado humano en proyectos clásicos de aprendizaje automático, y suele marcar la diferencia entre un modelo mediocre y uno excelente. Un ejemplo intuitivo es transformar una fecha de nacimiento en una edad, una variable mucho más útil para casi cualquier modelo. En el contexto del aprendizaje profundo moderno, esta etapa pierde parcialmente peso porque las redes aprenden representaciones automáticamente, pero sigue siendo relevante en la mayoría de los problemas tabulares.

El **modelado predictivo** es donde finalmente se entrenan los algoritmos, se evalúan y se comparan. Conviene desmitificar esta etapa ante los estudiantes, ya que suele ser percibida como el corazón del trabajo cuando en realidad ocupa una fracción menor del tiempo en un proyecto bien llevado. Una buena heurística para transmitir es que si el modelado lleva más tiempo que la limpieza, probablemente algo se está haciendo mal.

La **visualización y comunicación de resultados** es la etapa final, donde los hallazgos se traducen en formato comprensible para tomadores de decisión que no son técnicos. Aquí entra en juego la capacidad narrativa del analista. Un resultado que no logra ser entendido por quien debe usarlo, no existe a efectos prácticos.

### El ciclo como espiral

Vale la pena cerrar esta sección advirtiendo al estudiante que en la práctica el ciclo casi nunca se recorre una sola vez. Es más realista pensarlo como una espiral, donde cada vuelta refina la comprensión del problema, mejora los datos, ajusta los modelos y produce mejores comunicaciones. La idea de un proceso lineal con un final claro es una simplificación útil, pero no debe consolidarse como creencia.

---

## 2. Los roles profesionales del ecosistema de datos

### Una geografía de competencias

El diagrama de Venn de la diapositiva ilustra una verdad importante del mercado laboral actual. Las profesiones del ecosistema de datos se definen no por una habilidad única, sino por la intersección de varias dimensiones de competencia: comunicación, matemáticas, programación y comprensión de negocio. Cada rol ocupa una región distinta del espacio de habilidades, y conviene presentarlo así porque resulta más realista y más útil que listas cerradas de tareas.

### Data Engineer

El **ingeniero de datos** es responsable de la infraestructura que mueve, almacena y procesa los datos en una organización. Diseña y mantiene los flujos que llevan datos desde sus fuentes hasta los lugares donde otros profesionales los consumen. Sus herramientas típicas incluyen sistemas de orquestación de flujos como Airflow, motores de transformación como dbt, frameworks de procesamiento distribuido como Spark, y bases de datos de distintos tipos. Su perfil combina fuertemente programación y comprensión de sistemas, con menor énfasis en matemática estadística. Una analogía útil es la del ingeniero de tuberías: sin su trabajo nada fluye, pero su trabajo es invisible cuando funciona bien.

### Data Analyst

El **analista de datos** ocupa el cruce entre comunicación y negocio, con bases técnicas en programación y estadística descriptiva. Su tarea principal es responder preguntas de negocio a partir de datos existentes, generalmente mediante consultas, paneles de visualización e informes. A diferencia del científico de datos, su trabajo tiende a centrarse en describir lo que ocurrió, más que en predecir lo que ocurrirá. Esta distinción no es absoluta y los roles a menudo se solapan, especialmente en organizaciones pequeñas.

### Data Scientist

El **científico de datos** se sitúa en una intersección amplia entre matemáticas, programación y negocio. Su trabajo combina formulación de hipótesis, análisis estadístico, construcción de modelos predictivos y comunicación de hallazgos. En la práctica, este rol se ha diversificado mucho desde su popularización, y bajo el mismo título conviven perfiles muy distintos. Conviene transmitir al estudiante que el rol genérico está dando paso a especializaciones más precisas.

### Machine Learning Engineer

El **ingeniero de machine learning** combina las habilidades de un ingeniero de software con conocimiento profundo de modelos de aprendizaje automático. Se ocupa de llevar modelos desde el cuaderno experimental hasta sistemas en producción, escalables, monitoreados y mantenibles. Esta especialización ha crecido enormemente en los últimos años porque la industria descubrió que un modelo en un notebook no es un modelo en producción, y que el camino entre uno y otro requiere competencias específicas. Conviene mencionar la disciplina emergente de MLOps, que sistematiza este tránsito.

### El profesional ideal y la realidad

El centro del diagrama, el llamado ingeniero ideal, ocupa todas las intersecciones. Es importante señalar al estudiante que este perfil es una ficción útil más que una realidad alcanzable. Nadie domina todas las dimensiones al mismo nivel, y los equipos exitosos suelen construir su fortaleza precisamente en la complementariedad de perfiles especializados. Una pregunta productiva es preguntar al estudiante en qué región del diagrama se imagina, y qué dimensiones querría reforzar.

---

## 3. Arquitectura de datos: Data Lake, Data Warehouse y Data Marts

### La necesidad de organizar el dato

Antes de introducir los conceptos específicos, conviene problematizar la situación inicial. En una organización moderna, los datos no provienen de una única fuente sino de muchas: registros web, bases transaccionales, archivos generados por dispositivos del internet de las cosas, redes sociales y documentos en formatos diversos como JSON, CSV o PDF. Sin una arquitectura adecuada, esta heterogeneidad se vuelve inmanejable. La diapositiva presenta un esquema canónico que resuelve este problema mediante una serie de capas con propósitos diferenciados.

### Data Lake

El **lago de datos** es el repositorio donde se almacenan los datos crudos en su formato original, sin transformaciones previas significativas. Su característica esencial es la capacidad de absorber grandes volúmenes de información heterogénea, estructurada, semiestructurada o no estructurada. La filosofía del lago de datos es preservar la materia prima sin perder información, dejando para etapas posteriores la decisión sobre cómo procesarla. La metáfora del lago es deliberada: a diferencia de un depósito ordenado, el agua entra mezclada y se acumula sin clasificación previa.

Esta flexibilidad tiene un costo. Sin disciplina, un lago de datos puede convertirse en un pantano de datos, donde nadie sabe qué hay ni cómo está estructurado. La gobernanza, los metadatos y los catálogos de datos son herramientas indispensables para que un lago siga siendo útil con el tiempo.

### Procesos ETL y ELT

Entre las fuentes y los repositorios analíticos operan los procesos de **ingesta y transformación**. La sigla ETL refiere a extraer, transformar y cargar, mientras que la variante moderna ELT invierte el orden y carga primero los datos crudos para transformarlos después dentro del propio repositorio. La distinción no es meramente técnica: refleja un cambio en la economía del cómputo y el almacenamiento, donde resulta más barato guardar todo y transformar bajo demanda que decidir por adelantado qué se necesitará.

### Data Warehouse

El **almacén de datos** es la capa donde la información ya ha sido procesada, integrada, normalizada y limpiada. A diferencia del lago, aquí los datos están estructurados, tipados y conectados mediante esquemas relacionales. El almacén funciona como única fuente de verdad para la organización: cuando el departamento de finanzas y el departamento de marketing consultan información sobre los mismos clientes, encuentran cifras consistentes porque ambos se alimentan del mismo origen procesado. Es importante destacar este punto al estudiante porque captura algo profundo sobre la maduración de una organización: las decisiones basadas en datos solo son posibles cuando los datos son consistentes entre las distintas áreas que los usan.

### Data Marts

Los **mercados de datos** son subconjuntos del almacén orientados a usuarios o departamentos específicos. Cada departamento, por ejemplo ventas, finanzas o recursos humanos, recibe una vista especializada que contiene solo los datos relevantes para sus análisis. Esta organización resuelve varios problemas a la vez: mejora el desempeño de las consultas porque cada mart es más pequeño que el almacén completo, simplifica el acceso porque cada usuario solo ve lo que le concierne, y aumenta la seguridad porque limita la exposición de información sensible.

### Quién consume cada capa

Conviene cerrar señalando quién utiliza cada capa de esta arquitectura. Los científicos de datos y los ingenieros de machine learning suelen trabajar tanto con el lago como con el almacén, porque a veces necesitan información cruda que no llegó a procesarse. Los analistas de negocio, en cambio, suelen consumir principalmente los marts especializados de su área. Esta diferencia explica por qué los roles requieren competencias distintas y por qué la arquitectura debe servir a perfiles diversos.

---

## 4. Conceptos clave del dato para el aprendizaje automático

### El dataset como tabla

Una vez introducida la infraestructura, corresponde detenerse en cómo se presenta el dato al modelo. La representación más habitual es la de una tabla bidimensional. Aunque existen formatos más complejos, como tensores multidimensionales para imágenes o secuencias de longitud variable para texto, la tabla sigue siendo el caso canónico, especialmente en problemas tabulares clásicos de la industria.

### Instancia

Una **instancia**, también llamada ejemplo, observación o muestra, corresponde a una fila individual del conjunto de datos. Representa un caso particular sobre el cual se medirá o se predecirá algo. En el ejemplo de la diapositiva, cada fila representa a un conductor con sus atributos. Es importante hacer notar al estudiante que cada instancia es independiente del resto en los supuestos habituales del aprendizaje supervisado clásico. Esta suposición de independencia entre instancias, conocida como hipótesis de muestras independientes e idénticamente distribuidas, está implícita en la mayoría de las garantías teóricas de la disciplina, y conviene mencionarla aunque sea brevemente.

### Feature

Una **variable de entrada**, también llamada atributo, predictor o feature, es una columna del conjunto de datos que se usa como insumo del modelo. Las features pueden ser numéricas, categóricas, ordinales, temporales o textuales, y cada tipo requiere preprocesamiento específico antes de ser ingerido por un modelo. En el ejemplo presentado, edad y potencia son features numéricas, mientras que sexo y marca del coche son features categóricas que requerirán codificación adecuada.

Una distinción que merece atención es la diferencia entre variable cruda y feature. Una variable cruda es lo que aparece en la fuente original, mientras que una feature es lo que efectivamente se entrega al modelo, posiblemente después de transformaciones. La fecha de obtención del carné, por ejemplo, puede transformarse en años de experiencia al volante, una feature potencialmente más informativa.

### Label

El **label**, también llamado target, variable objetivo o variable dependiente, es la columna que el modelo intenta predecir a partir de las features. En el ejemplo, la columna sobre si el conductor tuvo accidentes es el label que el modelo aprenderá a predecir. Conviene destacar que la naturaleza del label determina el tipo de problema: cuando el label toma valores discretos hablamos de clasificación, cuando toma valores continuos hablamos de regresión.

### Notación matemática

Es buen momento para introducir la notación habitual. Las features se agrupan en una matriz que suele denotarse con la letra X mayúscula, donde cada fila es una instancia y cada columna una variable. El label se agrupa en un vector denotado con y minúscula. Esta convención es ubicua en la literatura y en el código, y dominarla facilita la lectura de cualquier material posterior. Una confusión común entre estudiantes es entre la X mayúscula como matriz y la x minúscula como una instancia individual, distinción que conviene aclarar desde el principio.

---

## 5. Aprendizaje supervisado y no supervisado

### La distinción fundamental

El aprendizaje automático suele dividirse en paradigmas según la naturaleza de la supervisión disponible durante el entrenamiento. Esta clasificación no es meramente taxonómica sino que tiene consecuencias profundas sobre qué se puede aprender, cómo se evalúa el aprendizaje y para qué problemas es adecuado cada paradigma.

### Aprendizaje supervisado

El **aprendizaje supervisado** es el paradigma donde el modelo aprende a partir de pares entrada-salida conocidos. Cada instancia del conjunto de entrenamiento incluye tanto sus features como su label correcto, y el algoritmo busca una función que aproxime esa correspondencia tan bien como sea posible. La palabra supervisión refiere precisamente a la presencia de esas respuestas conocidas, que funcionan como un docente que corrige al modelo durante su aprendizaje.

Una manera intuitiva de presentar este paradigma es compararlo con un estudiante que aprende con un libro de ejercicios resueltos. Después de practicar con muchos ejercicios cuya respuesta conoce, el estudiante adquiere la capacidad de resolver ejercicios nuevos cuyas respuestas no ha visto. El supuesto detrás de esta analogía, y detrás del aprendizaje supervisado en general, es que los problemas futuros pertenecen a la misma distribución que los problemas pasados. Cuando este supuesto se rompe, el modelo falla, y este es uno de los problemas más sutiles y persistentes en la disciplina.

Ejemplos típicos de aprendizaje supervisado incluyen la clasificación de correos como spam o no spam, la predicción del precio de una vivienda a partir de sus características, el diagnóstico médico a partir de imágenes radiológicas y la detección de fraude en transacciones financieras.

### Aprendizaje no supervisado

El **aprendizaje no supervisado** es el paradigma donde el modelo recibe únicamente las features, sin labels asociados. Su tarea es descubrir estructura latente en los datos: agrupamientos naturales, dimensiones de variación, asociaciones inesperadas o anomalías. La ausencia de supervisión implica también la ausencia de una métrica obvia de éxito, y por eso la evaluación de modelos no supervisados es notoriamente más difícil.

Una buena analogía es la del antropólogo que llega a una sociedad desconocida sin diccionario. Debe agrupar comportamientos, identificar patrones y proponer categorías sin tener acceso a las respuestas correctas. El criterio de éxito es la coherencia interna y la utilidad explicativa de las categorías propuestas, no su correspondencia con respuestas predefinidas.

Aplicaciones típicas incluyen la segmentación de clientes, donde se descubren grupos con comportamientos similares sin saber de antemano cuáles serán esos grupos; la reducción de dimensionalidad, donde se busca representar datos complejos en espacios más manejables; y la detección de anomalías, donde se identifican observaciones que no se ajustan a los patrones predominantes.

### Otros paradigmas

Aunque no aparecen explícitamente en la diapositiva, conviene mencionar al menos en passing otros dos paradigmas que el estudiante encontrará en su carrera. El **aprendizaje semi-supervisado** combina pocos datos etiquetados con muchos datos no etiquetados, aprovechando la estructura de estos últimos para mejorar lo aprendido de los primeros. El **aprendizaje por refuerzo** es radicalmente distinto: aquí el modelo, llamado agente, interactúa con un entorno tomando acciones y recibiendo recompensas, aprendiendo políticas de comportamiento mediante prueba y error. Este último paradigma es la base de muchos sistemas de juego, robótica y control automático.

---

## 6. El concepto de modelo

### Una función con parámetros

La diapositiva introduce el modelo mediante la fórmula y igual a f de x con parámetros theta. Esta expresión, aparentemente simple, condensa toda la idea del aprendizaje automático y merece detenerse en ella.

La letra f denota una **familia de funciones**, es decir, una clase de transformaciones posibles entre la entrada x y la salida y. La estructura de f está fijada por el ingeniero al momento de elegir el tipo de modelo. Una regresión lineal, una red neuronal y un árbol de decisión son tres familias de funciones distintas, cada una con su propia capacidad expresiva.

El parámetro x representa la **entrada** al modelo, que puede ser un vector de features tabulares, una imagen, un texto, un audio o cualquier otra representación numérica.

La letra griega theta, que se lee tita, representa los **parámetros internos** del modelo. Estos parámetros son los grados de libertad que el algoritmo de entrenamiento ajusta. En una regresión lineal son los coeficientes y el término independiente; en una red neuronal son los pesos y los sesgos de cada neurona; en un árbol son los puntos de corte y las clases asignadas en las hojas. La distinción entre la familia f y los parámetros theta es absolutamente central: la familia se elige a priori, los parámetros se aprenden.

Finalmente, y es la **salida del modelo**: una predicción que puede ser una etiqueta de clase, un valor numérico, una probabilidad o cualquier otra cosa según el problema.

### El entrenamiento como búsqueda

Conviene presentar el entrenamiento como una búsqueda. Fijada la familia f, el problema consiste en encontrar los valores de theta que hacen que las predicciones del modelo sobre los datos de entrenamiento se parezcan lo más posible a los labels conocidos. Esta búsqueda se formaliza mediante una **función de pérdida** que mide qué tan mal lo está haciendo el modelo, y un **algoritmo de optimización**, típicamente alguna variante del descenso por gradiente, que ajusta theta para reducir esa pérdida.

Una pregunta frecuente del estudiante es por qué no se prueban todas las combinaciones posibles de parámetros. La respuesta es que el espacio de parámetros es astronómico. Una red neuronal moderna puede tener miles de millones de parámetros, y aun una familia mucho más modesta es imposible de explorar exhaustivamente. La optimización inteligente es lo que hace viable el aprendizaje.

### Parámetros frente a hiperparámetros

Otra distinción que conviene introducir aunque no aparezca explícitamente en la diapositiva es la diferencia entre **parámetros** e **hiperparámetros**. Los parámetros son los grados de libertad que se ajustan durante el entrenamiento. Los hiperparámetros son configuraciones que el ingeniero fija antes de entrenar, como la cantidad de capas de una red, el ritmo de aprendizaje o la profundidad de un árbol. Los primeros se aprenden, los segundos se eligen, y la elección de hiperparámetros suele ser tan importante para el desempeño final como la elección de la familia misma.

---

## 7. División de los datos: entrenamiento, validación y prueba

### Por qué no basta con un solo conjunto

Una pregunta natural de un estudiante recién iniciado es por qué los datos se dividen en tres conjuntos. La respuesta requiere entender qué quiere lograrse: no basta con que un modelo funcione bien sobre los datos que vio durante el entrenamiento, sino que debe funcionar bien sobre datos nuevos. Esta capacidad de funcionar sobre datos no vistos se llama generalización, y es el verdadero objetivo del aprendizaje automático. Un modelo que memoriza perfectamente los datos de entrenamiento pero falla sobre datos nuevos es inútil.

Para medir la capacidad de generalización honestamente, es necesario reservar datos que el modelo no haya usado en ninguna etapa de su construcción. De ahí surge la práctica de dividir el conjunto original.

### Conjunto de entrenamiento

El **conjunto de entrenamiento** es la porción más grande del dataset, típicamente entre el sesenta y el ochenta por ciento, sobre la cual el algoritmo ajusta los parámetros del modelo. Es el material sobre el cual el modelo aprende efectivamente.

### Conjunto de validación

El **conjunto de validación**, también llamado conjunto de desarrollo, es una porción intermedia que se usa para tomar decisiones durante el desarrollo del modelo: comparar arquitecturas alternativas, ajustar hiperparámetros, decidir cuándo detener el entrenamiento, evaluar técnicas de regularización. El nombre validación puede confundir al estudiante, porque no se trata de validar el modelo final sino de validar las decisiones intermedias. Es importante señalar que aunque el modelo no entrena directamente sobre este conjunto, sí lo usa indirectamente a través de las decisiones que se toman mirándolo, por lo cual no constituye una evaluación verdaderamente independiente.

### Conjunto de prueba

El **conjunto de prueba**, también llamado conjunto de test, es la porción reservada para la evaluación final, una vez que todas las decisiones de modelado han sido tomadas. Debe usarse una única vez. Si se usa repetidamente para comparar modelos y elegir el mejor, deja de funcionar como evaluación honesta y se convierte, de facto, en un segundo conjunto de validación. Este error es muy común entre principiantes y vale la pena enfatizarlo con fuerza.

### Una analogía didáctica

Una analogía útil es la del estudiante que se prepara para un examen. El conjunto de entrenamiento son los ejercicios que practica durante el curso. El conjunto de validación son los simulacros de examen que hace para identificar sus debilidades y ajustar su estrategia de estudio. El conjunto de prueba es el examen final real, que enfrenta una sola vez y cuya nota es la medida honesta de su aprendizaje. Si el estudiante consigue de antemano el examen final y lo practica, su nota dejará de reflejar su conocimiento real.

### Consideraciones adicionales

Conviene mencionar al estudiante que cuando los datos son escasos, la división en tres conjuntos puede no ser práctica, y se recurre a técnicas como la validación cruzada, donde el conjunto de entrenamiento se rota sistemáticamente para hacer mejor uso de los datos disponibles. También conviene advertir que la división aleatoria simple no siempre es adecuada: en series temporales, por ejemplo, debe respetarse el orden cronológico, porque entrenar con datos futuros y evaluar con datos pasados es una forma de fuga de información que infla artificialmente el desempeño aparente del modelo.

---

## 8. Las técnicas fundamentales del aprendizaje automático

### Tres familias canónicas

La diapositiva presenta tres técnicas que cubren la mayor parte de los problemas que un practicante encuentra en sus primeros años: clasificación, regresión y agrupamiento. Las dos primeras pertenecen al paradigma supervisado y la tercera al no supervisado. Esta tripartición es una excelente puerta de entrada para organizar mentalmente el campo, aunque conviene aclarar que el ecosistema completo de técnicas es mucho más rico.

### Clasificación

La **clasificación** es el problema de asignar cada instancia a una de varias categorías predefinidas. El ejemplo de la diapositiva, distinguir adultos de niños a partir de altura y peso, es un caso de clasificación binaria. Cuando las categorías son más de dos hablamos de clasificación multiclase, y cuando una instancia puede pertenecer a varias categorías simultáneamente hablamos de clasificación multietiqueta.

El objetivo geométrico de un clasificador puede visualizarse como el trazado de fronteras de decisión que separan el espacio de features en regiones, cada una asociada a una clase. Modelos distintos producen fronteras de formas distintas: una regresión logística traza fronteras lineales, un árbol de decisión traza fronteras rectangulares paralelas a los ejes, una máquina de soporte vectorial con núcleo radial puede trazar fronteras curvas y suaves.

Aplicaciones típicas incluyen la detección de spam, el diagnóstico médico, la identificación de imágenes, el reconocimiento de voz y la verificación de identidad.

### Regresión

La **regresión** es el problema de predecir un valor numérico continuo. El ejemplo de la diapositiva, predecir un beneficio a partir de una inversión, es ilustrativo. A diferencia de la clasificación, la salida no es una etiqueta de un conjunto finito sino un número que puede tomar infinitos valores. Esto cambia tanto la métrica de evaluación como la naturaleza de los modelos aplicables.

Geométricamente, un modelo de regresión busca una función, frecuentemente una curva o superficie, que se ajuste lo mejor posible a la nube de puntos. La regresión lineal, históricamente la primera técnica del aprendizaje automático y todavía una de las más usadas, asume que la relación entre features y target es aproximadamente lineal.

Aplicaciones típicas incluyen la predicción de precios, la estimación de demanda, la previsión meteorológica, el pronóstico financiero y la estimación de tiempos de viaje.

### Agrupamiento

El **agrupamiento**, conocido también como clustering, es el problema de descubrir grupos naturales dentro de un conjunto de datos sin labels. A diferencia de la clasificación, las categorías no están predefinidas: el algoritmo debe descubrirlas. Esto cambia profundamente la naturaleza del problema. No hay una respuesta correcta única, sino soluciones más o menos coherentes según el criterio de similitud que se adopte.

El ejemplo de la diapositiva muestra dos grupos de individuos separados según peso y altura. En la práctica, los grupos descubiertos por un algoritmo de clustering deben ser luego interpretados por un analista humano, que les asigna significado a partir de las características compartidas dentro de cada grupo.

Aplicaciones típicas incluyen la segmentación de mercados, el análisis de comportamiento de usuarios, la organización automática de documentos y la identificación de comunidades en redes sociales.

### Una advertencia conceptual 

Es frecuente que los estudiantes confundan clasificación con agrupamiento porque ambos parecen relacionados con la idea de categorías. La distinción es crítica. En clasificación, las categorías están dadas de antemano y el modelo aprende a asignar nuevas instancias a esas categorías conocidas. En agrupamiento, no hay categorías de antemano y el modelo las descubre. Una manera memorable de fijar la distinción es decir que en clasificación las cajas existen y hay que repartir las cosas, mientras que en agrupamiento las cosas existen y hay que inventar las cajas.

---

## 9. Métricas de evaluación

### La pregunta fundamental

Una vez entrenado un modelo, ¿cómo sabemos si es bueno? Esta pregunta es menos trivial de lo que parece. La medida adecuada de la calidad de un modelo depende del problema, de los costos relativos de distintos tipos de errores y del contexto de uso. Reducir la evaluación a un único número siempre implica una pérdida de información, y es responsabilidad del analista entender qué información pierde con cada métrica.

### Accuracy

La **exactitud**, también llamada accuracy, es la métrica más intuitiva: la proporción de predicciones correctas sobre el total de predicciones. Es directa de calcular e interpretar, pero esconde un problema serio cuando las clases están desbalanceadas. Si en un problema de detección de fraude el noventa y nueve por ciento de las transacciones son legítimas, un modelo que prediga siempre legítimo alcanzará una exactitud del noventa y nueve por ciento, sin haber detectado un solo fraude. Este ejemplo, que conviene presentar al estudiante con cierta dramatización, ilustra por qué la exactitud puede ser engañosa y por qué se necesitan métricas complementarias.

### Precision

La **precisión**, en el sentido específico del aprendizaje automático, mide entre las instancias que el modelo etiquetó como positivas, qué proporción lo era realmente. Una precisión alta significa que cuando el modelo dice positivo, generalmente acierta. Esta métrica es crítica en contextos donde los falsos positivos tienen alto costo. Un ejemplo es la recomendación de tratamientos médicos invasivos: cada falso positivo implica someter a un paciente sano a un procedimiento innecesario.

### Recall

La **sensibilidad**, también llamada recall o tasa de verdaderos positivos, mide entre las instancias que eran realmente positivas, qué proporción detectó el modelo. Una sensibilidad alta significa que el modelo no se le escapan los positivos verdaderos. Esta métrica es crítica en contextos donde los falsos negativos son costosos. La detección de cáncer es el ejemplo paradigmático: dejar pasar un caso real puede ser fatal, mientras que un falso positivo solo implica análisis adicionales.

### La tensión entre precisión y sensibilidad

Una intuición central que conviene transmitir es que precisión y sensibilidad están en tensión. Un modelo muy conservador, que solo predice positivo cuando está muy seguro, tendrá alta precisión pero baja sensibilidad. Un modelo muy permisivo, que predice positivo a la menor señal, tendrá alta sensibilidad pero baja precisión. La elección del balance correcto depende del problema. La métrica F1, definida como la media armónica entre precisión y sensibilidad, es una manera habitual de combinarlas en un solo número, aunque oculta el balance específico elegido.

---

## 10. Matriz de confusión

### Estructura y lectura

La **matriz de confusión** es una herramienta visual y conceptual de enorme valor, porque hace tangibles los conceptos abstractos de las métricas anteriores. En el caso binario, organiza las predicciones en una tabla de dos por dos según la combinación entre clase real y clase predicha.

En la esquina superior izquierda aparecen los **verdaderos positivos**, instancias positivas que el modelo predijo correctamente. En la esquina inferior derecha aparecen los **verdaderos negativos**, instancias negativas correctamente predichas. La diagonal principal, formada por estas dos celdas, representa los aciertos del modelo. Las otras dos celdas, fuera de la diagonal, representan los errores.

Los **falsos positivos** son instancias negativas que el modelo predijo como positivas, conocidos en estadística clásica como error de tipo uno. Los **falsos negativos** son instancias positivas que el modelo predijo como negativas, conocidos como error de tipo dos. La nomenclatura proviene de la teoría de prueba de hipótesis y conviene mencionarla porque conecta con cursos previos de estadística que los estudiantes pueden haber tenido.

### Reconstrucción de las métricas

Desde la matriz de confusión pueden reconstruirse todas las métricas presentadas anteriormente. La exactitud es la suma de la diagonal sobre el total. La precisión es la primera celda dividida por la suma de la primera columna. La sensibilidad es la primera celda dividida por la suma de la primera fila. Esta visualización unificada ayuda a fijar las definiciones y a entender por qué cada métrica captura un aspecto diferente del desempeño.

### Costo asimétrico de los errores

Una discusión importante para mantener con los estudiantes es que los dos tipos de error no suelen tener el mismo costo. Confundir un correo legítimo con spam, perdiéndolo en la papelera, puede ser muy distinto de dejar pasar un correo de spam a la bandeja principal. Confundir un peatón con un poste, en el sistema de visión de un automóvil autónomo, es radicalmente distinto de confundir un poste con un peatón. Esta asimetría debe guiar la elección de la métrica principal y, en muchos casos, la calibración del modelo más allá del umbral de decisión por defecto.

### Generalización a múltiples clases

En problemas multiclase, la matriz de confusión se convierte en una matriz cuadrada de tamaño igual al número de clases. La diagonal sigue representando los aciertos, pero las celdas fuera de la diagonal informan qué clases se confunden con qué otras. Este análisis cualitativo es enormemente valioso: a veces dos clases distintas son sistemáticamente confundidas, lo que puede sugerir que el modelo carece de información discriminante o que las clases en realidad no son tan distintas como suponía el etiquetado.

---

## 11. Limitaciones estructurales: ruido, sesgo y varianza

### Tres fuentes irreductibles de error

Una vez introducida la maquinaria de los modelos y su evaluación, corresponde hablar de sus límites. Toda inteligencia artificial moderna sufre, en mayor o menor grado, tres fuentes de error: ruido, sesgo y varianza. La descomposición del error total en estos tres componentes es uno de los resultados teóricos más importantes del aprendizaje automático clásico y proporciona un vocabulario preciso para hablar de las fallas de los modelos.

### Ruido

El **ruido** es la variabilidad intrínseca del fenómeno que se intenta predecir. Para una misma entrada, la salida verdadera puede ser distinta porque el mundo no es completamente determinista, porque las variables que determinarían la salida no están todas disponibles o porque la medición misma introduce variabilidad. El ruido es irreducible: ningún modelo, por sofisticado que sea, puede predecir lo impredecible. La gráfica de la diapositiva muestra puntos de datos dispersos alrededor de la función verdadera. Esa dispersión es el ruido, y representa el límite inferior teórico del error que cualquier modelo puede alcanzar.

Es importante transmitir al estudiante que no todo error de un modelo refleja una falla del modelo. Parte del error proviene del fenómeno mismo. Reconocer esta cuota irreducible evita la búsqueda infructuosa de un modelo perfecto donde no puede existir.

### Sesgo

El **sesgo**, también llamado bias, refiere a la incapacidad del modelo, dada su estructura, de capturar la verdadera relación entre entrada y salida. Un modelo con alto sesgo es demasiado simple para el problema: sus predicciones son sistemáticamente desviadas, incluso después de un entrenamiento perfecto sobre datos sin ruido. La gráfica de la diapositiva muestra una recta intentando ajustar una función curva: por más datos que recibamos, una recta nunca podrá capturar la curvatura. Esto es sesgo.

El sesgo aparece típicamente cuando se elige una familia de modelos demasiado restrictiva para la complejidad del problema. Se diagnostica observando que tanto el error de entrenamiento como el error de prueba son altos. La cura del sesgo pasa por usar modelos más expresivos, agregar features informativas o construir representaciones más ricas.

### Varianza

La **varianza** refiere a la sensibilidad del modelo ajustado al conjunto particular de datos de entrenamiento usado. Un modelo con alta varianza ajusta soluciones muy distintas cada vez que cambia ligeramente el conjunto de entrenamiento, lo que indica que está capturando idiosincrasias específicas del conjunto en lugar de regularidades generales. La gráfica de la diapositiva muestra una función ajustada que se contorsiona para pasar cerca de cada punto de entrenamiento, perdiendo de vista la forma subyacente.

La alta varianza aparece típicamente cuando el modelo es demasiado expresivo para la cantidad de datos disponible. Se diagnostica observando que el error de entrenamiento es bajo pero el error de prueba es alto. La cura pasa por usar modelos más simples, recolectar más datos, aplicar técnicas de regularización o usar ensambles.

### La descomposición clásica

Para los estudiantes con base matemática suficiente, conviene mencionar que el error esperado de un modelo puede descomponerse, bajo ciertas hipótesis, en una suma de tres términos: el cuadrado del sesgo, la varianza y el ruido irreducible. Esta descomposición no es solo un resultado teórico elegante, sino una guía práctica para el diagnóstico: identificar cuál de los tres términos domina permite saber qué tipo de intervención tiene chances de mejorar el modelo.

---

## 12. El compromiso entre sesgo y varianza

### La tensión central del aprendizaje automático

El **compromiso entre sesgo y varianza** captura una tensión fundamental que atraviesa todo el aprendizaje automático. En general, las acciones que reducen el sesgo aumentan la varianza, y viceversa. Aumentar la complejidad del modelo reduce el sesgo porque amplía las funciones que puede representar, pero aumenta la varianza porque le da más capacidad para sobreajustarse a los datos. Simplificar el modelo hace lo contrario.

El analista debe encontrar el punto de equilibrio donde el error total es mínimo. Este punto no es fijo: depende de la complejidad del problema, de la cantidad y calidad de los datos disponibles y de los hiperparámetros elegidos. Encontrarlo es, en última instancia, una habilidad artesanal que se desarrolla con la experiencia.

### Underfitting, ajuste correcto y overfitting

Conviene introducir explícitamente los tres regímenes que conectan con la discusión anterior. El **underfitting**, o subajuste, es la situación donde el modelo es demasiado simple: presenta alto sesgo, su error de entrenamiento es alto y su error de prueba también lo es. El **overfitting**, o sobreajuste, es la situación donde el modelo es demasiado complejo: presenta alta varianza, su error de entrenamiento es muy bajo pero su error de prueba es considerablemente mayor. Entre ambos extremos se encuentra el **ajuste correcto**, donde el modelo captura los patrones generales sin perderse en el ruido específico de los datos de entrenamiento.

Una intuición visual poderosa para transmitir al estudiante es la siguiente: si trazamos el error de entrenamiento y el error de prueba en función de la complejidad del modelo, el error de entrenamiento disminuye monótonamente, mientras que el error de prueba primero disminuye, alcanza un mínimo y luego vuelve a crecer. El punto del mínimo del error de prueba es el ajuste correcto, y la zona a su derecha es la del sobreajuste.

### La analogía del tiro al blanco

La diapositiva incluye la clásica visualización con dianas, que merece comentarse en detalle porque es una forma efectiva. Imaginemos cuatro tiradores, cada uno representando una combinación distinta de sesgo y varianza.

El tirador de **bajo sesgo y baja varianza** acierta en el centro de la diana de manera consistente. Sus tiros se agrupan apretadamente alrededor del blanco. Este es el modelo ideal.

El tirador de **bajo sesgo y alta varianza** acierta en promedio en el centro, pero sus tiros están muy dispersos: algunos arriba, algunos abajo, algunos a los costados. Su puntería sería excelente si pudiéramos promediar todos sus tiros, pero cada tiro individual es impredecible. Este es el modelo que sobreajusta.

El tirador de **alto sesgo y baja varianza** agrupa sus tiros apretadamente, pero lejos del centro. Es consistente pero sistemáticamente desviado. Este es el modelo que subajusta.

El tirador de **alto sesgo y alta varianza** dispara lejos del centro y además con gran dispersión. Es la peor combinación posible y suele ocurrir con modelos mal especificados sobre datos insuficientes o ruidosos.

### Estrategias de control

Para cerrar la unidad, conviene mencionar el repertorio de técnicas disponibles para navegar este compromiso. La **regularización** penaliza la complejidad del modelo durante el entrenamiento, reduciendo la varianza al costo de algo de sesgo. El **aumento del conjunto de datos**, ya sea recolectando más muestras o usando técnicas de generación sintética, reduce la varianza sin aumentar el sesgo. Las **técnicas de ensamble**, como bagging y boosting, combinan múltiples modelos para reducir varianza o sesgo según el método. La **selección de modelos** mediante validación cruzada permite identificar empíricamente el nivel de complejidad adecuado para los datos disponibles.

---

## Cierre conceptual

Al finalizar esta unidad, el estudiante debería haber construido un mapa mental coherente que conecta los datos como materia prima con los modelos como funciones parametrizadas, pasando por la infraestructura que los sostiene, los profesionales que los manejan, las técnicas que los procesan, las métricas que los evalúan y las limitaciones que los acotan. Este mapa es lo que distingue a quien practica el aprendizaje automático con criterio de quien simplemente invoca funciones de bibliotecas sin entender lo que ocurre debajo.

Conviene cerrar la clase volviendo al principio. El aprendizaje automático no es magia, ni una colección de recetas, ni una promesa de automatización universal. Es una disciplina rigurosa, con fundamentos matemáticos, prácticas industriales y limitaciones estructurales. La diferencia entre un proyecto exitoso y un fracaso costoso suele estar en la calidad de las decisiones tomadas en cada etapa del ciclo presentado, no en la sofisticación del algoritmo final. Transmitir esta visión al estudiante es probablemente el aporte más duradero que esta unidad puede dejar.

