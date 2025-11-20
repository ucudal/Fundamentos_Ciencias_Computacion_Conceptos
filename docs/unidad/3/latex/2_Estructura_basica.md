# Estructura básica de un documento

### Entender la anatomía de un archivo .tex.

Mostrar y explicar:

```latex
\documentclass{article}

\usepackage[utf8]{inputenc}
\usepackage{graphicx}

\title{Mi Primer Informe en LaTeX}
\author{Nombre del Estudiante}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}
Texto de ejemplo.

\end{document}
```

### Explicar:

* `\documentclass{}` define el tipo (article, report, beamer…)
* `\usepackage{}` añade funcionalidades.
* Todo va entre `\begin{document}` y `\end{document}`.
* Compilar = convertir el código a PDF / html / Postscript

[🔙 Inicio de la unidad](../readme.md)