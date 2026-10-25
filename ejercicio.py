


import sqlite3


conexion = sqlite3.connect("supermercado.db")
cursor = conexion.cursor()


# 3. La consulta correcta: agrupamos por 'producto' (en singular, como se llama la columna)
cursor.execute("SELECT producto FROM pedidos GROUP BY producto HAVING COUNT(*) > 1")

# 4. Recuperamos y mostramos el resultado
resultados = cursor.fetchall()
print("Productos vendidos más de una vez:")
for fila in resultados:
    print(f"- {fila[0]}") # fila[0] extrae el texto de la tupla



# Inspeccionamos todos los registros de la tabla pedidos
cursor.execute("SELECT * FROM pedidos")
todos_los_pedidos = cursor.fetchall()

print("\n--- Contenido actual de la tabla pedidos ---")
for fila in todos_los_pedidos:
    print(fila)

cursor.execute("SELECT cliente, sum(precio) as total_gastado FROM pedidos where cliente= 'Pepe'")
total_gastado_por_pepe = cursor.fetchall()

print("\n--- Total gastado por Pepe ---")
for fila in total_gastado_por_pepe:
    print(fila)