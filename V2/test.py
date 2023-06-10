import numpy as np
import sympy as sp

def euler_method(f, x0, y0, h, num_iterations):
    x = x0
    y = y0
    
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(f)
    
    # Definir las variables simbólicas
    x_sym = sp.Symbol('x')
    y_sym = sp.Symbol('y')
    
    # Convertir la función a una función numérica
    f_num = sp.lambdify((x_sym, y_sym), f_expr)
    
    table = []
    
    for i in range(1,num_iterations+1):
        table.append([i, x, y, f_num(x, y), y + h * f_num(x, y)])
        
        y_new = y + h * f_num(x, y)
        x += h
        y = y_new
    
    return table

# Ejemplo de uso
f = "x**2 + y"
x0 = 0
y0 = 1
h = 0.1
num_iterations = 15

table = euler_method(f, x0, y0, h, num_iterations)

# Imprimir la tabla de iteraciones
print("Tabla de iteraciones:")
print("Iteración |    x    |    y    |   f(x,y)  |   y_{n+1}  ")
print("---------------------------------------------------")
for row in table:
    iteration, x, y, fx, yn1 = row
    print(f"{iteration:9d} | {x:.3f} | {y:.3f} | {fx:.3f} | {yn1:.3f}")
