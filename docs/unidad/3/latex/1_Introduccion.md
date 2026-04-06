# Introducción: ¿Qué es LaTeX y para qué sirve?

## ¿Qué es LaTeX?

LaTeX (pronunciado “LÉI-tex”, “LÁ-tej” o “LÁ-tex”) es un sistema para la composición tipográfica de documentos con calidad profesional, ampliamente utilizado en contextos académicos, científicos y técnicos.

A diferencia de herramientas tradicionales como procesadores de texto tipo WYSIWYG (por ejemplo, Microsoft Word o LibreOffice Writer), donde el usuario edita directamente el aspecto visual del documento, LaTeX funciona como un lenguaje de marcado. El documento se escribe como texto plano, incorporando comandos que describen la estructura y el significado del contenido.

Este archivo `.tex` no es el resultado final. Para obtener un documento legible, se procesa mediante un motor de composición (TeX), que interpreta los comandos y genera una salida formateada.

Tradicionalmente, este proceso generaba archivos en formato DVI (Device Independent), que luego podían convertirse a PostScript (PS) o PDF. En la práctica actual, los motores modernos como `pdflatex`, `xelatex` o `lualatex` generan directamente documentos PDF.

Sin embargo, el ecosistema de LaTeX permite múltiples tipos de salida:

* **PDF**: el formato más común para informes, artículos y tesis
* **PostScript (PS)**: utilizado históricamente en impresión profesional
* **DVI**: formato intermedio, hoy en gran medida obsoleto
* **HTML**: mediante herramientas como `latex2html`, `htlatex` o `pandoc`
* **Markdown / otros formatos**: usando conversores como `pandoc`

Esto implica que un mismo contenido fuente puede reutilizarse para distintos medios: impresión, web o distribución digital.

## ¿Por qué aprender LaTeX?

El uso de LaTeX no es universal ni obligatorio. Existen contextos donde otras herramientas pueden resultar más adecuadas. Sin embargo, en el ámbito de la ingeniería, la ciencia y la documentación técnica, LaTeX ofrece ventajas claras.

Una de sus principales fortalezas es la capacidad para representar contenido matemático con precisión y calidad tipográfica superior. Esto lo convierte en una herramienta estándar en disciplinas como matemática, física, informática e ingeniería.

Además, facilita la gestión de estructuras complejas dentro de un documento. Elementos como referencias cruzadas, notas al pie, bibliografía, índices o tablas de contenido pueden generarse y mantenerse automáticamente, reduciendo errores y esfuerzo manual.

Otro aspecto relevante es su extensibilidad. LaTeX cuenta con miles de paquetes que permiten ampliar sus funcionalidades, adaptándolo a distintos tipos de documentos y necesidades específicas.

En términos prácticos, LaTeX no se limita a producir informes. Existen clases y plantillas específicas para distintos tipos de documentos:

* **Artículos científicos** (`article`, `IEEEtran`, `elsarticle`)
* **Informes y tesis** (`report`, `book`, clases institucionales)
* **Presentaciones** mediante la clase `beamer`
* **Currículums vitae** con clases como `moderncv` o `awesome-cv`
* **Cartas formales** (`letter`)
* **Posters académicos** (`beamerposter`)

Esto permite utilizar una misma herramienta para múltiples necesidades de documentación profesional.

Una ventaja clave es la separación entre contenido y estilo. El autor escribe el contenido sin preocuparse por el formato final, que puede modificarse posteriormente sin alterar el texto. Esto facilita la reutilización y adaptación a normas institucionales.

En este contexto, es habitual el uso de plantillas. Universidades, revistas científicas y organizaciones proporcionan estilos predefinidos en LaTeX que aseguran consistencia y cumplimiento de estándares.

Herramientas como Overleaf simplifican este flujo al ofrecer edición en línea y acceso a una amplia biblioteca de plantillas listas para usar.

## ¿Cuándo usar LaTeX?

LaTeX es especialmente adecuado cuando el documento:

* contiene fórmulas matemáticas o notación técnica compleja
* requiere referencias cruzadas o bibliografía formal
* debe cumplir con un formato académico o institucional estricto
* necesita consistencia tipográfica en documentos largos
* puede requerir múltiples formatos de salida a partir de una misma fuente

En cambio, puede no ser la mejor opción en documentos de diseño libre, como materiales gráficos altamente personalizados o publicaciones con maquetación no estructurada.

* Referencia: [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes#What_is_LaTeX?)

[🔙 Inicio de la unidad](../readme.md)