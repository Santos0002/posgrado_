from modulo import Division, Responsable
import flet

# Operacion select
divisiones = Division.select()
for d in divisiones:
    print(d.id_division,d.nombre,d.ubicacion)

# OperacioN Insert 
#nueva_division = Division.create(id_division = "DASTRO", nombre = "Division academica de astronautas", ubicacion = "Cunduacan")

# Operacion Delete
"""
dastro = Division(id_division = "DASTRO")
dastro.delete_instance()
"""

#Operacion Update
#dastro = Division(id_division = "DASTRO",ubicacion = "Campus Chontalpa")
#dastro.save()


