# Uso de un estilo oficial

### Enseñar cómo LaTeX separa contenido y formato, y cómo usar un estilo institucional.

#### Explicación conceptual

Un archivo .sty es un paquete de estilo que define:

* Márgenes, tipo de letra, interlineado.
* Formato de títulos, tablas, figuras.
* Encabezado y pie de página institucional.

Permite mantener consistencia visual en todos los informes sin tener que repetir configuraciones.

#### Ejemplo básico

Supongamos que la institución entrega un archivo fecovi.sty con este contenido:

```latex
% fecovi.sty
\usepackage[a4paper, margin=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhead[L]{FECOVI}
\fancyhead[R]{Informe Académico}
\fancyfoot[C]{\thepage}
```

Entonces el documento del estudiante sería:

```latex
\documentclass{article}
\usepackage{fecovi}   % carga el estilo institucional

\title{Análisis de Servicios en la Nube}
\author{Nombre del Estudiante}
\date{\today}

\begin{document}
\maketitle

\section{Introducción}
Este informe fue elaborado siguiendo el estilo oficial de FECOVI.

\end{document}
```

💡 Demostración: mostrar en Overleaf cómo cambia automáticamente el aspecto del documento al incluir `\usepackage{fecovi}`.


[🔙 Inicio de la unidad](../readme.md)