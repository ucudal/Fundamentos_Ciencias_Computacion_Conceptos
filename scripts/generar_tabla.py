import yaml
from pathlib import Path
from collections import Counter
import re

MKDOCS_FILE = "mkdocs.yml"
OUTPUT_FILE = "scripts/estado_editorial.md"

STATUS_BADGES = {
    "DRAFT": "![DRAFT](https://img.shields.io/badge/status-DRAFT-lightgrey)",
    "IN_PROGRESS": "![IN_PROGRESS](https://img.shields.io/badge/status-IN--PROGRESS-blue)",
    "REVIEW": "![REVIEW](https://img.shields.io/badge/status-REVIEW-orange)",
    "COMPLETE": "![COMPLETE](https://img.shields.io/badge/status-COMPLETE-brightgreen)",
}

class IgnorePythonLoader(yaml.SafeLoader):
    pass

def ignore_python(loader, tag_suffix, node):
    return None

IgnorePythonLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/",
    ignore_python
)

def badge_global(porcentaje):
    if porcentaje < 30:
        color = "red"
    elif porcentaje < 70:
        color = "orange"
    else:
        color = "brightgreen"

    return f"![Progreso](https://img.shields.io/badge/progreso-{porcentaje}%25-{color})"


def github_link(responsable):
    responsable = responsable.strip()

    if responsable.startswith("@"):
        username = responsable[1:]
        return f"[@{username}](https://github.com/{username})"

    return responsable


def sort_key_subunidad(nombre):
    """
    Ordena correctamente 1.1, 1.2, 1.10
    """
    partes = nombre.split(".")
    return tuple(int(p) for p in partes if p.isdigit())


# -----------------------------
# Leer mkdocs.yml
# -----------------------------
with open(MKDOCS_FILE, encoding="utf-8") as f:
    config = yaml.load(f, Loader=IgnorePythonLoader)

unidad_titulos = {}

for item in config.get("nav", []):
    if isinstance(item, dict) and "Unidades" in item:

        for unidad in item["Unidades"]:

            if isinstance(unidad, dict):
                for titulo, ruta in unidad.items():
                    numero = ruta.split("/")[1]
                    unidad_titulos[numero] = titulo


# -----------------------------
# Leer metadata de archivos
# -----------------------------
agrupado = {}
contador_estados = Counter()
total_items = 0

faltantes = []

for path in Path("docs/unidad").glob("*/*/readme.md"):

    unidad = path.parts[2]
    subunidad = path.parts[3]

    lines = path.read_text(encoding="utf-8").splitlines()

    status = ""
    responsable = ""
    fecha = ""

    for line in lines[:10]:

        if line.startswith("status:"):
            status = line.split(":", 1)[1].strip()

        elif line.startswith("responsable:"):
            responsable = line.split(":", 1)[1].strip()

        elif line.startswith("ultima_actualizacion:"):
            fecha = line.split(":", 1)[1].strip()

    if not status or not responsable or not fecha:
        faltantes.append(str(path))

    if not status:
        continue

    if unidad not in agrupado:
        agrupado[unidad] = []

    agrupado[unidad].append((subunidad, status, responsable, fecha))

    contador_estados[status] += 1
    total_items += 1


# -----------------------------
# Calcular progreso
# -----------------------------
complete = contador_estados.get("COMPLETE", 0)

porcentaje = int((complete / total_items) * 100) if total_items else 0
badge = badge_global(porcentaje)


# -----------------------------
# Generar Markdown tabla
# -----------------------------
salida = "## Estado Editorial\n\n"

for unidad in sorted(agrupado.keys(), key=int):

    titulo = unidad_titulos.get(unidad, f"Unidad {unidad}")

    salida += f"### {titulo}\n\n"
    salida += "| Sub-unidad | Status | Responsable | Última actualización |\n"
    salida += "|------------|--------|-------------|----------------------|\n"

    for subunidad, status, responsable, fecha in sorted(
        agrupado[unidad], key=lambda x: sort_key_subunidad(x[0])
    ):

        badge_status = STATUS_BADGES.get(status, status)
        responsable_md = github_link(responsable)

        salida += f"| {subunidad} | {badge_status} | {responsable_md} | {fecha} |\n"

    salida += "\n"

Path(OUTPUT_FILE).write_text(salida, encoding="utf-8")

print(f"✔ Tabla generada en {OUTPUT_FILE}")


# -----------------------------
# Insertar en README
# -----------------------------
readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")

inicio = "<!-- ESTADO_EDITORIAL_START -->"
fin = "<!-- ESTADO_EDITORIAL_END -->"

bloque = f"""
{inicio}

{badge}

**Progreso global:** {porcentaje}%

### Estado editorial sub-secciones

- DRAFT: {contador_estados.get("DRAFT",0)}
- IN_PROGRESS: {contador_estados.get("IN_PROGRESS",0)}
- REVIEW: {contador_estados.get("REVIEW",0)}
- COMPLETE: {contador_estados.get("COMPLETE",0)}

---

{salida}

{fin}
"""

readme = re.sub(
    f"{inicio}.*?{fin}",
    bloque,
    readme,
    flags=re.DOTALL
)

readme_path.write_text(readme, encoding="utf-8")

print("✔ README actualizado")


# -----------------------------
# Reporte editorial
# -----------------------------
if faltantes:

    print("\n⚠ Archivos con metadata incompleta:\n")

    for f in faltantes:
        print(" -", f)

else:

    print("\n✔ Toda la metadata editorial está completa")
