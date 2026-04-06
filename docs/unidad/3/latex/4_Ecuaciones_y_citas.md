# Ecuaciones y bibliografía

## Escritura matemática

Uno de los principales motivos para utilizar LaTeX es su capacidad para representar expresiones matemáticas con alta calidad:
La ecuación de segundo grado es:

```latex
\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]
```

Las ecuaciones pueden integrarse en línea o en bloques independientes, y LaTeX gestiona su numeración automáticamente cuando es necesario.

## Bibliografía

La gestión de referencias es otro punto fuerte de LaTeX. Un ejemplo simple puede realizarse directamente en el documento:

```latex
\begin{thebibliography}{9}

\bibitem{knuth}
Donald Knuth,
\textit{The TeXbook},
Addison-Wesley, 1984.

\end{thebibliography}
```

Sin embargo, en contextos reales se utilizan herramientas más avanzadas como **BibTeX** o **BibLaTeX**, que permiten gestionar grandes volúmenes de referencias de forma automatizada y desacoplada del documento principal.

Un aspecto especialmente relevante es la facilidad con la que LaTeX permite aplicar **estándares de citación bibliográfica**, como APA, IEEE, Chicago, entre otros. Mediante paquetes específicos (por ejemplo,  `biblatex` con distintos estilos), es posible cambiar completamente el formato de las citas y la bibliografía sin modificar el contenido del documento.

Por ejemplo, utilizando `biblatex`:
	
```latex
\usepackage[style=apa]{biblatex}
\addbibresource{referencias.bib}
```

Este enfoque refuerza la separación entre contenido y formato: el autor se concentra en citar correctamente las fuentes, mientras que el sistema se encarga de aplicar el estilo requerido por la institución o publicación.

En entornos académicos, donde el cumplimiento de normas de citación es obligatorio, esta capacidad reduce errores y simplifica significativamente la producción de documentos formales.

[🔙 Inicio de la unidad](../readme.md)