import flet as ft
import peewee as pw
from modelo import Division
from modelo import Responsable
from modelo import Posgrado

def main(page: ft.Page):

    def mostrar_responsables (e: ft.ControlEvent):
       print("divicion",drp_division.value)   
          # Responsable
       lista = []
       reponsable = Responsable.select().where(Responsable.id_division==drp_division.value)
       for d in reponsable:
         lista.append(ft.dropdown.Option(key= d.id_responsable,text=d.nombre))
       drp_responsable.options = lista
       drp_responsable.update()

    def cerrar_ventana (e: ft.ControlEvent):
      page.window_close()
    def validar_campos (e: ft.ControlEvent):
      Error = None
      if  drp_responsable.value is None:
        Error= ("error: intoduce el nombre del responsable")
      elif txt_nombre.value.strip() =="":
        Error= ("error:ingrese su nombre nombre")
      elif drp_tipo.value is None:
        Error=("seleciona tu tipo de posgrado")
      elif drp_modalidad.value is None:
        Error= ("error:ingrese su modalidad")
      elif drp_division.value is None:
        Error=("seleciona tu divicion academica")
      else:

        guardar_datos()

      if Error is not None:  
        snackbar = ft.SnackBar(ft.Text(Error),show_close_icon=True)
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

    def guardar_datos():
        try:
            p = Posgrado.create(nombre=txt_nombre.value.strip(),
                        tipo=drp_tipo.value,
                        orientacion=radio_orientacion.value,
                        modalidad=drp_modalidad.value,
                        id_division=drp_division.value,
                        id_responsable=drp_responsable.value,
                        snp=chk_snp.value
                        )
            print("Datos guardados")
        except pw.IntegrityError as error:
            print("Error SQLite:", error)
        

        snackbar = ft.SnackBar(ft.Text("¡Todo bien!"), show_close_icon=True, bgcolor="green")
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()
    '''    
    # Configuración de la ventana
    page.window_width = 500
    page.window_height = 700
    page.title = "Alta de Posgrado"
    page.theme_mode = "WHITE"

    # Configuración de la AppBar
    appbar = ft.AppBar(title=ft.Text("Alta de Posgrado"),
                       center_title=True,
                       bgcolor="blue",
                       color="white")
    page.appbar = appbar
    '''
    # Campos de entrada
    txt_nombre = ft.TextField(label="Nombre")
    drp_tipo = ft.Dropdown(label="Tipo",
                           options=[ft.dropdown.Option("Especialidad"),
                                    ft.dropdown.Option("Maestría"),
                                    ft.dropdown.Option("Doctorado")])
    chk_snp = ft.Checkbox(label="Pertenece a SNP")
    chk_snp.checked = False  # Establecer el estado inicial del checkbox

    # Orientación (Simulado con botones de selección mutua)
    etiqueta=ft.Text("(Orientacion)", size=12)

    radio_orientacion = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Investigacion", label="Investigacion"),
        ft.Radio(value="Profecional", label="Profecional")
        
    ]))


    # Modalidad
    modalidades = [ft.dropdown.Option("Escolarizado"), ft.dropdown.Option("No Escolarizado")]
    drp_modalidad = ft.Dropdown(label="Modalidad", options=modalidades)

   # División
    lista2 = []
    divisiones = Division.select()
    for d in divisiones:
     lista2.append(ft.dropdown.Option(text=d.id_division))
    drp_division = ft.Dropdown(label="División", options=lista2, on_change=mostrar_responsables)


    drp_responsable = ft.Dropdown(label="Responsable", options=None)
    # Botones
    btn_guardar = ft.ElevatedButton("Guardar", icon="save", bgcolor="green", color="white", on_click=validar_campos)
    btn_cancelar = ft.ElevatedButton("Cancelar", icon="close", bgcolor="red", color="white", on_click=cerrar_ventana)
    '''
    # Agregar elementos a la página
    page.add(txt_nombre)
    page.add(drp_tipo)
    page.add(drp_modalidad)
    page.add(drp_division)
    page.add(drp_responsable)
    page.add(chk_snp)
    page.add(etiqueta)
    page.add(radio_orientacion)
   '''

    # Agregar botones
    row_botones = ft.Row([btn_guardar, btn_cancelar], alignment="center")
  #  page.add(row_botones)
      # Actualizar la página
   # page.update()
    columna = ft.Column([txt_nombre,drp_tipo,drp_modalidad,drp_division,drp_responsable,chk_snp,etiqueta,radio_orientacion,row_botones])
    return columna
    
if __name__=="__main__":
  ft.app(target=main)

