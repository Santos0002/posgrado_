import flet as ft
import responsable
import Alta_de_posgrado
import Bajas_De_posgrado
import tabla_responsable
import tabla_posgrado

def main(page: ft.Page):

    def mostrar_opcion(e: ft.ControlEvent):
        # Limpiar el contenido del contenedor principal
        contenedorPrincipal.content = None
        # Seleccionar la opción basada en el índice del botón seleccionado
        if e.control.selected_index == 0:
            contenedorPrincipal.content = Alta_de_posgrado.main(page)
        elif e.control.selected_index == 1:
            contenedorPrincipal.content = responsable.main(page)
        elif e.control.selected_index == 2:
            contenedorPrincipal.content = Bajas_De_posgrado.main(page)
        elif e.control.selected_index == 3:
            contenedorPrincipal.content = tabla_responsable.mostrar_tabla_responsable(page)
        elif e.control.selected_index == 4:
            contenedorPrincipal.content = tabla_posgrado.mostrar_tabla_posgrado(page)
        contenedorPrincipal.update()

    page.theme_mode = "light"
    page.title = "Sistema de posgrados"

    # Configurar el tamaño de la ventana
    page.window_width = 800  
    page.window_height = 600 

    # Definir los botones de navegación
    btnNuevoPosgrado = ft.NavigationRailDestination(
        label="Nuevo Posgrado",
        icon="add_circle_outlined",
        selected_icon="add_circle"
    )

    btnNuevoRevisor = ft.NavigationRailDestination(
        label="Nuevo Revisor",
        icon="person_add_outlined",
        selected_icon="person_add"
    )

    btnBajaPosgrado = ft.NavigationRailDestination(
        label="Baja Posgrado",
        icon="person_add_disabled",
        selected_icon="person_add_disabled"
    )
    
    btnMostrarTablaResponsable = ft.NavigationRailDestination(
        label="Mostrar Tabla Responsable",
        icon="table_chart_outlined",
        selected_icon="table_chart"
    )

    btnMostrarTablaPosgrado = ft.NavigationRailDestination(
        label="Mostrar Tabla Posgrado",
        icon="table_chart_outlined",
        selected_icon="table_chart"
    )

    listaBotones = [
        btnNuevoPosgrado,
        btnNuevoRevisor,
        btnBajaPosgrado,
        btnMostrarTablaResponsable,
        btnMostrarTablaPosgrado
    ]

    # Crear la barra de navegación
    navRail = ft.NavigationRail(
        bgcolor="blue70",
        destinations=listaBotones,
        on_change=mostrar_opcion
    )

    # Crear el contenedor principal que cambiará su contenido según la selección
    contenedorPrincipal = ft.Container(expand=True)

    # Crear una fila que contenga la barra de navegación y el contenedor principal
    fila = ft.Row([navRail, contenedorPrincipal], expand=True)
    
    # Agregar la fila a la página
    page.add(fila)

ft.app(target=main)
