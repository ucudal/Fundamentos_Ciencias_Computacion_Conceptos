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

## Ejemplo con cambio a un estilo UCUDAL

Supongamos que una institución define un estilo `ucudal.sty` más completo:

```latex
% ucudal.sty

\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{ucudal}[2026/04/06 Estilo de ejemplo UCUDAL]

\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{xcolor}

% Interlineado
\onehalfspacing

% Sin sangría, con separación entre párrafos
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8em}

% Color institucional simple
\definecolor{ucudalblue}{RGB}{0,70,140}

% Encabezado y pie
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textsc{Universidad Católica del Uruguay}}
\fancyhead[R]{\textsc{Informe Académico}}
\fancyfoot[C]{\thepage}

\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

% Hacer que también la primera página use fancy
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[L]{\textsc{Universidad Católica del Uruguay}}
  \fancyhead[R]{\textsc{Informe Académico}}
  \fancyfoot[C]{\thepage}
  \renewcommand{\headrulewidth}{0.6pt}
  \renewcommand{\footrulewidth}{0.4pt}
}

% Formato de secciones
\titleformat{\section}
  {\Large\bfseries\color{ucudalblue}}
  {\thesection.}{1em}{}

\titleformat{\subsection}
  {\large\bfseries\color{ucudalblue}}
  {\thesubsection.}{1em}{}

% Espaciado de títulos
\titlespacing*{\section}{0pt}{1.5em}{0.8em}
\titlespacing*{\subsection}{0pt}{1.2em}{0.5em}

% Título del documento más visible
\makeatletter
\renewcommand{\maketitle}{
  \begin{center}
    {\Huge\bfseries\color{ucudalblue}\@title \par}
    \vspace{1em}
    {\large \@author \par}
    \vspace{0.5em}
    {\normalsize \@date \par}
    \vspace{1.5em}
    \hrule
    \vspace{2em}
  \end{center}
}
\makeatother
```

Ahora, el documento no necesita preocuparse por nada de eso, solo usar el paquete de estilo:

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

\subsection{Ventajas}
La separación entre contenido y estilo permite reutilizar el mismo texto con distintas presentaciones.

\subsection{Aplicación}
Este enfoque es habitual en informes académicos, tesis y artículos científicos.

\section{Conclusión}
El estilo se aplica automáticamente.

\end{document}
```

## Qué cambia realmente

Al incorporar el estilo:

* encabezado en la primera página
* pie de página con numeración
* título grande y reformateado
* secciones en color y con otra jerarquía visual
* más espacio entre párrafos
* interlineado más amplio
* documento con aspecto institucional

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