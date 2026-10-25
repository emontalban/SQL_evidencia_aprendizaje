import sqlite3

# 1. Conectar y crear el archivo de la base de datos 'programacion.db'
conn = sqlite3.connect("Reto_Avanzado_A/programacion.db")
cursor = conn.cursor()

# 2. Crear la tabla con columnas estructuradas y uniformes
cursor.execute("""
CREATE TABLE IF NOT EXISTS lenguajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    creador TEXT,
    anio INTEGER,
    compania TEXT,
    paradigma TEXT
)
""")

# 3. Lista con los 10 registros consistentes
lenguajes_data = [
    ("Python", "Guido van Rossum", 1991, "Independiente", "Multiparadigma"),
    ("JavaScript", "Brendan Eich", 1995, "Netscape", "Web / Interpretado"),
    ("C", "Dennis Ritchie", 1972, "Bell Labs", "Procedural"),
    ("C++", "Bjarne Stroustrup", 1985, "Bell Labs", "Multiparadigma"),
    ("Java", "James Gosling", 1995, "Sun Microsystems", "Orientado a Objetos"),
    ("Ruby", "Yukihiro Matsumoto", 1995, "Independiente", "Multiparadigma"),
    ("PHP", "Rasmus Lerdorf", 1994, "Independiente", "Web / Servidor"),
    ("Swift", "Chris Lattner", 2014, "Apple", "Multiparadigma"),
    ("Rust", "Graydon Hoare", 2010, "Mozilla", "Sistemas / Concurrente"),
    ("TypeScript", "Anders Hejlsberg", 2012, "Microsoft", "Tipado / Web"),
]

# Insertar los 10 registros de manera masiva
cursor.executemany(
    """
    INSERT OR IGNORE INTO lenguajes (nombre, creador, anio, compania, paradigma)
    VALUES (?, ?, ?, ?, ?)
""",
    lenguajes_data,
)

# Guardar los cambios (commit) en la base de datos
conn.commit()

# 4. Ejecutar una consulta SQL para comprobar y mostrar los resultados desde Python
print("--- 10 LENGUAJES DE PROGRAMACIÓN EN LA BASE DE DATOS ---")
cursor.execute(
    "SELECT nombre, creador, anio, compania, paradigma FROM lenguajes ORDER BY anio"
)

for fila in cursor.fetchall():
    print(
        f"• {fila[0]} ({fila[2]}) | Creador: {fila[1]} | Compañía: {fila[3]} | Enfoque: {fila[4]}"
    )

# 5. Cerrar la conexión correctamente
conn.close()