#!/bin/bash

BASE_DIR="docs/unidad"
ERROR=0
VALID_STATUS=("DRAFT" "IN_PROGRESS" "REVIEW" "COMPLETE")
OUTPUT_RAW="scripts/estado_editorial_raw.txt"
> "$OUTPUT_RAW"

echo "🔎 Verificando estructura editorial..."

# ----------------------------------------
# 1️⃣ Validación estructura
# ----------------------------------------

for unidad in "$BASE_DIR"/*; do
    if [ -d "$unidad" ]; then
        if [ ! -f "$unidad/readme.md" ]; then
            echo "❌ Falta readme.md en unidad: $unidad"
            ERROR=1
        fi
    fi
done

for subunidad in "$BASE_DIR"/*/*; do
    if [ -d "$subunidad" ]; then
        if [ ! -f "$subunidad/readme.md" ]; then
            echo "❌ Falta readme.md en sub-unidad: $subunidad"
            ERROR=1
        fi
    fi
done

# ----------------------------------------
# 2️⃣ Validación de status + fecha
# ----------------------------------------

for sub_readme in "$BASE_DIR"/*/*/readme.md; do

    UNIDAD=$(basename "$(dirname "$(dirname "$sub_readme")")")
    SUBUNIDAD=$(basename "$(dirname "$sub_readme")")

    if ! grep -q "^status:" "$sub_readme"; then
        echo "❌ Falta status en $sub_readme"
        ERROR=1
        continue
    fi

    STATUS=$(grep "^status:" "$sub_readme" | awk '{print $2}')

    VALID=0
    for s in "${VALID_STATUS[@]}"; do
        if [ "$STATUS" == "$s" ]; then
            VALID=1
        fi
    done

    if [ $VALID -eq 0 ]; then
        echo "❌ status inválido en $sub_readme → '$STATUS'"
        ERROR=1
    fi

    RESPONSABLE=$(grep "^responsable:" "$sub_readme" | cut -d':' -f2- | xargs)

    FECHA=$(grep "^ultima_actualizacion:" "$sub_readme" | awk '{print $2}')

    # Validación formato fecha AAAA-MM-DD
    if [[ ! $FECHA =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "❌ Fecha inválida en $sub_readme → '$FECHA' (formato requerido AAAA-MM-DD)"
        ERROR=1
    else
        # Validación fecha real (portable Linux/macOS)
        if date -j -f "%Y-%m-%d" "$FECHA" "+%Y-%m-%d" >/dev/null 2>&1; then
            : # OK en macOS
        elif date -d "$FECHA" "+%Y-%m-%d" >/dev/null 2>&1; then
            : # OK en Linux
        else
            echo "❌ Fecha inexistente en $sub_readme → '$FECHA'"
            ERROR=1
        fi
    fi

    echo "$UNIDAD|$SUBUNIDAD|$STATUS|$RESPONSABLE|$FECHA" >> "$OUTPUT_RAW"

done

# ----------------------------------------
# 3️⃣ Verificar que ningún otro archivo tenga status
# ----------------------------------------

for file in $(find "$BASE_DIR" -name "*.md" ! -path "*/readme.md"); do
    if grep -q "^status:" "$file"; then
        echo "❌ status no permitido en archivo: $file"
        ERROR=1
    fi
done

# ----------------------------------------
# Resultado final
# ----------------------------------------

if [ $ERROR -eq 0 ]; then
    echo "✅ Estructura editorial correcta."
    echo
    echo "📄 Generando tabla..."

    python3 scripts/generar_tabla.py || exit 1

    echo "✔ Tabla generada correctamente."
else
    echo
    echo "🚨 Se encontraron errores."
    exit 1
fi

