status: IN_PROGRESS
responsable: @LylCB, @aleaurre
ultima_actualizacion: 2026-05-31

# [Alfabetización en IA](./1.0_alfabetización_en_IA.md)

## ¿Qué es la IA?
Delimitamos qué cuenta como IA y qué no, distinguiéndola de la programación tradicional y de otros sistemas automáticos.
Recorremos la relación entre IA, machine learning y deep learning para ordenar el vocabulario antes de entrar en detalle.

## Historia
Hilo conductor de Turing a hoy: prueba de Turing, inviernos de la IA, surgimiento del ML y salto reciente con redes profundas.
Mostramos que cada gran avance respondió a un problema técnico concreto, para evitar tanto el hype como el escepticismo.

## Impacto Ambiental
Analizamos el costo energético y de cómputo de entrenar y desplegar modelos a gran escala.
Discutimos huella de carbono, consumo de agua y la asimetría entre quienes producen y quienes sufren ese impacto.

## Ética
Abordamos sesgos, deepfakes, privacidad y responsabilidad a partir de casos reales (COMPAS, Arup, Air Canada, NYT vs. OpenAI).
Introducimos el marco regulatorio actual (EU AI Act y discusiones locales) como contexto del trabajo profesional con IA.

## Utilización de Modelos
Criterios para elegir un modelo según la tarea, los datos disponibles y las restricciones del contexto.
Práctica guiada de prompting y parámetros de inferencia (temperatura, top-p) en un entorno tipo Google AI Studio.

# [Machine Learning](./1.1_aprendizaje_automático.md)

## Conceptos clave
Idea central: aprender una función a partir de ejemplos etiquetados para generalizar a datos nuevos.
Vocabulario base: dataset, features, label, instancia y división entre entrenamiento y prueba.

## Modelos
Recorrido por familias representativas: regresión lineal y logística, árboles de decisión y k-NN.
Mostramos que distintos modelos imponen distintos sesgos inductivos y conviene elegir según el problema.

## Métricas de evaluación
Accuracy y matriz de confusión con sus cuatro cuadrantes (VP, VN, FP, FN) como punto de partida.
Precision, recall y F1 para entender que ninguna métrica única captura todos los tipos de error.

## Limitaciones Estructurales
Overfitting, underfitting y el problema de generalizar más allá del conjunto de entrenamiento.
Sesgos en los datos, fugas de información (data leakage) y supuestos que el modelo no puede cuestionar por sí mismo.

### [Actividad/Tarea](./Actividad_Practica_Aprendizaje_Automático.ipynb)


# [Neural Networks](./1.2_redes_neuronales.md)

## Conceptos clave
Idea central: una red neuronal es una función parametrizada que compone neuronas en capas y ajusta sus pesos a partir de datos para generalizar.

## Neurona
Unidad mínima: una suma ponderada de las entradas más un sesgo, pasada por una función de activación que decide la salida.
Límite fundamental: un perceptrón simple solo separa clases linealmente (no resuelve XOR), y eso motiva apilar neuronas en capas.

## Arquitecturas: de shallow a deep
Una sola capa oculta basta para aproximar cualquier función continua (teorema de aproximación universal), pero sin garantías sobre cuántas unidades hacen falta ni sobre poder entrenarla.
La profundidad aporta eficiencia y representaciones jerárquicas: rasgos simples en las primeras capas, conceptos abstractos en las últimas.

## ¿Cómo aprende una red?
Ciclo de cuatro pasos: predecir (forward pass), medir el error (pérdida), calcular gradientes (backpropagation) y ajustar pesos (descenso por gradiente con tasa η).
Se repite por épocas: backpropagation calcula el gradiente, mientras que la optimización es la que efectivamente mueve los pesos.

## Tipos de Redes Neuronales
No hay una arquitectura única: se elige según el dato y el problema (MLP para tabular, CNN para imágenes, RNN/LSTM para secuencias). Los Transformers, basados en autoatención, son el estado del arte y la base de los grandes modelos de lenguaje (LLMs).

## Limitaciones y cuidados
Sobreajuste, subajuste y el desafío de generalizar más allá del conjunto de entrenamiento.
Sesgos en los datos y confusiones frecuentes a evitar: perceptrón ≠ neurona moderna, y backpropagation ≠ descenso por gradiente.


[🔙 Inicio de la unidad](../readme.md)
