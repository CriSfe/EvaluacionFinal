import tkinter as tk
from Fase2 import Fase2CristhianHolguin as fase2
from Fase3 import Fase3CristhianQuintero as fase3
from Fase4 import Fase4CristhianQuinteroHolguinScript as fase4

class VentanaMenu:

    def __init__(self):
        pass


    def abrir_fase2(self):
        proyectFase2 = fase2.GestionParticipantes()
        proyectFase2.abrir_ventana_registro()

    def abrir_fase3(self):
        #parent = None
        gestor = fase3.GestorPacientes()
        proyectFase3 = fase3.VentanaControlUsuario(None, gestor)
        proyectFase3.crear_interfaz()

    def abrir_fase4(self):
        proyectFase4 = fase4.VentanaPrincipal()
        proyectFase4.dibujar_arbol()

    def mostrar_menu(self):
        ventana = tk.Tk()
        ventana.title("Ventana de Menú - Consolidación Fase 5")
        ventana.resizable(False, False)

        #Dimensiones de la ventana
        ancho_ventana = 400
        alto_ventana = 350

        #obtener dimensiones de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()   
        alto_pantalla = ventana.winfo_screenheight()

        #Calcular posición x e y para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        #Establecer dimensiones y posición de la ventana
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        #Titulo principal del ventana menu
        titulo_menu = tk.Label(ventana, text="Bienvenido al Menú Principal", font=("Arial", 16))
        titulo_menu.pack(pady=20)


        #Elementos del menú
        # Crear un frame para contener los elementos del menú y evitar mezclar pack y grid en la ventana principal
        frame_menu = tk.Frame(ventana)
        frame_menu.pack(pady=10)

        # Fila 1: Fase 2
        labelPaso2 = tk.Label(frame_menu, text="Proyecto de la Fase 2", font=("Arial", 12))
        labelPaso2.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        botonFase2 = tk.Button(frame_menu, text="Abrir Fase 2", bg="bisque1", width=12, command=self.abrir_fase2)
        botonFase2.grid(row=0, column=1, padx=5, pady=10, sticky="e")

        # Fila 2: Fase 3
        labelPaso3 = tk.Label(frame_menu, text="Proyecto de la Fase 3", font=("Arial", 12))
        labelPaso3.grid(row=1, column=0, padx=5, pady=10, sticky="w")
        botonFase3 = tk.Button(frame_menu, text="Abrir Fase 3", bg="bisque1", width=12, command=self.abrir_fase3)
        botonFase3.grid(row=1, column=1, padx=5, pady=10, sticky="e")

        # Fila 3: Fase 4
        labelPaso4 = tk.Label(frame_menu, text="Proyecto de la Fase 4", font=("Arial", 12))
        labelPaso4.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        botonFase4 = tk.Button(frame_menu, text="Abrir Fase 4", bg="bisque1", width=12, command=self.abrir_fase4)
        botonFase4.grid(row=2, column=1, padx=5, pady=10, sticky="e")

        #Boton para salir de la aplicación
        botonSalir = tk.Button(ventana, text="Salir", width=10, bg="brown3", command=ventana.destroy)
        botonSalir.pack(pady=10)
    
        ventana.mainloop()