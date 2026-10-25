import sqlite3

conn = sqlite3.connect("Reto_3/escuela.db")
cursor = conn.cursor()

# Consultar todos los estudiantes
print("--- ESTUDIANTES ---")
cursor.execute("SELECT * FROM estudiantes")
for fila in cursor.fetchall():
    print(fila)

# Consultar los cursos y sus profesores
print("\n--- CURSOS ---")
cursor.execute("SELECT * FROM cursos")
for fila in cursor.fetchall():
    print(fila)

conn.close()