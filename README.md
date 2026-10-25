# Aprendizaje de SQL, Python e Inteligencia Artificial

Este repositorio recoge mi proceso de aprendizaje de SQL y Python,
utilizando la inteligencia artificial como apoyo para comprender
conceptos, practicar y resolver dudas.

Incluye diarios de aprendizaje individual, una misión de investigación
y ejercicios prácticos.

## Documentación de aprendizaje

| Documento | Contenido |
|---|---|
| [Diario SQL](diario-sql.md) | Consultas, ejercicios y explicaciones de SQL. |
| [Profesora personal](profesora-personal.md) | Preguntas, respuestas y actividades de aprendizaje con ayuda de la IA. |
| [Misión de investigación](mision-investigacion.md) | Respuestas y reflexiones sobre cómo trabajan juntos SQL y Python. |

## Ejercicios prácticos

| Carpeta | Contenido |
|---|---|
| [Reto 3](reto-3/) | Ejemplo de Python que ejecuta una consulta SQL y recupera sus resultados. |
| [Reto avanzado A](reto-avanzado-a/) | Creación de una base de datos SQLite de lenguajes de programación e inserción de diez registros. |
| [Reto avanzado B](reto-avanzado-b/) | Detección y corrección de dos errores en un programa de Python que utiliza SQLite. |
| [Reto avanzado C](reto-avanzado-c/) | Análisis de lenguajes de programación utilizando SQLite, Python y pandas. |
| [Datos](data/) | Carpeta que contiene la base de datos compartida por los retos avanzados A, B y C. |

## Herramientas utilizadas

- Python.
- SQLite, mediante el módulo `sqlite3`.
- Pandas, en el reto avanzado C.
- Visual Studio Code.
- Inteligencia artificial como apoyo al aprendizaje.

## Cómo utilizar este repositorio

1. Consulta los documentos de aprendizaje.
2. Abre la carpeta del reto que quieras realizar.
3. Lee sus instrucciones antes de ejecutar el código.
4. Ejecuta primero el reto avanzado A para preparar la base de datos compartida.

El reto avanzado C dispone de instrucciones para crear
un entorno virtual e instalar sus dependencias:

[Instalación y ejecución del reto avanzado C](reto-avanzado-c/README.md)

## Base de datos compartida

Los retos avanzados A, B y C utilizan la misma base de datos:
`programacion.db`, almacenada en la carpeta `data`.

Contiene una tabla llamada `lenguajes` con diez registros
y seis columnas:

| Columna | Contenido |
|---|---|
| `id` | Identificador generado automáticamente. |
| `nombre` | Nombre del lenguaje de programación. |
| `creador` | Persona que creó el lenguaje. |
| `anio` | Año de creación registrado. |
| `compania` | Compañía o contexto de origen. |
| `paradigma` | Etiqueta descriptiva del lenguaje. |

El reto avanzado A prepara la tabla e inserta los registros.
El reto avanzado B permite practicar la detección de errores
al consultar la base de datos.
El reto avanzado C recupera sus datos para analizarlos
con Python y pandas.

## Objetivo

Comprender cómo utilizar SQL para consultar datos y Python
para procesarlos y analizarlos, explicando el código
con mis propias palabras.