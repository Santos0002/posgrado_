import sqlite3
import pandas as pd
import flet as ft
from simpledt import DataFrame

def mostrar_tabla_posgrado(page: ft.Page):
    # Conectar a la base de datos
    conexion = sqlite3.connect('posgrado.sqlite3')
    cursor = conexion.cursor()

    # Ejecutar la consulta para obtener los datos de la tabla 'posgrado'
    cursor.execute('SELECT id_posgrado, nombre, tipo, activo, snp, orientacion, modalidad, id_division, id_responsable FROM posgrado')
    datos_posgrado = cursor.fetchall()

    # Crear un DataFrame directamente desde los datos obtenidos
    df = pd.DataFrame(datos_posgrado, columns=['Clave', 'Nombre', 'Tipo', 'Activo', 'SNP', 'Orientación', 'Modalidad', 'División', 'Responsable'])

    # Número de filas por página
    filas_por_pagina = 10
    num_paginas = len(df) // filas_por_pagina + (1 if len(df) % filas_por_pagina > 0 else 0)
    current_page = 0

    # Crear un contenedor para la tabla
    container = ft.Container()

    # Crear una función para actualizar la tabla
    def actualizar_tabla(page_index):
        nonlocal current_page
        current_page = page_index
        start = current_page * filas_por_pagina
        end = start + filas_por_pagina
        df_pagina = df.iloc[start:end]

        # Crear una DataTable de simpledatatable con el DataFrame de la página actual
        simpledt_df = DataFrame(df_pagina)
        dt = simpledt_df.datatable

        # Personalizar la apariencia de la DataTable
        dt.bgcolor = ft.colors.LIGHT_BLUE  # Cambiar el color de fondo del encabezado
        dt.border = ft.border.all(2, ft.colors.RED_900)  # Cambiar el color y grosor del borde
        dt.font_size = 6  # Cambiar el tamaño de letra a un tamaño más pequeño
        dt.font_color = ft.colors.WHITE  # Cambiar el color del texto
        dt.headers = ['Clave', 'Nombre', 'Tipo', 'Activo', 'SNP', 'Orientación', 'Modalidad', 'División', 'Responsable']  # Cambiar el título de los encabezados

        # Limpiar el contenedor y agregar la nueva tabla
        container.content = dt
        page.update()

    # Crear botones de navegación
    def crear_botones_navegacion():
        botones = []
        for i in range(num_paginas):
            btn = ft.ElevatedButton(text=f"Página {i+1}", on_click=lambda e, i=i: actualizar_tabla(i))
            botones.append(btn)
        return ft.Row(botones)

    # Crear la interfaz inicial
    actualizar_tabla(current_page)
    botones_navegacion = crear_botones_navegacion()

    # Crear un contenedor principal para la tabla y los botones de paginación
    main_container = ft.Column(
        [container, botones_navegacion],
        expand=True
    )

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Devolver el contenedor principal para que pueda ser agregado a la página
    return main_container

# Si se ejecuta este archivo como script principal, inicia la aplicación
if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(mostrar_tabla_posgrado(page))

    ft.app(target=main)
