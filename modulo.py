import peewee as pw

bd_posgrado = pw.SqliteDatabase("posgrado.sqlite3")


class Division(pw.Model):
    id_division = pw.TextField(primary_key=True)
    nombre = pw.TextField(null=True)
    ubicacion = pw.TextField(null=True)

    class Meta:
        database = bd_posgrado


class Responsable(pw.Model):
    id_responsable = pw.TextField(primary_key=True)
    nombre = pw.TextField(null=True)
    grado = pw.TextField(null=True)
    contacto = pw.TextField(null=True)
    id_division = pw.ForeignKeyField(
        column_name="id_division", field="id_division", model=Division
    )

    class Meta:
        database = bd_posgrado


class Posgrado(pw.Model):
    id_posgrado = pw.IntegerField(primary_key=True)
    nombre = pw.TextField()
    tipo = pw.TextField()
    activo = pw.TextField()
    snp = pw.TextField()
    orientacion = pw.TextField()
    modalidad = pw.TextField()
    id_division = pw.ForeignKeyField(
        column_name="id_division", field="id_division", model=Division
    )
    id_responsable = pw.ForeignKeyField(
        column_name="id_responsable", field="id_responsable", model=Responsable
    )

    # Ligar la clase a esta base de datos
    class Meta:
        database = bd_posgrado
