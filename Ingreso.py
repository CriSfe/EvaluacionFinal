import tkinter as tk
import tkinter as ttk
import ventana_menu as vm
from tkinter import messagebox


class IngresoApp:
    CLAVE_BASE = "123"
    input_clave = ""
    ventana_menu = None

    def __init__(self):
        self.clave = ""
        
    def validar_clave(self):
        self.clave = self.input_clave.get()

        if (self.clave.strip() == ""):
            messagebox.showwarning("Advertencia", "Debe ingresar una clave.")
        elif (self.clave.strip() != self.CLAVE_BASE):
            messagebox.showerror("Error", "Clave incorrecta.")
        else:
            objMenuApp = vm.VentanaMenu()
            objMenuApp.mostrar_menu()
            #self.cerrar_ventana()

    def cerrar_ventana(self):
        self.abrir_menu.destroy()

    def accionMenuAcercaDe(self):
        messagebox.showinfo("Información", "Consolidación Fase 5\nDesarrollo de la Aplicación - Python Tkinter\nEstudiante: Cristhian Quintero Holguín \nGrupo: 114")

    def abrir_menu(self):
        #Creación de la ventana del menú principal
        self.ventana_menu = tk.Tk()
        self.ventana_menu.title("Menú Principal - Consolidación Fase 5")
        self.ventana_menu.resizable(False, False)

        #Dimensiones de la ventana
        ancho_ventana = 400
        alto_ventana = 300

        #obtener dimensiones de la pantalla
        ancho_pantalla = self.ventana_menu.winfo_screenwidth()
        alto_pantalla = self.ventana_menu.winfo_screenheight()

        #Calcular posición x e y para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        #Establecer dimensiones y posición de la ventana
        self.ventana_menu.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        #Titulo principal del ventana ingreso
        titulo_menu = ttk.Label(self.ventana_menu, text="Menú de al Sistema", font=("Arial", 16))
        titulo_menu.pack(pady=20)

        #Elementos del menú
        label_contraseña = tk.Label(self.ventana_menu, text="Bienvenido al sistema.\n Ingrese la clave", font=("Arial", 12))
        label_contraseña.pack(pady=10)
        self.input_clave = tk.Entry(self.ventana_menu, show="*", font=("Arial", 12))
        self.input_clave.pack(pady=10)
        self.input_clave.focus_set()

        #Boton para validar la clave y salir de la aplicación
        boton_validar = tk.Button(self.ventana_menu, text="Validar Clave", bg="darkseagreen4" , command=self.validar_clave, font=("Arial", 12))
        boton_validar.pack(pady=10)

        boton_salir = tk.Button(self.ventana_menu, text="Salir", bg="brown3", command=self.ventana_menu.quit, font=("Arial", 12))
        boton_salir.pack(pady=10)

        #Menu de opciones
        menu_bar = tk.Menu(self.ventana_menu)
        menu_ayuda = tk.Menu(menu_bar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.accionMenuAcercaDe)
        menu_bar.add_cascade(label="Ayuda", background="darkslategray3", menu=menu_ayuda)    
        self.ventana_menu.config(menu=menu_bar)


        self.ventana_menu.mainloop()