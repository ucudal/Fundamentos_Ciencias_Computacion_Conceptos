# Estructura básica de un documento

Un documento en LaTeX es un archivo de texto plano con extensión `.tex`. Su estructura sigue una organización bien definida que separa el preámbulo del contenido.

Un ejemplo mínimo es el siguiente:

```
\documentclass{article}

\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}

\title{Mi primer documento}
\author{Autor}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}

Este es un documento básico en LaTeX.

\end{document}
```

## Anatomía de un archivo .tex

Comprender la anatomía de un documento es fundamental para trabajar con LaTeX de forma efectiva. En términos generales, se distinguen tres partes:

El **preámbulo**, donde se define la configuración global del documento, incluyendo idioma, codificación, paquetes y metadatos.

El inicio del documento, marcado por `\begin{document}`, donde comienza el contenido visible.

El **cuerpo del documento**, donde se organizan los distintos elementos: secciones, texto, figuras, tablas y ecuaciones.

Finalmente, el documento se cierra con \end{document}.

Este modelo estructurado permite que el documento sea fácilmente mantenible y escalable.


[🔙 Inicio de la unidad](../readme.md)