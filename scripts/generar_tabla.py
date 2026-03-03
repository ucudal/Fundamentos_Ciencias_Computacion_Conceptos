import yaml
from pathlib import Path
from collections import Counter
import re

MKDOCS_FILE = "mkdocs.yml"
RAW_FILE = "scripts/estado_editorial_raw.txt"
OUTPUT_FILE = "scripts/estado_editorial.md"

STATUS_BADGES = {
    "DRAFT": "![DRAFT](https://img.shields.io/badge/status-DRAFT-lightgrey)",
    "IN_PROGRESS": "![IN_PROGRESS](https://img.shields.io/badge/status-IN--PROGRESS-blue)",
    "REVIEW": "![REVIEW](https://img.shields.io/badge/status-REVIEW-orange)",
    "COMPLETE": "![COMPLETE](https://img.shields.io/badge/status-COMPLETE-brightgreen)",
}


# -----------------------------
# Badge global progreso
# -----------------------------
def badge_global(porcentaje):
    if porcentaje < 30:
        color = "red"
    elif porcentaje < 70:
        color = "orange"
    else:
        color = "brightgreen"

    return f"![Progreso](https://img.shields.io/badge/progreso-{porcentaje}%25-{color})"


# -----------------------------
# Convierte usuario a link GitHub
# -----------------------------
def github_link(responsable):
    responsable = responsable.strip()

    if responsable.startswith("@"):
        username = responsable[1:]
        return f"[@{username}](https://github.com/{username})"

    return responsable


# -----------------------------
# Leer mkdocs.yml
# -----------------------------
with open(MKDOCS_FILE) as f:
    config = yaml.safe_load(f)

unidad_titulos = {}

for item in config.get("nav", []):
    if isinstance(item, dict) and "Unidades" in item:
        for unidad in item["Unidades"]:
            for titulo, ruta in unidad.items():
                numero = ruta.split("/")[1]
                unidad_titulos[numero] = titulo


# -----------------------------
# Leer RAW + contar estados
# -----------------------------
agrupado = {}
contador_estados = Counter()
total_items = 0

for linea in Path(RAW_FILE).read_text().splitlines():

    linea = linea.strip()
    if not linea:
        continue

    partes = linea.split("|")

    if len(partes) != 5:
        print(f"⚠ Línea ignorada por formato incorrecto: {linea}")
        continue

    unidad, subunidad, status, responsable, fecha = [p.strip() for p in partes]

    if unidad not in agrupado:
        agrupado[unidad] = []

    agrupado[unidad].append((subunidad, status, responsable, fecha))

    contador_estados[status] += 1
    total_items += 1


# -----------------------------
# Calcular progreso
# -----------------------------
complete = contador_estados.get("COMPLETE", 0)

if total_items > 0:
    porcentaje = int((complete / total_items) * 100)
else:
    porcentaje = 0

badge = badge_global(porcentaje)


# -----------------------------
# Generar Markdown tabla
# -----------------------------
salida = "## Estado Editorial\n\n"

salida += "- ![DRAFT](https://img.shields.io/badge/status-DRAFT-lightgrey) → Contenido inicial\n"
salida += "- ![IN_PROGRESS](https://img.shields.io/badge/status-IN--PROGRESS-blue) → En desarrollo\n"
salida += "- ![REVIEW](https://img.shields.io/badge/status-REVIEW-orange) → En revisión académica\n"
salida += "- ![COMPLETE](https://img.shields.io/badge/status-COMPLETE-brightgreen) → Material finalizado\n\n"

for unidad in sorted(agrupado.keys(), key=int):
    titulo = unidad_titulos.get(unidad, f"Unidad {unidad}")
    salida += f"### {titulo}\n\n"
    salida += "| Sub-unidad | Status | Responsable | Última actualización |\n"
    salida += "|------------|--------|-------------|----------------------|\n"

    for subunidad, status, responsable, fecha in sorted(agrupado[unidad]):

        badge_status = STATUS_BADGES.get(status, status)
        responsable_md = github_link(responsable)

        salida += f"| {subunidad} | {badge_status} | {responsable_md} | {fecha} |\n"

    salida += "\n"

Path(OUTPUT_FILE).write_text(salida)

print(f"✔ Tabla generada en {OUTPUT_FILE}")


# -----------------------------
# Insertar en README.md
# -----------------------------
readme_path = Path("README.md")
readme = readme_path.read_text()

inicio = "<!-- ESTADO_EDITORIAL_START -->"
fin = "<!-- ESTADO_EDITORIAL_END -->"

bloque_editorial = f"""
{inicio}

{badge}

**Progreso global:** {porcentaje}%  

### Estado editorial sub-secciones (de las Unidades)

- DRAFT: {contador_estados.get("DRAFT", 0)}
- IN_PROGRESS: {contador_estados.get("IN_PROGRESS", 0)}
- REVIEW: {contador_estados.get("REVIEW", 0)}
- COMPLETE: {contador_estados.get("COMPLETE", 0)}

---

{salida}

{fin}
"""

readme = re.sub(
    f"{inicio}.*?{fin}",
    bloque_editorial,
    readme,
    flags=re.DOTALL
)

readme_path.write_text(readme)

print("✔ README actualizado con dashboard editorial")
