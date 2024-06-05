import sqlite3
import pandas as pd
import flet as ft
from simpledt import DataFrame

def mostrar_tabla_responsable(page: ft.Page):
    # Conectar a la base de datos
    conexion = sqlite3.connect('posgrado.sqlite3')
    cursor = conexion.cursor()

    # Ejecutar la consulta para obtener los datos de la tabla 'responsable'
    cursor.execute('SELECT id_responsable, nombre, grado, correo, id_division FROM responsable')
    datos_responsable = cursor.fetchall()

    # Crear un DataFrame directamente desde los datos obtenidos
    df = pd.DataFrame(datos_responsable, columns=['Clave', 'Nombre', 'Grado', 'Correo', 'División'])

    # Crear una DataTable de simpledatatable con el DataFrame
    simpledt_df = DataFrame(df)
    dt = simpledt_df.datatable

    # Personalizar la apariencia de la DataTable
    dt.bgcolor = ft.colors.LIGHT_BLUE  # Cambiar el color de fondo del encabezado
    dt.border = ft.border.all(2, ft.colors.RED_900)  # Cambiar el color y grosor del borde
    dt.font_size = 14  # Cambiar el tamaño de letra
    dt.font_color = ft.colors.WHITE  # Cambiar el color del texto
    dt.headers = ['Clave', 'Nombre', 'Grado', 'Correo', 'División']  # Cambiar el título de los encabezados

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Devolver la DataTable para que pueda ser agregada a la página
    return dt
