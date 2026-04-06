status: REVIEW
responsable: @JoacoViera
ultima_actualizacion: 2026-04-05

# Unidad 3: Git - Control de versiones

## Control de versiones

Un sistema de control de versiones (VCS) registra los cambios realizados en archivos a lo largo del tiempo. Permite volver a versiones anteriores, ver quién modificó qué y cuándo, recuperar archivos borrados o modificados, y colaborar con otros desarrolladores.

El control de versiones es fundamental en el desarrollo de software moderno, donde múltiples personas trabajan sobre el mismo código base y donde la capacidad de rastrear cambios y revertir errores resulta esencial para mantener la calidad del proyecto.

## ¿Qué es Git?

Git es un sistema de control de versiones distribuido, gratuito y de código abierto. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux.

La característica de ser **distribuido** significa que cada desarrollador tiene una copia completa del historial del proyecto. Esto permite trabajar sin conexión a la red y proporciona redundancia natural de los datos.

Entre las características principales de Git se encuentran:

- **Snapshots, no diferencias:** Git guarda "fotos" del estado de los archivos en cada commit, en lugar de almacenar solo las diferencias.
- **Operaciones locales:** casi todo se hace sin conexión a red, lo que permite trabajar de forma independiente.
- **Integridad:** todo se verifica con checksums (SHA-1), garantizando que los datos no se corrompan.
- **Solo agrega datos:** es difícil perder información una vez que ha sido registrada en Git.

## Los tres estados

Git tiene tres estados principales para los archivos:

- **Modified:** el archivo ha sido modificado pero no se ha preparado para el próximo commit.
- **Staged:** el archivo ha sido marcado para incluirse en el próximo commit.
- **Committed:** los datos han sido guardados de forma segura en la base de datos local.

Estos estados se corresponden con tres áreas de trabajo:

- **Working Directory:** donde editas tus archivos directamente.
- **Staging Area (Index):** donde preparas los cambios que formarán parte del próximo commit.
- **Git Directory (.git):** donde se guarda el historial completo del proyecto.

El flujo típico es: `Working Dir → Staging Area → Git Directory`.

## Configuración inicial

### Instalación

En sistemas Linux (Debian/Ubuntu):

```bash
sudo apt install git
```

En macOS:

```bash
brew install git
```

En Windows, se descarga desde `https://git-scm.com`.

### Configurar identidad

Lo primero que debe hacerse tras instalar Git es configurar el nombre y email:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Para verificar la configuración:

```bash
git config --list
```

### Obtener ayuda

Git proporciona documentación integrada:

```bash
git help <comando>
git <comando> --help
man git-<comando>
```

Por ejemplo: `git help config` muestra la documentación del comando config.

## Comandos básicos

### Crear un repositorio

Para inicializar un nuevo repositorio en un directorio existente:

```bash
cd mi_proyecto
git init
```

Esto crea el directorio `.git` con toda la estructura necesaria para el control de versiones.

### Clonar un repositorio

Para obtener una copia de un repositorio existente:

```bash
git clone https://github.com/usuario/repo.git
```

Esto descarga todo el historial del proyecto, no solo los archivos actuales.

### Ver estado

El comando `git status` muestra el estado actual del repositorio:

```bash
git status
```

Indica en qué rama estás, qué archivos han sido modificados, cuáles están en staging y cuáles no tienen seguimiento.

### Agregar archivos (staging)

Para preparar archivos para el próximo commit:

```bash
git add archivo.txt      # agregar un archivo específico
git add .                # agregar todos los archivos
git add *.py             # agregar por patrón
```

Los archivos pasan de estado "modified" a "staged".

### Hacer commit

Para guardar los cambios preparados en el historial:

```bash
git commit -m "Mensaje descriptivo"
```

El commit guarda una "foto" del estado actual de los archivos en staging. Es importante escribir mensajes claros y descriptivos. Por ejemplo: `"Agrega validación de email en formulario"`.

## Ver historial

### git log

Para ver el historial de commits:

```bash
git log              # historial completo
git log --oneline    # una línea por commit
git log --graph      # muestra ramas gráficamente
git log -n 5         # últimos 5 commits
```

### git diff

Para ver las diferencias entre versiones:

```bash
git diff             # cambios no staged
git diff --staged    # cambios en staging
git diff HEAD~1      # comparar con commit anterior
```

## Deshacer cambios

### Quitar del staging

Para sacar un archivo del área de staging sin perder los cambios:

```bash
git restore --staged archivo.txt
```

El archivo vuelve a estado "modified" pero mantiene los cambios.

### Descartar cambios locales

Para descartar los cambios en un archivo y volver a la versión del último commit:

```bash
git restore archivo.txt
```

**Cuidado:** esto descarta permanentemente los cambios no committed.

### Modificar último commit

Para modificar el mensaje o agregar archivos olvidados al último commit:

```bash
git commit --amend
```

**Nota:** solo debe usarse si el commit no ha sido compartido con otros.

### Guardar cambios temporalmente (stash)

El stash permite guardar temporalmente los cambios sin hacer commit:

```bash
git stash            # guardar cambios actuales
git stash list       # ver stashes guardados
git stash pop        # recuperar y eliminar último stash
git stash apply      # recuperar sin eliminar
```

Es útil cuando necesitas cambiar de rama pero tienes cambios sin commitear.

## Ramas (Branches)

### ¿Qué es una rama?

Una rama es una línea independiente de desarrollo. Permite trabajar en features sin afectar el código principal, experimentar de forma segura y colaborar en paralelo con otros desarrolladores.

### Comandos de ramas

```bash
git branch                    # listar ramas
git branch nueva-rama         # crear rama
git checkout nueva-rama       # cambiar de rama
git checkout -b otra-rama     # crear y cambiar en un solo comando
```

### Fusionar ramas (merge)

Para integrar los cambios de una rama en otra:

```bash
git checkout main
git merge nueva-rama
```

Esto integra los cambios de `nueva-rama` en `main`.

### Eliminar ramas

```bash
git branch -d rama    # eliminar rama fusionada
git branch -D rama    # forzar eliminación
```

## Repositorios remotos

### ¿Qué es un remoto?

Un repositorio remoto es una versión del proyecto alojada en Internet o en una red. Permite colaborar con otros desarrolladores y mantener una copia de respaldo del código.

Servicios populares incluyen GitHub, GitLab y Bitbucket.

### Comandos remotos

```bash
git remote -v                 # ver remotos configurados
git remote add origin URL     # agregar remoto
```

### Push y Pull

```bash
git push origin main    # subir cambios al remoto
git pull origin main    # descargar y fusionar cambios
git fetch origin        # descargar sin fusionar
```

## Archivo .gitignore

El archivo `.gitignore` especifica qué archivos Git debe ignorar. Es útil para excluir:

- Archivos compilados (`*.pyc`, `*.class`)
- Dependencias (`node_modules/`)
- Archivos de configuración local
- Archivos con secretos (`.env`)

Ejemplo de `.gitignore`:

```
# Archivos de Python
*.pyc
__pycache__/

# Dependencias de Node
node_modules/

# Variables de entorno
.env

# Archivos del sistema
.DS_Store
```

## Flujo de trabajo básico

Un workflow típico de trabajo con Git sigue estos pasos:

1. `git pull` - obtener últimos cambios del remoto
2. Editar archivos
3. `git status` - revisar cambios
4. `git add .` - preparar cambios
5. `git commit -m "mensaje"` - guardar cambios
6. `git push` - compartir cambios

### Resumen de comandos

```bash
git init          # Crear repositorio
git clone URL     # Clonar repositorio
git status        # Ver estado
git add .         # Agregar cambios
git commit -m ""  # Guardar cambios
git log           # Ver historial
git branch        # Manejar ramas
git checkout      # Cambiar rama
git merge         # Fusionar ramas
git pull          # Descargar cambios
git push          # Subir cambios
```

## Conclusión

Git es una herramienta fundamental en el desarrollo de software moderno. Su modelo distribuido, junto con características como las ramas y el staging area, proporciona flexibilidad y seguridad en el manejo del código fuente.

Dominar los conceptos básicos de Git permite colaborar efectivamente en proyectos de cualquier tamaño y mantener un historial ordenado de los cambios realizados. A medida que se adquiere experiencia, funcionalidades más avanzadas como rebase, cherry-pick o bisect amplían las posibilidades de gestión del código.

## Bibliografía

* Pro Git (Scott Chacon y Ben Straub) [Libro oficial gratuito](https://git-scm.com/book/es/v2)
* Git Documentation [Documentación oficial](https://git-scm.com/doc)

[🔙 Inicio de la unidad](../readme.md)
