import flet as ft
from modelo import Division, Responsable, Posgrado

def main(page: ft.Page):
    def mostrar_posgrados_por_division(e: ft.ControlEvent):
        division_seleccionada = dprDivision.value
        posgrados = Posgrado.select().where(Posgrado.id_division == division_seleccionada, Posgrado.activo == "Sí")
        lista_posgrados = [ft.dropdown.Option(key=p.id_posgrado, text=p.nombre) for p in posgrados]
        dprPosgrado.options = lista_posgrados
        etiqueta.visible = False  # Ocultar la etiqueta al cambiar la división
        page.update()
    
    def mostrar_datos(e: ft.ControlEvent):
        etiqueta.visible = True
        page.update()

    def baja_posgrado(e: ft.ControlEvent):
        if dprPosgrado.value is None:
            print("Selecciona el posgrado")
            return
        try:
            p = Posgrado(id_posgrado=dprPosgrado.value, activo="No")
            p.save()
            mostrar_mensaje("Se dio de baja el posgrado")
            print("Registro modificado")
        except pw.IntegrityError as error:
            print(error)

    def mostrar_mensaje(mensaje):
        snackbar = ft.SnackBar(ft.Text(mensaje), show_close_icon=True, bgcolor="Green")
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

    """
    page.window_width = 500
    page.window_height = 400
    page.title = "Baja de posgrado"
    page.theme_mode = "Light"
    appBar = ft.AppBar(
        title=ft.Text("Baja de posgrado"),
        center_title=True,
        bgcolor="Blue",
        color="white",
    )
    """

    divisiones = Division.select()
    lista_divisiones = [ft.dropdown.Option(key=d.id_division, text=d.id_division) for d in divisiones]
    dprDivision = ft.Dropdown(label="Seleccione la División", options=lista_divisiones, on_change=mostrar_posgrados_por_division)

    lista_posgrados = []
    dprPosgrado = ft.Dropdown(label="Seleccione el posgrado", options=lista_posgrados, on_change=mostrar_datos)

    btnBaja = ft.ElevatedButton("Dar baja", icon="Save", bgcolor="green", color="white", on_click=baja_posgrado)
    btnCancelar = ft.ElevatedButton("Cancelar", icon="close", bgcolor="red", color="white", on_click=None)
    rowBotnes = ft.Row([btnCancelar, btnBaja], alignment="center")

    etiqueta = ft.Text("¿Seguro que desea dar de baja este programa?", size=18, visible=False)

    """
    page.appbar = appBar
    page.add(dprDivision, dprPosgrado, etiqueta, rowBotnes)
    page.update()
    """

#ft.app(target=main)

    columna = ft.Column([dprDivision,dprPosgrado,etiqueta, rowBotnes])

    return columna

if __name__=="__main__":
    def main2(page: ft.Page):
        # - Para modificar el largo de nuestra ventana
        page.window_width = 500

        # - Para modificar el ancho de nuestra ventana
        page.window_height = 600

        # - Agrega el titulo a la ventana
        page.title = "Sistema posgrado"

        # - Cambia el color del tema de la ventana
        page.theme_mode = "Light"
    

    # - Agrega un titulo dentro de la ventana, centrada
        appBar = ft.AppBar(title=ft.Text("Dar de Baja"),center_title=True, bgcolor="blue",color="white")
        page.appbar = appBar
        page.add(main(page))

    ft.app(target=main2)