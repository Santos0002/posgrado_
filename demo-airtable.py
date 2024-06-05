from pyairtable import Api
import pprint

api = Api("patM8m8O17bD5vEUc.0c44ff6c798f1a6556501eca3df41c9dfcb4e441b4cf2f3d4b4e36403ef3d039")
table = api.table("appeLGxou41ySo7Nw", "division")

registros = table.all()

pprint.pprint(registros)

for r in registros:
    pprint.pprint(r["fields"])

nueva = {"id_division": "DAF", "nombre": "División Academica de Filosofia", "ubicacion": "Campus Chontalpa"}

table.create(nueva)

