# Reto avanzado C: mini análisis de datos

Proyecto de práctica para recuperar datos de SQLite desde Python,
calcular una estadística sencilla y convertir los resultados
en un DataFrame de pandas.

El enunciado está disponible en [EJERCICIO.md](EJERCICIO.md).

## Requisitos previos

- Tener Python instalado.
- Disponer de un editor como Visual Studio Code.
- Haber ejecutado el reto avanzado A para preparar la base de datos.

## Archivos utilizados

| Archivo | Función |
|---|---|
| `main.py` | Código del análisis. |
| `requirements.txt` | Dependencias del proyecto. |
| `EJERCICIO.md` | Enunciado y pasos del ejercicio. |
| `../data/programacion.db` | Base de datos compartida con los otros retos avanzados. |

## 1. Abrir la carpeta del reto

Abre la carpeta principal del repositorio en VS Code.

En la terminal de PowerShell, entra en la carpeta del reto:

```powershell
cd Reto-Avanzado_C
```

Los siguientes comandos se ejecutan desde esta carpeta.

## 2. Crear el entorno virtual

```powershell
python -m venv .venv
```
Este comando crea la carpeta `.venv`, donde se guardarán
el entorno virtual y sus paquetes.

Solo necesitamos crear el entorno una vez.

## 3. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Normalmente aparecerá `(.venv)` al principio de la línea
de la terminal.

En VS Code, abre la paleta de comandos, busca
«Python: Select Interpreter» y selecciona el intérprete
de la carpeta `.venv` de este reto.

Instalamos las librerias
```powershell
python -m pip install pandas
```

## 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Este comando lee `requirements.txt` e instala pandas
y sus dependencias.

No es necesario instalar `sqlite3`, porque está incluido
en la biblioteca estándar de Python.

## 5. Ejecutar el programa

Una vez escrito el código en `main.py`:

```powershell
python main.py
```

El programa utilizará la base de datos `programacion.db`
de la carpeta `data` del repositorio.

## 6. Desactivar el entorno virtual

Al terminar:

```powershell
deactivate
```

## Volver a trabajar en el proyecto

En las siguientes sesiones, entra en la carpeta del reto
y activa el entorno:

```powershell
cd Reto_Avanzado_C
.\.venv\Scripts\Activate.ps1
```

No necesitas volver a crear el entorno ni instalar
las dependencias si ya están instaladas.