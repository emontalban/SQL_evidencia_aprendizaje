import sqlite3

# Conectar a la base de datos de lenguajes de programación
conn = sqlite3.connect("Reto_Avanzado_A/programacion.db")

cursor = conn.cursor()

# Intentamos consultar la información de la base de datos
conn.execute("SELECT nombre, anio FROM lenguaje")
resultados = conn.fetchall()

# Mostrar los resultados por pantalla
for fila in resultados:
  print(f"Lenguaje: {fila[0]} ({fila[1]})")

# Cerrar la conexión
conn.close()