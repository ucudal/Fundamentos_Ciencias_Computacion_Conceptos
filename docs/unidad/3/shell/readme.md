status: COMPLETE
responsable: @pilasguru
ultima_actualizacion: 2025-11-26

# Unidad 3: Shell y Scripts

## El shell como interfaz del sistema

El shell es la interfaz textual que permite a los usuarios interactuar directamente con el sistema operativo. A diferencia de las interfaces gráficas, el shell expone de forma explícita las operaciones que se realizan sobre el sistema, permitiendo ejecutar comandos, encadenar operaciones y automatizar tareas.

Desde el punto de vista conceptual, el shell actúa como intermediario entre el usuario y el kernel. El usuario emite instrucciones en forma de comandos, y el shell las interpreta y las traduce en llamadas al sistema operativo.

Este modelo resulta particularmente potente en entornos donde la automatización, la repetibilidad y el control fino son necesarios, como la administración de sistemas, el desarrollo de software o el procesamiento de datos.

## Diferencias de entorno: Unix-like y Windows

Existen dos grandes familias de entornos donde el uso del shell es habitual. Por un lado, los sistemas Unix-like, como Linux y macOS, donde el uso de shells como Bash es tradicional. Por otro lado, los sistemas Windows, donde PowerShell se ha consolidado como la herramienta principal de automatización.

En sistemas Linux y macOS, el shell opera principalmente sobre texto plano. Los comandos producen salidas textuales que pueden ser redirigidas, filtradas y transformadas. Este modelo favorece la composición de herramientas pequeñas.

En Windows, PowerShell introduce un enfoque diferente: trabaja con objetos en lugar de texto. Esto permite manipular datos estructurados de forma más directa, aunque mantiene una sintaxis que recuerda a los shells tradicionales.

Ambos enfoques son válidos y responden a filosofías distintas. En la práctica profesional, es común tener que desenvolverse en ambos entornos.

## Ejecución de comandos

La unidad básica de trabajo en un shell es el comando. Un comando puede ser un programa, una utilidad del sistema o una función del propio shell.

En Bash, un comando típico puede verse así:

```bash
ls -l /var/log
```

Este comando lista el contenido de un directorio en formato detallado.

En PowerShell, un equivalente conceptual sería:

```powershell
Get-ChildItem -Path C:\Windows\Logs
```

Aunque ambos comandos cumplen funciones similares, el enfoque difiere. Bash devuelve texto que el usuario interpreta, mientras que PowerShell devuelve objetos que pueden ser manipulados directamente.

## Composición de comandos y pipes

Una de las características más poderosas del shell es la posibilidad de encadenar comandos. Esto se logra mediante el uso de pipes (`|`), que permiten que la salida de un comando sea utilizada como entrada de otro.

En Bash:

```bash
ps aux | sort -nrk 3 | head -5
```

Este pipeline lista procesos, los ordena por consumo de CPU y muestra los cinco más altos.

En PowerShell:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

Aquí se logra el mismo objetivo, pero operando sobre objetos en lugar de texto.

Este mecanismo permite construir operaciones complejas a partir de herramientas simples, lo que constituye uno de los principios fundamentales del uso del shell.

## Variables de entorno

Los shells permiten definir y utilizar variables que almacenan valores temporales durante la ejecución.

En Bash:

```bash
INSTITUCION="UCU"
echo "Estamos en la $INSTITUCION"
```

En PowerShell:

```powershell
$Institucion = "UCU"
Write-Output "Estamos en la $Institucion"
```

Además, ambos entornos disponen de variables de entorno del sistema, como PATH, que define dónde se buscan los ejecutables.

En Bash:

```bash
echo $PATH
```

En PowerShell:

```powershell
$env:PATH
```

Las variables son fundamentales para parametrizar scripts y evitar valores hardcodeados.

## Scripts: automatización de tareas

Un script es un archivo que contiene una secuencia de comandos que se ejecutan de forma automatizada. Permite encapsular tareas repetitivas y ejecutarlas de manera consistente.

En Bash, un script básico podría ser:

```bash
#!/bin/bash

PROCESOS=$(ps aux | grep $USER | wc -l)
echo "El usuario $USER está ejecutando $PROCESOS procesos"
```

Este script cuenta la cantidad de procesos asociados al usuario actual.

En PowerShell, el equivalente sería:

```powershell
$procesos = (Get-Process | Where-Object { $_.UserName -like "*$env:USERNAME*" }).Count
Write-Output "El usuario $env:USERNAME está ejecutando $procesos procesos"
```

Aunque la lógica es similar, la forma de acceder a los datos refleja nuevamente la diferencia entre texto (Bash) y objetos (PowerShell).

## Ejecución de scripts

Para ejecutar scripts, cada entorno tiene sus propias convenciones.

En sistemas Unix-like:

```bash
chmod +x script.sh
./script.sh
```

En Windows con PowerShell:

```powershell
.\script.ps1
```

En PowerShell también es relevante la política de ejecución (Execution Policy), que puede restringir la ejecución de scripts por motivos de seguridad.

## Parámetros y variables especiales

Los scripts pueden recibir parámetros desde la línea de comandos.

En Bash:

```bash
echo "Nombre del script: $0"
echo "Primer argumento: $1"
echo "Todos los argumentos: $@"
```

En PowerShell:

```powershell
Write-Output "Primer argumento: $args[0]"
Write-Output "Todos los argumentos: $args"
```

Esto permite construir scripts reutilizables y dinámicos.

## Estructuras de control

Los scripts incorporan estructuras de control que permiten tomar decisiones y repetir operaciones.

En Bash:

```bash
if [ "$1" == "hola" ]; then
  echo "Saludo detectado"
fi
```

En PowerShell:

```powershell
if ($args[0] -eq "hola") {
  Write-Output "Saludo detectado"
}
```

También existen estructuras de programación como `for` y `while`, que permiten iterar sobre datos o repetir acciones.

Estas estructuras de programación son esenciales para pasar de simples comandos a lógica más elaborada.

## Expresiones regulares

Las expresiones regulares permiten definir patrones de búsqueda sobre texto. Son ampliamente utilizadas en herramientas de línea de comandos para filtrar información.

En Bash, usando `grep`:

```bash
grep -E "^[a-z]+$" archivo.txt
```

En PowerShell:

```powershell
Select-String -Pattern "^[a-z]+$" archivo.txt
```

El uso de expresiones regulares permite realizar búsquedas complejas y precisas, lo que resulta particularmente útil en el análisis de logs o procesamiento de datos.

## Permisos y control de acceso

En sistemas Unix-like, los permisos de archivos se representan mediante el modelo `rwx` (lectura, escritura, ejecución), aplicado a usuario, grupo y otros.

Un ejemplo típico:

```bash
chmod 755 script.sh
```

Esto otorga permisos completos al propietario y permisos de lectura y ejecución al resto.

En Windows, el modelo es diferente y se basa en listas de control de acceso (ACL). PowerShell permite inspeccionar estos permisos:

```powershell
Get-Acl archivo.txt
```

Aunque los modelos difieren, ambos sistemas buscan controlar quién puede acceder o modificar los recursos.

## Conclusión

El uso del shell y los scripts constituye una herramienta central en la computación moderna. Permite automatizar tareas, gestionar sistemas y procesar información de manera eficiente.

Comprender tanto Bash como PowerShell amplía significativamente las capacidades del profesional, permitiéndole trabajar en distintos entornos y adaptarse a diferentes contextos tecnológicos.

El dominio de estos conceptos no solo mejora la productividad, sino que también facilita una comprensión más profunda del funcionamiento interno de los sistemas operativos.


## Bibliografia

* The Linux Command Line (William Shotts) [sitio web oficial descarga PDF](https://www.linuxcommand.org/tlcl.php)
* Bash Guide for Beginners (Machtelt Garrels) [Ver PDF](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)

[🔙 Inicio de la unidad](../readme.md)
