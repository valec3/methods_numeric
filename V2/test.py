import tkinter as tk
import math
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import font
from tkinter.constants import END
from config import Config
from metodos import *
import numpy as np
import sympy as sp
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
        self.metodo_current = ""
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.frame_main.pack(fill="both", padx=10, pady=10)
        
    def setup_fonts(self):
        self.font_style = font.Font(weight="bold", family="Arial")
        self.window.option_add("*Font", self.font_style)
        
    def setup_widgets(self):
        self.notebook = ttk.Notebook(self.frame_main,height=700)

        self.create_tab(self.notebook,"MB", "Metodo de Biseccion","           Biseccion        ","  x_i","  x_u")
        self.create_tab(self.notebook,"MN", "Metodo de Newton-Raphson","  Newton-Raphson   ","Punto inicial")
        self.create_tab(self.notebook,"MP", "Metodo de Punto fijo","         Punto Fijo         ","x_0")
        self.create_tab(self.notebook,"ME", "Metodo de Euler","               Euler            ","x_0","y_0","h")
        self.create_tab(self.notebook,"MS", "Metodo de la secante","           Secante           ","x_0","x_1")
        self.create_tab(self.notebook,"MS", "Metodo de la falsa Posicion","         Falsa posicion           ","x_0","x_1")
    def create_tab(self, notebook, ID_method,content,text_tab,label_txt1=None,label_txt2=None,label_txt3=None):
        self.metodo_current=ID_method
        tab = tk.Frame(notebook)
        label = tk.Label(tab, text=content)
        label.grid(row=0, column=0,columnspan=5,pady=20)
        lbl_func = tk.Label(tab,text="  Ingrese su funcion:   ")
        lbl_func.grid(row=5,column=0,columnspan=2,pady=10)
        ety_func = tk.Entry(tab,width=60)
        ety_func.grid(row=5,column=2,columnspan=4)
        lbl_miss = tk.Label(tab,text="  Ingrese el error:   ")
        lbl_miss.grid(row=6,column=0,columnspan=2,pady=10)
        ety_miss = tk.Entry(tab)
        ety_miss.grid(row=6,column=2)
        
        lbl_steps = tk.Label(tab,text="  Pasos(max):   ")
        lbl_steps.grid(row=7,column=0,columnspan=2,pady=10)
        ety_steps = tk.Entry(tab)
        ety_steps.grid(row=7,column=2)
        
        if (label_txt3 is not None) and (label_txt2 is not None) and (label_txt1 is not None):
            label_ext_0 = tk.Label(tab, text=label_txt1)
            label_ext_0.grid(row=20, column=1,pady=10)
            ety_ext_0 = tk.Entry(tab,width=15)
            ety_ext_0.grid(row=20,column=2,padx=10)
            
            label_ext_1 = tk.Label(tab, text=label_txt2)
            label_ext_1.grid(row=20, column=3,pady=10)
            ety_ext_1 = tk.Entry(tab,width=15)
            ety_ext_1.grid(row=20,column=4,padx=10)
            
            label_ext_2 = tk.Label(tab, text=label_txt3)
            label_ext_2.grid(row=21, column=1,pady=10)
            ety_ext_2 = tk.Entry(tab,width=15)
            ety_ext_2.grid(row=21,column=2,padx=10)
            
            btn_calc = tk.Button(tab,text="Calcular",width=10,command=lambda :self.ejecutar_metodo(tab,ety_func, ety_miss,ety_steps,ety_ext_0,ety_ext_1,ety_ext_2))
            btn_rest = tk.Button(tab,text="Reset",width=10,command=lambda :self.reset_results(ety_func, ety_miss,ety_steps,ety_ext_0,ety_ext_1,ety_ext_2))
        elif (label_txt1 is not None) and (label_txt2 is not None):
            label_ext_0 = tk.Label(tab, text=label_txt1)
            label_ext_0.grid(row=20, column=1,pady=10)
            ety_ext_0 = tk.Entry(tab,width=15)
            ety_ext_0.grid(row=20,column=2,padx=10)
            
            label_ext_1 = tk.Label(tab, text=label_txt2)
            label_ext_1.grid(row=20, column=3,pady=10)
            ety_ext_1 = tk.Entry(tab,width=15)
            ety_ext_1.grid(row=20,column=4,padx=10)
            
            btn_calc = tk.Button(tab,text="Calcular",width=10,command=lambda :self.ejecutar_metodo(tab,ety_func, ety_miss,ety_steps,ety_ext_0,ety_ext_1))
            btn_rest = tk.Button(tab,text="Reset",width=10,command=lambda :self.reset_results(ety_func, ety_miss,ety_steps,ety_ext_0,ety_ext_1))
        elif label_txt1 is not None:
            label_ext_0 = tk.Label(tab, text=label_txt1)
            label_ext_0.grid(row=20, column=1,pady=10)
            ety_ext_0 = tk.Entry(tab,width=15)
            ety_ext_0.grid(row=20,column=2,padx=10)
            
            btn_calc = tk.Button(tab,text="Calcular",width=10,command=lambda :self.ejecutar_metodo(tab,ety_func, ety_miss,ety_steps,ety_ext_0))
            btn_rest = tk.Button(tab,text="Reset",width=10,command=lambda :self.reset_results(ety_func, ety_miss,ety_steps,ety_ext_0))
        else:
            btn_calc = tk.Button(tab,text="Calcular",width=10,command=lambda :self.ejecutar_metodo(tab,ety_func, ety_miss,ety_steps))
            btn_rest = tk.Button(tab,text="Reset",width=10,command=lambda :self.reset_results(ety_func, ety_miss,ety_steps))
        btn_calc.grid(row=30,column=2,pady=20)
        btn_rest.grid(row=30,column=3,pady=20)
        notebook.add(tab, text=text_tab)
        # Definir los campos de la tabla
        self.fields = ["ITERACION", "X", "F (x)", "ERROR"]

        # Definir los datos de ejemplo
        self.data = [
                    (0, 0, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0),
                ]
        
    def create_table(self,root, fields, data):
        # Crear el árbol (Treeview)
        self.tree = ttk.Treeview(root, columns=fields, show="headings")
        # Definir configuraciones de estilo
        self.tree.tag_configure("oddrow", background="lightblue")
        self.tree.tag_configure("evenrow", background="white", foreground="blue")
        # Configurar las columnas
        for field in fields:
            self.tree.heading(field, text=field)
            self.tree.column(field, width=100)
        
        # Insertar los datos en la tabla
        for row in data:
            self.tree.insert("", "end", values=row)
        
        # Mostrar la tabla
        self.tree.grid(row=50,column=0,columnspan=5,pady=40)
        
    def reset_results(self,ety_func, ety_miss,ety_step,ety_ext0=None,ety_ext1=None,ety_ext2=None):
        # Vaciar el contenido de las entradas
        ety_func.delete(0, END)
        ety_miss.delete(0, END)
        ety_step.delete(0, END)
        if ety_ext0 is not None:
            ety_ext0.delete(0, END)
        if ety_ext1 is not None:
            ety_ext1.delete(0, END)
        if ety_ext2 is not None:
            ety_ext2.delete(0, END)
        registros=self.tree.get_children()

        for elemento in registros:
            self.tree.delete(elemento) 
    def calculate(self, entry_func, entry_miss,entry_step,ety_x_i=None,ety_x_u=None,ety_h=None):
        try:
            # Aquí puedes realizar los cálculos necesarios utilizando los valores de las entradas
            func_txt = entry_func.get()  if entry_func.get() != '' else 0
            tol = float(entry_miss.get()) if entry_miss.get() != '' else 0.0004
            step = int(entry_step.get()) if entry_step.get() != '' else 100
            x_i = float(ety_x_i.get()) if ety_x_i is not None else 0
            x_u = float(ety_x_u.get()) if ety_x_u is not None else 0
            h = float(ety_h.get()) if ety_h is not None else 0
            
            if self.notebook.index("current") == 0:
                self.data = biseccion(func_txt,x_i,x_u,tol,step)
                self.fields = ["ITERACION", "X_i","X_u","X", "ERROR"]
            elif self.notebook.index("current") == 1:
                self.data = newton_raphson(func_txt, x_i, tol, step)
                self.fields = ["ITERACION", "X","ERROR","f(x)"]
            elif self.notebook.index("current") == 2:
                self.data = punto_fijo(func_txt, x_i,tol,step)
                self.fields = ["ITERACION","X","ERROR","f(x)","x new"]
            elif self.notebook.index("current") == 3:
                self.data = euler_method(func_txt, x_i,x_u,h,step)
                self.fields = ["ITERACION","X","Y","f(x,y)","y_{n+1}"]
            elif self.notebook.index("current") == 4:
                self.data = secante_method(func_txt, x_i,x_u,tol,step)
                self.fields = ["ITERACION","X","f (x)","ERROR"]
            elif self.notebook.index("current") == 5:
                self.data = falsa_posicion(func_txt, x_i,x_u,tol,step)
                self.fields = ["ITERACION","X","f (x)","ERROR"]

                
        except ValueError:
            
            self.config.show_error("Error", "Ingrese valores numéricos válidos para los parámetros.")

        except Exception as e:
            self.config.show_error("Error", str(e))
            
    def mi_funcion(self,x,expresion):
        # Definir la variable simbólica
        x_sym = sp.Symbol('x')
        # Convertir la función en una expresión SymPy
        f_expr = sp.sympify(expresion)
        # Convertir la función y la derivada a funciones numéricas
        f_num = sp.lambdify(x_sym, f_expr)
        try:
            y = eval(expresion)
        except NameError:
            y =f_num(x)
        return y
    def ejecutar_metodo(self,tab,entry_func, entry_miss,entry_step,x_i=None,x_u=None,h=None):
        
        self.calculate(entry_func, entry_miss,entry_step,x_i,x_u,h)
        self.frame_tabla = tk.Frame(tab)
        self.frame_tabla.grid(row=15)
        self.create_table(tab, self.fields, self.data)
        self.graficar_func(entry_func.get())
    def graficar_func(self,expresion):
        if self.notebook.index("current") != 3 :
            x = np.linspace(-10, 10, 100)
            y = self.mi_funcion(x,expresion)

            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Gráfico de la función')
            plt.grid(True)
        else:
            # Convertir la función en una expresión SymPy
            f_expr = sp.sympify(expresion)
            
            # Definir las variables simbólicas
            x_sym = sp.Symbol('x')
            y_sym = sp.Symbol('y')
            
            # Convertir la función a una función numérica
            f_num = sp.lambdify((x_sym, y_sym), f_expr)
            # Generar los datos para graficar
            x = np.linspace(-5, 5, 100)
            y = np.linspace(-5, 5, 100)
            X, Y = np.meshgrid(x, y)
            Z = f_num(X, Y)

            # Crear la figura y los ejes
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Graficar la función
            ax.plot_surface(X, Y, Z, cmap='viridis')

            # Configurar etiquetas y título
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('f(x, y)')
            ax.set_title(expresion)

        # Mostrar el gráfico
        plt.show()

    def run(self):
        
        self.window.mainloop()
    
APLICACION = MyApp()
APLICACION.run()
