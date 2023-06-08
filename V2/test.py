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
        self.window.resizable(1,1)
        self.window.iconbitmap("icono.ico")
        # Configurar la fuente global
        self.setup_fonts()
        
        # Crear un widget Label con la imagen de fondo
        # background_label = tk.Label(self.window, image=self.config.bg_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # background_label.lower()  # Mover el fondo al fondo de la pila de widgets
        
        # crear notebook
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
        label1.pack(pady=20)
        # Crear el campo de entrada (entry)
        entry_1 = tk.Entry(self.tab1)
        entry_1.pack()
        # Crear el botón
        button_1 = tk.Button(self.tab1, text="Enviar", command=print("hola"))
        button_1.pack()
        
        
        label2 = tk.Label(self.tab2, text="Content for Tab 2")
        label2.grid(row=0, column=1)
        # Crear el campo de entrada (entry)
        label_2_raiz_txt = tk.Label(self.tab2, text="Nombre:")
        label_2_raiz_txt.grid(row=1, column=0, sticky="e")
        entry_2 = tk.Entry(self.tab2)
        entry_2.grid(row=1, column=1)
        entry_2_dot = tk.Entry(self.tab2)
        entry_2_dot.grid(row=4, column=1)
        # Crear el botón
        button_2 = tk.Button(self.tab2, text="Enviar", command=print("hola"))
        button_2.grid(row=5, column=1)

        label3 = tk.Label(self.tab3, text="Content for Tab 3")
        label3.pack(pady=20)
        
        label4 = tk.Label(self.tab4, text="Content for Tab 4")
        label4.pack(pady=20)
        
        # Mostrar el notebook
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        # Mostrar frame1 al inicio
        self.frame_main.pack(fill="both",padx=10, pady=10)
    
    def setup_fonts(self):
        self.font_style = font.Font(weight="bold", family="Arial")
        self.window.option_add("*Font", self.font_style)
    def setup_widgets(self):
        self.notebook = ttk.Notebook(self.frame_main)

        self.create_tab(self.notebook, "Content for Tab 1","           Biseccion        ")
        self.create_tab(self.notebook, "Content for Tab 2","  Newton-Raphson   ")
        self.create_tab(self.notebook, "Content for Tab 3","         Punto Fijo         ")
        self.create_tab(self.notebook, "Content for Tab 4","               Euler            ")
        self.create_tab(self.notebook, "Content for Tab 5","           Secante           ")
    def create_tab(self, notebook, content,text_tab):
        tab = tk.Frame(notebook)
        label = tk.Label(tab, text=content)
        label.pack(pady=20)
        self.create_entry(tab)
        self.create_button(tab)
        notebook.add(tab, text=text_tab)
    def run(self):
        self.window.mainloop()

APLICACION = MyApp()
APLICACION.run()
        