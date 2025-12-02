import tkinter as tk
from tkinter import messagebox
from datetime import datetime

### ------- CLASES DE LA LÓGICA DEL ÁRBOL BINARIO----------

class Nodo:
    def __init__(self, valor, nivel):
        self.valor = valor
        self.nivel = nivel #Controla el limite de los niveles
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.orden_insercion = []  # Lista para registrar el orden de inserción de los nodos

    ### ----------- funcion Agregar Nodo----------------------
    def agregarNodo(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor, nivel=1)
            self.orden_insercion.append(valor)  # Registrar el nodo insertado
        else:
            self._agregar(self.raiz, valor)
    
    def _agregar(self, nodo, valor):
        if valor == nodo.valor:
            raise Exception("Nodo repetido")
        
    # Limite de 4 niveles solamente
        if nodo.nivel == 4:
            raise Exception("No se permiten más de 4 niveles")
        
        if valor < nodo.valor:
            if nodo.izq:
                self._agregar(nodo.izq, valor)
            else:
                nodo.izq = Nodo(valor, nodo.nivel + 1)
                self.orden_insercion.append(valor)  
        else:
            if nodo.der:
                self._agregar(nodo.der, valor)
            else:
                nodo.der = Nodo(valor, nodo.nivel + 1)
                self.orden_insercion.append(valor)  
    
    ##----------funcion Buscar Nodo----------------------
    def buscarNodo(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            raise Exception("Nodo no encontrado")

        if valor == nodo.valor:
            return nodo
        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        else:
            return self._buscar(nodo.der, valor)
        
    ## --------Funcion Recorridos de los Nodos ---------

    def recorrido(self, modo):
        resultado = []
        if modo == "preorden":
            self.preorden(self.raiz, resultado)
        elif modo == "inorder":
            self.inorden(self.raiz, resultado)
        elif modo == "posorden":
            self.posorden(self.raiz, resultado)
        return resultado

    def preorden(self, nodo, lista):
        if nodo:
            lista.append(nodo.valor)
            self.preorden(nodo.izq, lista)
            self.preorden(nodo.der, lista)
    
    def inorden(self, nodo, lista):
        if nodo:
            self.inorden(nodo.izq, lista)
            lista.append(nodo.valor)
            self.inorden(nodo.der, lista)

    def posorden(self, nodo, lista):
        if nodo:
            self.posorden(nodo.izq, lista)
            self.posorden(nodo.der, lista)
            lista.append(nodo.valor)


### ------------- INTERFACES (LOGIN / PRINCIPAL) ---------

class VentanaLogin:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fase 4_Cristhian Quintero Holguin")

        tk.Label(self.root, text="Aplicación: Árboles Binarios").pack()
        tk.Label(self.root, text="Estudiante: Cristhian Quintero Holguin").pack()
        tk.Label(self.root, text=f"Fecha: {datetime.now().date()}").pack()

        tk.Label(self.root, text="Contraseña: ").pack()

        self.passw = tk.Entry(self.root, show="-")
        self.passw.pack()

        tk.Button(self.root, text="Ingresar", command=self.validar).pack()

        self.root.mainloop()

    def validar(self):
        if self.passw.get() == "UNAD":
            self.root.destroy()
            VentanaPrincipal()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

### ----------- VENTANA PRINCIPAL DE LOS ARBOLES --------------------
class VentanaPrincipal:

    

    def __init__(self):
            self.arbol = ArbolBinarioBusqueda()


            self.win = tk.Tk()
            self.win.title("Árbol Binario de Búsqueda")
            self.win.geometry("1000x700")

            #frame superior para los controles
            frame_controles = tk.Frame(self.win)
            frame_controles.grid(row=0, column=0, columnspan=5, pady=10)

                #Entrada de datos
            tk.Label(frame_controles, text="Ingrese un número:").grid(row=0, column=0, padx=5)
            self.entrada = tk.Entry(frame_controles, width=10)
            self.entrada.grid(row=0, column=1, padx=5)
            self.entrada.bind("<Return>", lambda e: self.agregar())

            # Botones
            tk.Button(self.win, text="Agregar Nodo", command=self.agregar).grid(row=1, column=0, padx=5, pady=5)
            tk.Button(self.win, text="Buscar Nodo", command=self.buscar).grid(row=1, column=1, padx=5, pady=5)
            tk.Button(self.win, text="Mostrar Recorrido", command=self.mostrar_recorridos).grid(row=1, column=2, padx=5, pady=5)
            tk.Button(self.win, text="Limpiar Arbol", command=self.limpiar_arbol).grid(row=1, column=3, padx=5, pady=5)
            tk.Button(self.win, text="Salir", command=self.win.destroy).grid(row=1, column=4, padx=5, pady=5)


            #Opciones de los recorridos
            self.recorrido_var = tk.StringVar(value="inorder")
            tk.Label(frame_controles, text="Tipos de Recorrido:").grid(row=2, column=0, padx=5)
            tk.Radiobutton(frame_controles, text="Preorden", variable=self.recorrido_var, value="preorden").grid(row=2, column=1)
            tk.Radiobutton(frame_controles, text="Inorden", variable=self.recorrido_var, value="inorder").grid(row=2, column=2)
            tk.Radiobutton(frame_controles, text="Posorden", variable=self.recorrido_var, value="posorden").grid(row=2, column=3)   

            # Resultado de los recorridos
            self.resultado = tk.Label(self.win, text="", fg="blue")
            self.resultado.grid(row=3, column=0, columnspan=5, pady=5)

            #Canvas para dibujar el árbol
            self.canva = tk.Canvas(self.win, width=900, height=500, bg="white", highlightthickness=1, highlightbackground="gray")
            self.canva.grid(row=4, column=0, columnspan=5, pady=10)

            #Frame para los recorridos
            frame_recorridos = tk.Frame(self.win)
            frame_recorridos.grid(row=5, column=0, columnspan=5, pady=10)

            tk.Label(frame_recorridos, text="Preorden:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5)
            tk.Label(frame_recorridos, text="Inorden:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5)
            tk.Label(frame_recorridos, text="Posorden:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5)
            tk.Label(frame_recorridos, text="Insercción:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=5)

            self.txt_pre = tk.Label(frame_recorridos, text="", font=("Arial", 12))
            self.txt_pre.grid(row=0, column=1, columnspan=3, sticky="w")

            self.txt_in = tk.Label(frame_recorridos, text="", font=("Arial", 12))
            self.txt_in.grid(row=1, column=1, columnspan=3, sticky="w")

            self.txt_pos = tk.Label(frame_recorridos, text="", font=("Arial", 12))
            self.txt_pos.grid(row=2, column=1, columnspan=3, sticky="w")

            self.txt_ins = tk.Label(frame_recorridos, text="", font=("Arial", 12), fg="green") 
            self.txt_ins.grid(row=3, column=1, columnspan=3, sticky="w")


            self.circulos = {}
            self.coordenadas = {}

            self.win.mainloop()
            

    ### Funciones para dibujar el arbol
    def dibujar_arbol(self, resaltar=None, destacado=None):
        self.canva.delete("all")
        self.circulos.clear()
        self.coordenadas.clear()

        if self.arbol.raiz:
            posiciones = {}
            self._calcular_posiciones(self.arbol.raiz, 450, 50, 220, posiciones)
            self.coordenadas = posiciones
            self._dibujar_nodos(self.arbol.raiz, posiciones, resaltar, destacado)

    def _calcular_posiciones(self, nodo, x, y, dx, posiciones):
        if nodo:
            posiciones[nodo.valor] = (int(x), int(y))

            new_dx = max(30, int(dx / 1.8))
            if nodo.izq:
                self._calcular_posiciones(nodo.izq, x - new_dx, y + 80, new_dx, posiciones)
            if nodo.der:
                self._calcular_posiciones(nodo.der, x + new_dx, y + 80, new_dx, posiciones)

    def _dibujar_nodos(self, nodo, posiciones, resaltar, destacado, padre=None):
        if nodo:
            x, y = posiciones[nodo.valor]
            
            #Dibujar línea al padre
            if padre:
                x0, y0 = posiciones[padre.valor]
                self.canva.create_line(x0, y0 + 25, x, y - 25, width=2)
            #Colores
            fill = "lightblue"
            outline = "blue"


            if resaltar and nodo.valor in resaltar:
                fill = "orange"
            if destacado and nodo.valor == destacado:
                outline = "magenta"
                fill = "yellow"
            
            #Dibujar circulo
            circ = self.canva.create_oval(x - 25, y - 25, x + 25, y + 25, fill=fill, outline=outline, width=2) 

            #Dibujar el texto
            self.canva.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"), fill="gray")

            self.circulos[nodo.valor] = circ

            #Dibujar hijos
            self._dibujar_nodos(nodo.izq, posiciones, resaltar, destacado, nodo)
            self._dibujar_nodos(nodo.der, posiciones, resaltar, destacado, nodo)



    
      
    def animar_inserccion(self, valor):
        ## Animar la inserción destacando el nodo recien creado
        self.dibujar_arbol(destacado=valor)
        self.win.after(1000, lambda: self.dibujar_arbol())
                

    ### ---- Funciones de trabajar con los nodos (agregar, buscar, limpiar y actualizar los recorridos)
    
    #1---- Función Agregar Nodo -----
    def agregar(self):
        try:
            text= self.entrada.get().strip()
            if not text:
                messagebox.showwarning("Advertencia", "Debes ingresar un número")
                return

            valor = int(text)
            self.arbol.agregarNodo(valor)
            self.entrada.delete(0, tk.END)
            self.animar_inserccion(valor)
            self.actualizar_recorridos()
            self.resultado.config(text=f"Nodo {valor} agregado correctamente")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    #2---- Función Buscar Nodo -----
    def buscar(self):
        try:
            texto = self.entrada.get().strip()
            if not texto:
                messagebox.showwarning("Advertencia", "Debe ingresar un número")
                return
            
            valor = int(texto)
            nodo = self.arbol.buscarNodo(valor)
            messagebox.showerror("Encontrado", f"Nodo {nodo.valor} encontrado")
            self.dibujar_arbol(destacado=valor)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #3---- Función Mostrar Recorridos -----
    def mostrar_recorridos(self):
        modo = self.recorrido_var.get()
        recorrido = self.arbol.recorrido(modo)
        self.resultado.config(text=f"{modo}: {recorrido}", fg="green")
        self.dibujar_arbol(resaltar=recorrido if recorrido else None, destacado=None)

    #4--- Función limpiar Arbol -----
    def limpiar_arbol(self):
        self.arbol = ArbolBinarioBusqueda()
        self.canva.delete("all")
        self.resultado.config(text="Árbol limpiado", fg="blue")
        self.circulos.clear()
        self.coordenadas.clear()
        self.actualizar_recorridos()

    

    def actualizar_recorridos(self):
        pre, inn, pos = [], [], []
        self.arbol.preorden(self.arbol.raiz, pre)
        self.arbol.inorden(self.arbol.raiz, inn)
        self.arbol.posorden(self.arbol.raiz, pos)

        self.txt_pre.config(text=str(pre) if pre else "[]")
        self.txt_in.config(text=str(inn) if inn else "[]")
        self.txt_pos.config(text=str(pos)if pos else "[]")
        self.txt_ins.config(text=str(self.arbol.orden_insercion) if self.arbol.orden_insercion else "[]")  # ← NUEVA

## --------Lanzar la ventana de login ---------
if __name__ == "__main__":
    VentanaLogin()