# Ejemplo completo de informe

A continuación se muestra un ejemplo simplificado que integra varios de los elementos vistos:

```latex
\documentclass{article}
\usepackage[spanish]{babel}
\usepackage{graphicx}

% --- Índice alfabético ---
\usepackage{makeidx}
\makeindex

\title{Informe de ejemplo}
\author{Estudiante}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Este documento muestra la estructura básica de un informe en LaTeX.
\end{abstract}

\section{Introducción}

LaTeX permite escribir documentos estructurados\footnote{LaTeX es ampliamente utilizado en entornos académicos y científicos por su calidad tipográfica y capacidad de automatización.}.
Además, facilita la organización del contenido y su reutilización\index{LaTeX}\index{documentos estructurados}.

\section{Desarrollo}

\subsection{Ejemplo matemático}

Una ecuación clásica en física es:

\[
E = mc^2
\]

\index{ecuaciones}

\subsection{Ejemplo de lista}

\begin{itemize}
\item Punto uno
\item Punto dos
\end{itemize}

\index{listas}

\section{Conclusión}

El uso de LaTeX mejora la calidad de los documentos académicos y permite aplicar estándares formales de escritura\index{calidad tipográfica}.

% --- Bibliografía ---
\begin{thebibliography}{9}

\bibitem{overleaf}
Overleaf,
\textit{Learn LaTeX},
\url{https://www.overleaf.com/learn}

\end{thebibliography}

% --- Impresión del índice ---
\newpage
\printindex

\end{document}
```

Este ejemplo sintetiza la estructura típica de un informe académico sencillo.

[🔙 Inicio de la unidad](../readme.md)