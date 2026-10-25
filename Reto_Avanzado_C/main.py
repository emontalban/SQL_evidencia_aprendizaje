import sqlite3
import pandas as pd
from pathlib import Path

# Carpeta donde está main.py: la carpeta del reto C.
carpeta_reto = Path(__file__).resolve().parent

# Subimos a la carpeta principal y entramos en data.
db_path = carpeta_reto.parent / "data" / "programacion.db"

if not db_path.is_file():
  raise FileNotFoundError(
      f"⚠️ No se encontró la base de datos en {db_path}. Verifícalo antes de"
      " continuar."
  )

# Conectamos con la base de datos.
conexion = sqlite3.connect(db_path)
cursor = conexion.cursor()

print("Conexión realizada correctamente.")
# Ejecutamos la consulta SQL.
cursor.execute("""
    SELECT nombre, creador, anio, compania, paradigma
    FROM lenguajes
    ORDER BY anio
""")

# Recuperamos los resultados como una lista de tuplas.
lenguajes = cursor.fetchall()

# Ya tenemos los datos en Python y podemos cerrar la conexión.
conexion.close()

# Mostramos cada registro.
print("\n--- Lenguajes de programación ---")

for lenguaje in lenguajes:
    print(lenguaje)

# Creamos una lista vacía para guardar los años.
anios = []

for lenguaje in lenguajes:
    # El año está en la posición 2 de cada tupla.
    anios.append(lenguaje[2])

print("\n--- Estadísticas ---")

if anios:
    print("Año más antiguo:", min(anios))
    print("Año más reciente:", max(anios))
else:
    print("No hay datos para analizar.")

# Creamos una tabla de pandas con los datos recuperados.
df = pd.DataFrame(
    lenguajes,
    columns=["nombre", "creador", "anio", "compania", "paradigma"]
)

print("\n--- DataFrame de lenguajes ---")
print(df.to_string(index=False))


# Convertimos el DataFrame en una tabla con bordes.
tabla = df.to_markdown(index=False, tablefmt="grid")

# La primera línea nos permite conocer el ancho de la tabla.
ancho = len(tabla.splitlines()[0])

# Centramos el título utilizando ese ancho.
print()
print("LENGUAJES DE PROGRAMACIÓN".center(ancho))
print(tabla)