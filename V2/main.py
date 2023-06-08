import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import END
from config import Config

class MyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.config = Config()
        self.window.geometry(self.config.size)
        self.window.title("Metodos numericos")
        self.frame_main = tk.Frame(self.window)
        
        self.setup_fonts()
        self.setup_widgets()
        self.window.resizable(1, 1)
        self.window.iconbitmap("icono.ico")
        
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.frame_main.pack(fill="both", padx=10, pady=10)
        
    def setup_fonts(self):
        self.font_style = font.Font(weight="bold", family="Arial")
        self.window.option_add("*Font", self.font_style)
        
    def setup_widgets(self):
        self.notebook = ttk.Notebook(self.frame_main)

        self.create_tab(self.notebook, "Metodo de Biseccion","           Biseccion        ")
        self.create_tab(self.notebook, "Metodo de Newton-Raphson","  Newton-Raphson   ")
        self.create_tab(self.notebook, "Metodo de Punto fijo","         Punto Fijo         ")
        self.create_tab(self.notebook, "Metodo de Euler","               Euler            ")
        self.create_tab(self.notebook, "Metodo de la secante","           Secante           ")
    def create_tab(self, notebook, content,text_tab):
        tab = tk.Frame(notebook)
        label = tk.Label(tab, text=content)
        label.grid(row=0, column=0,columnspan=5,padx=30,pady=20)
        lbl_func = tk.Label(tab,text="  Ingrese su funcion:   ")
        lbl_func.grid(row=5,column=0,columnspan=2,pady=10)
        ety_func = tk.Entry(tab)
        ety_func.grid(row=5,column=2)
        lbl_miss = tk.Label(tab,text="  Ingrese el error:   ")
        lbl_miss.grid(row=6,column=0,columnspan=2,pady=10)
        ety_miss = tk.Entry(tab)
        ety_miss.grid(row=6,column=2)
        btn_calc = tk.Button(tab,text="Calcular",width=10,command=lambda :self.calculate(ety_func, ety_miss))
        btn_calc.grid(row=10,column=2,pady=20)
        notebook.add(tab, text=text_tab)
        # Definir los campos de la tabla
        fields = ["ITERACION", "X", "F (x)", "ERROR"]

        # Definir los datos de ejemplo
        data = [
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02),
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02),
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02),
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02),
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02),
            (1, 0.5, 0.25, 0.1),
            (2, 0.7, 0.49, 0.05),
            (3, 0.9, 0.81, 0.02)
        ]
        frame_tabla = tk.Frame(tab)
        frame_tabla.grid(row=15)
        self.create_table(tab, fields, data)
    def create_table(self,root, fields, data):
        # Crear el árbol (Treeview)
        tree = ttk.Treeview(root, columns=fields, show="headings")
        # Definir configuraciones de estilo
        tree.tag_configure("oddrow", background="lightblue")
        tree.tag_configure("evenrow", background="white", foreground="blue")
        # Configurar las columnas
        for field in fields:
            tree.heading(field, text=field)
            tree.column(field, width=100)
        
        # Insertar los datos en la tabla
        for row in data:
            tree.insert("", "end", values=row)
        
        # Mostrar la tabla
        tree.grid(row=15,column=2,columnspan=5,pady=10)
    def calculate(self, entry_func, entry_miss):
        # Aquí puedes realizar los cálculos necesarios utilizando los valores de las entradas
        print(eval(entry_func.get()))
        # Vaciar el contenido de las entradas
        entry_func.delete(0, END)
        entry_miss.delete(0, END)
    def mi_funcion(self,x,expresion):
        return eval(expresion)
    def run(self):
        self.window.mainloop()

APLICACION = MyApp()
APLICACION.run()
