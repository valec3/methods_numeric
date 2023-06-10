import math
import numpy as np
import sympy as sp

def f(expresion, x):
    return eval(expresion)

def biseccion(func_txt, x_i, x_u,tol=0.0004):
    """
    Encuentra la raíz de la función f en el intervalo [x_i,x_u]
    usando el método de bisección con una tolerancia dada.
    """
    tabla = []
    conteo=0
    raiz_ant=0
    ea=1
    #Paso 1
    if f(func_txt,x_i) * f(func_txt,x_u) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    
    while ea > tol: #criterio de paro
        #Paso 2
        raiz = (x_i + x_u) / 2 #aproximacion de la raiz
        ea=abs((raiz-raiz_ant)/raiz)
        conteo+=1
        fa = f(func_txt,x_i)
        fb = f(func_txt,x_u)
        fc = f(func_txt,raiz)
        tabla.append([conteo,x_i,x_u,raiz,ea])
        print(f"{conteo}\t{x_i:.4f}\t{x_u:.4f}\t{raiz:.4f}\t{f(func_txt,raiz):.2f}\t{ea:.4f}")
        #Paso 3
        if fa*fc == 0: #c)
            return tabla
        elif fa * fc < 0: #a)
            x_u = raiz
        elif fa * fc > 0: #b)
            x_i = raiz
        raiz_ant =raiz #guardamos la raiz anterior
        if conteo>70:
            break
    print(tabla)
    print("sadasd")
    return tabla

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

def newton_raphson(f, x0, tolerance, max_iterations):
    x = x0
    iterations = 1
    error = np.inf
    
    # Definir la variable simbólica
    x_sym = sp.Symbol('x')
    
    # Convertir la función en una expresión SymPy
    f_expr = sp.sympify(f)
    
    # Calcular la derivada
    f_prime = sp.diff(f_expr, x_sym)
    
    # Convertir la función y la derivada a funciones numéricas
    f_num = sp.lambdify(x_sym, f_expr)
    f_prime_num = sp.lambdify(x_sym, f_prime)
    
    table = []
    
    while error > tolerance and iterations < max_iterations:
        fx = f_num(x)
        fpx = f_prime_num(x)
        x_new = x - fx / fpx
        error = np.abs(x_new - x)
        table.append([iterations, x, error, fx])
        x = x_new
        iterations += 1
    
    return table


