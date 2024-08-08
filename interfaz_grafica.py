from customtkinter import *
import tkinter as tk
###
from dependencias import *
from algoritmo_aleatorio import main_algoritmo_aleatorio
from algoritmo_simple import main_algoritmo_simple
from algoritmo_principal import main_algoritmo_principal
from algoritmo_busqueda_completa import main_algoritmo_busqueda_completa


class Frame_Columna(CTkFrame):
    def __init__(self, master):
        super().__init__(master) 

        self.cambiar_color_d = CTkButton(master=self, text="Modo Oscuro", fg_color="#1A5276", command = self.cambiar_color_dark)
        self.cambiar_color_d.pack(pady=5, side="top")

        self.cambiar_color_l = CTkButton(master=self, text="Modo Claro", fg_color="#BB8FCE", command = self.cambiar_color_light)
        self.cambiar_color_l.pack(pady=5, side="top")

        self.empty_label = CTkLabel(master=self, text = "", fg_color = "transparent")
        self.empty_label.pack(pady = 80, side= "top")

        self.exit = CTkButton(master=self, text="Salir", fg_color="red", command = self.salir)
        self.exit.pack(pady=5, side="bottom")

        self.reset = CTkButton(master=self, text="Reiniciar", fg_color="#D4AC0D", command = self.reiniciar)
        self.reset.pack(pady=5, side="bottom")

    def cambiar_color_dark(self):
        set_appearance_mode("dark")

    def cambiar_color_light(self):
        set_appearance_mode("light")

    def reiniciar(self):
        self.master.destroy()
        run()

    def salir(self):
        self.master.destroy()


class Frame_Principal(CTkFrame):
    def __init__(self, master):
        super().__init__(master) 

        self.abrir_tipo()

    def abrir_tipo(self):
        label = CTkLabel(master=self, text="Selecciona el Tipo de Grafo que Quieres Cargar", font= ("Helvetica", 30))
        label.grid(row = 0, column = 0, pady = 10, padx = 5)

        button_seleccionar_barrio = CTkButton(master= self, text = "Seleccionar un Barrio", command = lambda : self.selector_ubicacion("barrio"))
        button_seleccionar_barrio.grid(row = 1, column = 0, pady = 5, padx = 5)

        button_seleccionar_localidad = CTkButton(master= self, text = "Seleccionar una Localidad",  command = lambda : self.selector_ubicacion("localidad"))
        button_seleccionar_localidad.grid(row = 2, column = 0, pady = 5, padx = 5)

        advertencia = CTkLabel(master = self, text = "No es recomendable usar grafos tan grandes", fg_color="transparent")
        advertencia.grid(row = 3, column = 0, pady = 10, padx = 5)
        
        button_seleccionar_ciudad = CTkButton(master= self, text = "Seleccionar una Ciudad",  command = lambda : self.selector_ubicacion("ciudad"))
        button_seleccionar_ciudad.grid(row = 4, column = 0, pady = 3, padx = 5)

    def limpiar_self(self):
        for widget in self.winfo_children():
            widget.destroy()

    def selector_ubicacion(self, tipo):

        self.limpiar_self()

        if tipo == "barrio":
            opciones = ('Ciudad Jardín (Sur)', 'Ciudad Salitre (Occ.)', 'El Restrepo', 'Las Nieves', 'Modelia', 'Niza')
            nombre_interno = ('UPZ Ciudad Jardín, Bogotá, Colombia', 
                            'UPZ Ciudad Salitre Occidental, Bogotá, Colombia', 
                            'UPZ Restrepo, Bogotá, Colombia', 
                            'UPZ Las Nieves, Bogotá, Colombia', 
                            'UPZ Modelia, Bogotá, Colombia', 
                            'UPZ Niza, Bogotá, Colombia')
            
            label = CTkLabel(master=self, text="Selecciona el Barrio Cargar", font= ("Helvetica", 30))
            label.grid(row = 0, column = 0, pady = 10, padx = 5)

            for i in range(len(opciones)):
                opcion = nombre_interno[i]
                interno = nombre_interno[i]

                b = CTkButton(master=self, text=opcion, command=lambda interno=interno: self.cargar_grafo(interno))
                b.grid(row = i + 1, column = 0, pady = 5)
            

        if tipo == "localidad":
            opciones = ("Antonio Nariño", "Bosa", "Candelaria", "Engativá", "Kennedy", "Puente Aranda", "Suba", "Teusaquillo")
            nombre_interno = ("Localidad Antonio Nariño, Bogotá, Colombia", 
                            "Localidad Bosa, Bogotá, Colombia", 
                            "Localidad La Candelaria, Bogotá, Colombia",
                            "Localidad Engativá, Bogotá, Colombia", 
                            "Localidad Kennedy, Bogotá, Colombia",  
                            "Localidad Puente Aranda, Bogotá, Colombia", 
                            "Localidad Suba, Bogotá, Colombia", 
                            "Localidad Teusaquillo,Bogotá, Colombia")
            
            label = CTkLabel(master=self, text="Selecciona la Localidad a Cargar", font= ("Helvetica", 30))
            label.grid(row = 0, column = 0, pady = 10, padx = 5)

            for i in range(len(opciones)):
                opcion = nombre_interno[i]
                interno = nombre_interno[i]

                b = CTkButton(master=self, text=opcion, command=lambda interno=interno: self.cargar_grafo(interno))
                b.grid(row = i + 1, column = 0, pady = 5)

        if tipo == "ciudad":
            opciones = ("Armenia", "Cúcuta", "Montería", "Popayan", "Yopal")
            nombre_interno = ("Armenia, Capital, Quindio, Colombia", 
                            "Cúcuta, Norte de Santander, Colombia", 
                            "Montería, Córdoba, Colombia", 
                            "Popayán, Cauca, Colombia", 
                            "Yopal, Casanare, Colombia")

            label = CTkLabel(master=self, text="Selecciona la Localidad a Cargar", font= ("Helvetica", 30))
            label.grid(row = 0, column = 0, pady = 10, padx = 5)

            for i in range(len(opciones)):
                opcion = nombre_interno[i]
                interno = nombre_interno[i]

                b = CTkButton(master=self, text=opcion, command=lambda interno=interno: self.cargar_grafo(interno))
                b.grid(row = i + 1, column = 0, pady = 5)

            return

    def cargar_grafo(self, nombre):
        tk.messagebox.showinfo("Cargando", f"Se cargara el Grafo con la etiqueta:\n {nombre} \n\nCierra el grafo para continuar")
        try:
            self.G = importar_grafos(nombre)
        except Exception as err:
            tk.messagebox.showerror("Error", f"Error: {err}")
            return 
        ver_grafo(self.G, nombre)
        self.cargar_selector_cuadrantes()

    def cargar_selector_cuadrantes(self):
        self.limpiar_self()

        self.nodos = self.G.nodes(data=True)
        self.aristas = self.G.edges(data=True)

        self.grafo = transformacion_grafo(self.G)
        self.cuadrantes = crear_cuadrantes(self.nodos)

        self.presupuesto = tk.simpledialog.askfloat("Presupuesto", "Escribe el presupuesto que va a tener el proyecto")
        self.costo_metro = tk.simpledialog.askfloat("Presupuesto", "Escribe el costo de construir un metro de via")

        self.lista_puntos = []

        self.label_peticion = CTkLabel(master=self, text="")
        self.label_peticion.grid(row=0, column=0, pady=5)

        self.frame_cuadricula = CTkFrame(master=self)
        self.frame_cuadricula.grid(row=1, column=0, pady=5)

        self.label_seleccion_info = CTkLabel(master=self, text="Cuadrantes Seleccionados = []")
        self.label_seleccion_info.grid(row=2, column=0, pady=5)

        self.boton_finalizar = CTkButton(master=self, text="Terminar Selección", fg_color="red", command=self.calculo_principal)
        self.boton_finalizar.grid(row=3, column=0, pady=5)

        self.iniciar_proceso()

    def iniciar_proceso(self):

        punto = []
        for tipo_punto in ("Inicio", "Destino"):

            for widget in self.frame_cuadricula.winfo_children():
                widget.destroy()

            ubicaciones_geo = (
                "NorOccidente",
                "Norte",
                "NorOriente",
                "Occidente",
                "Centro",
                "Oriente",
                "SurOccidente",
                "Sur",
                "SurOriente"
            )

            ub_acortadas = ("NW", "N", "NE", "W", "C", "E","SW", "S", "SE" )

            def cambiar_valor(i):
                def controlador():
                    punto.append(i)
                    if len(punto) == 2:
                        self.lista_puntos.append(tuple(punto))
                        self.label_seleccion_info.configure(text=f"Puntos guardados: {[(ub_acortadas[a - 1], ub_acortadas[b - 1]) for (a, b) in self.lista_puntos]}")
                        print(f"Puntos guardados: {self.lista_puntos}")
                        punto.clear()
                return controlador

            # Crear botones
            for i in range(9):
                col_c = i % 3
                row_c = i // 3
                boton_cuadrante = CTkButton(
                    master=self.frame_cuadricula,
                    text=ubicaciones_geo[i],
                    command=cambiar_valor(i + 1)
                )
                boton_cuadrante.grid(row=row_c, column=col_c, pady=5, padx=5)

    def calculo_principal(self):
        self.limpiar_self()

        self.lista_nodos = [(elegir(self.cuadrantes[a]), elegir(self.cuadrantes[b])) for (a,b) in self.lista_puntos]

        ver_grafo_con_puntos(self.G, self.lista_nodos)      

        self.label_simulaciones = CTkLabel(master = self, text = "Selecciona las simulaciones que quieras correr: ", font = ("Open Sans", 20, "bold"))
        self.label_simulaciones.grid(row = 0, column = 0, pady = 5)

        self.boton_simulacion_sencilla = CTkButton(master = self, text = "Correr Simulación Sin Inversión", fg_color="#E67E22", command = self.simulacion_sencilla)
        self.boton_simulacion_sencilla.grid(row = 1, column = 0, pady = 5, padx = 4)

        self.label_sencilla_eficiencia = CTkLabel(master = self, text = "Duración trayecto por ciudadano = INF")
        self.label_sencilla_eficiencia.grid(row = 1, column = 1, pady = 5, padx = 2)

        self.label_sencilla_duracion = CTkLabel(master = self, text = "Duración algoritmo = INF")
        self.label_sencilla_duracion.grid(row = 1, column = 2, pady = 5, padx = 2)

        self.boton_simulacion_aleatoria = CTkButton(master = self, text = "Correr Simulación Aleatoria", fg_color="#B9511f", command=self.simulacion_aleatoria)
        self.boton_simulacion_aleatoria.grid(row = 2, column = 0, pady = 5, padx = 4)

        self.label_aleatoria_eficiencia = CTkLabel(master = self, text = "Duración trayecto por ciudadano = INF")
        self.label_aleatoria_eficiencia.grid(row = 2, column = 1, pady = 5, padx = 2)

        self.label_aleatoria_duracion = CTkLabel(master = self, text = "Duración algoritmo = INF")
        self.label_aleatoria_duracion.grid(row = 2, column = 2, pady = 5, padx = 2)

        self.boton_simulacion_principal = CTkButton(master = self, text = "Correr Simulación Principal", fg_color="#BA310E", command = self.simulacion_principal)
        self.boton_simulacion_principal.grid(row = 3, column = 0, pady = 5, padx = 4)

        self.label_principal_eficiencia = CTkLabel(master = self, text = "Duración trayecto por ciudadano = INF")
        self.label_principal_eficiencia.grid(row = 3, column = 1, pady = 5, padx = 2)

        self.label_principal_duracion = CTkLabel(master = self, text = "Duración algoritmo = INF")
        self.label_principal_duracion.grid(row = 3, column = 2, pady = 5, padx = 2)

        self.boton_simulacion_completa = CTkButton(master = self, text = "Correr Busqueda Completa", fg_color="#761212", command = self.simulacion_completa)
        self.boton_simulacion_completa.grid(row = 4, column = 0, pady = 5, padx = 4)

        self.label_completa_eficiencia = CTkLabel(master = self, text = "Duración trayecto por ciudadano = INF")
        self.label_completa_eficiencia.grid(row = 4, column = 1, pady = 5, padx = 2)

        self.label_completa_duracion = CTkLabel(master = self, text = "Duración algoritmo = INF")
        self.label_completa_duracion.grid(row = 4, column = 2, pady = 5, padx = 2)

    def simulacion_sencilla(self):
        print(self.grafo)
        # print(self.G)
        print(self.lista_nodos )
        print(self.presupuesto)
        print(self.costo_metro)
        vias_mejoradas = main_algoritmo_simple(grafo = self.grafo, G = self.G, lista_pares_puntos= self.lista_nodos, presupuesto=self.presupuesto, costo_metro=self.costo_metro)
        

    def simulacion_aleatoria(self):
        print(self.grafo)
        # print(self.G)
        print(self.lista_nodos )
        print(self.presupuesto)
        print(self.costo_metro)
        vias_mejoradas = main_algoritmo_aleatorio(grafo = self.grafo, G = self.G, lista_pares_puntos= self.lista_nodos, presupuesto=self.presupuesto, costo_metro=self.costo_metro)

    def simulacion_principal(self):
        print(self.grafo)
        # print(self.G)
        print(self.lista_nodos )
        print(self.presupuesto)
        print(self.costo_metro)
        vias_mejoradas = main_algoritmo_principal(grafo = self.grafo, G = self.G, lista_pares_puntos= self.lista_nodos, presupuesto=self.presupuesto, costo_metro=self.costo_metro)



    def simulacion_completa(self):
        print(self.grafo)
        # print(self.G)
        print(self.lista_nodos )
        print(self.presupuesto)
        print(self.costo_metro)
        vias_mejoradas = main_algoritmo_busqueda_completa(grafo = self.grafo, G = self.G, lista_pares_puntos= self.lista_nodos, presupuesto=self.presupuesto, costo_metro=self.costo_metro)
        


class VentanaPrincipal:
    def __init__(self):
        self.app = CTk()
        self.app.configure(geometry = "500x700")
        self.frame_columna = Frame_Columna(master=self.app)
        self.frame_columna.configure(fg_color = "#1B2631")
        self.frame_columna.grid(row=0, column=0, pady=5)
        
        self.frame_principal = Frame_Principal(master=self.app)
        self.frame_principal.configure(fg_color = "#566573")
        self.frame_principal.grid(row=0, column=1, pady=5, padx = 10) 

        self.run()

    def run(self):
        self.app.mainloop()

    def __del__(self):
        tk.messagebox.showinfo("Hasta Luego!", "GRAP-UR® \n\nsmorenope@unal.edu.co\sapalacioso@unal.edu.co\njdiazav@unal.edu.co\n\nIntroducción a las Ciencias de la Computación y la Programación\nUniversidad Nacional de Colombia 2024")

def run():
    app = VentanaPrincipal()
    

if __name__ == "__main__":
    run()