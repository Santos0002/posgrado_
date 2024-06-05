import sqlite3
import pprint
def version_sqlite():
    conexion = sqlite3.connect("posgrado.sqlite3")
    cursor = conexion.cursor()
    consulta = "SELECT sqlite_version()"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    print(" - Version sqlite: ", resultado)
    cursor.close()
    conexion.close()

def consultar_responsables():
    conexion = sqlite3.connect("posgrado.sqlite3")
    cursor = conexion.cursor()
    consulta = "SELECT * FROM responsable"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    pprint.pprint(resultado)
    cursor.close()
    conexion.close()

def agregar_responsable(id_responsable, nombre, grado, contacto, id_division):
    conexion = sqlite3.connect("posgrado.sqlite3")
    cursor = conexion.cursor()
    consulta = "INSERT INTO responsable VALUES (?,?,?,?,?)"
    cursor.execute(consulta, [id_responsable,nombre,grado,contacto,id_division])
    conexion.commit()
    cursor.close()
    conexion.close()

#agregar_responsable("222h17018", "Diego Hechem Calderon", "Lic", "9331", "DACyTI")
consultar_responsables()
