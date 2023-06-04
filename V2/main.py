import tkinter as tk
from tkinter import ttk
from tkinter import font
import customtkinter
from PIL import Image, ImageTk
import tkinter.constants 

from config import Config

class MyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.config = Config()
        self.window.geometry(self.config.size)
        self.window.title("Metodos numericos")
        self.frame_main = tk.Frame(self.window)
        
        # Configurar la fuente global
        self.font_style = font.Font(weight="bold",family="Arial")
        self.window.option_add("*Font", self.font_style)
        
        # Crear un widget Label con la imagen de fondo
        # background_label = tk.Label(self.window, image=self.config.bg_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # background_label.lower()  # Mover el fondo al fondo de la pila de widgets
        
        # Aplicar los estilos al notebook
        self.notebook = ttk.Notebook(self.frame_main)
        
        # Crear las pestañas
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)
        self.tab3 = tk.Frame(self.notebook)
        self.tab4 = tk.Frame(self.notebook)
        self.tab5 = tk.Frame(self.notebook)
        
        # Agregar las pestañas al notebook
        self.notebook.add(self.tab1, text="           Biseccion        ")
        self.notebook.add(self.tab2, text="  Newton-Raphson   ")
        self.notebook.add(self.tab3, text="         Punto Fijo         ")
        self.notebook.add(self.tab4, text="               Euler            ")
        self.notebook.add(self.tab5, text="           Secante           ")
        
        # Agregar contenido a cada pestaña
        label1 = tk.Label(self.tab1, text="Content for Tab 1")
        label1.pack(pady=200)
        
        label2 = tk.Label(self.tab2, text="Content for Tab 2")
        label2.pack(pady=200)
        
        label3 = tk.Label(self.tab3, text="Content for Tab 3")
        label3.pack(pady=200)
        
        label4 = tk.Label(self.tab4, text="Content for Tab 4")
        label4.pack(pady=200)
        
        # Mostrar el notebook
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        button = customtkinter.CTkButton(self.window, text="CTkButton", command=print("hola"))
        button.invoke()
        # Mostrar frame1 al inicio
        self.frame_main.pack(fill="both",padx=10, pady=10)
        
    def show_frame(self, frame):
        # Ocultar todos los frames
        # self.frame_biseccion.pack_forget()
        # self.frame_newton.pack_forget()
        
        # Mostrar el frame especificado
        # frame.pack()
        pass
    def run(self):
        self.window.mainloop()

APLICACION = MyApp()
APLICACION.run()
        