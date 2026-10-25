import sqlite3

# 1. Conectar y crear la base de datos 'escuela.db'
conn = sqlite3.connect("data/escuela.db")
cursor = conn.cursor()

# 2. Crear las tablas principales
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    correo TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_curso TEXT NOT NULL,
    profesor TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudiante_id INTEGER,
    curso_id INTEGER,
    nota REAL,
    FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY(curso_id) REFERENCES cursos(id)
)
""")

# 3. Insertar datos de prueba en 'estudiantes'
estudiantes_data = [
    ("Lucía Gómez", 20, "lucia.gomez@email.com"),
    ("Mateo Pérez", 22, "mateo.perez@email.com"),
    ("Sofía Rodríguez", 19, "sofia.rodriguez@email.com"),
    ("Alejandro Ruiz", 21, "alejandro.ruiz@email.com"),
    ("Valentina Torres", 23, "valentina.torres@email.com"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO estudiantes (nombre, edad, correo) VALUES (?, ?, ?)",
    estudiantes_data,
)

# 4. Insertar datos de prueba en 'cursos'
cursos_data = [
    ("Python para Principiantes", "Carlos Mendoza"),
    ("Bases de Datos SQL", "Elena Vargas"),
    ("Introducción a la IA", "Javier Alarcón"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO cursos (nombre_curso, profesor) VALUES (?, ?)",
    cursos_data,
)

# 5. Insertar datos de prueba en 'matriculas'
matriculas_data = [
    (1, 1, 9.5),
    (1, 2, 8.8),
    (2, 1, 7.5),
    (3, 3, 9.0),
    (4, 2, 6.5),
    (5, 1, 8.2),
    (5, 3, 9.4),
]
cursor.executemany(
    "INSERT OR IGNORE INTO matriculas (estudiante_id, curso_id, nota) VALUES (?, ?, ?)",
    matriculas_data,
)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print(
    "¡Base de datos 'escuela.db' creada y poblada con éxito con datos de prueba!"
)