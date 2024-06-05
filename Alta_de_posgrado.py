import flet as ft
from modelo import Division, Responsable, Posgrado  # Asegúrate de importar Posgrado

def main(page: ft.Page):
    def guardar_datos(e):
        # Obtener los datos ingresados por el usuario
        nombre_posgrado = txtNombre_Posgrado.value
        grado = drpGrado.value
        snp = "Sí" if c1.value else "No"
        orientacion = cg.value
        modalidad = ca.value
        division = drpDivision.value
        responsable = drpResponsable.value

        # Buscar la división y responsable seleccionados
        division_obj = Division.get(Division.id_division == division)
        responsable_obj = Responsable.get(Responsable.nombre == responsable)

        # Guardar los datos en la base de datos
        try:
            nuevo_posgrado = Posgrado.create(
                nombre=nombre_posgrado,
                tipo=grado,
                activo="Sí",
                snp=snp,
                orientacion=orientacion,
                modalidad=modalidad,
                id_division=division_obj,
                id_responsable=responsable_obj
            )
            mostrar_mensaje("Posgrado guardado correctamente", "green")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            mostrar_mensaje("Error al guardar los datos", "red")

    def mostrar_mensaje(mensaje, color):
        snackbar = ft.SnackBar(ft.Text(mensaje), show_close_icon=True, bgcolor=color)
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

    txtNombre_Posgrado = ft.TextField(
        label="Nombre de posgrado(Todo en mayuscula)", bgcolor="white"
    )

    opciones = [
        ft.dropdown.Option("Doctorado"),
        ft.dropdown.Option("Maestria"),
        ft.dropdown.Option("Especialidad"),
    ]
    drpGrado = ft.Dropdown(label="Seleccione el tipo:", options=opciones)

    c1 = ft.Checkbox(label="Pertenece al SNP", value=False)

    etiqueta_2 = ft.Text("Indique la orientacion", size=20)
    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="Profesional", label="Profesional"),
                ft.Radio(value="Investigador", label="Investigador"),
            ]
        )
    )

    etiqueta_3 = ft.Text("Indique la modalidad", size=20)
    ca = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="Escolarizada", label="Escolarizada"),
                ft.Radio(value="No escolarizada", label="No escolarizada"),
            ]
        )
    )

    lista = []
    divisiones = Division.select()
    for d in divisiones:
        option = ft.dropdown.Option(text=d.id_division)
        lista.append(option)
    drpDivision = ft.Dropdown(label=" - Selecione su division - ", options=lista)

    listaR = []
    responsable = Responsable.select()
    for d in responsable:
        option = ft.dropdown.Option(text=d.nombre)
        listaR.append(option)
    drpResponsable = ft.Dropdown(label=" - Selecione el responsable - ", options=listaR)

    btnGuardar = ft.ElevatedButton(
        "Guardar", icon="Save", bgcolor="green", color="white", on_click=guardar_datos
    )
    btnCancelar = ft.ElevatedButton(
        "Cancelar", icon="close", bgcolor="red", color="black"
    )

    rowBotnes = ft.Row([btnCancelar, btnGuardar], alignment="center")

    columna = ft.Column([txtNombre_Posgrado, drpGrado, etiqueta_2, cg, etiqueta_3, ca, drpDivision, drpResponsable, c1, rowBotnes])

    return columna

if __name__=="__main__":
    def main2(page: ft.Page):
        page.window_width = 500
        page.window_height = 700
        page.title = "Sistema posgrado"
        page.theme_mode = "Light"

        appBar = ft.AppBar(title=ft.Text("Alta de posgrado"), center_title=True, bgcolor="blue", color="white")
        page.appbar = appBar
        page.add(main(page))

    ft.app(target=main2)
