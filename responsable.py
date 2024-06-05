import flet as ft  
from modelo import Division
from modelo import Responsable

def main(page: ft.Page):
    def validar_campos(e: ft.ControlEvent):
        error = None
        if txtResponsable.value.strip() == "":
            error = "Error: Introduce el numero de empleado"
        elif txtNombre.value.strip() == "":
            error = "Error: Introduce su nombre"
        elif drpGrado.value is None:
            error = "Error: Selecciona el grado"
        elif txtCorreo.value.strip() == "":
            error = "Error: Introduce el correo"
        elif drpDivision.value is None:
            error = "Error: Selecciona la division"
        else:
            guardar_datos()
            print("- Numero de responsable: ",txtResponsable.value)
            print("- Nombre: ",txtNombre.value)
            print("- Grado: ",drpGrado.value)
            print("- Correo: ",txtCorreo.value)
            print("- Division: ",drpDivision.value)

        if error is not None:
            snackbar = ft.SnackBar(ft.Text(error),show_close_icon=True,bgcolor="orange")
            page.snack_bar = snackbar
            snackbar.open = True
            page.update()

    def guardar_datos():
        snackbar = ft.SnackBar(ft.Text(" Datos guardados "),show_close_icon=True, bgcolor="Green")
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

        responsable = Responsable.create(id_responsable=txtResponsable.value.strip(),
                                        nombre=txtNombre.value.strip(),
                                        grado=drpGrado.value,
                                        correo=txtCorreo.value.strip(),
                                        id_division=drpDivision.value)

    def cerrar_ventana(e: ft.ControlEvent):
        page.window_close()

    """

    # - Para modificar el largo de nuestra ventana
    page.window_width = 500

    # - Para modificar el ancho de nuestra ventana
    page.window_height = 600

    # - Agrega el titulo a la ventana
    page.title = "Sistema posgrado"

    # - Cambia el color del tema de la ventana
    page.theme_mode = "Light"
    

    # - Agrega un titulo dentro de la ventana, centrada
    appBar = ft.AppBar(title=ft.Text("Nuevo registro"),center_title=True, bgcolor="blue",color="white")
    page.appbar = appBar
    """
    # - Agregar una caja de texto
    txtResponsable = ft.TextField(label="Numero de empleado")
    etiqueta = ft.Text(" - Todo en mayusculas - ", size=12)
    txtNombre = ft.TextField(label="Nombre")
    opciones = [ft.dropdown.Option("Doctorado"),ft.dropdown.Option("Maestria")]
    drpGrado = ft.Dropdown(label=" - Selecione su grado - ",options=opciones)
    txtCorreo = ft.TextField(label="Correo")

    #Agregar las divisiones de la base de datos
    lista = []
    divisiones = Division.select()
    for d in divisiones:
        option = ft.dropdown.Option(text=d.id_division)
        lista.append(option)
    
    drpDivision = ft.Dropdown(label=" - Selecione su division - ", options=lista)

    #Botones
    btnGuardar = ft.ElevatedButton("Guardar",icon="save",bgcolor="green", color="white",on_click=validar_campos)
    btnCancelar = ft.ElevatedButton("Cancelar",icon="close",bgcolor="red", color="white",on_click=cerrar_ventana)
    rowBotones = ft.Row([btnCancelar,btnGuardar],alignment="center")
    ''''
    page.add(txtResponsable)
    page.add(etiqueta)
    page.add(txtNombre)
    page.add(drpGrado)
    page.add(txtCorreo)
    page.add(drpDivision)
    page.add(rowBotones)

    # - Esta debe ser la ultima linea de la funcion
    # - Sirve para actualizar el formulario o la ventana nueva
    page.update()
    '''

    columna = ft.Column([txtResponsable,etiqueta,txtNombre, drpGrado, txtCorreo, drpDivision, rowBotones])

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
        appBar = ft.AppBar(title=ft.Text("Nuevo registro"),center_title=True, bgcolor="blue",color="white")
        page.appbar = appBar
        page.add(main(page))

    ft.app(target=main2)