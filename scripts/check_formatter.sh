#!/usr/bin/env bash

ERRORS=0
VALID_STATUS="DRAFT|IN_PROGRESS|REVIEW|COMPLETE"

check_file() {

    file="$1"

    line1=$(sed -n '1p' "$file")
    line2=$(sed -n '2p' "$file")
    line3=$(sed -n '3p' "$file")
    line4=$(sed -n '4p' "$file")

    # status
    if [[ $line1 =~ ^status:[[:space:]]+([A-Z_]+)$ ]]; then
        status="${BASH_REMATCH[1]}"
        if ! [[ $status =~ ^($VALID_STATUS)$ ]]; then
            echo "Status inválido en: $file ($status)"
            ERRORS=1
        fi
    else
        echo "Falta o mal status en: $file"
        ERRORS=1
    fi

    # responsable (cualquier texto no vacío)
    if ! [[ $line2 =~ ^responsable:[[:space:]]+.+$ ]]; then
        echo "Error responsable en: $file"
        ERRORS=1
    fi

    # fecha formato ISO
    if ! [[ $line3 =~ ^ultima_actualizacion:[[:space:]]+[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "Error fecha (YYYY-MM-DD) en: $file"
        ERRORS=1
    fi

    # línea vacía
    if [[ -n "$line4" ]]; then
        echo "Falta línea vacía después del metadata en: $file"
        ERRORS=1
    fi
}

while read -r file; do
    check_file "$file"
done < <(find docs/unidad -mindepth 3 -maxdepth 3 -name "readme.md")

exit $ERRORS
