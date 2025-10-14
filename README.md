# DSI-PPAI-CU23

## 📋 Descripción
Sistema de registro para la revisión manual de eventos sísmicos autodetectados.  
Proyecto desarrollado para la cátedra de Diseño de Sistemas de Información - Caso de Uso 23.

---

## 📝 Caso de Uso 23

**Título**: Registrar Revisión Manual de Eventos Sísmicos Autodetectados

**Descripción**: Sistema que permite a los analistas sísmicos revisar manualmente eventos detectados automáticamente por sensores, validar su autenticidad y registrar observaciones relevantes.

---

## 🏗️ Estructura del Proyecto

```
DSI-PPAI-CU23/
│
├── .venv/                   # Entorno virtual (no se sube a Git)
│   ├── Include/
│   ├── Lib/                 # Librerias instaladas en el entorno virtual
│   ├── Scripts/             # Scripts del entorno virtual
│   ├── .gitignore           # Archivos ignorados por Git (creado por venv)
│   └── pyvenv.cfg           # Configuración del entorno virtual
│
├── src/                     # Código fuente de la aplicación
│   ├── boundaries/          # Interfaces/Pantallas (capa de presentación)
│   ├── controllers/         # Controladores (lógica de negocio)
│   ├── data/                # Gestión de datos
│   ├── entities/            # Entidades del dominio
│   └── main.py              # Punto de entrada de la aplicación
│
├── .gitignore               # Archivos ignorados por Git
├── README.md                # Este archivo
└── requirements.txt         # Dependencias del proyecto
```

### 📂 Explicación de carpetas

- **`.venv/`**: Entorno virtual de Python con todas las dependencias instaladas de forma aislada.
- **`src/boundaries/`**: Interfaces de usuario y pantallas (Flet) - capa de presentación.
- **`src/controls/`**: Controladores que manejan la lógica de negocio del caso de uso.
- **`src/data/`**: Gestión y acceso a datos.
- **`src/entities/`**: Clases del modelo de dominio (eventos sísmicos, usuarios, etc.).
- **`src/main.py`**: Archivo principal que inicia la aplicación.

---

## 🚀 Inicio Rápido

### 1️⃣ Clonar e instalar

```bash
# Clonar el repositorio desde develop
git clone -b develop https://github.com/tu-usuario/DSI-PPAI-CU23.git
cd DSI-PPAI-CU23

# Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate          # Linux/Mac
.venv\Scripts\activate             # Windows

pip install -r requirements.txt
```

### 2️⃣ Ejecutar

```bash
# Asegurate de tener el entorno activado: (.venv)
python src/main.py
```

### 3️⃣ Salir

```bash
deactivate
```

---

## 🌿 Workflow de Git

### 📋 Estructura de Ramas

```
main (protegida)
  └── develop (protegida)
        ├── feat/nueva-funcionalidad
        ├── fix/correccion-bug
        ├── doc/actualizar-readme
        └── style/mejorar-interfaz
```

- **`main`**: Rama de producción (protegida, no se trabaja directamente)
- **`develop`**: Rama de desarrollo (protegida, no se trabaja directamente)
- **Ramas de trabajo**: Se crean desde `develop` con prefijos específicos

### 🏷️ Nomenclatura de Ramas

```bash
feat/nombre-descriptivo      # Nueva funcionalidad
fix/nombre-del-bug          # Corrección de errores
hotfix/nombre-urgente       # Corrección urgente
doc/nombre-documentacion    # Documentación
style/nombre-estilo         # Cambios de estilo/UI
```

### 🔄 Flujo de Trabajo Completo

#### 1. Crear nueva rama de trabajo

```bash
# Asegurate de estar en develop actualizado
git switch develop
git pull origin develop

# Crear y cambiar a tu nueva rama
git switch -c feat/registro-eventos-sismicos
```

#### 2. Realizar cambios y commits

```bash
# Hacer tus cambios en el código...

# Agregar archivos modificados
git add .

# Commit con formato: "prefijo: descripción"
git commit -m "feat: implementar formulario de registro de eventos"
git commit -m "feat: agregar validación de datos sísmicos"
git commit -m "fix: corregir formato de fecha en evento"
```

#### 3. Subir cambios a GitHub

```bash
# Primer push (crear la rama en remoto)
git push -u origin feat/registro-eventos-sismicos

# Pushes siguientes (la rama ya existe)
git push
```

#### 4. Crear Pull Request en GitHub

1. Ve a GitHub → pestaña **Pull Requests**
2. Click en **New Pull Request**
3. Seleccionar:
   - **Base**: `develop`
   - **Compare**: tu rama (ej: `feat/registro-eventos-sismicos`)
4. **Título**: Nombre de la rama (ej: `feat/registro-eventos-sismicos`)
5. **Descripción**: Lista de cambios realizados
   ```markdown
   ## Cambios realizados
   
   - Implementado formulario de registro de eventos
   - Agregada validación de datos sísmicos
   - Corregido formato de fecha en evento
   - Conectado controlador con interfaz
   ```
6. Click en **Create Pull Request**
7. Esperar revisión y aprobación del equipo

### 📝 Formato de Commits

```bash
# Formato general
prefijo: descripción breve en minúsculas

# Ejemplos correctos
feat: agregar pantalla de listado de eventos
fix: corregir error en cálculo de magnitud
doc: actualizar README con instrucciones de instalación
style: mejorar diseño de botones principales
hotfix: resolver error crítico en guardado de datos

# ❌ Ejemplos incorrectos
Agregué una nueva función          # Sin prefijo
feat: Agregar Pantalla             # Mayúsculas innecesarias
arreglé un bug                     # Sin prefijo adecuado
```

### 🔍 Comandos Útiles

```bash
# Ver en qué rama estás
git branch

# Ver estado de cambios
git status

# Ver historial de commits
git log --oneline

# Actualizar tu rama con los últimos cambios de develop
git switch develop
git pull origin develop
git switch tu-rama
git merge develop
# O más facil
git switch tu-rama
git pull origin develop

# Descartar cambios locales (¡cuidado!)
git checkout -- archivo.py
git reset --hard  # Descarta TODOS los cambios
```

### ⚠️ Reglas Importantes

- ✅ **SIEMPRE** crear ramas desde `develop` actualizado
- ✅ **NUNCA** hacer commit directamente en `main` o `develop`
- ✅ **SIEMPRE** usar el formato de commits con prefijo
- ✅ Mantener commits atómicos (un cambio = un commit)
- ✅ Escribir descripciones claras y concisas
- ✅ Probar el código antes de hacer push
- ✅ Revisar Pull Requests de compañeros

---

## 📦 Gestión de Dependencias

### Instalar una nueva librería

```bash
# Asegurate de tener el entorno activado
pip install nombre-libreria

# Actualizar requirements.txt
pip freeze > requirements.txt

# Commitear los cambios
git add requirements.txt
git commit -m "Agregada librería nombre-libreria"
```

### Ver paquetes instalados

```bash
pip list
```

### Verificar que el entorno está activado

```bash
# Linux/Mac
echo $VIRTUAL_ENV

# Windows (CMD)
echo %VIRTUAL_ENV%

# Windows (PowerShell)
echo $env:VIRTUAL_ENV
```

Si muestra la ruta a `.venv`, está activado ✅

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación
- **Flet**: Framework para crear interfaces de usuario
- **venv**: Gestión de entornos virtuales

---

## 👥 Equipo de Desarrollo

*[Agregar nombres de los integrantes del grupo]*

---

## 📄 Licencia

Este proyecto es desarrollado con fines educativos para la cátedra de Diseño de Sistemas de Información.

---

## 🔗 Enlaces Útiles

- [Documentación de Flet](https://flet.dev/)
- [Documentación de Python](https://docs.python.org/3/)
- [Guía de venv](https://docs.python.org/3/library/venv.html)

---

## ⚠️ Notas Importantes

- **NO** subir la carpeta `.venv/` a Git (está en `.gitignore`)
- **SÍ** mantener actualizado el archivo `requirements.txt`
- **SIEMPRE** trabajar con el entorno virtual activado
