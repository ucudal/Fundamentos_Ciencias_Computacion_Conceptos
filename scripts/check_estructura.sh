#!/bin/bash

BASE_DIR="docs/unidad"
ERROR=0
VALID_STATUS=("DRAFT" "IN_PROGRESS" "REVIEW" "COMPLETE")

echo "🔎 Verificando estructura editorial..."

# ----------------------------------------
# 1️⃣ Cada unidad debe tener readme.md
# ----------------------------------------
for unidad in "$BASE_DIR"/*; do
    if [ -d "$unidad" ]; then
        if [ ! -f "$unidad/readme.md" ]; then
            echo "❌ Falta readme.md en unidad: $unidad"
            ERROR=1
        fi
    fi
done

# ----------------------------------------
# 2️⃣ Cada sub-unidad debe tener readme.md
# ----------------------------------------
for subunidad in "$BASE_DIR"/*/*; do
    if [ -d "$subunidad" ]; then
        if [ ! -f "$subunidad/readme.md" ]; then
            echo "❌ Falta readme.md en sub-unidad: $subunidad"
            ERROR=1
        fi
    fi
done

# ----------------------------------------
# 3️⃣ Validación de status
# ----------------------------------------

# 3a) Ningún readme de UNIDAD debe tener status
for unidad_readme in "$BASE_DIR"/*/readme.md; do
    if grep -q "^status:" "$unidad_readme"; then
        echo "❌ status no permitido en readme de UNIDAD: $unidad_readme"
        ERROR=1
    fi
done

# 3b) Cada readme de SUB-UNIDAD debe tener status válido
for sub_readme in "$BASE_DIR"/*/*/readme.md; do
    if grep -q "^status:" "$sub_readme"; then
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
    else
        echo "❌ Falta status en sub-unidad: $sub_readme"
        ERROR=1
    fi
done

# 3c) Ningún archivo que NO sea readme.md puede tener status
for file in $(find "$BASE_DIR" -name "*.md" ! -name "readme.md"); do
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
else
    echo "🚨 Se encontraron errores."
    exit 1
fi
