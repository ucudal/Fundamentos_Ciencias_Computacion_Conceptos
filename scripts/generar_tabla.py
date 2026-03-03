import yaml
from pathlib import Path

MKDOCS_FILE = "mkdocs.yml"
RAW_FILE = "scripts/estado_editorial_raw.txt"
OUTPUT_FILE = "scripts/estado_editorial.md"

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
# Leer datos generados por bash
# -----------------------------
agrupado = {}

for linea in Path(RAW_FILE).read_text().splitlines():

    linea = linea.strip()

    if not linea:
        continue  # Ignorar líneas vacías

    partes = linea.split("|")

    if len(partes) != 5:
        print(f"⚠ Línea ignorada por formato incorrecto: {linea}")
        continue

    unidad, subunidad, status, responsable, fecha = [p.strip() for p in partes]

    if unidad not in agrupado:
        agrupado[unidad] = []

    agrupado[unidad].append((subunidad, status, responsable, fecha))

# -----------------------------
# Generar Markdown
# -----------------------------
salida = "## Estado Editorial\n\n"

for unidad in sorted(agrupado.keys(), key=int):
    titulo = unidad_titulos.get(unidad, f"Unidad {unidad}")
    salida += f"### {titulo}\n\n"
    salida += "| Sub-unidad | Status | Responsable | Última actualización |\n"
    salida += "|------------|--------|-------------|----------------------|\n"

    for subunidad, status, responsable, fecha in sorted(agrupado[unidad]):
        salida += f"| {subunidad} | {status} | {responsable} | {fecha} |\n"

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

nuevo_bloque = f"{inicio}\n\n{salida}\n{fin}"

import re

readme = re.sub(
    f"{inicio}.*?{fin}",
    nuevo_bloque,
    readme,
    flags=re.DOTALL
)

readme_path.write_text(readme)

print("✔ README actualizado con estado editorial")

