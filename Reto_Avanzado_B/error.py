import sqlite3

# 1. Conectar a la base de datos de lenguajes de programación
conn = sqlite3.connect("programacion.db")

# 2. Crear el cursor (¡El error 1 solucionado!)
cursor = conn.cursor()

# 3. Ejecutar la consulta con el nombre de tabla correcto (¡El error 2 solucionado!)
cursor.execute("SELECT nombre, anio FROM lenguajes")
resultados = cursor.fetchall()

# Mostrar los resultados por pantalla
for fila in resultados:
  print(f"Lenguaje: {fila[0]} ({fila[1]})")

# 4. Cerrar la conexión correctamente
conn.close()