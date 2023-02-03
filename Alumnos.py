import sqlite3

conn = sqlite3.connect('Alumnos.db')
cursor = conn.cursor()

query = f"SELECT id FROM Alumnos WHERE nombre={'Juan'}"
print("Nombre del Alumno: ", query)

rows = cursor.execute(query)
data = rows.fetchone()

conn.commit()
cursor.close()
conn.close()
