# Variables de entorno y configuración básica

### Crear un script básico

Crear archivo: script.sh

Agregar shebang:

```sh
#!/bin/bash
```

### Comandos dentro

Dar permisos:

```sh
chmod +x script.sh
```

Ejecutar: ./script.sh


Contenidos que pueden entrar sin abrumar:

Variables locales dentro de script
Argumentos: $1, $2, $@

Condicionales:

```sh
if [ -f archivo.txt ]; then
    echo "Existe"
fi
```

Loops simples (solo for):

```sh
for f in *.txt; do
    echo "$f"
done
```

exit codes y && / ||

[🔙 Inicio de la unidad](../readme.md)