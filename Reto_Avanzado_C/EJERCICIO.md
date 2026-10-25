# Reto avanzado C: mini análisis de datos

## Enunciado

Recupera datos de una tabla con Python, calcula una
estadística sencilla y muestra los resultados.

Si ya conoces pandas, investiga cómo convertir
los resultados en un DataFrame.

## Datos que utilizaremos

Utilizaremos la base de datos `programacion.db`,
almacenada en la carpeta `data` del repositorio.

La tabla `lenguajes` contiene diez registros y estas columnas:

| Columna | Descripción |
|---|---|
| `id` | Identificador generado automáticamente. |
| `nombre` | Nombre del lenguaje. |
| `creador` | Persona que creó el lenguaje. |
| `anio` | Año de creación registrado. |
| `compania` | Compañía o contexto de origen. |
| `paradigma` | Etiqueta descriptiva del lenguaje. |

La base de datos se prepara en el reto avanzado A.
En este ejercicio utilizaremos los datos existentes.

## Objetivos

- Conectar Python con una base de datos SQLite.
- Ejecutar una consulta SQL.
- Recuperar y mostrar los resultados.
- Calcular una estadística sencilla con Python.
- Convertir los resultados en un DataFrame de pandas.

## Preparación

Sigue las instrucciones del [README.md](README.md)
para crear el entorno virtual e instalar las dependencias.

Escribe el programa en el archivo `main.py`.

## Paso 1. Conectar con la base de datos

Importa `sqlite3` y abre una conexión con
`data/programacion.db`.

Construye la ruta tomando como referencia la ubicación
de `main.py`, para que funcione aunque ejecutes el programa
desde otra carpeta.

Crea un cursor para ejecutar las instrucciones SQL.

## Paso 2. Recuperar los datos

Escribe una consulta SQL que obtenga estas columnas
de la tabla `lenguajes`:

- nombre
- creador
- anio
- compania
- paradigma

Ejecuta la consulta con `execute()` y recupera
los resultados con `fetchall()`.

## Paso 3. Mostrar los resultados

Recorre los registros con un bucle y muestra
la información en la terminal.

## Paso 4. Calcular una estadística sencilla

Utiliza Python para obtener el menor y el mayor
de los años recuperados.

Muestra ambos resultados indicando qué representan.

Con los datos de práctica, los resultados esperados son:

- Año más antiguo: 1972.
- Año más reciente: 2014.

## Paso 5. Crear un DataFrame

Importa pandas y convierte los resultados recuperados
en un DataFrame.

Asigna estos nombres a sus columnas:

- nombre
- creador
- anio
- compania
- paradigma

Muestra el DataFrame en la terminal.

## Paso 6. Cerrar la conexión

Cierra la conexión con SQLite cuando hayas terminado
de recuperar los datos.
