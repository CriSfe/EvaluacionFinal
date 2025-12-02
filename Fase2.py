"""Aplicación: Gestión de Participantes
Autor: Cristhian Fernando Quintero Holguín"""


from tkinter import *  # Importa la librería Tkinter para crear interfaces gráficas
from tkinter import ttk # Importa ttk para usar widgets temáticos
from tkinter import messagebox # Importa messagebox para mostrar cuadros de diálogo


class GestionParticipantes:
    def __init__(self):
        self.root = Tk()
        self.root.title("Melodías Perfectas - Login")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        #Funcion Centrar Ventana
        self.centrar_ventana(self.root, 450, 300)

        #Lista para almacenar los estudiantes registrados
        self.estudiantes = []

        #Diccionario que almacena las técnicas artisticas con sus costos por clase
        self.tecnicas_artisticas_costos = {
            "Dibujo": 70000,
            "Pintura": 85000,
            "Escritura": 100000,
            "Fotografía": 90000,
            "Grabado": 75000
        }

        #Iniciar con la ventana de validar contraseña
        self.ventana_ingreso()


    def centrar_ventana(self, ventana, ancho, alto):
        ###se Centra la ventana en la pantalla
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    #"------------------------------------
    #  1. VENTANA DE INICIO - LOGIN
    # ------------------------------------"

    def ventana_ingreso(self):      
        #Titulo de la ventana
        titulo = Label(self.root, text="Aplicación: Gestión de Participantes", font=("Verdana", 16, "bold"), fg="#1e5d9b")
        titulo.pack(pady=10)
        autor = Label(self.root, text="Autor: Cristhian Fernando Quintero Holguín", font=("Verdana", 10), fg="#1e5d9b")
        autor.pack(pady=5)

        # Separador visual
        separador = Frame(self.root, height=3, bg="gray")
        separador.pack(fill=X, padx=50, pady=20)

        # Marco para el login
        marco_login = LabelFrame(self.root, text="Acceder al Sistema", 
                                font=("Verdana", 12, "bold"), fg="#46627e")
        marco_login.pack(pady=20, padx=50, fill=X)

        #Campo de ingreso de la contraseña
        Label(self.root, text="Contraseña:", font=("Verdana", 12)).pack(pady=(15,7))


        #Variable para almacenar la contraseña ingresada
        self.entrada_contrasena = Entry(marco_login, show="*", font=("Verdana", 12), width=20, justify=CENTER)
        self.entrada_contrasena.pack(pady=5)
        
        # Vincular Enter para ingresar
        self.entrada_contrasena.bind('<Return>', lambda e: self.validar_contrasena())

        #Boton Ingreso
        self.boton_ingreso = Button(marco_login, text="Ingresar", font=("Verdana", 12, "bold"), bg="green", fg="white", command=self.validar_contrasena, cursor="hand2")
        self.boton_ingreso.pack(pady=15)
        
        #Etiqueta para mostrar mensajes de éxito
        self.label_mensaje = Label(self.root, text="", font=("Verdana", 10), fg="green")
        self.label_mensaje.pack(pady=5)

        #Etiqueta para mostrar mensajes de error
        self.label_error = Label(self.root, text="", font=("Verdana", 10), fg="red")
        self.label_error.pack(pady=5)

        # Enfocar el cursor en el campo de la contraseña al iniciar la ventana
        self.entrada_contrasena.focus()



# Función para validar de la contraseña
    def validar_contrasena(self):
        contrasena_correcta = "123"
        contrasena_ingresada = self.entrada_contrasena.get()

        if contrasena_ingresada == contrasena_correcta:
            self.label_mensaje.config(text="Acceso concedido", fg="green")
            self.root.after(500, self.abrir_ventana_registro) #Esperar y se abre el formulario de registro
        else:
            self.label_error.config(text="Contraseña incorrecta. Inténtalo de nuevo.", fg="red")
            self.entrada_contrasena.delete(0, END)
            self.entrada_contrasena.focus()    

    #"-------------------------------------------
    # 2. VENTANA DE REGISTRO DE ESTUDIANTES 
    # -------------------------------------------"
    def abrir_ventana_registro(self):
        
        #ocultar la ventana de login
        self.root.withdraw()
        
        #Crear la ventana de registro
        self.ventana_registro = Toplevel(self.root)
        self.ventana_registro.title("Melodías Perfectas - Registro de Estudiantes")
        self.ventana_registro.geometry("650x550")
        self.ventana_registro.resizable(False, False)


        #Centrar la ventana
        self.centrar_ventana(self.ventana_registro, 650, 550)

        #Si se cierra la ventana de registro, se abre la ventana de login
        self.ventana_registro.protocol("WM_DELETE_WINDOW", self.volver_al_login)

        #Titulo de la ventana
        titulo_registro = Label(self.ventana_registro, text="Registro de Estudiantes", font=("Verdana", 16, "bold"), fg="#09437c")
        titulo_registro.pack(pady=15)


        #Marco del formulario
        self.marco_formulario = LabelFrame(self.ventana_registro, 
                                           text="Ingrese los datos del estudiante", 
                                           font=("Verdana", 12, "bold"), fg="#46627e")
        self.marco_formulario.pack(pady=10, padx=30, fill=BOTH, expand=True)

        self.crear_formulario()
        self.crear_botones()

# Formulario de registro

    def crear_formulario(self):

        #Fame para organizar de mejor manera los campos
        marco_formulario = Frame(self.marco_formulario)
        marco_formulario.pack(pady=20, padx=20, fill=BOTH, expand=True)
        
        # 1. Identificación
        Label(marco_formulario, text="Identificación:",
               font=("Verdana", 12, "bold")).grid(row=0, column=0, sticky=E, padx=(0,10), pady=8)
        self.entrada_identificacion = Entry(marco_formulario, font=("Verdana", 12), width=25)
        self.entrada_identificacion.grid(row=0, column=1, pady=8, sticky=W)

        # 2. Nombre Completo
        Label(marco_formulario, text="Nombre Completo:", font=("Verdana", 12, "bold")).grid(row=1, column=0, sticky=E, padx=(0,10), pady=8)
        self.entrada_nombre = Entry(marco_formulario, font=("Verdana", 12), width=25)
        self.entrada_nombre.grid(row=1, column=1, pady=8, sticky=W)

        # 3. Género
        Label(marco_formulario, text="Género:", font=("Verdana", 12, "bold")).grid(row=2, column=0, sticky=E, padx=(0,10), pady=8)
        
        self.genero_var = IntVar()

            #Frame de los Buttons
        frame_genero = Frame(marco_formulario)
        frame_genero.grid(row=2, column=1, sticky=W, pady=8)
        
        Radiobutton(frame_genero, text="Masculino", variable=self.genero_var, 
                   value=1, font=("Verdana", 12)).pack(side=LEFT, padx=(0,15))
        Radiobutton(frame_genero, text="Femenino", variable=self.genero_var, 
                   value=2, font=("Verdana", 12)).pack(side=LEFT)
        

        # 4. Técnica Artistica
        Label(marco_formulario, text="Técnica Artística:", font=("Verdana", 12, "bold")).grid(row=3, column=0, sticky=E, padx=(0,10), pady=8)
        self.tecnica_artistica_dropdown = ttk.Combobox(marco_formulario, values=list(self.tecnicas_artisticas_costos.keys()), font=("Verdana", 12), width=22, state="readonly")
        self.tecnica_artistica_dropdown.grid(row=3, column=1, pady=8, sticky=W)
            #Evento que actualiza el costo por clase al seleccionar una técnica
        self.tecnica_artistica_dropdown.bind("<<ComboboxSelected>>", self.actualizar_costo)

        # 5. Costo por Clase (Deshabiliado)
        Label(marco_formulario, text="Costo por Clase:", font=("Verdana", 12, "bold")).grid(row=4, column=0, sticky=E, padx=(0,10), pady=8)
        self.entrada_costo = Entry(marco_formulario, font=("Verdana", 12), width=25, 
                                  state="disabled", disabledbackground="white",
                                  disabledforeground="gray")
        self.entrada_costo.grid(row=4, column=1, pady=8, sticky=W)
        
        # 6. Número de Clases
        Label(marco_formulario, text="Número de Clases:", font=("Verdana", 12, "bold")).grid(row=5, column=0, sticky=E, padx=(0,10), pady=8)
        self.spin_clases = Spinbox(marco_formulario, from_=1, to=20, font=("Verdana", 12, "bold"), width=23, justify=CENTER)
        self.spin_clases.grid(row=5, column=1, pady=8, sticky=W)

        #Enfocar en el primer campo = Identificacion
        self.entrada_identificacion.focus()


    #Funcion para actualizar  el costo por clase al seleccionar una técnica
    def actualizar_costo(self, event=None):
        tecnica_seleccionada = self.tecnica_artistica_dropdown.get()

        if tecnica_seleccionada in self.tecnicas_artisticas_costos:
            costo = self.tecnicas_artisticas_costos[tecnica_seleccionada]
            
            #Habilitar temporalmente para actualizar el valor
            self.entrada_costo.config(state="normal")
            self.entrada_costo.delete(0, END)
            self.entrada_costo.insert(0, f"${costo:,}")
            self.entrada_costo.config(state="disabled")

    #Crear los botones de guardar, reporte y salir
    def crear_botones(self):


        marco_botones = Frame(self.ventana_registro)
        marco_botones.pack(pady=20)

        # Botón Guardar Registro
        self.boton_guardar_registro = Button(marco_botones, text="Guardar Registro", fg="white", bg="green", command=self.guardar_registro, font=("Verdana", 12, "bold"), width=15, height=2,cursor="hand2")
        self.boton_guardar_registro.grid(row=0, column=0, padx=10)

        #Botón Mostrar Reporte
        self.boton_reporte = Button(marco_botones, text="Calcular Costo /\nMostrar Reporte",  fg="white", bg="blue", command=self.mostrar_reporte, font=("Verdana", 12, "bold"), width=15, height=2,cursor="hand2")
        self.boton_reporte.grid(row=0, column=1, padx=10)

        # Botón Salir
        self.boton_salir = Button(marco_botones, text="Salir", fg="white", bg="red", command=self.confirmar_salida, font=("Verdana", 12, "bold"), width=15, height=2,cursor="hand2")
        self.boton_salir.grid(row=0, column=2, padx=10)


    # -------------------------
    # 3. FUNCIONES DE LA APLICACIÓN
    # -------------------------
    #Validar que los campos esten llenos
    def validar_campos(self):

        if not self.entrada_identificacion.get().strip():
            messagebox.showerror("Error", "El campo 'Identificación' es obligatorio.")
            self.entrada_identificacion.focus()
            return False
        
        if not self.entrada_nombre.get().strip():
            messagebox.showerror("Error", "El campo 'Nombre Completo' es obligatorio.")
            self.entrada_nombre.focus()
            return False
        
        if self.genero_var.get() not in [1, 2]:
            messagebox.showerror("Error", "Seleccione un género.")
            return False
        
        if not self.tecnica_artistica_dropdown.get():
            messagebox.showerror("Error", "Seleccione una técnica artística.")
            self.tecnica_artistica_dropdown.focus()
            return False
        
        if not self.spin_clases.get() or int(self.spin_clases.get()) < 1:
            messagebox.showerror("Error", "El campo 'Número de Clases' es obligatorio.")
            self.spin_clases.focus()
            return False
        
        return True

    #Guardar el registro del estudiante
    def guardar_registro(self):

        if not self.validar_campos():
            return
        
        try: 
            #Diccionario creado con los datos del estudiante
            estudiante = {
                'identificacion': self.entrada_identificacion.get().strip(),
                'nombre': self.entrada_nombre.get().strip(),
                'genero': 'Masculino' if self.genero_var.get() == 1 else 'Femenino',
                'tecnica_artistica': self.tecnica_artistica_dropdown.get(),
                'costo_por_clase': self.tecnicas_artisticas_costos[self.tecnica_artistica_dropdown.get()],
                'numero_clases': int(self.spin_clases.get())
            }

            #Verificar que no se repita un estudiante
            for est in self.estudiantes:
                if est['identificación'] == estudiante['identificacion']:
                    messagebox.showerror("Error", f"El estudiante que intentas ingresar ya está registrado: {estudiante['identificacion']}")
                    return
                
            #Agrega el estudiante a la lista 
            self.estudiantes.append(estudiante)

            messagebox.showinfo("Éxito", f"Estudiante registrado exitosamente. {estudiante['nombre']}")
            
            #Limpia el formulario
            self.limpiar_formulario()

        except ValueError:
            messagebox.showerror("Error", "Hay un error al procesar los datos.")
        
###Mostrar el reporte del ultimo estudiante que se haya registrado y el coste total
    def mostrar_reporte(self):
        #Verifica que haya estudiantes registrados
        if not self.validar_campos():
            return
        
        try:
            #"---- Se obtiene los datos con los datos actuales----------"
            identificacion = self.entrada_identificacion.get().strip()
            nombre = self.entrada_nombre.get().strip()
            genero = "Masculino" if self.genero_var.get() == 1 else "Femenino"
            tecnica = self.tecnica_artistica_dropdown.get()
            costo_clase = self.tecnicas_artisticas_costos[tecnica]
            numero_clases = int(self.spin_clases.get())
            total_pagar = costo_clase * numero_clases


            #"----------------Crear la ventana de reporte------------------"
            ventana_reporte = Toplevel(self.ventana_registro)
            ventana_reporte.title("Reporte de Estudiante")
            ventana_reporte.geometry("500x400")
            ventana_reporte.resizable(False, False)

            #Centrar la ventana de Reporte
            self.centrar_ventana(ventana_reporte, 500, 400)


            #Título del reporte
            Label(ventana_reporte, text = "REPORTE DEL ESTUDIANTE", font=("Verdana", 12, "bold")).pack(pady=5)
            
            #Marco para la información del estudiante
            marco_reporte = LabelFrame(ventana_reporte, text="Información detallada",font=("Verdana", 12, "bold"), fg="gray")
            marco_reporte.pack(pady=10, padx=20, fill=BOTH, expand=True)
            

            info_texto = f"""
    IDENTIFICACIÓN:    {identificacion}

    NOMBRE COMPLETO:   {nombre}

    GÉNERO:            {genero}

    TÉCNICA ARTÍSTICA: {tecnica}

    NÚMERO DE CLASES:  {numero_clases}

    COSTO POR CLASES: ${costo_clase:,}

    TOTAL A PAGAR:    ${total_pagar:,}
    """
            Label(marco_reporte, text=info_texto, justify=LEFT, font=("Verdana", 12), fg="gray").pack(pady=20, padx=20)

            #Botón para cerrar el reporte
            Button(ventana_reporte, text="Cerrar Reporte", command=ventana_reporte.destroy, bg="gray", fg="white", font=("Verdana", 10, "bold"),
                   width=20, cursor="hand2").pack(pady=15)
            

        except ValueError:
            messagebox.showerror("Error", "Error al calcular el reporte")

    #---Función para limpiar los campos del formulario-----
    def limpiar_formulario(self):

        self.entrada_identificacion.delete(0, END)
        self.entrada_nombre.delete(0, END)
        self.genero_var.set(0)
        self.tecnica_artistica_dropdown.set("")

        #Limpiar los campos de costo
        self.entrada_costo.config(state="normal")
        self.entrada_costo.delete(0, END)
        self.entrada_costo.config(state="disabled")

        #Resetear el Spinbox
        self.spin_clases.delete(0, END)
        self.spin_clases.insert(0, "1")

        #Enfocar en el primer campo = Identificacion
        self.entrada_identificacion.focus()
    
    # ----------------------------
    #   4. FUNCIONES DE NAVEGACIÓN ENTRE VENTANAS
    # ----------------------------

    ##----Función para volver al login-------
    def volver_al_login(self):
        self.ventana_registro.destroy()
        self.root.deiconify() #Muestra la ventana de login nuevamente
        self.entrada_contrasena.delete(0, END)
        self.label_mensaje.config(text="")
        self.entrada_contrasena.focus()

    #función para confirmar la salida de la aplicación
    def confirmar_salida(self):
        respuesta = messagebox.askyesno("Confirmar Salida", "¿Estás seguro de que deseas salir de la aplicación?")
    
        if respuesta:
            self.root.quit()

    #Función ejecutar la aplicación
    def ejecutar(self):
        self.root.mainloop()

# ------------------------------
# 5. CLASE ESTUDIANTE
# ------------------------------

class Estudiante:
    def __init__(self, identificacion, nombre, genero, tecnica_artistica, costo_por_clase, numero_clases):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.tecnica_artistica = tecnica_artistica
        self.costo_por_clase = costo_por_clase
        self.numero_clases = numero_clases
    
    def calcular_costo_total(self):
        return self.costo_por_clase * self.numero_clases

    def __str__(self):
        return f"{self.nombre} - {self.identificacion}"

# ------------------------------
# 6. EJECUCIÓN PRINCIPAL
# ------------------------------


if __name__ == "__main__":
    print("...Iniciando aplicación Melodías Perfectas...")
    print("Autor: Cristhian Fernando Quintero Holguín")
    print("Contraseña de prueba: 123")
    print("-" * 50)

    app = GestionParticipantes()
    app.ejecutar()
    