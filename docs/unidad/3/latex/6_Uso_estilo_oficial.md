# Uso de un estilo oficial

En entornos académicos y profesionales, es habitual que las instituciones definan guías de estilo específicas. Estas guías establecen criterios formales que afectan a todo el documento: márgenes, tipografía, jerarquía de títulos, numeración, encabezados, formato de citas y bibliografía.

En herramientas tradicionales, estos aspectos suelen configurarse manualmente en cada documento. En LaTeX, en cambio, se encapsulan en **clases (`.cls`) o paquetes de estilo (`.sty`)**, lo que permite aplicar un formato completo de manera automática y consistente.

Este enfoque permite que el autor se concentre exclusivamente en el contenido, delegando la presentación en una definición reutilizable.

Es especialmente relevante en:

* tesis universitarias
* artículos científicos
* informes institucionales
* documentos técnicos normalizados

## Explicación conceptual

Un archivo `.sty` es un paquete que define reglas de presentación del documento. Puede controlar, entre otros aspectos:

* márgenes y tamaño de página
* tipografía (familia, tamaño, interlineado)
* formato de títulos y secciones
* encabezados y pies de página
* estilo de figuras, tablas y captions
* comportamiento de listas y numeraciones

Desde el punto de vista de ingeniería, esto introduce una separación clara:

* **contenido** → lo escribe el autor
* **estilo** → lo define la institución o el proyecto

Esto permite:

* consistencia entre múltiples documentos
* mantenimiento centralizado del formato
* adaptación rápida a distintos estándares

## Ejemplo con cambio visual significativo

Supongamos que una institución define un estilo `ucudal.sty` más completo:

```latex
% ucudal.sty

\usepackage[a4paper, margin=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{setspace}

% Interlineado
\onehalfspacing

% Encabezado y pie
\pagestyle{fancy}
\fancyhead[L]{UCUDAL}
\fancyhead[R]{Informe Académico}
\fancyfoot[C]{\thepage}

% Formato de títulos
\titleformat{\section}
  {\large\bfseries}
  {\thesection.}{1em}{}

\titleformat{\subsection}
  {\normalsize\bfseries}
  {\thesubsection.}{1em}{}
```

Ahora, el documento del estudiante no necesita preocuparse por nada de eso:

```latex
\documentclass{article}
\usepackage[spanish]{babel}
\usepackage{ucudal}

\title{Análisis de Servicios en la Nube}
\author{Nombre del Estudiante}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}
Este informe fue elaborado siguiendo el estilo oficial de UCUDAL.

\section{Desarrollo}
El contenido se escribe sin preocuparse por el formato.

\section{Conclusión}
El estilo se aplica automáticamente.

\end{document}
```

## Qué cambia realmente

Al incorporar el estilo:

* se modifican márgenes y espaciado
* aparece encabezado institucional
* los títulos cambian de formato
* el documento adquiere consistencia visual

Y lo más importante:

> **El contenido no cambia en absoluto.**

## Relación con el mundo real

Este mecanismo es el que utilizan:

* revistas científicas (IEEE, ACM, Elsevier)
* universidades (plantillas de tesis)
* organismos públicos y empresas
* proyectos open source con documentación técnica

El autor escribe su trabajo dentro de una estructura definida, y el sistema garantiza que el resultado cumpla con el estándar requerido.


[🔙 Inicio de la unidad](../readme.md)