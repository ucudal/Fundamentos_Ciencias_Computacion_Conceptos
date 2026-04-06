# Elementos básicos

## Texto y secciones

La organización del contenido se realiza mediante comandos estructurales:

```latex
\section{Título de sección}
\subsection{Subsección}
\subsubsection{Nivel inferior}
```

El texto se escribe de forma natural, sin necesidad de preocuparse por estilos visuales como tamaño de fuente o alineación.

## Listas

LaTeX permite construir listas ordenadas y no ordenadas de forma sencilla:

```latex
\begin{itemize}
\item Primer elemento
\item Segundo elemento
\end{itemize}
```

```latex
\begin{enumerate}
\item Paso uno
\item Paso dos
\end{enumerate}
```

## Figuras

La inclusión de imágenes se realiza mediante el paquete graphicx:

```latex
\usepackage{graphicx}

\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{imagen.png}
\caption{Ejemplo de figura}
\end{figure}
```

LaTeX gestiona automáticamente la numeración y el posicionamiento.

## Tablas

Las tablas se definen mediante el entorno tabular:

```latex
\begin{tabular}{|c|c|}
\hline
Columna 1 & Columna 2 \\
\hline
Dato A & Dato B \\
\hline
\end{tabular}
```

Para documentos más complejos, existen paquetes que mejoran significativamente el diseño de tablas.

## Elementos para el armado de un informe real

Un informe académico no es solo un conjunto de secciones, sino una estructura coherente que suele incluir:

* portada
* resumen (abstract)
* introducción
* desarrollo
* conclusiones
* referencias

LaTeX facilita esta organización mediante clases de documento específicas (`article`, `report`, `book`) y paquetes adicionales.

Por ejemplo, para generar un resumen:

```latex
\begin{abstract}
Este informe presenta...
\end{abstract}
```


[🔙 Inicio de la unidad](../readme.md)